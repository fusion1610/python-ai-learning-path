# Day 2 — AI Chat Backend with Memory 🚀

This project is part of my journey transitioning from Software Engineer to Applied AI Engineer.

## 📌 What I Built

An AI-powered backend using FastAPI and a local LLM (via Ollama) that supports **multi-turn conversations (chat memory)**.

Unlike a simple chatbot, this system can understand context by processing previous messages in a conversation.

---

## ⚙️ Tech Stack

* Python
* FastAPI
* Ollama (local LLM)
* Requests
* Pydantic

---

## 🧠 Key Concepts Implemented

### 1. Chat Memory

Instead of sending a single message, the API accepts a list of messages:

* `user`
* `assistant`

This allows the model to generate context-aware responses.

---

### 2. System Prompt

A system message is added to control AI behavior:

```
"You are a helpful AI assistant"
```

---

### 3. Memory Limiting

Only the last few messages are sent to the model to:

* reduce latency
* avoid token overflow

---

## 📁 Project Structure

```
day-02-chat-memory/
│
├── app/
│   └── main.py       # FastAPI app with /chat endpoint
|   └── test_ai.py    # Testing script
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ▶️ How to Run

### 1. Start Ollama

```
ollama serve
```

### 2. Run FastAPI server

```
uvicorn main:app --reload
```

### 3. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Example Request

```json
{
  "messages": [
    {"role": "user", "content": "What is FastAPI?"},
    {"role": "assistant", "content": "FastAPI is a Python web framework."},
    {"role": "user", "content": "Why is it popular?"}
  ]
}
```

---

## ✅ Example Response

```json
{
  "response": "FastAPI is popular because it is fast, easy to use, and supports automatic API documentation."
}
```

---

## 🔥 What I Learned

* How to implement chat memory using message history
* How LLMs use context to generate better responses
* How to structure AI APIs using FastAPI
* Importance of limiting context (memory management)

---

## 🚀 Next Steps

* Add structured JSON outputs (Day 3)
* Build real-world use cases (invoice/data extraction)
* Improve prompt control and validation

---

## 📌 Note

This project uses a local LLM via Ollama, so no external API or cost is involved.

---

## 🔑 Key Takeaway
On Day 2, I implemented chat memory by passing message history to the LLM. Since LLMs are stateless, maintaining context on the application side is necessary. I also added a system prompt to control behavior and limited the history to optimize performance.

---

## 📢 Journey

This is Day 2 of my 45-day journey into AI Engineering.
