import requests
import os

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def call_llm(prompt: str):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "qwen/qwen3.6-plus:free",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a customer support assistant. Answer only from given context."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    data = response.json()

    # Debug safety
    if "choices" not in data:
        print("ERROR:", data)
        return "LLM failed"

    return data["choices"][0]["message"]["content"]