# Micrograd Notes

## What To Focus On

Micrograd is small enough that you can actually read the whole thing. That is its power.

Focus on these ideas:

## 1. A `Value` Is More Than A Number

Each object stores:

- the numeric data
- the gradient
- the parents that produced it
- the operation used to create it
- a backward function

That means the program keeps both the answer and the history of how the answer was made.

## 2. Local Derivatives Build Global Learning

Each operation only needs to know how to push gradients to its direct parents.

Examples:

- addition sends the same gradient backward to both parents
- multiplication sends each parent the other parent's value times the gradient

Backprop works because many small local rules combine into a full-chain update.

## 3. Graph Order Matters

You cannot compute gradients backward from a node before the nodes after it are ready. That is why a topological ordering is useful.

## 4. Gradients Accumulate

If a node affects the output through more than one path, it must add gradient contributions together. This is one of the most important ideas in the whole course.

## 5. The Point Of The Exercise

You are not learning micrograd to become a micrograd expert. You are learning it so larger frameworks feel less mysterious later.

## Questions To Ask While Studying

- What exact rule is this operation using during backward?
- Where is the chain rule hiding here?
- If I changed this value slightly, how would the output react?
- Which line of code actually stores the gradient?
