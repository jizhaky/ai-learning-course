"""Week 1: a single neuron with weights and an activation function."""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class Neuron:
    weights: list[float]
    bias: float

    def raw_score(self, inputs: list[float]) -> float:
        if len(inputs) != len(self.weights):
            raise ValueError("Number of inputs must match number of weights.")
        return sum(weight * value for weight, value in zip(self.weights, inputs)) + self.bias

    def activate(self, score: float) -> float:
        # tanh squashes the score into the range [-1, 1]
        return math.tanh(score)

    def __call__(self, inputs: list[float]) -> tuple[float, float]:
        score = self.raw_score(inputs)
        return score, self.activate(score)


def describe_prediction(activated_score: float) -> str:
    if activated_score > 0.5:
        return "strong yes"
    if activated_score > 0.0:
        return "weak yes"
    if activated_score > -0.5:
        return "weak no"
    return "strong no"


def main() -> None:
    neuron = Neuron(weights=[0.8, -0.4, 0.6], bias=-0.1)

    examples = [
        ("studied hard, slept well, anxious", [1.0, 0.2, 0.1]),
        ("did not study, distracted, confident", [0.1, 1.0, 0.8]),
        ("studied some, calm, focused", [0.6, 0.1, 0.9]),
    ]

    print("Single neuron demo\n")
    print("Weights:", neuron.weights)
    print("Bias:", neuron.bias)
    print()

    for label, inputs in examples:
        raw, activated = neuron(inputs)
        print(f"Example: {label}")
        print(f"  inputs      = {inputs}")
        print(f"  raw score   = {raw:.4f}")
        print(f"  activated   = {activated:.4f}")
        print(f"  interpretation: {describe_prediction(activated)}")
        print()

    print("Try editing the weights, bias, or example inputs and rerun the script.")


if __name__ == "__main__":
    main()
