"""Prepare a tiny GPT-style dataset for CPU-safe experiments."""

from __future__ import annotations

from pathlib import Path
import json

import tiktoken


DEFAULT_CORPUS = """
Small models can still teach big lessons.
The goal is not to train the world's best GPT on a laptop.
The goal is to understand the workflow: text, tokens, batches, loss, and sampling.
Clear experiments beat vague ambition.
Changing one variable at a time produces better learning.
"""


def main() -> None:
    base_dir = Path(__file__).parent
    corpus_path = base_dir / "tiny_corpus.txt"

    if corpus_path.exists():
        text = corpus_path.read_text()
        source = str(corpus_path.name)
    else:
        text = DEFAULT_CORPUS.strip()
        source = "embedded default corpus"

    encoding = tiktoken.get_encoding("gpt2")
    tokens = encoding.encode(text)

    split_index = max(1, int(len(tokens) * 0.9))
    train_tokens = tokens[:split_index]
    val_tokens = tokens[split_index:]

    (base_dir / "train_tokens.txt").write_text(" ".join(map(str, train_tokens)))
    (base_dir / "val_tokens.txt").write_text(" ".join(map(str, val_tokens)))

    metadata = {
        "source": source,
        "tokenizer": "gpt2",
        "total_tokens": len(tokens),
        "train_tokens": len(train_tokens),
        "val_tokens": len(val_tokens),
        "first_20_tokens": tokens[:20],
    }
    (base_dir / "metadata.json").write_text(json.dumps(metadata, indent=2))

    print("Prepared tiny dataset")
    print("  source:", source)
    print("  total tokens:", len(tokens))
    print("  train tokens:", len(train_tokens))
    print("  val tokens:", len(val_tokens))
    print("  wrote:", base_dir / "train_tokens.txt")
    print("  wrote:", base_dir / "val_tokens.txt")
    print("  wrote:", base_dir / "metadata.json")


if __name__ == "__main__":
    main()
