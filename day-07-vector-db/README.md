# Day 7 — Scalable RAG with FAISS Vector Database 🚀

This project is part of my journey transitioning from Software Engineer to Applied AI Engineer.

## 📌 What I Built

A scalable Retrieval Augmented Generation (RAG) system using:

* FastAPI
* Hugging Face embeddings
* FAISS vector database
* Semantic search
* Ollama LLM

This version replaces manual similarity comparison with efficient vector indexing using FAISS, making retrieval faster and scalable for larger datasets.

---

# 🧠 What’s New (Upgrade from Day 6)

## Day 6:

* Manual retrieval using cosine similarity
* Retrieval over in-memory embeddings

## Day 7:

* FAISS vector database ✅
* Vector indexing ✅
* Scalable semantic retrieval ✅
* Schema-based API structure ✅
* Cleaner backend architecture ✅

---

# ⚙️ Tech Stack

* Python
* FastAPI
* Hugging Face Sentence Transformers
* Meta FAISS
* Ollama
* Requests
* Pydantic

---

# 🔁 System Flow

```text id="l8k3v2"
User Question
      ↓
Convert query → embedding
      ↓
Search FAISS vector index
      ↓
Retrieve top relevant chunks
      ↓
Inject context into prompt
      ↓
LLM generates grounded response
```

---

# 📁 Project Structure

```text id="9v4t7m"
day-07-vector-db/
│
├── app/
│   ├── main.py
│   │
│   ├── data/
│   │   └── data.txt
│   │
│   ├── schemas/
│   │   └── chat.py
│   │
│   └── utils/
│       ├── rag_utils.py
│       └── vector_store.py
│
├── test_ai.py
├── requirements.txt
└── README.md
```

---

# 🧠 Key Concepts Implemented

## 1. Vector Database

Embeddings are stored inside a FAISS vector index for efficient semantic retrieval.

---

## 2. Vector Indexing

The FAISS index organizes embeddings for fast similarity search.

---

## 3. Semantic Search

User queries are converted into embeddings and matched against stored vectors.

---

## 4. Scalable Retrieval

Instead of comparing against every embedding manually, FAISS performs optimized vector search.

---

## 5. Schema-Based API Design

Request and response models are separated into Pydantic schemas for cleaner backend architecture.

---

## 6. Grounded AI Responses

The LLM answers only using retrieved context to reduce hallucinations.

---

# 🔥 What I Learned

* Difference between embeddings and vector databases
* How FAISS performs scalable similarity search
* Why vector indexing is critical for production RAG systems
* Importance of modular backend architecture
* How schema-based APIs improve maintainability

---

# ▶️ How to Run

## 1. Install dependencies

```text id="s1v2k8"
pip install -r requirements.txt
```

---

## 2. Start Ollama

```text id="y2m5n0"
ollama serve
```

---

## 3. Run FastAPI server

```text id="c7p9q2"
uvicorn app.main:app --reload
```

---

## 4. Open Swagger UI

```text id="u8d3e1"
http://127.0.0.1:8000/docs
```

---

# 🧪 Example Request

```json id="v5q1r8"
{
  "message": "Why is FastAPI useful for AI applications?"
}
```

---

# ✅ Example Response

```json id="d2n7m4"
{
  "response": "FastAPI is useful for AI systems because it is lightweight, scalable, and integrates easily with machine learning models.",
  "context_used": [
    "...retrieved chunks..."
  ]
}
```

---

# ⚠️ Challenges Faced

## Issue:

Manual retrieval using cosine similarity would not scale efficiently for large datasets.

## Fix:

Introduced FAISS vector indexing for optimized similarity search and retrieval.

---

# 🚀 Next Steps

* Add metadata filtering
* Multi-document retrieval
* PDF ingestion
* Hybrid search strategies
* Advanced ranking techniques

---

# 🔑 Key Takeaway

On Day 7, I improved my RAG pipeline by introducing a vector database using FAISS for scalable semantic retrieval.

Previously, retrieval was done using manual cosine similarity over all embeddings, which works for small datasets but doesn’t scale efficiently. To solve this, I created a FAISS vector index to store embeddings and perform optimized similarity search.

Now, when a user asks a question, the query is converted into an embedding, searched against the FAISS index, and the most relevant chunks are retrieved efficiently before being sent to the LLM.

I also improved the backend structure by introducing schema-based request and response models using Pydantic, making the API cleaner and more maintainable.

---

# 📢 Journey

This is Day 7 of my 45-day journey into AI Engineering.
