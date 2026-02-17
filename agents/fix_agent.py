from typing import Dict,Tuple

from utils.llm_client import call_llm

SYSTEM_PROMPT = """
You are a precise code transformation agent.

Rules:
- Follow the instruction exactly
- If instruction requests language conversion, fully convert the code
- Do not mix languages
- Output must be syntactically valid
- Return ONLY code
"""

def generate_fix(code: str, instruction: str, review: str) -> Tuple[str,Dict]:
    prompt = f"""
Instruction:
{instruction}

Review Findings:
{review}

Code:
{code}

Return updated code only.
"""
    response,tokens = call_llm(SYSTEM_PROMPT, prompt)

    print(f"\n\nFix_agent : {response}")

    return response,tokens
