
# HR Resource Query Chatbot

## Overview
An AI-powered HR assistant that helps identify suitable employees from an internal database based on user queries. It leverages semantic search using FAISS and Sentence Transformers, and generates human-like recommendations via the LLaMA 3 model running locally through Ollama.

## Features
- 🔍 Semantic employee search with Sentence Transformers + FAISS
- 🤖 Natural language responses from LLaMA 3 via Ollama
- ⚡ FastAPI backend serving a REST API
- 🖥️ Streamlit frontend for interactive chat
- 🧩 Extensible architecture for models, data, or logic

## Architecture
- **Frontend**: Streamlit app for query input and result display
- **Backend**: FastAPI server with endpoints for chat and search
- **Semantic Search**: Employee embeddings indexed using FAISS
- **LLM Response**: Uses Ollama’s local API to call LLaMA 3
- **Data**: Local JSON file (`employees.json`) containing employee records

## Setup & Installation

### Prerequisites
- Python 3.9+
- Ollama installed (`https://ollama.com/download`)

### 1. Clone the Repository
```bash
git clone https://github.com/your-org/hr-chatbot.git
cd hr-chatbot
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Pull LLaMA 3 via Ollama
```bash
ollama pull llama3
```

### 5. Start FastAPI Backend
```bash
uvicorn main:app --reload
```

### 6. Run Streamlit Frontend
```bash
streamlit run app.py
```

## API Documentation

### `POST /chat`
**Description**: Takes a user query, finds top employee matches, and returns a natural language response.

**Payload:**
```json
{
  "query": "Looking for a React developer with AWS"
}
```

**Response:**
```json
{
  "response": "Based on your request, Alice Johnson and Priya Singh are great fits...",
  "matches": [ ... ]
}
```

### `GET /employees/search?skill=Python`
**Description**: Returns all employees with the specified skill.

**Response:**
```json
[
  {
    "name": "Alice Johnson",
    "skills": ["Python", "React", "AWS"],
    ...
  },
  ...
]
```

## AI Development Process

- **Tools Used**: ChatGPT, GitHub Copilot
- **Phases Supported**:
  - *Code generation*: Initial drafts for FastAPI, Streamlit, and FAISS logic
  - *Debugging*: Helped resolve embedding shape mismatches, request formats
  - *Architecture*: Suggestions for modular design between API, model, and UI
- **Estimated AI Contribution**: ~70% of code was AI-assisted, 30% hand-written
- **Notable AI Contributions**:
  - Prompt design for LLaMA3 integration
  - Semantic search using FAISS and sentence-transformers
- **Manual Work**:
  - Streamlit layout tuning
  - Final prompt tuning for professional tone
  - Fixing request failures due to mismatched embedding input formats

## Technical Decisions

- **Local vs Cloud LLM**: Ollama was chosen for local inferencing to avoid latency, API cost, and ensure data privacy.
- **Why LLaMA 3**: Balanced performance, local availability, and compatibility with Ollama.
- **FAISS for similarity search**: Fast and scalable for small to mid-size datasets.
- **Trade-offs**:
  - Local LLMs need hardware support (RAM/CPU)
  - Higher control vs slower first-time setup

## Future Improvements

- 🔄 Stream LLM responses with real-time feedback
- 📊 Add analytics for employee search frequency
- 🧠 Support multiple LLMs (e.g., Gemini, GPT-4)
- 🗃 Move to a real database (e.g., PostgreSQL)
- 🔐 User authentication for access control
