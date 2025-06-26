import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")

# Open file context
with open ("knowledge.txt", "r", encoding="utf-8") as f:
    context = f.read()

# Startup message
print("📚 RAG Chat. Ask anything related to the knowledge.txt file!\n")

while True:
    user_input = input("🧑‍💻 You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

# Query to Together API w/ context
    messages = [
        {"role": "system", "content": "You are an assistant that only knows the following text:\n" + context},
        {"role": "user", "content": user_input}
    ]

    response = requests.post(
        "https://api.together.xyz/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/Meta-Llama-3-8B-Instruct-Lite",
            "messages": messages
        }
    )

    if response.status_code == 200:
        answer = response.json()["choices"][0]["message"]["content"]
        print("🤖 GPT:", answer.strip(), "\n")
    else:
        print("Error", response.status_code, response.text)