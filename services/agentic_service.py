from config.ai_config import MAX_RETRIES, TARGET_FILE
from agents.reasoning_agent import modify_code
from agents.validation_agent import validate_code
from utils.file_utils import read_file, write_file, file_exists
from utils.llm_client import call_llm

LANGUAGE_DETECT_PROMPT = """
Detect the programming language of the following code.
Return only the language name.
"""

def detect_language(code: str) -> str:
    return call_llm(LANGUAGE_DETECT_PROMPT, code)

def run_agentic_fix(instruction: str):

    if not file_exists(TARGET_FILE):
        return {"status": "error", "message": "Target file not found"}

    retries = 0
    history = "None"

    original_code = read_file(TARGET_FILE)
    current_code = original_code

    while retries < MAX_RETRIES:

        modified_code = modify_code(
            current_code,
            instruction,
            history
        )

        new_language = detect_language(modified_code)

        valid, message = validate_code(modified_code, new_language)

        if valid:
            write_file(TARGET_FILE, modified_code)

            return {
                "status": "success",
                "language": new_language,
                "retries": retries,
                "updated_file": TARGET_FILE
            }

        history = message
        current_code = modified_code
        retries += 1

    return {
        "status": "failed",
        "reason": history
    }
