import os
import requests
from dotenv import load_dotenv

load_dotenv()

MCP_API_KEY = os.getenv("MCP_API_KEY")
MCP_AGENT_URL = "https://agent.mcp.run/v1/chat"  # ← à adapter si besoin

def run_agent(prompt: str) -> str:
    if not MCP_API_KEY:
        return "❌ Missing MCP_API_KEY in .env"

    try:
        headers = {
            "Authorization": f"Bearer {MCP_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "input": prompt,
            "session_id": "user-session-id"
        }

        r = requests.post(MCP_AGENT_URL, headers=headers, json=payload)
        r.raise_for_status()
        response = r.json()
        return response.get("output", "✅ OK but no 'output' key in MCP response.")

    except Exception as e:
        return f"❌ MCP Error: {str(e)}"
