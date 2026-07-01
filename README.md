# SHL Assessment Recommendation Chatbot

## Overview

This project is an AI-powered chatbot that recommends and compares SHL assessments based on hiring requirements.

It uses:

- FastAPI
- Google Gemini
- Sentence Transformers
- Hybrid Retrieval (Keyword + Embeddings)

---

## Features

- Recommend SHL assessments
- Compare two SHL assessments
- Multi-turn conversation support
- Intent detection
- Off-topic refusal
- Swagger API documentation

---

## Tech Stack

- Python 3.11
- FastAPI
- Google Gemini
- Sentence Transformers
- FAISS
- Uvicorn

---

## Installation

```bash
git clone <repository-url>

cd shl-assessment-agent

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Run:

```bash
uvicorn app.main:app --reload
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

## API

### GET /health

Returns

```json
{
    "status":"ok"
}
```

---

### POST /chat

Example

```json
{
  "messages":[
    {
      "role":"user",
      "content":"Looking for a Python developer"
    }
  ]
}
```

---

## Project Structure

```
app/
    main.py
    models.py
    scraper.py
    retriever.py
    chatbot_service.py
    comparison_service.py
    conversation_manager.py
    embeddings.py
    gemini_client.py

data/
    shl_catalog.json

requirements.txt
README.md
```

---

## Future Improvements

- Better semantic ranking
- Dynamic comparison extraction
- Deployment with Docker
- Authentication