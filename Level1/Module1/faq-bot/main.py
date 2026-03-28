import requests

def faq_bot(user_input):
    prompt = f"""
You are a precise FAQ assistant.

TASK:
Answer the user's question clearly, concisely, and directly.

RULES:
- Maximum 80 words (STRICT limit)
- No introductions, no filler text
- No explanations beyond what is needed
- If unknown, say: "Answer not available."

FORMAT:
Answer:
- Point 1
- Point 2
- Point 3 (only if needed)

QUESTION:
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


while True:
    user = input("\nAsk your question (type 'exit' to quit): ")

    if user.lower() == "exit":
        break

    print("\nBot:", faq_bot(user))

