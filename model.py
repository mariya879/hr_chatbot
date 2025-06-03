import json
import faiss
import numpy as np
import requests
from sentence_transformers import SentenceTransformer

# Initialize sentence transformer for embedding
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Load employee data
with open("data/employees.json") as f:
    employees = json.load(f)["employees"]

# Convert employee data to text for embedding
texts = [
    f"{e['name']} with skills {', '.join(e['skills'])}, {e['experience_years']} years experience, projects: {', '.join(e['projects'])}, availability: {e['availability']}"
    for e in employees
]

# Compute and index embeddings
embeddings = embedder.encode(texts, convert_to_numpy=True)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Search top-K relevant employees
def query_employees(query, top_k=3):
    query_vec = embedder.encode([query], convert_to_numpy=True)
    D, I = index.search(np.array(query_vec), top_k)
    return [employees[i] for i in I[0]]

# Generate response using Ollama (LLaMA 3)
def generate_response(query, matched_employees):
    prompt = f"""
You are an HR assistant. A user asked: "{query}"
Based on the employee database below, suggest the best matches:

{json.dumps(matched_employees, indent=2)}

Respond in a professional tone with relevant recommendations.
"""
    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    })
    return res.json()["response"].strip()
