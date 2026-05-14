import requests
import json

url = "http://localhost:11434/api/chat"

payload = {
    "model": "llama3.2:3b",
    "messages": [
        {
            "role": "system",
            "content": """
                    You are a data extraction system.

                    Extract the following fields:
                    - vendor (string)
                    - amount (number)

                    You are a strict JSON generator.

                    Return ONLY valid JSON.
                    No explanation.
                    No extra text.
                    No markdown.
                    """
        },
        {
            "role": "user",
            "content": "Invoice from Amazon for ₹5000"
        }
    ],
    "stream": False
}

response = requests.post(url, json=payload)

output = response.json()["message"]["content"]

try:
    parsed = json.loads(output)
    print("Parsed JSON:", parsed)
except:
    print("Invalid JSON:", output)