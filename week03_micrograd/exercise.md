# Guided Micrograd Exercise

Use the original micrograd code as your base reference. Then complete these tasks.

## Exercise A: Add ReLU

1. Add a `relu()` method to the `Value` class.
2. During the forward pass, output `0` when the input is negative and the input itself otherwise.
3. During the backward pass:
   - pass the gradient through unchanged if the input was positive
   - pass `0` backward if the input was negative

Write a quick test case:

- input `-2.0` should produce output `0`
- input `3.0` should produce output `3.0`

## Exercise B: Trace A Tiny Graph

Create values:

- `a = 2.0`
- `b = -3.0`
- `c = 10.0`
- `d = a * b + c`

Then:

1. Draw the graph.
2. Predict the sign of each gradient before calling backward.
3. Check your prediction after running backward.

## Exercise C: Explain A Gradient In Plain Language

Pick one gradient from your graph and finish this sentence:

“If I changed this value upward a tiny bit, the final output would likely ______ because ______.”

## Deliverable

Write a short note with:

- what you changed
- what worked
- what confused you
- one thing that feels clearer now
