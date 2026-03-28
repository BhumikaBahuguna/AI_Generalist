import requests

chat_history = []

def chatbot(user_input):
    # Add user input
    chat_history.append(f"User: {user_input}")

    # Limit memory (last 6 messages only)
    if len(chat_history) > 6:
        chat_history.pop(0)

    full_prompt = f"""
You are a smart, conversational AI assistant.

CONVERSATION:
{chr(10).join(chat_history)}

TASK:
Answer the latest user message naturally using relevant context.

RULES:
- Understand references like "it", "that", "this" using past messages
- Do NOT mention "conversation history" or explain your reasoning
- Do NOT repeat previous answers
- Answer like a human (natural tone, not robotic)
- Be concise but complete
- If unsure, say: "I’m not sure."

STYLE:
- Prefer short paragraphs or bullet points (only if helpful)
- Keep it clean and readable

CONSTRAINT:
- STRICT: Response must be under 80 words
- If longer, shorten it before answering
- Prefer brevity over detail

OUTPUT FORMAT:
- Start with a direct answer (1–2 lines)
- Then optional bullet points (if needed)

Assistant:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": full_prompt,
            "stream": False
        }
    )

    reply = response.json()["response"]

    # Add assistant reply
    chat_history.append(f"Assistant: {reply}")

    return reply


while True:
    user = input("\nYou: ")

    if user.lower() == "exit":
        print("Goodbye!")
        break

    print("Bot:", chatbot(user))