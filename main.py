from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="MindWeaver API 🚀")
app.include_router(router)

