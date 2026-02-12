from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

def request_fix(code: str, error: str) -> str:
    prompt = f"""
You are a strict Python code repair agent.

Code:
{code}

Error:
{error}

Return ONLY the corrected full code.
Do not explain anything.
"""

    response = client.responses.create(
        model=MODEL,
        input=prompt
    )

    return response.output[0].content[0].text
