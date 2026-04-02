import requests

def summarize(user_input):
    prompt = f"""
You are an AI summarizer.

TASK:
Summarize the following text.

RULES:
- Keep under 80 words
- Prefer paragraph format
- Use bullets ONLY if clearly needed

TEXT:
{user_input}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )

    return response.json()["response"]