# from utils.llm_client import call_llm
#
# SYSTEM_PROMPT = """
# You are a strict code quality evaluator.
#
# Score the proposed solution from 0–100.
#
# Criteria:
# - Correctness
# - Instruction compliance
# - Safety of change
#
# Return ONLY the numeric score.
# """
#
# def evaluate_fix(code: str, instruction: str) -> int:
#     prompt = f"""
# Instruction:
# {instruction}
#
# Code:
# {code}
# """
#     score_text = call_llm(SYSTEM_PROMPT, prompt)
#
#     try:
#         return int(score_text)
#     except:
#         return 0

from utils.llm_client import call_llm

SYSTEM_PROMPT = """
You are a strict evaluator.

Score 0–100 based on:
- Syntax validity likelihood
- Instruction compliance
- Completeness

Return ONLY the number.
"""

def evaluate_fix(code: str, instruction: str) -> int:
    prompt = f"""
Instruction:
{instruction}

Code:
{code}
"""
    text = call_llm(SYSTEM_PROMPT, prompt)

    try:
        return int(text)
    except:
        return 0
