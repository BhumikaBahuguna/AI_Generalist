import requests
from memory import get_memory

def generate(user_input):
    prompt = f"""
You are a content generator.

CONTEXT:
{get_memory()}

TASK:
Generate content based on user request.

SPECIAL RULE:
- If user asks for DSA questions:
    → Generate EXACTLY 3 questions
    → No explanation
    → No extra text

GENERAL RULES:
- Follow user request strictly
- Do not add unnecessary content

INPUT:
{user_input}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )

    return response.json()["response"]