from utils.llm_client import call_llm

SYSTEM_PROMPT = """
You are a Python syntax repair engine.

Rules:
- Return ONLY corrected Python code
- No explanations
- No markdown
- Preserve original logic
- Fix syntax errors only
"""

def request_fix(code: str, error_msg: str) -> str:
    user_prompt = f"""
The following Python code contains a syntax error.

Error:
{error_msg}

Code:
{code}

Return corrected Python code only.
"""

    return call_llm(SYSTEM_PROMPT, user_prompt)
