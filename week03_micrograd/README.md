# Week 3: Micrograd

## Objective

Study a tiny autodiff engine closely enough that backprop stops feeling like magic.

## Required Videos

- Andrej Karpathy: “The spelled-out intro to neural networks and backpropagation”
- Optional: revisit Week 2 before watching if gradients still feel abstract

## Tasks

1. Read `micrograd_notes.md`.
2. Watch the required Karpathy video with a notebook open.
3. Complete the guided exercise in `exercise.md`.
4. Draw one small computation graph by hand and annotate the gradient flow.

## Deliverables

- Annotated notes on the `Value` object
- A completed exercise with your own comments
- One hand-drawn or typed computation graph

## Checkpoint Questions

- Why does each `Value` need to know its parents?
- Why do gradients add together from multiple paths?
- What happens if backward passes happen in the wrong order?
- What did micrograd make clearer than Week 2?

## Suggested Workflow

Do not rush. Pause the video whenever the graph grows and trace the local derivative yourself.
