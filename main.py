from fastapi import FastAPI, Request
from pydantic import BaseModel
from model import query_employees, generate_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatQuery(BaseModel):
    query: str

@app.post("/chat")
async def chat(query: ChatQuery):
    matches = query_employees(query.query)
    response = generate_response(query.query, matches)
    return {"response": response, "matches": matches}

@app.get("/employees/search")
async def search_employees(skill: str = None):
    if not skill:
        return employees
    return [e for e in employees if skill in e["skills"]]