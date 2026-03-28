# Attention Notes

## Core Idea

Attention is a smart lookup rule. The current token asks, “Which earlier pieces of information matter most right now?”

## What To Notice In The Notebook

- The query is fixed for the current step.
- Each key gets a score based on how well it matches the query.
- The scores become weights after normalization.
- The final output is not just one value vector. It is a weighted mix.

## Why This Matters

Without attention, a model has a harder time deciding which earlier words are relevant. With attention, it can re-focus for each new token.

## Questions To Answer In Your Own Words

- Why do the weights add up to 1?
- Why can one token matter more than another?
- What would happen if all scores were almost the same?
- How is this different from just averaging all values?

## Co-Author Prompt

If this notebook felt too easy, too hard, or too abstract, write down one specific change that would improve it for the next student.
