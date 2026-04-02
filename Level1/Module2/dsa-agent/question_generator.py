import requests

def generate_prompt(topic, difficulty):
    return f"""
You are a Data Structures and Algorithms expert.

OBJECTIVE:
Generate strictly relevant DSA questions.

CONTEXT:
User is preparing for coding interviews.

INSTRUCTIONS:
- Generate EXACTLY 3 questions
- Questions must ONLY belong to the given topic
- Match the given difficulty level
- Cover different patterns

RULES:
- DO NOT include questions from other topics
- DO NOT add explanations, examples, or solutions
- DO NOT add extra text
- Each question must be 1–2 lines

CONSTRAINTS:
- STRICT: Follow format exactly

OUTPUT FORMAT:

Topic: {topic}
Difficulty: {difficulty}

Questions:
1. 
2. 
3. 

FINAL TASK:
Generate 3 {difficulty} level questions strictly on "{topic}".
"""

def generate_dsa_questions(topic, difficulty):
    topic = topic.title()
    difficulty = difficulty.capitalize()

    prompt = generate_prompt(topic, difficulty)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]