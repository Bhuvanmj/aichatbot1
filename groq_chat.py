# Original still works (ask_groq_single)
import os
import httpx
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Modified function that accepts full chat history
async def ask_groq(messages: list):
    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "system", "content": "You are a helpful assistant."}] + messages
    }
    async with httpx.AsyncClient() as client:
        res = await client.post(API_URL, headers=headers, json=data)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"]

# Original single-message function retained
async def ask_groq_single(message: str):
    return await ask_groq([{"role": "user", "content": message}])
