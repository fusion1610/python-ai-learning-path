import requests

url = "http://localhost:11434/api/chat"

with open("data.txt", "r") as f:
    context = f.read()

question = "Why is FastAPI popular?"

messages = [
    {
        "role": "system",
        "content": "Answer based ONLY on the provided context"
    },
    {
        "role": "user",
        "content": f"""
                Context:
                {context}

                Question:
                {question}
                """
    }
]

payload = {
    "model": "llama3.2:3b",
    "messages": messages,
    "stream": False
}

response = requests.post(url, json=payload)

output = response.json()["message"]["content"]

print(response.json()["message"]["content"])