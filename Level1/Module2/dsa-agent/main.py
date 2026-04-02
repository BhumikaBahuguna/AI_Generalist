from intent_extractor import extract_intent
from question_generator import generate_dsa_questions
from formatter import clean_output


def parse_intent(text):
    lines = text.split("\n")
    topic = ""
    difficulty = ""

    for line in lines:
        if "Topic:" in line:
            topic = line.split(":")[1].strip()
        if "Difficulty:" in line:
            difficulty = line.split(":")[1].strip()

    # 🔥 Defaults
    if not topic:
        topic = "Arrays"
    if not difficulty:
        difficulty = "Medium"

    return topic, difficulty


print("=== AI DSA Agent ===")

while True:
    user_input = input("\nAsk: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # 🔹 Step 1: Extract intent
    intent = extract_intent(user_input)
    topic, difficulty = parse_intent(intent)

    print(f"\n[Detected] Topic: {topic}, Difficulty: {difficulty}")

    # 🔹 Step 2: Generate questions
    result = generate_dsa_questions(topic, difficulty)

    # 🔹 Step 3: Clean output
    result = clean_output(result)

    print("\nGenerated Questions:\n")
    print(result)