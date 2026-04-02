# 🤖 AI DSA Agent (Prompt Chaining System)

## 📌 Overview

This project is a multi-step AI system that generates DSA questions from natural language input.

It uses **prompt chaining** to:

1. Extract intent (topic + difficulty)
2. Generate structured questions
3. Clean and format output

---

## 🚀 Features

* Natural language input ("Give me medium array questions")
* Automatic topic & difficulty detection
* Structured question generation
* Clean and consistent output
* Fully offline using Ollama

---

## 🛠️ Tech Stack

* Python
* Requests
* Ollama (Llama 3)

---

## ⚙️ Setup Instructions

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Install Ollama

Download from: https://ollama.com

### 3. Run model

```
ollama run llama3
```

### 4. Run project

```
python main.py
```

---

## 🧪 Example Usage

```
Give me medium DSA questions on arrays
I want hard graph problems
easy tree questions
```

---

## 🧠 Architecture

User Input
↓
Intent Extraction
↓
Question Generation
↓
Output Cleaning

---

## 🎯 Learning Outcomes

* Prompt chaining
* Modular AI systems
* Intent parsing
* Structured prompting
* Output control

---

## 📌 Future Improvements

* Add solution generation
* Add web UI
* Add multiple model support
* Store question history
