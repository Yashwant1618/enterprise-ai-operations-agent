import os

from dotenv import load_dotenv
from pinecone import Pinecone
from app.embeddings import create_embedding

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index("enterprise-ai-operations")


def retrieve(question, top_k=3):
    query_vector = create_embedding(question)

    results = index.query(
        vector=query_vector,
        top_k=top_k,
        include_metadata=True
    )

    return results

if __name__ == "__main__":
    question = "How many paid leave days are employees entitled to?"

    results = retrieve(question)

    for match in results["matches"]:
        print("Score:", match["score"])
        print("Text:", match["metadata"]["text"])
        print()