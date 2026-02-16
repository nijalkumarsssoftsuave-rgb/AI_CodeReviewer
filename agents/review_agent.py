# review agent
from utils.llm_client import call_llm

SYSTEM_PROMPT = """
You are a senior code reviewer.

Tasks:
- Identify why the code may fail after modification
- Detect language mismatch issues
- Detect partial conversions
Return ONLY the review.
"""

def review_code(code: str, instruction: str, history: str) -> str:
    prompt = f"""
Instruction:
{instruction}

Previous Issues:
{history}

Code:
{code}
"""
    return call_llm(SYSTEM_PROMPT, prompt)
