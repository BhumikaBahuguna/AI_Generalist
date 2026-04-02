import requests

def extract_intent(user_input):
    prompt = f"""
You are an AI system that extracts structured data.

TASK:
Extract the topic and difficulty from the user input.

RULES:
- Topic must be a DSA topic (Arrays, Graphs, Trees, Dynamic Programming, etc.)
- Difficulty must be Easy, Medium, or Hard
- If missing, infer the most reasonable value

CONSTRAINTS:
- STRICT: Output only in given format
- No extra text

OUTPUT FORMAT:
Topic: <topic>
Difficulty: <difficulty>

INPUT:
{user_input}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]