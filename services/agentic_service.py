from config.ai_config import MAX_RETRIES, TARGET_FILE
from agents.review_agent import review_code
from agents.fix_agent import generate_fix
from agents.evalution_agent import evaluate_fix
from agents.decision_agent import decide
from agents.validation_agent import validate_code
from utils.file_utils import read_file, write_file, file_exists
from utils.llm_client import call_llm

LANGUAGE_DETECT_PROMPT = """
Detect the programming language of the following code.
Return only the language name.
"""

def detect_language(code: str) -> str:
    return call_llm(LANGUAGE_DETECT_PROMPT, code)

def is_conversion_request(instruction: str) -> bool:
    keywords = ["convert", "translate", "rewrite in", "change to"]
    instruction = instruction.lower()
    return any(k in instruction for k in keywords)

def run_agentic_fix(instruction: str):

    if not file_exists(TARGET_FILE):
        return {"status": "error", "message": "Target file not found"}

    retries = 0
    history = "None"

    current_code = read_file(TARGET_FILE)

    while retries < MAX_RETRIES:

        review = review_code(current_code, instruction, history)

        modified_code = generate_fix(current_code, instruction, review)

        language = detect_language(modified_code)

        valid, message = validate_code(modified_code, language)

        if not valid:

            if is_conversion_request(instruction):
                history = f"Invalid {language} syntax. Fix syntax. Error: {message}"
            else:
                history = message

            current_code = modified_code
            retries += 1
            continue

        score = evaluate_fix(modified_code, instruction)

        if decide(score):
            write_file(TARGET_FILE, modified_code)
            return {
                "status": "success",
                "score": score,
                "language": language,
                "retries": retries,
                "updated_file": TARGET_FILE
            }

        history = f"Rejected. Score={score}"
        current_code = modified_code
        retries += 1

    return {
        "status": "failed",
        "reason": history
    }
