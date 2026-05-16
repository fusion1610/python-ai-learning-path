# Day 4 — RAG Basics (Retrieval Augmented Generation) 🚀

This project is part of my journey transitioning from Software Engineer to Applied AI Engineer.

## 📌 What I Built

A basic **RAG (Retrieval Augmented Generation)** system using FastAPI and a local LLM (via Ollama), where the AI answers questions based on custom data instead of relying only on its internal knowledge.

---

## 🧠 What is RAG?

RAG is a technique where we:

1. Provide external data (documents)
2. Inject relevant context into the prompt
3. Generate answers grounded in that data

Instead of:

* LLM guessing answers ❌

We make it:

* LLM answer using provided context ✅

---

## ⚙️ Tech Stack

* Python
* FastAPI
* Ollama (local LLM)
* Requests
* Pydantic

---

## 🔁 System Flow

```id="6z9kcx"
User Question
     ↓
Load custom data (data.txt)
     ↓
Inject context into prompt
     ↓
Send to LLM
     ↓
LLM generates grounded answer
```

---

## 📁 Project Structure

```id="2s4q3g"
day-04-rag-basics/
│
├── app/
│   └── main.py       # FastAPI app with /ask endpoint
|   └── test_ai.py    # Testing script for RAG
|   └── data.txt      # Custom knowledge base
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

### 1. Start Ollama

```id="ph3l62"
ollama serve
```

### 2. Run FastAPI server

```id="8a6o59"
uvicorn main:app --reload
```

### 3. Open Swagger UI

```id="7xk7y8"
http://127.0.0.1:8000/docs
```

---

## 🧪 Example Request

```json id="s2c8pv"
{
  "message": "Why is FastAPI popular?"
}
```

---

## ✅ Example Response

```json id="d1f6i4"
{
  "response": "FastAPI is popular because it is fast and supports automatic API documentation."
}
```

---

## 🧠 Key Concepts Implemented

### 1. Context Injection

Instead of asking the LLM directly, we provide relevant data as context.

---

### 2. Grounded Responses

The AI is instructed to answer only using the provided context, reducing hallucination.

---

### 3. Separation of Knowledge

* Model = reasoning
* Data = knowledge

---

## ⚠️ Limitation of Current Approach

* Entire document is passed every time ❌
* Not scalable for large data
* No intelligent retrieval

---

## 🚀 What’s Next

* Add embeddings (convert text to vectors)
* Implement vector search (similarity-based retrieval)
* Build full RAG pipeline

---

## 🔥 What I Learned

* How to integrate custom data with LLMs
* Why RAG is important for real-world AI systems
* Difference between model knowledge and external knowledge
* Importance of context for accurate responses

---

## 📌 Note

This is a basic implementation of RAG using full context injection.
More advanced RAG systems use embeddings and vector databases for efficient retrieval.

---

## 📢 Journey

This is Day 4 of my 45-day journey into AI Engineering.
