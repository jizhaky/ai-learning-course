# Week 4: Text Prediction

## Objective

Build a tiny character-level text generator and see how probabilities turn into creative-looking output.

## Required Videos

- Andrej Karpathy: “makemore” Part 1
- Optional: rewatch the section on sampling after you run the script

## Tasks

1. Run `python week4_textgen.py`.
2. Generate at least three samples.
3. Change the temperature or start prompt.
4. Add one or two of your own lines to `tiny_dataset.txt` and regenerate.

## Deliverables

- Three generated text samples
- One note about how the dataset affected the output
- One note about what temperature changed

## Checkpoint Questions

- What probabilities is the model using to choose the next character?
- Why does a tiny dataset limit the quality of the model?
- What does temperature do during sampling?
- Why can output sound coherent even when the model is small?

## Stretch Idea

Try replacing the simple bigram logic with a trigram context and compare output quality.
