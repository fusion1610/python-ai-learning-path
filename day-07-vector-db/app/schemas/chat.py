from pydantic import BaseModel
from typing import List


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str
    context_used: List[str]