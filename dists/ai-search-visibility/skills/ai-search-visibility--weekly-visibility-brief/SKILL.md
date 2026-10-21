---
name: ai-search-visibility--weekly-visibility-brief
description: "Use when the user asks how their visibility changed, or when the weekly brief routine runs."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["ai-search-visibility", "grok-bot", "from-grok-bot-team", "marketing"]
    related_skills: ["ai-search-visibility--getting-started", "ai-search-visibility--build-the-prompt-list", "ai-search-visibility--run-a-visibility-check", "ai-search-visibility--capture-a-pasted-answer", "ai-search-visibility--citation-source-audit", "ai-search-visibility--share-of-answer-comparison"]
---
# Weekly visibility brief

Inputs: today's capture, the previous capture, the spot check log, the prompt list, and what the user sells.

1. Open with one line: the date range, how many prompts you ran, and how many of them recommended them at all.
2. What moved. One block per prompt that changed, with the old rung, the new rung, the quoted sentence, and the source link. No block for a prompt that sat still.
3. Who is winning. The three names that appeared most across the run, each with a count and one line on what the answers credit them for.
4. So what. Two to four lines written for this user's job. Dropping out of a comparison prompt reads differently from never appearing on a category prompt, so say which one this is. Say it is unclear when it is unclear.
5. One thing to do this week. A single change, named specifically: a page to write, a page to fix, a source to get listed on. Pull it from the citation audit when you have one, and offer to draft it.
6. Sources and gaps. Every link you pulled, and any prompt still waiting on a paste, with the prompt written out so they can copy it.

Rules: no claim without a quote and a link. Never pad the brief to look busy. A week with nothing moving gets one line saying visibility held steady and where they stand, not a full brief. Fold in anything the spot check already reported instead of reporting it twice.

Save the brief dated under the visibility folder and attach it here, then deliver it to the destination the user picked. Anything that posts or emails goes to them as a draft first.
