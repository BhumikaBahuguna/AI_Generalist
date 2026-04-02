import requests

def detect_intent(user_input):
    prompt = f"""
You are an AI intent classifier.

TASK:
Classify user intent into one of:
- EXPLAIN
- GENERATE
- SUMMARIZE

RULES:
- EXPLAIN → user asks to explain concepts
- GENERATE → user asks to create questions, ideas, content
- SUMMARIZE → user asks to summarize text

CONSTRAINT:
- Output only one line

OUTPUT FORMAT:
Intent: <intent>

INPUT:
{user_input}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )

    return response.json()["response"]