from config.ai_config import MAX_RETRIES, TARGET_FILE
from agents.review_agent import review_code
from agents.fix_agent import generate_fix
from agents.evalution_agent import evaluate_fix
from agents.decision_agent import decide
from agents.validation_agent import validate_code
from utils.file_utils import read_file, write_file, file_exists
from utils.llm_client import call_llm
from agents.memory_agent import MemoryAgent

LANGUAGE_DETECT_PROMPT = """
Detect the programming language of the following code.
Return only the language name.
"""

def detect_language(code: str):
    response, tokens = call_llm(LANGUAGE_DETECT_PROMPT, code)
    print(f"\nLanguage : {response}")
    return response, tokens

def is_conversion_request(instruction: str) -> bool:
    keywords = ["convert", "translate", "rewrite in", "change to"]
    instruction = instruction.lower()
    return any(k in instruction for k in keywords)


memory = MemoryAgent()
PLATEAU_LIMIT = 2

def run_agentic_fix(instruction: str):

    if not file_exists(TARGET_FILE):
        return {"status": "error", "message": "Target file not found"}

    retries = 0
    plateau_count = 0
    last_score = None

    total_tokens_used = 0
    tokens_report = {}

    current_code = read_file(TARGET_FILE)

    history = memory.load("history", "None")

    while retries < MAX_RETRIES:

        iteration_tokens = 0  # RESET PER ITERATION

        print(f"\n--- Iteration {retries + 1} ---")

        review, token1 = review_code(current_code, instruction, history)
        iteration_tokens += token1["total_tokens"]

        modified_code, token2 = generate_fix(current_code, instruction, review)
        iteration_tokens += token2["total_tokens"]

        language, token3 = detect_language(modified_code)
        iteration_tokens += token3["total_tokens"]

        valid, message, token4 = validate_code(modified_code, language)
        iteration_tokens += token4["total_tokens"]

        tokens_report[f"iteration{retries + 1}"] = iteration_tokens
        total_tokens_used += iteration_tokens

        print(f"Iteration Tokens: {iteration_tokens}")

        if not valid:

            history = f"Invalid {language}: {message}"

            memory.append("iteration_log", {
                "iteration": retries,
                "event": "validation_failure",
                "reason": history,
                "tokens": iteration_tokens
            })

            memory.save("history", history)

            current_code = modified_code
            retries += 1
            continue

        val_score,tokens = evaluate_fix(modified_code, instruction)
        score = val_score

        print(f"Score: {score}")

        if last_score is not None and score <= last_score:
            plateau_count += 1
        else:
            plateau_count = 0

        last_score = score

        if plateau_count >= PLATEAU_LIMIT:

            reason = f"Early stopping: score plateau detected (score={score})"

            memory.append("iteration_log", {
                "iteration": retries,
                "event": "early_stop",
                "reason": reason,
                "tokens": iteration_tokens
            })

            memory.save("history", reason)

            return {
                "status": "stopped",
                "reason": reason,
                "tokens": tokens_report,
                "total_tokens": total_tokens_used
            }

        decision = decide(score)

        memory.append("iteration_log", {
            "iteration": retries,
            "event": "decision",
            "tokens": iteration_tokens,
            **decision
        })

        print(decision["reason"])

        if decision["accepted"]:

            write_file(TARGET_FILE, modified_code)

            memory.append("successful_fixes", {
                "instruction": instruction,
                "score": score,
                "language": language,
                "tokens": total_tokens_used
            })

            memory.save("history", "None")

            return {
                "status": "success",
                "score": score,
                "language": language,
                "retries": retries,
                "updated_file": TARGET_FILE,
                "tokens": tokens_report,
                "total_tokens": total_tokens_used
            }

        history = f"Rejected. Score={score}"

        memory.save("history", history)

        current_code = modified_code
        retries += 1

    return {
        "status": "failed",
        "reason": history,
        "tokens": tokens_report,
        "total_tokens": total_tokens_used
    }
