---
name: customer-stories--pull-proof-for-a-claim
description: "Use when the user needs the right quote, number, or customer example for a specific claim, slide, page, or objection they are handling."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["customer-stories", "grok-bot", "sales"]
    related_skills: ["customer-stories--getting-started", "customer-stories--add-sources-to-the-proof-bank", "customer-stories--mine-a-batch-of-calls", "customer-stories--write-a-case-study", "customer-stories--testimonials-and-pull-quotes", "customer-stories--build-a-deal-proof-one-pager"]
---
# Pull proof for a claim

Inputs: the claim they want to support, who the audience is, and the proof bank.

1. Make them state the claim in one sentence before you search. A vague ask gets a vague pull.
2. Search the bank for quotes and numbers that support that exact claim. Rank by how directly each one supports it, then by how recent it is, then by how recognizable the customer is to this audience.
3. Return three to five options. Each one: the quote or number word for word, who said it and when, the source, and one line on why it fits.
4. Say plainly when the bank has nothing that supports the claim. Offer the closest adjacent proof and name the gap. Never stretch a quote to cover a claim it does not make.
5. Flag anything not yet approved for public use, and anything older than 12 months, before it lands on a slide.
6. Offer the anonymized version of anything approved anonymized only, for example "a 200 person engineering team" in place of the name.

Output: the ranked options with attribution and approval state on each, then one line naming the strongest and why.

Fallbacks: an empty bank means run intake on whatever they can paste first, even one call. A claim about a competitor is out of scope, you only carry what customers said.
