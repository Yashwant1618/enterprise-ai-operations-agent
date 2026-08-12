import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def create_embedding(text):
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return result.embeddings[0].values


if __name__ == "__main__":
    text = "Employees are entitled to 20 paid leave days."

    vector = create_embedding(text)

    print("Embedding generated successfully!")
    print("Number of dimensions:", len(vector))
    print("First 10 values:", vector[:10])