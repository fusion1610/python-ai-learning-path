import requests

url = "http://localhost:11434/api/chat"

# Chat history (simulate conversation)
messages = [
    {"role": "user", "content": "What is FastAPI?"},
    {"role": "assistant", "content": "FastAPI is a Python web framework."},
    {"role": "user", "content": "Why is it popular?"}
]

payload = {
    "model": "llama3.2:3b",
    "messages": messages,
    "stream": False
}

response = requests.post(url, json=payload)

# Debug (VERY IMPORTANT)
print("Full response:")
print(response.json())

# Actual output
print("\nAI Response:")
print(response.json()["message"]["content"])