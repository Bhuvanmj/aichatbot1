from fastapi import FastAPI
from pydantic import BaseModel
from groq_chat import ask_groq

app = FastAPI()

class ChatRequest(BaseModel):
    messages: list  # Accept full list of messages

@app.post("/chat")
async def chat(req: ChatRequest):
    reply = await ask_groq(req.messages)
    return {"response": reply}
