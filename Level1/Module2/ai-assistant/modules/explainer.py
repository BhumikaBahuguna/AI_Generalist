import requests
from memory import get_memory

def explain(user_input):
    prompt = f"""
You are an AI educator.

CONTEXT:
{get_memory()}

TASK:
Explain the concept clearly.

RULES:
- Simple explanation
- Use 1 example
- Keep under 100 words
- No unnecessary jargon

INPUT:
{user_input}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )

    return response.json()["response"]