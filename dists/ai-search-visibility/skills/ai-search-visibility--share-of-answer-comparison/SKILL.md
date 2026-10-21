---
name: ai-search-visibility--share-of-answer-comparison
description: "Use when the user asks how often they come up compared to rivals, or wants a scoreboard they can show someone."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["ai-search-visibility", "grok-bot", "from-grok-bot-team", "marketing"]
    related_skills: ["ai-search-visibility--getting-started", "ai-search-visibility--build-the-prompt-list", "ai-search-visibility--run-a-visibility-check", "ai-search-visibility--capture-a-pasted-answer", "ai-search-visibility--weekly-visibility-brief", "ai-search-visibility--citation-source-audit"]
---
# Share of answer comparison

Inputs: every capture you have, the prompt list, and the rival names.

1. Count, across the most recent run: for the user and for each rival, how many prompts recommended them, cited them, mentioned them, and left them out.
2. Build one table. A row per company, a column per rung on the ladder, and a last column for the share of prompts where they were recommended or cited.
3. Break it out by prompt kind: category, problem, comparison, brand. A company can own comparison prompts and be invisible on problem prompts, and that gap is the whole point of the table.
4. Break it out by surface too when you have three or more, since an assistant and a search result often disagree, and the disagreement tells them where to spend.
5. Add the trend when you have two or more runs: movement per company since the last run. Call a trend only with three or more runs. Below that, say you are pointing at a direction.
6. Write three to five lines under the table: where the user is strongest, the prompt kind they are weakest on, which rival is gaining, and what the table does not tell them.

Rules: only count what a capture shows. Never fill a cell from an older run without marking the date it came from. A one-word difference in how an answer is phrased is not a change in position, so do not score it as one.

Save the scoreboard dated under the visibility folder and attach it.
