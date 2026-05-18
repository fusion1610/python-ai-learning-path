# Day 6 — Advanced RAG System 🚀

This project is part of my journey transitioning from Software Engineer to Applied AI Engineer.

## 📌 What I Built

An improved **RAG (Retrieval Augmented Generation)** system using FastAPI, Hugging Face embeddings, semantic search, and advanced chunking strategies.

This version improves retrieval quality and response grounding by introducing:

* smart chunking
* chunk overlap
* flexible top-k retrieval
* better prompt grounding

---

## 🧠 What’s New (Upgrade from Day 5)

### Day 5:

* Basic chunking
* Fixed retrieval
* Basic prompts

### Day 6:

* Smart word-based chunking ✅
* Chunk overlap for context continuity ✅
* Configurable top-k retrieval ✅
* Improved grounding prompts ✅
* Cleaner retrieval architecture ✅

---

## ⚙️ Tech Stack

* Python
* FastAPI
* Hugging Face Sentence Transformers
* Scikit-learn
* Ollama
* Requests

---

## 🔁 System Flow

```text id="p4q8tf"
User Question
      ↓
Convert query → embedding
      ↓
Compare with chunk embeddings
      ↓
Retrieve top relevant chunks
      ↓
Inject context into prompt
      ↓
LLM generates grounded response
```

---

## 📁 Project Structure

```text id="2tw43i"
day-06-advanced-rag/
│
├── app/
│   ├── main.py
│   │
│   ├── data/
│   │   └── data.txt
│   │
│   └── utils/
│       └── rag_utils.py
│
├── test_ai.py
├── requirements.txt
└── README.md
```

---

## 🧠 Key Concepts Implemented

### 1. Smart Chunking

Instead of splitting text line-by-line, documents are split into fixed-size word chunks.

---

### 2. Chunk Overlap

Chunks share overlapping words to preserve context continuity between chunks.

---

### 3. Embeddings

Text is converted into vectors using Hugging Face embedding models.

---

### 4. Semantic Search

Relevant chunks are retrieved using cosine similarity instead of keyword matching.

---

### 5. Top-K Retrieval

The system retrieves the top K most relevant chunks dynamically.

---

### 6. Grounded Responses

The LLM is instructed to answer only using the retrieved context.

---

## 🔥 What I Learned

* Why chunking strategy affects retrieval quality
* Importance of overlap in preserving context
* How retrieval tuning improves AI responses
* How production-style RAG systems are structured
* Practical use of embeddings and semantic search

---

## ▶️ How to Run

### 1. Install dependencies

```text id="m72lh4"
pip install -r requirements.txt
```

### 2. Start Ollama

```text id="hvm77m"
ollama serve
```

### 3. Run FastAPI server

```text id="v1m2pk"
uvicorn app.main:app --reload
```

### 4. Open Swagger UI

```text id="mq53vx"
http://127.0.0.1:8000/docs
```

---

## 🧪 Example Request

```json id="xxz63q"
{
  "message": "What are FastAPI advantages?"
}
```

---

## ✅ Example Response

```json id="qu98kp"
{
  "response": "FastAPI is known for high performance, automatic API documentation generation, and easy integration with AI systems.",
  "context_used": [
    "...retrieved chunks..."
  ]
}
```

---

## ⚠️ Challenges Faced

### Issue:

Retrieval quality was poor with large chunks.

### Fix:

* Reduced chunk size
* Added overlap
* Improved prompt grounding
* Tuned top-k retrieval

---

## 🚀 Next Steps

* Add vector databases (FAISS/Chroma)
* Handle PDFs and large documents
* Improve ranking strategies
* Build scalable retrieval pipelines

---

## 🔑 Key Takeaways

On Day 6, I improved my RAG pipeline to make it more production-like by focusing on retrieval quality and system architecture.

I replaced naive line-based chunking with fixed-size chunking and added chunk overlap to preserve context continuity between chunks. I also implemented configurable top-k retrieval using cosine similarity so the system can dynamically retrieve the most relevant context.

Additionally, I improved prompt grounding to reduce hallucinations and refactored the retrieval logic into a separate utility module for cleaner architecture.

This helped me understand that building effective RAG systems is largely about optimizing retrieval quality, not just calling an LLM.

---

## 📢 Journey

This is Day 6 of my 45-day journey into AI Engineering.
