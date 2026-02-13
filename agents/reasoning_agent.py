from utils.llm_client import call_llm

SYSTEM_PROMPT = """
You are an autonomous code modification agent.

Responsibilities:
- Detect programming language from code
- Understand user intent from instruction
- Apply minimal correct changes
- Preserve semantics unless change is requested
- Return ONLY modified code
- Never explain
- Never use markdown
"""

def modify_code(code: str, instruction: str, history: str) -> str:
    user_prompt = f"""
Instruction:
{instruction}

Previous Failures:
{history}

Code:
{code}

Return updated code only.
"""

    return call_llm(SYSTEM_PROMPT, user_prompt)
