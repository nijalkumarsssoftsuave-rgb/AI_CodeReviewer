from utils.llm_client import call_llm

SYSTEM_PROMPT = """
You are a strict syntax validator.

Tasks:
- Determine if the code is syntactically valid for the specified language
- Do NOT attempt to fix anything
- Do NOT explain

Return format:
VALID
or
INVALID: <short reason>
"""

def validate_code(code: str, language_hint: str):

    prompt = f"""
Language:
{language_hint}

Code:
{code}
"""

    result = call_llm(SYSTEM_PROMPT, prompt).strip()

    if result.startswith("VALID"):
        return True, "OK"

    if result.startswith("INVALID"):
        return False, result

    return False, "Validator produced unexpected response"
