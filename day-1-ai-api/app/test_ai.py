import requests

url = "http://localhost:11434/api/chat"

payload = {
    "model": "llama3.2:3b",
    "messages": [
        {"role": "user", "content": "Explain FastAPI in simple terms"}
    ],
    "stream": False
}

response = requests.post(url, json=payload)

print(response.json()["message"]["content"])