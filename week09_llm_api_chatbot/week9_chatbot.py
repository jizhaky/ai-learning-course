"""Week 9: simple CLI chatbot using a local environment variable."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request

from dotenv import load_dotenv


API_URL = "https://api.openai.com/v1/chat/completions"


def chat_completion(api_key: str, model: str, messages: list[dict[str, str]]) -> str:
    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.7,
    }

    request = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=60) as response:
        data = json.loads(response.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"].strip()


def main() -> None:
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    if not api_key:
        raise SystemExit(
            "Missing OPENAI_API_KEY. Copy .env.example to .env and add your key."
        )

    system_prompt = (
        "You are a helpful AI coach for a teenager learning how machine learning works. "
        "Be encouraging, concise, and concrete. Prefer examples over jargon."
    )
    messages: list[dict[str, str]] = [{"role": "system", "content": system_prompt}]

    print("CLI chatbot ready. Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"quit", "exit"}:
            print("Goodbye.")
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        try:
            reply = chat_completion(api_key, model, messages)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            print(f"API error {exc.code}: {body}")
            continue
        except Exception as exc:  # pragma: no cover - local script behavior
            print(f"Request failed: {exc}")
            continue

        print(f"Bot: {reply}\n")
        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
