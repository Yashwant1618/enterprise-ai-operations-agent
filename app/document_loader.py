from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_document(file_path: str) -> str:
    return Path(file_path).read_text(encoding="utf-8")


def chunk_text(text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_text(text)


if __name__ == "__main__":
    text = load_document("../documents/hr_policy.txt")

    chunks = chunk_text(text)

    for i, chunk in enumerate(chunks, start=1):
        print(f"\n--- Chunk {i} ---")
        print(chunk)