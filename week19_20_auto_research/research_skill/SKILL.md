# Research Skill

## Purpose
Conduct thorough web research on a topic and produce a well-sourced report.

## When to Use
When the user:
- Starts a message with "Research:" or "Look up:"
- Asks a factual question that benefits from multiple sources
- Asks you to "find out about" or "investigate" something

## Behavior

### Research Process
1. **Clarify the question**: Make sure you understand what the user is asking. If ambiguous, ask one clarifying question.
2. **Plan searches**: Come up with 2-3 different search queries that approach the topic from different angles.
3. **Search**: Use `web_search` for each query.
4. **Read sources**: Use `web_fetch` to read the most promising 3-5 results.
5. **Extract facts**: Pull out key facts, data points, and quotes. Note which source each fact came from.
6. **Synthesize**: Combine everything into a clear, organized report.
7. **Cite sources**: Include numbered source URLs at the bottom.

### Output Format

```
## [Topic]

[2-3 sentence overview]

### [Section 1]
- Key point (source: [1])
- Key point (source: [2])

### [Section 2]
- Key point (source: [1])
- Key point (source: [3])

### Key Takeaway
[1-2 sentence summary of the most important finding]

### Sources
1. [URL] - [Brief description]
2. [URL] - [Brief description]
3. [URL] - [Brief description]
```

### Quality Rules
- Include at least 3 distinct sources
- Never present information from only one source as fact
- If sources disagree, say so and explain both sides
- Include specific numbers, dates, and facts — not just vague summaries
- Keep the report between 200-500 words unless the user asks for more
- Always end with a "Sources" section with clickable URLs

## Tools
- `web_search`: Search the web for information
- `web_fetch`: Read the full content of a web page

## Examples

**User**: Research: What are the health benefits of intermittent fasting?

**Agent**:
## Health Benefits of Intermittent Fasting

Intermittent fasting (IF) is an eating pattern that cycles between periods of fasting and eating. Research has shown several potential health benefits.

### Weight Management
- IF can reduce calorie intake by 10-25% and increase metabolic rate by 3.6-14% (source: [1])
- Studies show average weight loss of 3-8% over 3-24 weeks (source: [2])

### Metabolic Health
- May reduce insulin resistance and lower blood sugar levels (source: [1])
- Can reduce inflammation markers in the body (source: [3])

### Brain Health
- May increase growth of new nerve cells (source: [2])
- Animal studies show potential protection against Alzheimer's (source: [3])

### Important Caveats
- Not recommended for pregnant women, children, or people with eating disorders (source: [1])
- Results vary significantly between individuals (source: [2])

### Key Takeaway
IF shows promising health benefits, especially for weight management and metabolic health, but it's not suitable for everyone and more long-term human studies are needed.

### Sources
1. [URL] - Healthline overview of IF research
2. [URL] - Harvard Health review
3. [URL] - NIH research summary
