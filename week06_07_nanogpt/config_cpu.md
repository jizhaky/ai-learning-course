# CPU-Safe Rules For NanoGPT Experiments

These rules are strict on purpose.

## Allowed

- Tiny text files
- Small context windows
- Small batch sizes
- Short runs meant for learning, not for leaderboard chasing
- Comparing one variable at a time

## Not Allowed

- Large datasets
- Long overnight training runs
- Huge vocab experiments without a reason
- Multi-hour runs “just to see what happens”
- Anything that overheats the laptop or makes the rest of the machine unusable

## Recommended Boundaries

- Context window: keep it small
- Batch size: tiny
- Number of steps: short enough to finish in minutes, not hours
- Model size: as small as possible while still teaching the concept

## Decision Rule

If an experiment will not help you learn a specific idea, do not run it.

## Co-Author Prompt

If a rule here feels too strict or not strict enough, propose a better rule and explain why.
