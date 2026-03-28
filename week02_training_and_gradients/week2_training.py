"""Week 2: manual gradient descent on a tiny regression problem."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def make_dataset() -> tuple[np.ndarray, np.ndarray]:
    x = np.linspace(-2.0, 2.0, 25)
    y = 2.0 * x + 1.0
    return x, y


def train(
    x: np.ndarray,
    y: np.ndarray,
    learning_rate: float = 0.1,
    steps: int = 80,
) -> tuple[float, float, list[float]]:
    weight = -1.5
    bias = 0.0
    losses: list[float] = []

    for step in range(steps):
        predictions = weight * x + bias
        errors = predictions - y
        loss = float(np.mean(errors ** 2))
        losses.append(loss)

        # These are the analytical gradients of mean squared error.
        grad_weight = float(2.0 * np.mean(errors * x))
        grad_bias = float(2.0 * np.mean(errors))

        weight -= learning_rate * grad_weight
        bias -= learning_rate * grad_bias

        if step % 10 == 0 or step == steps - 1:
            print(
                f"step={step:02d} "
                f"loss={loss:.6f} "
                f"weight={weight:.4f} "
                f"bias={bias:.4f}"
            )

    return weight, bias, losses


def save_loss_plot(losses: list[float], output_path: Path) -> None:
    plt.figure(figsize=(7, 4))
    plt.plot(losses, color="tab:blue", linewidth=2)
    plt.title("Manual Gradient Descent Loss")
    plt.xlabel("Training step")
    plt.ylabel("Mean squared error")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def main() -> None:
    x, y = make_dataset()
    weight, bias, losses = train(x, y)

    output_path = Path(__file__).with_name("loss_curve.png")
    save_loss_plot(losses, output_path)

    print("\nFinal model:")
    print(f"  weight = {weight:.4f}")
    print(f"  bias   = {bias:.4f}")
    print(f"  sample prediction for x=1.5 -> {weight * 1.5 + bias:.4f}")
    print(f"\nSaved loss plot to: {output_path}")


if __name__ == "__main__":
    main()
