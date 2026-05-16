# Day 5 — Real RAG with Embeddings & Semantic Search 🚀

This project is part of my journey transitioning from Software Engineer to Applied AI Engineer.

## 📌 What I Built

A **real Retrieval Augmented Generation (RAG) system** using FastAPI, Hugging Face embeddings, and a local LLM (via Ollama).

Unlike the previous version (Day 4), this system retrieves only the **most relevant data chunks** using semantic search before sending them to the LLM.

---

## 🧠 What’s New (Upgrade from Day 4)

### Day 4:

* Entire document passed to LLM ❌
* Not scalable

### Day 5:

* Text is split into chunks ✅
* Each chunk converted into embeddings ✅
* Relevant chunks retrieved using similarity search ✅
* Only relevant context sent to LLM ✅

---

## ⚙️ Tech Stack

* Python
* FastAPI
* Hugging Face (Sentence Transformers)
* Scikit-learn (cosine similarity)
* Ollama (local LLM)
* Requests

---

## 🔁 System Flow

```id="z8z5d4"
User Question
     ↓
Convert query → embedding
     ↓
Compare with stored embeddings
     ↓
Retrieve top relevant chunks
     ↓
Send context + question to LLM
     ↓
Generate grounded answer
```

---

## 📁 Project Structure

```id="m2uqjw"
day-05-rag-embeddings/
│
├── app/
│   └── main.py              # FastAPI app
│
├── data/
│   └── data.txt             # Knowledge base
│
│── utils/
│   └── rag_utils.py         # Chunking + embeddings + retrieval      
│ 
├── test_ai.py               # End-to-end testing script
├── requirements.txt
├── README.md

```

---

## ▶️ How to Run

### 1. Install dependencies

```id="6f5k2w"
pip install -r requirements.txt
```

### 2. Start Ollama

```id="u9r6ch"
ollama serve
```

### 3. Run FastAPI server

```id="z9xg7n"
uvicorn app.main:app --reload
```

### 4. Open Swagger UI

```id="2u7trm"
http://127.0.0.1:8000/docs
```

---

## 🧪 Example Request

```json id="wzuy7t"
{
  "message": "Why is FastAPI popular?"
}
```

---

## ✅ Example Response

```json id="o7p1r6"
{
  "response": "FastAPI is popular because it is fast and supports automatic API documentation.",
  "context_used": [
    "FastAPI is fast and easy to use.",
    "It supports automatic API documentation."
  ]
}
```

---

## 🧠 Key Concepts Implemented

### 1. Embeddings

Text is converted into vectors using Hugging Face models to capture semantic meaning.

---

### 2. Semantic Search

Instead of keyword matching, similarity is calculated using cosine similarity.

---

### 3. Retrieval

Only the most relevant chunks are selected and passed to the LLM.

---

### 4. Context Injection

The LLM is guided using retrieved context to produce accurate and grounded responses.

---

## 🔥 What I Learned

* How embeddings enable semantic understanding of text
* Why retrieval improves scalability and accuracy
* How to build a real RAG pipeline
* How Hugging Face models are used in production systems

---

## ⚠️ Limitations

* Basic chunking strategy (line-based)
* No vector database (in-memory only)
* Retrieval can be improved with better ranking

---

## 🚀 Next Steps

* Improve chunking strategies
* Introduce vector databases (FAISS/Chroma)
* Optimize retrieval pipeline
* Build production-grade RAG system

---

## 🔑 Key Takeaway

On Day 5, I built a full RAG pipeline using embeddings and semantic search.

Instead of passing the entire document to the model, I split the data into smaller chunks and generated embeddings using Hugging Face’s sentence-transformers. Then, for each user query, I converted the query into an embedding and used cosine similarity to retrieve the most relevant chunks.

Only those relevant chunks were passed as context to the LLM, which improved both accuracy and scalability. This helped me understand how real-world AI systems retrieve and use external knowledge efficiently.

---

## 📢 Journey

This is Day 5 of my 45-day journey into AI Engineering.
