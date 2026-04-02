chat_history = []

def add_to_memory(user, bot):
    chat_history.append(f"User: {user}")
    chat_history.append(f"Assistant: {bot}")

    # keep last 6 messages
    if len(chat_history) > 6:
        chat_history.pop(0)

def get_memory():
    return "\n".join(chat_history)