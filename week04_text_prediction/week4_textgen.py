"""Week 4: a tiny character-level text generator."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import random


def load_lines() -> list[str]:
    dataset_path = Path(__file__).with_name("tiny_dataset.txt")
    return [line.strip() for line in dataset_path.read_text().splitlines() if line.strip()]


def build_bigram_counts(lines: list[str]) -> dict[str, Counter[str]]:
    counts: dict[str, Counter[str]] = defaultdict(Counter)

    for line in lines:
        text = "^" + line + "$"
        for current_char, next_char in zip(text, text[1:]):
            counts[current_char][next_char] += 1

    return counts


def sample_next(counter: Counter[str], temperature: float) -> str:
    chars = list(counter.keys())
    weights = []
    for count in counter.values():
        scaled = count ** (1.0 / max(temperature, 1e-6))
        weights.append(scaled)
    return random.choices(chars, weights=weights, k=1)[0]


def generate_text(
    counts: dict[str, Counter[str]],
    start: str = "",
    max_length: int = 80,
    temperature: float = 1.0,
) -> str:
    if not start:
        current_char = "^"
        generated = []
    else:
        generated = list(start)
        current_char = start[-1]

    for _ in range(max_length):
        options = counts.get(current_char) or counts["^"]
        next_char = sample_next(options, temperature)
        if next_char == "$":
            break
        generated.append(next_char)
        current_char = next_char

    return "".join(generated)


def main() -> None:
    random.seed(7)
    lines = load_lines()
    counts = build_bigram_counts(lines)

    print("Loaded dataset lines:", len(lines))
    print("Vocabulary size:", len(counts))
    print()

    for temperature in (0.7, 1.0, 1.4):
        print(f"Temperature {temperature:.1f}")
        for _ in range(3):
            print("  ", generate_text(counts, temperature=temperature))
        print()

    print("Try editing tiny_dataset.txt and rerunning the script.")


if __name__ == "__main__":
    main()
