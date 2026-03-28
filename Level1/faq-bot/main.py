import requests

def faq_bot(user_input):
    prompt = f"""
You are an intelligent FAQ assistant.

Objective:
Answer the question clearly and concisely.

Instructions:
- Provide a direct answer
- Use bullet points for key ideas

Constraints:
- STRICTLY under 100 words
- Do NOT exceed limit
- Avoid unnecessary explanation

Output Format:
Answer:
<your answer>

User Question:
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

