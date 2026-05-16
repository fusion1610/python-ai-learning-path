# Day 3 — Structured Outputs with AI (JSON Extraction) 🚀

This project is part of my journey transitioning from Software Engineer to Applied AI Engineer.

## 📌 What I Built

An AI-powered backend using FastAPI and a local LLM (via Ollama) that extracts **structured data (JSON)** from unstructured text.

Instead of returning plain text responses, the system generates **clean, machine-readable JSON output**, enabling real-world automation use cases.

---

## ⚙️ Tech Stack

* Python
* FastAPI
* Ollama (local LLM)
* Requests
* Pydantic
* JSON parsing

---

## 🧠 Key Concepts Implemented

### 1. Structured Outputs

The AI is prompted to return responses strictly in JSON format instead of natural language.

Example:

Input:

```text
Invoice from Amazon for ₹5000
```

Output:

```json
{
  "vendor": "Amazon",
  "amount": 5000
}
```

---

### 2. Prompt Engineering for JSON

A strict system prompt is used to enforce structured output:

```text
You are a strict JSON generator.
Return ONLY valid JSON.
Do not include explanation or extra text.
```

---

### 3. JSON Validation

The response is parsed using Python’s `json.loads()` to ensure:

* valid JSON format
* reliable downstream usage

---

### 4. API-Based Extraction System

A FastAPI endpoint (`/extract`) is created to:

* accept user input
* send it to the LLM
* return structured JSON data

---

## 📁 Project Structure

```
day-03-structured-output/
│
│──app/
|   ├── main.py              # FastAPI app with /extract endpoint
|   ├── test_ai.py           # Testing script for structured output
|      
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
  "message": "Invoice from Flipkart for ₹12000"
}
```

---

## ✅ Example Response

```json
{
  "data": {
    "vendor": "Flipkart",
    "amount": 12000
  }
}
```

---

## ⚠️ Challenges & Fixes

### Problem:

AI sometimes returns extra text along with JSON.

### Solution:

* Use strict system prompts
* Enforce JSON-only output
* Validate response using `json.loads()`

---

## 🔥 What I Learned

* How to convert AI responses into structured data
* Importance of prompt engineering for output control
* How to validate and safely parse AI outputs
* Building AI-powered data extraction APIs

---

## 🚀 Real-World Applications

* Invoice processing systems
* Resume parsing
* Email data extraction
* CRM automation workflows

---

## 📌 Note

This project uses a local LLM via Ollama, so no external API cost is involved.

---

## 🔑 Key Takeaway
On Day 3, I built an AI-powered data extraction system where the model returns structured JSON instead of plain text.

I used prompt engineering with a strict system prompt to force the LLM to output only valid JSON for fields like vendor and amount. Then, in my FastAPI backend, I parsed the response using json.loads to ensure the output is usable and reliable.

So instead of just generating responses, I made the system produce structured data that can directly power automation workflows like invoice processing.

---

## 📢 Journey

This is Day 3 of my 45-day journey into AI Engineering.
