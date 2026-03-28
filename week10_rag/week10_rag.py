"""Week 10: local RAG using bag-of-words cosine similarity."""

from __future__ import annotations

from collections import Counter
from math import sqrt
from pathlib import Path
import re


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z']+", text.lower())


def vectorize(text: str) -> Counter[str]:
    return Counter(tokenize(text))


def cosine_similarity(a: Counter[str], b: Counter[str]) -> float:
    shared_words = set(a) & set(b)
    dot_product = sum(a[word] * b[word] for word in shared_words)
    norm_a = sqrt(sum(value * value for value in a.values()))
    norm_b = sqrt(sum(value * value for value in b.values()))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)


def load_chunks() -> list[str]:
    notes_path = Path(__file__).with_name("sample_notes.txt")
    return [chunk.strip() for chunk in notes_path.read_text().split("\n\n") if chunk.strip()]


def retrieve(question: str, chunks: list[str], top_k: int = 2) -> list[tuple[float, str]]:
    question_vector = vectorize(question)
    scored = []
    for chunk in chunks:
        score = cosine_similarity(question_vector, vectorize(chunk))
        scored.append((score, chunk))
    scored.sort(key=lambda item: item[0], reverse=True)
    return scored[:top_k]


def answer_question(question: str, retrieved_chunks: list[tuple[float, str]]) -> str:
    evidence = "\n\n".join(chunk for _, chunk in retrieved_chunks if chunk)
    return (
        "Answer draft based on retrieved notes:\n"
        f"{evidence}\n\n"
        "Now rewrite that evidence in your own words."
    )


def main() -> None:
    chunks = load_chunks()
    print("Local RAG demo ready. Type 'quit' to exit.\n")

    while True:
        question = input("Question: ").strip()
        if question.lower() in {"quit", "exit"}:
            print("Goodbye.")
            break
        if not question:
            continue

        retrieved = retrieve(question, chunks)
        print("\nRetrieved chunks:")
        for rank, (score, chunk) in enumerate(retrieved, start=1):
            print(f"\n[{rank}] score={score:.3f}")
            print(chunk)

        print("\n" + answer_question(question, retrieved) + "\n")


if __name__ == "__main__":
    main()
