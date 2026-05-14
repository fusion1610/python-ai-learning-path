from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import requests
import json

app = FastAPI()

class ExtractRequest(BaseModel):
    message: str

@app.post("/extract")
def extract(req: ExtractRequest):

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.2:3b",
            "messages": [
                {
                    "role": "system",
                    "content": """
                                You are a strict JSON generator.

                                Extract:
                                - vendor
                                - amount

                                Return ONLY JSON.
                                """
                },
                {
                    "role": "user",
                    "content": req.message
                }
            ],
            "stream": False
        }
    )

    raw_output = response.json()["message"]["content"]

    try:
        parsed = json.loads(raw_output)
        return {"data": parsed}
    except:
        return {"error": "Invalid JSON", "raw": raw_output}