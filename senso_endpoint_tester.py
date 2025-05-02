import requests
import os
from dotenv import load_dotenv

load_dotenv()

SENSO_API_KEY = os.getenv("SENSO_API_KEY")
BASE_URL = "https://api.senso.ai/"

COMMON_ENDPOINTS = [
    "noodle/",
    "sdk/ask/",
    "agents/ask/",
    "interactions/ask/",
    "interactions/",
    "chat/",
    "query/",
    "v1/query",
    "model/ask/",
    "ai/ask/",
]

def test_endpoints(prompt="Hello from the hackathon"):
    headers = {
        "Authorization": f"Bearer {SENSO_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"prompt": prompt}

    for endpoint in COMMON_ENDPOINTS:
        url = BASE_URL + endpoint
        print(f"Testing: {url}")
        try:
            r = requests.post(url, headers=headers, json=payload, timeout=10)
            print(f"Status: {r.status_code}")
            if r.status_code == 200:
                print("✅ SUCCESS!")
                print("Response:", r.text)
                return
        except Exception as e:
            print(f"❌ Error: {e}")
    print("🔴 No working endpoint found.")

if __name__ == "__main__":
    test_endpoints()

