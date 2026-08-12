import os

from dotenv import load_dotenv
from google import genai
from app.retriever import retrieve


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_context(question):
    results = retrieve(question)

    context = ""

    for match in results["matches"]:
        context += match["metadata"]["text"] + "\n"

    return context


def generate_answer(question):
    context = get_context(question)

    prompt = f"""
You are an HR policy assistant.

Answer the user's question using only the information provided
in the context below.

If the answer is not available in the context, say:
"I could not find this information in the HR policy."

Context:
{context}

User question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    question = "How many paid leave days are employees entitled to?"

    answer = generate_answer(question)

    print("Answer:")
    print(answer)