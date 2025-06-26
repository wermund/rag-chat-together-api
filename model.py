import os, requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")

response = requests.get(
    "https://api.together.xyz/v1/models",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
)

print(response.status_code, response.json())