# 🧠 Smart AI Chatbot (Context-Aware)

## 📌 Overview

This project is a context-aware AI chatbot built using a local LLM (Llama 3 via Ollama).
Unlike basic bots, it maintains conversation history and understands follow-up queries.

---

## 🚀 Features

* Context-aware responses (memory-based)
* Handles references like "it", "that"
* Structured prompt system
* Controlled output (word limits, formatting)
* Fully offline (no API required)

---

## 🛠️ Tech Stack

* Python
* Requests library
* Ollama (Llama 3)

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Ollama

Download from: https://ollama.com

### 3. Run Model

```bash
ollama run llama3
```

### 4. Run Chatbot

```bash
python main.py
```

---

## 🧪 Example Conversation

```
You: What is Python?
You: Is it used in AI?
You: Give examples
```

---

## 🧠 Key Concepts

* Stateful vs Stateless AI systems
* Context management
* Prompt structuring
* Memory optimization

---

## ⚙️ Improvements Implemented

* Chat history window (last 6 messages)
* Natural conversation tone
* Strict response constraints

---

## 📌 Future Improvements

* Add GUI (Streamlit / Web App)
* Save chat history to file/database
* Add multi-model support
* Voice input/output

---

## 🎯 Learning Outcome

Built a real-world AI chatbot system with:

* Memory
* Context understanding
* Controlled outputs
