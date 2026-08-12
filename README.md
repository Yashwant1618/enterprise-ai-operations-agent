# Enterprise AI Operations Assistant

A Retrieval-Augmented Generation (RAG) based AI assistant for answering enterprise HR policy questions using a company knowledge base.

The application combines document processing, embeddings, vector search, LLM-based response generation, FastAPI, and a Streamlit web interface to provide grounded answers from enterprise policy documents.

---

## Project Overview

Enterprise employees often need quick answers to questions related to company policies and procedures.

This project demonstrates how Generative AI and RAG can be used to build an enterprise knowledge assistant that retrieves relevant information from internal documents before generating an answer.

The assistant is currently configured with an HR policy knowledge base.

Example questions include:

- How many paid leave days are employees entitled to?
- What is the procedure for taking 5 days off?
- How should emergency leave be communicated?

---

## Key Features

- Document loading and text processing
- Text chunking for knowledge retrieval
- Semantic embeddings
- Vector storage using Pinecone
- Similarity-based document retrieval
- Retrieval-Augmented Generation (RAG)
- Gemini-powered answer generation
- FastAPI backend
- Streamlit web interface
- Example questions for users
- Loading and error handling
- Out-of-scope question handling
- Grounded responses based on the available HR policy

---

## Architecture

```text
                    HR Policy Document
                           |
                           v
                  Document Processing
                           |
                           v
                    Text Chunking
                           |
                           v
                    Gemini Embeddings
                           |
                           v
                       Pinecone
                    Vector Database
                           |
                           |
User ---> Streamlit ---> FastAPI
                           |
                           v
                    RAG Retrieval
                           |
                           v
                  Relevant HR Context
                           |
                           v
                         Gemini
                           |
                           v
                    Generated Answer
                           |
                           v
                      Streamlit UI