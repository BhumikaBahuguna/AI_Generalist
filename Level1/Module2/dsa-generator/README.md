# 🧠 DSA Question Generator (AI-Powered)

## 📌 Overview

This project generates Data Structures and Algorithms (DSA) practice questions using a local LLM (Llama 3 via Ollama).
It uses structured Markdown prompting to ensure consistent and high-quality outputs.

---

## 🚀 Features

* Topic-based question generation
* Difficulty control (Easy / Medium / Hard)
* Structured output format
* Fully offline (no API required)

---

## 🛠️ Tech Stack

* Python
* Requests
* Ollama (Llama 3)

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

```bash id="s1"
pip install -r requirements.txt
```

### 2. Install Ollama

Download from: https://ollama.com

### 3. Run Model

```bash id="s2"
ollama run llama3
```

### 4. Run the App

```bash id="s3"
python main.py
```

---

## 🧪 Example Usage

```id="s4"
Topic: Arrays
Difficulty: Medium
```

---

## 🧠 Key Concepts Learned

* Markdown Prompt Engineering
* Structured AI outputs
* Prompt templating
* Local LLM integration

---

## 📌 Future Improvements

* Add solution generation
* Add difficulty tuning logic
* Web UI (Streamlit/React)
* Save generated questions
