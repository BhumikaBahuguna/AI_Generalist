def generate_prompt(topic, difficulty):
    return f"""
You are a Data Structures and Algorithms expert.

OBJECTIVE:
Generate strictly relevant DSA questions based on user input.

CONTEXT:
The user is preparing for coding interviews and wants focused practice.

INSTRUCTIONS:
- Generate EXACTLY 3 questions
- Questions must ONLY belong to the given topic
- Match the given difficulty level
- Cover different problem-solving patterns within the topic

RULES:
- DO NOT include questions from other topics
- DO NOT add explanations, examples, or solutions
- DO NOT add any extra sections or text
- Each question must be concise (1–2 lines)

CONSTRAINTS:
- STRICT: Follow output format EXACTLY
- STRICT: Do not include any text before or after the format
- STRICT: Do not modify labels (Topic, Difficulty, Questions)

OUTPUT FORMAT (FOLLOW EXACTLY):

Topic: {topic}
Difficulty: {difficulty}

Questions:
1. 
2. 
3. 

FINAL TASK:
Generate 3 {difficulty} level DSA questions strictly on the topic "{topic}".
"""