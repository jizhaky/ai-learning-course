"""Environment check for the AI learning syllabus."""

from __future__ import annotations

import importlib
import platform
import sys


REQUIRED_PACKAGES = [
    ("numpy", "numpy"),
    ("matplotlib", "matplotlib"),
    ("torch", "torch"),
    ("tiktoken", "tiktoken"),
    ("python-dotenv", "dotenv"),
]


def main() -> int:
    print("Python executable:", sys.executable)
    print("Python version:", platform.python_version())

    if sys.version_info < (3, 11):
      print("ERROR: Python 3.11 or newer is required.")
      return 1

    print("\nPackage imports:")
    for label, module_name in REQUIRED_PACKAGES:
        try:
            module = importlib.import_module(module_name)
        except Exception as exc:  # pragma: no cover - local environment script
            print(f"  - {label}: FAILED ({exc})")
            return 1
        else:
            version = getattr(module, "__version__", "unknown")
            print(f"  - {label}: OK ({version})")

    import torch  # imported above, kept here for readability

    print("\nTorch device info:")
    print("  - torch version:", torch.__version__)
    print("  - CUDA available:", torch.cuda.is_available())
    print("  - MPS available:", torch.backends.mps.is_available())
    preferred_device = "mps" if torch.backends.mps.is_available() else "cpu"
    print("  - Preferred local device for this course:", preferred_device)
    print("\nEnvironment check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
