import requests
from prompt_template import generate_prompt


# 🔹 Strong cleaning function
def clean_output(text, expected_topic, expected_difficulty):
    lines = text.strip().split("\n")

    cleaned = []
    inside_valid_section = False

    for line in lines:
        line_strip = line.strip()

        # Skip unwanted generic lines
        if "Here are" in line_strip:
            continue

        # Detect topic line
        if line_strip.lower().startswith("topic:"):
            if expected_topic.lower() in line_strip.lower():
                inside_valid_section = True
                cleaned.append(f"Topic: {expected_topic}")
            else:
                inside_valid_section = False
            continue

        # Detect difficulty line
        if line_strip.lower().startswith("difficulty:"):
            if expected_difficulty.lower() in line_strip.lower():
                cleaned.append(f"Difficulty: {expected_difficulty}")
            continue

        # Only keep content inside correct topic
        if inside_valid_section:
            cleaned.append(line)

    return "\n".join(cleaned)


# 🔹 Main function
def generate_dsa_questions(topic, difficulty):

    topic = topic.title()
    difficulty = difficulty.capitalize()

    prompt = generate_prompt(topic, difficulty)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.2  # 🔥 reduce randomness
            }
        }
    )

    reply = response.json()["response"]

    # 🔥 Apply strict cleaning
    reply = clean_output(reply, topic, difficulty)

    return reply


# 🔹 CLI Interface
print("=== DSA Question Generator ===")

while True:
    topic = input("\nEnter topic (or 'exit'): ")
    if topic.lower() == "exit":
        break

    difficulty = input("Enter difficulty (easy/medium/hard): ")

    result = generate_dsa_questions(topic, difficulty)

    print("\nGenerated Questions:\n")
    print(result)