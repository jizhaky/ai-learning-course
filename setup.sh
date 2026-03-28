#!/usr/bin/env bash
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"

echo "Creating virtual environment with ${PYTHON_BIN}..."
"${PYTHON_BIN}" -m venv .venv

echo "Activating environment..."
source .venv/bin/activate

echo "Upgrading pip..."
python -m pip install --upgrade pip

echo "Installing requirements..."
python -m pip install -r requirements.txt

echo
echo "Setup complete."
echo "Next steps:"
echo "  1. source .venv/bin/activate"
echo "  2. python run_checks.py"
echo "  3. open week01_neural_network_basics/README.md"
