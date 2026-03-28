"""
Week 14: Tool Implementations
==============================
Real tool functions that the agent can call.
Each function takes simple arguments and returns a string result.
"""

import os
import urllib.request
import urllib.error
import html.parser


class HTMLTextExtractor(html.parser.HTMLParser):
    """Simple HTML parser that extracts visible text."""

    def __init__(self):
        super().__init__()
        self.result = []
        self._skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "head"):
            self._skip = True

    def handle_endtag(self, tag):
        if tag in ("script", "style", "head"):
            self._skip = False

    def handle_data(self, data):
        if not self._skip:
            text = data.strip()
            if text:
                self.result.append(text)

    def get_text(self):
        return "\n".join(self.result)


def web_search(url: str) -> str:
    """
    Fetches a URL and returns the text content.
    Strips HTML tags so Claude gets readable text.

    Args:
        url: The full URL to fetch (must start with http:// or https://)

    Returns:
        The text content of the page, or an error message.
    """
    try:
        if not url.startswith(("http://", "https://")):
            return f"Error: URL must start with http:// or https://. Got: {url}"

        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (AI Learning Course Agent)"},
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            raw = response.read().decode("utf-8", errors="replace")

        # Strip HTML tags to get readable text
        extractor = HTMLTextExtractor()
        extractor.feed(raw)
        text = extractor.get_text()

        # Truncate if too long (Claude has context limits)
        if len(text) > 5000:
            text = text[:5000] + "\n\n[... truncated — page was too long ...]"

        return text if text else "Page loaded but no readable text found."

    except urllib.error.HTTPError as e:
        return f"HTTP Error {e.code}: {e.reason}"
    except urllib.error.URLError as e:
        return f"URL Error: {e.reason}"
    except Exception as e:
        return f"Error fetching URL: {e}"


def read_file(file_path: str) -> str:
    """
    Reads a local file and returns its contents.

    Args:
        file_path: Path to the file to read.

    Returns:
        The file contents, or an error message.
    """
    try:
        # Security: don't allow reading sensitive files
        blocked = [".env", "id_rsa", "id_ed25519", ".ssh", "passwd", "shadow"]
        if any(b in file_path.lower() for b in blocked):
            return "Error: cannot read sensitive files (.env, SSH keys, etc.)"

        if not os.path.exists(file_path):
            return f"Error: file not found: {file_path}"

        with open(file_path, "r") as f:
            content = f.read()

        if len(content) > 5000:
            content = content[:5000] + "\n\n[... truncated ...]"

        return content

    except Exception as e:
        return f"Error reading file: {e}"


def calculate(expression: str) -> str:
    """
    Evaluates a math expression safely.

    Args:
        expression: A math expression like "42 * 67 + 13" or "2**10".

    Returns:
        The result as a string, or an error message.
    """
    allowed_chars = set("0123456789+-*/.() eE")
    if not all(c in allowed_chars for c in expression):
        return "Error: only numbers and math operators (+-*/.()) are allowed."

    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"


# TODO: Add your own tool function here!
# Some ideas:
#
# def list_directory(path: str) -> str:
#     """List files in a directory."""
#     ...
#
# def get_weather(city: str) -> str:
#     """Fetch weather from wttr.in."""
#     url = f"https://wttr.in/{city}?format=3"
#     ...
