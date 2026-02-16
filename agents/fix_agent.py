# from utils.llm_client import call_llm
#
# SYSTEM_PROMPT = """
# You are a precise code modification agent.
#
# Rules:
# - Apply minimal corrections
# - Preserve behavior unless change requested
# - Return ONLY modified code
# - No explanations
# """
#
# def generate_fix(code: str, instruction: str, review: str) -> str:
#     prompt = f"""
# Instruction:
# {instruction}
#
# Review Findings:
# {review}
#
# Code:
# {code}
#
# Return updated code only.
# """
#     return call_llm(SYSTEM_PROMPT, prompt)


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

def generate_fix(code: str, instruction: str, review: str) -> str:
    prompt = f"""
Instruction:
{instruction}

Review Findings:
{review}

Code:
{code}

Return updated code only.
"""
    return call_llm(SYSTEM_PROMPT, prompt)
