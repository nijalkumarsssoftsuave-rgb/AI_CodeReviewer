from typing import Tuple, Dict

from utils.llm_client import call_llm

SYSTEM_PROMPT = """
You are a strict evaluator.

Score 0–100 based on:
- Syntax validity likelihood
- Instruction compliance
- Completeness

Return ONLY the number.
"""

def evaluate_fix(code: str, instruction: str) -> Tuple[int,Dict]:
    prompt = f"""
Instruction:
{instruction}

Code:
{code}
"""
    text,tokens = call_llm(SYSTEM_PROMPT, prompt)

    try:
        return int(text), tokens
    except:
        return 0,tokens
