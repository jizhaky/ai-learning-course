# 12-Week Syllabus

## Course Arc

The course moves from first principles to small systems:

1. neuron
2. training loop
3. backprop intuition
4. tiny text model
5. attention
6. GPT-style data prep
7. CPU-safe experimentation
8. PyTorch
9. API chatbot
10. local RAG
11. project proposal and prototype
12. polish, explain, and ship

## Dynamic Update Rule

This syllabus has a stable spine and a live layer.

- Stable spine: the 12-week sequence and build-first philosophy
- Live layer: new videos, repo changes, papers, and posts that should be folded into the right week or added as a current-events bonus

Always check `CURRENT_UPDATES.md` before starting a new week. That file is where the most recent additions should land.

## Week 1: Neural Network Basics

- Objective: Understand a single neuron as weighted inputs plus a nonlinearity.
- Deliverable: Run `week1_neuron.py` and write one paragraph explaining how the weights affect output.
- Checkpoints:
  - What does a weight do?
  - Why do we need an activation function?
  - What changes when one input gets larger?

## Week 2: Training And Gradients

- Objective: See gradient descent as repeated error correction.
- Deliverable: Run `week2_training.py`, generate a loss plot, and explain why the loss goes down.
- Checkpoints:
  - What is the loss measuring?
  - Why does the learning rate matter?
  - What happens if the learning rate is too large?

## Week 3: Micrograd

- Objective: Build intuition for backpropagation and computation graphs.
- Deliverable: Complete the guided modification exercise and annotate the key parts of Karpathy's `Value` class.
- Checkpoints:
  - What is a computation graph?
  - Why do gradients accumulate?
  - Why do we need a topological ordering for backprop?

## Week 4: Text Prediction

- Objective: Build a tiny character-level generator from scratch.
- Deliverable: Generate new text from `week4_textgen.py` and compare outputs before and after changing temperature or context length.
- Checkpoints:
  - What does the model actually learn from text?
  - What makes output repetitive or random?
  - Why is a bigger context sometimes helpful?

## Week 5: Attention

- Objective: Understand attention numerically before using big frameworks.
- Deliverable: Work through the notebook and explain the roles of queries, keys, and values in plain language.
- Checkpoints:
  - What score is attention computing?
  - Why do we use a weighted sum?
  - Why is attention better than looking at one token alone?

## Week 6: NanoGPT Data Prep

- Objective: Prepare tiny text data in a GPT-style workflow.
- Deliverable: Run `prepare_data.py` and inspect the generated training and validation files.
- Checkpoints:
  - Why split train and validation data?
  - Why tokenize text instead of keeping it as raw strings?
  - What information gets lost in tiny datasets?

## Week 7: NanoGPT CPU Experiments

- Objective: Practice disciplined experimentation with strict CPU limits.
- Deliverable: Fill out `experiment_log.md` for at least three runs and write one insight you trust.
- Checkpoints:
  - What counts as a fair comparison between runs?
  - Why should only one variable change at a time?
  - What does “small enough to finish” mean on a laptop?

## Week 8: PyTorch

- Objective: Rebuild familiar ideas using PyTorch tensors and modules.
- Deliverable: Train the small PyTorch model and explain which parts PyTorch handles automatically.
- Checkpoints:
  - What does autograd give you?
  - What still needs to be designed by the programmer?
  - Why is `model.train()` different from `model.eval()`?

## Week 9: LLM API Chatbot

- Objective: Call an external model safely using environment variables.
- Deliverable: Build a CLI chatbot that answers in a consistent style using a secret key from `.env`.
- Checkpoints:
  - Why should API keys never be hardcoded?
  - What should be logged and what should stay private?
  - What prompt changes produce better responses?

## Week 10: Local RAG

- Objective: Retrieve useful local notes before generating an answer.
- Deliverable: Run `week10_rag.py` and show which notes were retrieved for a question.
- Checkpoints:
  - What is the difference between retrieval and generation?
  - Why can RAG reduce hallucinations?
  - What are the weaknesses of simple keyword similarity?

## Week 11: Final Project Proposal

- Objective: Choose a realistic project and build a first version.
- Deliverable: Pick one idea, define scope, and adapt the template.
- Checkpoints:
  - Who is the user?
  - What is the smallest useful version?
  - What can be finished in two weeks?

## Week 12: Final Project Ship

- Objective: Polish the project, explain design choices, and demo it.
- Deliverable: A working local project, short demo, and retrospective.
- Checkpoints:
  - What worked?
  - What broke?
  - What would you improve with one more week?

## Required Videos And Readings

- Week 1: 3Blue1Brown, “But what is a Neural Network?”
- Week 2: 3Blue1Brown, “Gradient descent, how neural networks learn”
- Week 3: Andrej Karpathy, “The spelled-out intro to neural networks and backpropagation”
- Week 4: Andrej Karpathy, “makemore” Part 1
- Week 5: StatQuest or another short visual transformer attention explainer
- Week 6–7: Andrej Karpathy, “Let’s build GPT”
- Week 8: Official PyTorch 60-minute blitz sections on tensors, autograd, and training
- Week 9: OpenAI API quickstart or equivalent official API quickstart
- Week 10: A short RAG explainer video plus the provided notes
- Week 11–12: Watch one product demo from a small AI app and analyze its scope
