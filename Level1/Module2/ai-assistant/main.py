from intent_router import detect_intent
from modules.explainer import explain
from modules.generator import generate
from modules.summarizer import summarize
from memory import add_to_memory
from formatter import clean_output


def parse_intent(text):
    for line in text.split("\n"):
        if "Intent:" in line:
            return line.split(":")[1].strip()
    return "EXPLAIN"


print("=== AI Assistant (ChatGPT-lite) ===")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Step 1: detect intent
    intent_raw = detect_intent(user_input)
    intent = parse_intent(intent_raw)

    # Step 2: route to correct module
    if intent == "GENERATE":
        response = generate(user_input)
    elif intent == "SUMMARIZE":
        response = summarize(user_input)
    else:
        response = explain(user_input)

    # Step 3: clean output
    response = clean_output(response)

    # Step 4: save memory
    add_to_memory(user_input, response)

    print("\nAssistant:", response)