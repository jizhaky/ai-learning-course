"""Week 8: a tiny PyTorch classifier on synthetic data."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import torch
from torch import nn


def make_dataset(seed: int = 7, n_per_class: int = 80) -> tuple[torch.Tensor, torch.Tensor]:
    rng = np.random.default_rng(seed)
    class_a = rng.normal(loc=(-1.4, -1.0), scale=(0.45, 0.45), size=(n_per_class, 2))
    class_b = rng.normal(loc=(1.2, 1.1), scale=(0.45, 0.45), size=(n_per_class, 2))

    features = np.vstack([class_a, class_b]).astype(np.float32)
    labels = np.concatenate([np.zeros(n_per_class), np.ones(n_per_class)]).astype(np.float32)

    return torch.from_numpy(features), torch.from_numpy(labels).unsqueeze(1)


def build_model(hidden_size: int = 16) -> nn.Module:
    return nn.Sequential(
        nn.Linear(2, hidden_size),
        nn.Tanh(),
        nn.Linear(hidden_size, 1),
    )


def main() -> None:
    torch.manual_seed(7)
    device = torch.device("cpu")
    features, labels = make_dataset()
    features, labels = features.to(device), labels.to(device)

    model = build_model().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.05)
    loss_fn = nn.BCEWithLogitsLoss()

    losses: list[float] = []
    epochs = 200

    for epoch in range(epochs):
        model.train()
        logits = model(features)
        loss = loss_fn(logits, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        losses.append(float(loss.item()))
        if epoch % 25 == 0 or epoch == epochs - 1:
            print(f"epoch={epoch:03d} loss={loss.item():.4f}")

    model.eval()
    with torch.no_grad():
        probs = torch.sigmoid(model(features))
        predictions = (probs >= 0.5).float()
        accuracy = (predictions == labels).float().mean().item()

    output_path = Path(__file__).with_name("week8_loss_curve.png")
    plt.figure(figsize=(7, 4))
    plt.plot(losses, color="tab:green", linewidth=2)
    plt.title("PyTorch Training Loss")
    plt.xlabel("Epoch")
    plt.ylabel("Binary cross-entropy")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print(f"\nFinal accuracy: {accuracy * 100:.2f}%")
    print(f"Saved loss curve to: {output_path}")


if __name__ == "__main__":
    main()
