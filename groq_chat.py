# groq_chat.py

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

# ✅ Safe version: Handles API errors gracefully
async def ask_groq(messages: list):
    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "system", "content": "You are a helpful assistant."}] + messages
    }

    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(API_URL, headers=headers, json=data)
            res.raise_for_status()  # raises HTTPStatusError if 4xx/5xx
            return res.json()["choices"][0]["message"]["content"]
    except httpx.HTTPStatusError as e:
        return f"⚠️ Groq API error: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"❌ Internal server error: {str(e)}"

# Still works for quick single message
async def ask_groq_single(message: str):
    return await ask_groq([{"role": "user", "content": message}])
