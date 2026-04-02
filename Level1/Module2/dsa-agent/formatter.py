def clean_output(text):
    lines = text.strip().split("\n")

    cleaned = []
    for line in lines:
        # Remove unwanted intro text
        if "Here are" in line:
            continue

        # Fix missing Topic label
        if line.strip().lower() in ["arrays", "graphs", "trees", "dynamic programming"]:
            line = f"Topic: {line.strip().title()}"

        cleaned.append(line)

    return "\n".join(cleaned)