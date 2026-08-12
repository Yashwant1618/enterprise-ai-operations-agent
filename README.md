# Enterprise AI Operations Assistant

A RAG-based AI assistant that answers HR policy questions from an internal
HR policy document.

## What I built

I built this project to understand how an enterprise AI assistant can retrieve
relevant information from company documents before generating an answer.

The application:
- Takes a question from the user
- Converts the question into an embedding
- Searches Pinecone for relevant HR policy content
- Sends the retrieved context to Gemini
- Displays the answer through a Streamlit interface

## Tech Stack

Python
Gemini
Pinecone
RAG
FastAPI
Streamlit
LangChain

## How it works

User Question
     ↓
Embedding
     ↓
Pinecone similarity search
     ↓
Relevant HR policy
     ↓
Gemini
     ↓
Answer

## Example

Question:
"How many paid leave days are employees entitled to?"

The assistant retrieves the relevant HR policy and returns the answer.

## Run locally

Create a virtual environment:

python -m venv .venv

Activate it:

.\.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Create a `.env` file:

GEMINI_API_KEY=your_key
PINECONE_API_KEY=your_key

Run the backend:

uvicorn main:app --reload

Run the frontend:

streamlit run streamlit_app.py

## Project Structure

app/
documents/
tests/
main.py
streamlit_app.py
requirements.txt

## What I learned

- Building a basic RAG pipeline
- Working with embeddings and vector search
- Integrating Gemini with an application
- Building APIs using FastAPI
- Creating an AI interface using Streamlit