from fastapi import APIRouter
from agent.planner import run_agent

router = APIRouter()

@router.get("/")
def home():
    return {"message": "MindWeaver backend is running!"}

@router.get("/ask")
def ask_agent(prompt: str):
    response = run_agent(prompt)
    return {"response": response}
