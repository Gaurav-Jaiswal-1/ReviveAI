from fastapi import FastAPI
from models import get_response

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Healthcare, Fitness, and Skincare Chatbot"}

@app.get("/chat")
def chat(user_input: str, category: str):
    return {"response": get_response(user_input, category)}
