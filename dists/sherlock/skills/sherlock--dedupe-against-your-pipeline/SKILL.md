---
name: sherlock--dedupe-against-your-pipeline
description: "Use when the user already has candidates in play, pastes an ATS export or a list, or asks whether you are about to surface someone they know."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["sherlock", "grok-bot", "from-grok-bot-team", "recruiting-people"]
    related_skills: ["sherlock--getting-started", "sherlock--read-the-role", "sherlock--source-a-batch", "sherlock--lookalike-search", "sherlock--draft-outreach", "sherlock--shortlist-review"]
---
# Dedupe against your pipeline

Inputs: an ATS export as CSV, a spreadsheet or a link, a pasted list of names, or forwarded notes. Ashby, Greenhouse, Lever, Workable, and the rest all export CSV, so ask for the export rather than a login. With Google Sheets connected, read the sheet in place and say which tab and which columns you used.

1. Say which columns you found before you change anything.
2. Map them onto: name, current company, role they are in play for, stage, last touch date, owner, and do not contact.
3. Match against the shortlist on name plus current company. Normalize case, accents, punctuation, and common nickname forms before you compare.
4. Near matches, same name at a different company or the same company spelled two ways, go into a short "check these" list. Never merge two people on a hunch.
5. Mark everyone in the pipeline as already in play so batches skip them, and carry the stage and the owner across so the user knows who has them.
6. Anyone marked do not contact stays out of every batch, every draft, every recap, and every shared list. Keep their name and that flag, nothing else.
7. Report the numbers: rows read, matched, near matches to check, and new.

No export at all is fine. Ask for whoever is already in play, first name and company is enough, and treat that as the list until something better arrives.

Never write anything back into their ATS. You read the export, you do not manage their system of record.

Save under the search folder.
