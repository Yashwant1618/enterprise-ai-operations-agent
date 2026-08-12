import os

from dotenv import load_dotenv
from pinecone import Pinecone
from embeddings import create_embedding
from document_loader import load_document, chunk_text

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index("enterprise-ai-operations")


def store_chunks(chunks):
    for i, chunk in enumerate(chunks, start=1):
        vector = create_embedding(chunk)

        index.upsert(
            vectors=[
                {
                    "id": f"chunk-{i}",
                    "values": vector,
                    "metadata": {
                        "text": chunk
                    }
                }
            ]
        )

    print(f"{len(chunks)} chunks stored successfully!")


if __name__ == "__main__":
    text = load_document("../documents/hr_policy.txt")

    chunks = chunk_text(text)

    print(f"Number of chunks: {len(chunks)}")

    store_chunks(chunks)

    print(index.describe_index_stats())

