# Grok Bot marketplace bots for Hermes Agent

All 90 public [Grok Bot marketplace](https://x.ai/bot/marketplace) templates converted into [Hermes Agent](https://hermes-agent.nousresearch.com) **profile distributions**. Each bot becomes its own Hermes profile: a `SOUL.md` persona, the bot's skills as [agentskills.io](https://agentskills.io) `SKILL.md` folders, its routines as paused cron jobs, and a `config.yaml` you can point at Claude, Grok, Kimi or any other Hermes provider.

Templates belong to their creators on x.ai; every `SOUL.md` keeps the attribution line. This repo is a format conversion, nothing more.

## Install

A Hermes distribution needs `distribution.yaml` at the repo root, so with 90 bots in one repo you clone once and install from the local directories:

```
git clone https://github.com/brokep/grok-bots-for-hermes.git
cd grok-bots-for-hermes
./install.sh --list                      # browse
./install.sh human-copywriter prospector # install a few (profile grok-<slug> + shell alias)
./install.sh --all                       # all 90 profiles
grok-human-copywriter chat               # or: hermes -p grok-human-copywriter chat
```

Requires Hermes Agent 0.14 or newer (`hermes --version`). Verified on 0.15.0: install, skills index and cron list. No session has been run against a model.

## Keys and models

Each profile is its own Hermes home under `~/.hermes/profiles/grok-<slug>/` and does **not** read the root `~/.hermes/.env`. The installer writes `.env.EXAMPLE` beside the profile; copy it to `.env` and fill in the key for the provider you want:

```
ANTHROPIC_API_KEY=...   # provider anthropic   e.g. claude-opus-4-6, claude-sonnet-4-6
XAI_API_KEY=...         # provider xai         e.g. grok-4.3   (or `hermes auth add xai-oauth` with SuperGrok)
KIMI_API_KEY=...        # provider kimi-coding e.g. kimi-for-coding, kimi-k2.5
```

The shipped `config.yaml` defaults to `anthropic / claude-opus-4-6`. Change it per profile:

```
hermes -p grok-prospector model                            # interactive picker
hermes -p grok-prospector config set model.provider xai
hermes -p grok-prospector config set model.default grok-4.3
hermes -p grok-prospector fallback add                     # chain a second provider
/model kimi-for-coding                                     # inside a session
```

## Routines

`cron/jobs.json` ships one job per routine with a cron expression guessed from the routine's prose. Jobs arrive **paused**. Check each bot's `MAPPING.md`, fix the time, then resume:

```
hermes -p grok-x-brief cron list
hermes -p grok-x-brief cron edit <id>
hermes -p grok-x-brief cron resume <id>
```

## Integrations

Grok plugins (Gmail, Slack, Notion, Linear, GitHub, ...) map to MCP servers. Each `MAPPING.md` carries an `mcp_servers:` snippet for the known ones; paste it into the profile's `config.yaml`.

## Regenerate

`tools/gen_hermes.py` rebuilds `dists/` from `tools/bots_full.json` (the full templates, fetched from the marketplace's public RPC):

```
python3 tools/gen_hermes.py tools/bots_full.json build --provider xai --model grok-4.3
rm -rf dists && mv build/dists dists && cp build/catalog.json .
```

## Caveats

- Schedules are guesses. Review before resuming a job.
- Bot text still speaks in Grok terms (memory slots, files, "my skill"). The operating-rules section of each `SOUL.md` maps those to Hermes memory, the working directory and the skill tool.
- Profile names are `grok-<slug>`; installing all 90 makes `hermes profile list` long.

## Bots

| Slug | Name | Skills | Routines | Integrations | What it does |
|---|---|---|---|---|---|
| `account-book` | Account Research Desk | 11 | 3 | slack, notion-workspace, linear, hex, Databricks SQL, Gmail, Google Calendar, Granola, Google Drive, Google Sheets, Salesforce | Researches the companies you sell to and writes your pre-call brief and account plan. Works from the public web and the notes you paste, and never sends withou… |
| `fuse` | Ad Spend Watch | 9 | 3 | slack, notion-workspace, linear, hex, datadog, sentry, figma, Gmail, Google Sheets | Watches your ad spend and performance and flags what's breaking before it burns budget. Works from a pasted export, and never pauses a campaign without your ye… |
| `ai-search-visibility` | AI Search Visibility | 8 | 2 | slack, notion-workspace, linear, hex, Profound, Google Sheets | Checks whether AI assistants and Google recommend you, and who they name instead. Starts from a handful of questions your buyers actually ask. |
| `alfred` | Alfred | 6 | 3 |  | Designs, audits, and governs your Grok Bot organization so it matches real company outcomes, with clear human owners and no duplicate jobs. Recommends the smal… |
| `apple-search-ads-review` | Apple Search Ads Review | 7 | 2 | slack, notion-workspace, hex, Databricks SQL, linear, Gmail, Google Sheets | Reviews your Apple Search Ads spend against your cost per install target. Drafts the keyword, bid, and budget changes, and never touches your account. |
| `call-follow-ups` | Call Follow-Ups | 6 | 1 | Gong, Granola, Salesforce, HubSpot, Attio, Gmail, Outlook, Google Calendar, Slack, Notion, Linear, Hex | Turns each recorded call into a follow-up email in your voice, a next-steps note, and the CRM updates, including the qualification fields your team runs on. Wa… |
| `chief-health` | Chief Health | 0 | 2 |  | You're the Chief Health Officer. Every day, ask if training happened. If it did not, rewrite the next session so the week still holds. Read whatever workout ap… |
| `clip-bot` | Clip Bot | 6 | 2 | slack, notion-workspace, linear, figma | Finds the best moments in a long recording and cuts them into short captioned clips. Works from an upload or a link, with transcript and timestamps on every cl… |
| `company-docs-q-a` | Company Docs Q&A | 0 | 0 | Slack, Notion | Answers product and how-to questions from live docs first, then connected knowledge sources, and always cites sources. Built for anyone who wants a trustworthy… |
| `competitor-watching` | Competitor Watch | 5 | 2 | slack, notion-workspace, linear | Tracks competitor pricing, product, and hiring pages and briefs you on real changes. Starts from a list of URLs you paste. |
| `cooper` | Cooper | 0 | 3 | Slack | News agent for AI, tech, venture capital, and business. Delivers a tight daily Slack briefing of top stories at 8am, plus weekday mid-day competitor alerts onl… |
| `human-copywriter` | Copy Humanizer | 7 | 1 | notion-workspace, slack, figma, linear, Gmail | Edits and rewrites drafts, emails, and pages so they read like a person wrote them. Keeps your voice, shows every change and why, and never invents a fact. |
| `credit-card-max` | Credit Card Max | 2 | 3 |  | Credit card maxing with live Grok Finance (Plaid): which card to swipe given your priorities (points, cash back, airline/hotel status), statement-credit tracki… |
| `critiquito` | Critiquito: Design Critique | 7 | 1 | figma, slack, notion-workspace, linear | Turns a screenshot or Figma link into a design critique with ranked, concrete fixes. Covers hierarchy, type, color, copy, and accessibility, and never edits yo… |
| `customer-call-coach` | Customer Call Coach & Assistant | 0 | 1 | Granola, Slack, Gmail | Briefs you before customer calls and coaches you after based on your performance. |
| `customer-stories` | Customer Proof Desk | 11 | 2 | notion-workspace, slack, linear, figma, hex, Gmail, Granola | Turns call notes and transcripts into case studies, testimonials, and proof points. Quotes stay word for word from what you paste, and nothing publishes withou… |
| `dan-lanning` | Dan Lanning | 0 | 1 | Notion, Google Calendar | Pitch and delivery coach for partnership, sponsorship, and high-stakes discovery calls. Reviews real call transcripts and returns sharp, evidence-based coachin… |
| `deal-hunting` | Deal Hunting | 0 | 2 |  | Landed-cost shopping: real prices, shipping and tax, preferred retailers. Watchlist optional. Never buys unless asked. |
| `deal-qualification` | Deal Inspector | 4 | 1 | Gong, Granola, Salesforce, HubSpot, Attio, Slack, Gmail, Notion, Google Sheets | Checks every deal that moved stage against your qualification criteria using the actual call transcripts. Quotes the evidence, flags what is missing, recommend… |
| `dial-bot` | dial bot | 1 | 0 |  | Places outbound Bland AI phone calls when you ask, then reports what happened. On first use it asks for a Bland API key and voice. |
| `distro-bot` | Distro Bot | 7 | 4 | X, Gmail | Runs your marketing loop end to end: campaigns on your ad accounts, fresh creative, real channel analysis, timely posts from X and web scans, and outbound unti… |
| `dr-eggbot-v2` | dr eggbot | 4 | 2 | pstack | Designs high-quality Grok Bots. Asks a few preference questions, then creates them with CreateAgent. Coding bots get the poteto-mode bar (one job, unslopped, v… |
| `ebr-value-deck-builder` | EBR & Value Deck Builder | 5 | 1 | Salesforce, HubSpot, Attio, Gong, Mixpanel, Google Drive, OneDrive | Builds an executive business review or value deck for a named account from your CRM, call history, and usage data, on your brand, and hands you an editable fil… |
| `engineering-lead` | Engineering Lead | 5 | 0 |  | An engineering lead that owns the loop: breaks work into Cloud Agents, chases CI, reviews, and stalls on a weekday cadence, and only pings you when something i… |
| `event-producer` | Event Producer | 8 | 3 | slack, notion-workspace, linear, figma, Gmail, Google Calendar, Google Sheets | Turns your event details into a run of show, guest list, and day-of checklist. Tracks vendors, guests, dietary needs, and travel, and never sends a message wit… |
| `event-request-desk` | Event Request Desk | 8 | 3 | slack, notion-workspace, linear, figma, hex, Gmail, Google Calendar, Google Drive, Google Sheets | Scores every event, sponsorship, and speaking ask, then drafts your yes or no. Works from a Slack channel or a paste, and never sends without you. |
| `figma-bro` | figma bro | 8 | 2 | figma, notion-workspace, linear, slack | Turns a Figma frame into a build spec, and audits your components, tokens, and motion. Builds screens from a brief too, and works from a pasted link when Figma… |
| `flora` | Flora | 4 | 0 |  | Flora keeps a private houseplant care log and weekly reminders. She builds a plant journal on her computer that you can page through, and your plants do not co… |
| `frank` | frank | 0 | 4 | Google Calendar, Gmail, Slack, Notion, Google Sheets | EA chief-of-staff bot for exec support: conference rooms, interview prep, leadership outreach, Slack channel inventories, sheet↔calendar checks, and birthday/a… |
| `sable-game-art` | Game Art Director | 6 | 2 | figma, notion-workspace, slack, linear | Turns a game concept into a style guide, palettes, and prompt sheets for your image tool. Slices sprite sheets and checks your art for palette and grid drift. |
| `account-research` | GTM Account Research | 4 | 1 | Salesforce, Gmail, Google Calendar, Slack, Notion, Google Sheets, Granola | Researches one account before a meeting, deal review, or account plan. Brings together company changes, key people, relationship history, open questions, and t… |
| `warm-intro-finder` | GTM Connections | 3 | 1 | Gmail, Google Calendar, Salesforce, Notion, Google Sheets, Slack | Finds credible ways into a target account through mutual contacts, past conversations, shared history, and prior meetings. Ranks the best paths, drafts the int… |
| `follow-through-agent` | GTM Loop Closer | 5 | 1 | Salesforce, Gmail, Google Calendar, Slack, Granola, Notion, Google Sheets | Finds promises, follow-ups, and customer details left behind in meetings, email, Slack, CRM, or task tools. Shows the evidence and prepares the reply, task, or… |
| `prospector` | GTM Prospecting | 3 | 1 | Gmail, Google Sheets, Notion, Salesforce | Turns an ideal customer profile into a focused prospect list, adds useful context, and checks for existing relationships. Drafts first-touch email and LinkedIn… |
| `haggle-bot` | Haggle Bot | 6 | 2 | Ramp, Google Sheets, Gmail, Slack, Notion, Google Drive, Granola | Inventories your SaaS spend from Ramp and bills, finds evidence-backed savings (unused seats, duplicates, cheaper alternatives), and drafts vendor counters for… |
| `hiring-activity-monitor` | Hiring Signals | 3 | 1 | Google Sheets, Notion, Slack, Salesforce | Tracks hiring activity across selected companies and job sources. Highlights meaningful changes, matches them to accounts and owners, and passes the right cont… |
| `home-robots` | Home robots | 7 | 0 |  | Control home robots from chat: a Segway Navimow, a Matic vacuum, and other official vacuums, mowers, and Matter robots. Connect each once, then say start, paus… |
| `imogen` | Imogen | 0 | 0 |  | Imogen the Impala Image Interpreter writes brief, copyable alt text focused on the most important part of an image, so images are accessible to blind people. |
| `import-bot` | Import Bot | 20 | 0 |  | Brings your setup from Claude Cowork, Codex, ChatGPT, OpenClaw, and Hermes into Grok Bot, then creates the expert bots that cover it or adds to the bots you al… |
| `last30days` | last30days | 1 | 0 |  | Research what people actually say about any topic in the last 30 days. Installs the latest last30days skill from GitHub, walks first-run setup (ScrapeCreators… |
| `leadsworth` | Lead Pipeline Desk | 7 | 2 | slack, notion-workspace, linear, hex, Databricks SQL, Gmail, Google Sheets, Salesforce | Scores your inbound leads, merges duplicates, assigns an owner, and flags what's stuck. Works from a CRM export, a sheet, or a paste, and never sends anything… |
| `engineer-bot` | Lingxi's Engineer Bot | 1 | 0 | Notion | A hands-off engineering supervisor. It boards work, launches cloud agents, watches PRs on a 30-minute cadence, and only asks you to merge. For anyone who wants… |
| `love` | Love ❤️ | 0 | 3 | Google Calendar | Takes the admin out of being a good Partner so the attention can go where it counts. Reminds, researches, and queues dates, tables, and presents; you book, buy… |
| `luma-pages` | Luma Pages | 0 | 0 | Notion | Builds and updates private Luma event pages for field marketers — copy, branding, registration settings, capacity and waitlist, and registration-list hygiene.… |
| `market-researcher` | Market Researcher | 10 | 2 | X, Google Sheets, Google Drive, Slack | Tracks how competitors market: their ads and creative, landing pages, offers, pricing, channel mix, search overlap, and content cadence, then delivers a weekly… |
| `marketing-analyst` | Marketing Analyst | 9 | 3 | Google Sheets, Google Drive, Gmail, Slack | Turns your ad platform exports into weekly and monthly paid media reports with commentary, answers reporting asks with the real number and its source, and watc… |
| `echo` | Meeting Recap Deck | 8 | 2 | figma, Google Slides, notion-workspace, slack, linear, Gmail, Google Calendar, Granola, Gong | Turns your meeting notes into a recap deck in your slide template. Works from notes you paste or upload, and never invents a quote. |
| `nightly-audit-engineer` | Nightly Audit Engineer | 0 | 1 |  | A nightly engineering auditor that researches a whole codebase, then ships one cleanup per area. Built for teams that want a research-then-spread-out cleanup h… |
| `nyc-parent` | NYC Parent | 0 | 0 |  | A family chief of staff for New York City parents. It tracks school, calendar, activities, and household logistics, turns incoming information into next action… |
| `office-ops-desk` | Office Ops Desk | 7 | 3 | slack, notion-workspace, linear, Gmail, Google Calendar, Google Sheets | Tracks office shipments, facilities issues, and team birthdays, then writes the digests. Works from a pasted list or a spreadsheet, and never sends without you. |
| `pg` | Outbound Prospecting | 8 | 3 | slack, notion-workspace, linear, Gmail, Google Sheets, X, Salesforce | Finds prospects that match your ideal customer, then drafts a first message to each one. Every name is researched on the public web, and nothing sends without… |
| `overheard` | Overheard | 2 | 1 | X, Slack | Watches Reddit, Hacker News, news sites, and X for third-party mentions of your name, brand, and URLs, then sends a short weekday digest when something clears… |
| `tally` | Paid Media Report Desk | 6 | 3 | slack, notion-workspace, linear, hex, Databricks SQL, Gmail, Google Sheets | Turns your Google Ads, Meta, and LinkedIn exports into one weekly report with commentary. Answers reporting asks in Slack with real numbers, and never posts wi… |
| `performance-marketer` | Performance Marketer | 8 | 1 | Google Sheets, Google Drive, Slack | Turns approved ad copy into paused campaign shells for messaging tests in the ad platforms the user signs in to, with a review sheet they approve first and a s… |
| `pfp-bot` | Pfp Bot | 8 | 0 | X | Turns your X photo, an upload, a selfie, or a pet pic into a tiny Grokbot-style icon with capsule eyes that keeps the hair, colors, and signature look. Style a… |
| `pipeline-health-and-forecast` | Pipeline Pulse | 3 | 1 | Salesforce, Gmail, Slack, Granola, Notion, Google Sheets | Scans your full pipeline for movement, stale next steps, forecast risk, and CRM gaps. Shows what changed across the book and drafts the updates needed to keep… |
| `pitch-deck-coach` | Pitch Deck Coach | 4 | 0 |  | Reviews a pitch deck and reports what an investor is likely to understand, believe, question, and remember, then helps strengthen the story, evidence, and slid… |
| `pm-bot` | PM bot | 3 | 1 |  | Acts as your PM. Writes the dated cut: what's in, what's out, and how you'll know it's done. Engineering doesn't start until you approve it. |
| `product-idea-stress-test` | Product Idea Stress Test | 3 | 0 |  | Investigates a product or startup idea for founders. Surfaces what has to be true, evidence for and against, the assumption most likely to kill it, and what to… |
| `product-marketer` | Product Marketer | 9 | 1 | Google Drive, Google Sheets, Notion, X | Learns your product, brand, and market, turns competitive research into positioning principles every message is measured against, and drafts landing page, ads,… |
| `customer-question-drafter` | Product Support Inbox Assistant | 0 | 0 | Slack, Gmail, Granola | Helps you find and draft answers to product questions. Never sends emails without you. |
| `marketing-project-manager` | Project Manager | 7 | 2 | Linear, Notion, Slack, Google Drive, Google Calendar | Turns a campaign or launch goal into a dated plan across research, positioning, landing pages, ads, and analytics, then tracks every work item, chases status w… |
| `projects-manager` | Projects Manager | 1 | 0 | Notion, Slack | Runs your team's projects from Notion: one row per project, a channel per project, and tasks your specialist bots claim. You decide, agents execute, and it nev… |
| `proto-bot` | Proto Bot | 9 | 2 | Figma, Slack, X | Turns your daily ideas into live, shareable prototypes in your real app, built as draft pull requests with click-path screenshots and a short video, plus Figma… |
| `qa-bot` | QA bot | 3 | 1 | Vercel | Acts as your QA on the live deploy: runs the acceptance checklist and says pass or fail before you ship. |
| `mr-toms` | Recruiting Coordinator | 8 | 7 | slack, notion-workspace, linear, figma, Gmail, Google Calendar, Granola, Google Sheets, Ashby | Schedules interview loops, preps your interviewers, and chases what's stalled. Works from your calendar or a pasted list, and never emails a candidate without… |
| `researchy` | Researchy | 1 | 0 |  | A research and fact-check desk that runs every pass on the latest Grok model with live web search. For anyone who needs sourced, dated claims instead of a trai… |
| `sales-call-coach` | Sales Call Coach | 8 | 2 | notion-workspace, slack, linear, Gong, Google Calendar | Scores your sales calls and tells you what to fix before the next one. Works from a pasted transcript or an uploaded recording. |
| `sell-bot` | Sell Bot | 11 | 10 | Gmail, Google Calendar, Granola, Google Sheets, Slack, X | Works your whole customer journey: outreach in your voice, booked calls with prep and follow-ups, proposals and contracts, then activation, support and billing… |
| `seo-aeo-desk` | SEO & AEO Desk | 7 | 3 | notion-workspace, slack, linear, hex, Profound, Google Sheets | Turns your keywords into content ideas and writer-ready briefs for search and AI answers. Works from a pasted keyword list or your Search Console. |
| `sequencer` | Sequencer | 9 | 4 | Gmail, Google Sheets, Salesforce, Google Calendar, Slack | Runs outbound as a staff function: queues prospects that match your ICP, keeps sequence state on your tracker, and stages every touch as a draft in your voice… |
| `signal-prospector` | Signal Prospector | 5 | 1 | Salesforce, HubSpot, Attio, Mixpanel, X, Hunter, Clay, Gmail, Slack | Finds the accounts and people in your CRM and product data that just showed intent, ranks them, and drafts the first touch. Runs on a schedule, explains every… |
| `site-audit` | Site Audit | 0 | 2 |  | SEO + content + speed + a11y + CRO + schema audit. Scored, P0/P1/P2, evidence URLs. Monthly diff. No invented metrics. |
| `skippy` | skippy | 1 | 0 |  | A San Francisco street-cleaning assistant. Paste a Maps pin, address, or intersection and it tells you the next posted sweep on that curb. Uses public city dat… |
| `stalk-bot` | Stalk Bot | 19 | 3 | AgentMail, X, Gmail, Slack, Salesforce, Google Sheets | Signs up for your competitors' newsletters and products under its own research email, walks their onboarding on video, and watches their site, pricing, changel… |
| `startup-qa-bot` | Startup QA Bot | 5 | 1 | AgentMail, GitHub, Linear | Walks your product every weekday in its own test account and tells you what shipped, what got unshipped, what broke (with repro steps and screenshots), and whi… |
| `image-gen-bot` | Stills & Clips Desk | 6 | 1 | slack, notion-workspace, figma, linear | Pulls stills, thumbnails, and short clips out of your footage, sized for where they go. Cleans up screenshots for docs too, and writes the caption and alt text. |
| `seed-a91e4c` | SWE | 7 | 0 |  | Cursor's software engineer bot: writes code, triages issues, monitors production, and more. |
| `sherlock` | Talent Discovery | 9 | 2 | slack, notion-workspace, linear, figma, Gmail, Google Sheets, Ashby | Finds candidates for open roles that match your criteria and aren't already in your ATS. |
| `tech-demos` | Tech Demos | 1 | 1 | X | Weekday X-bookmark scout that picks one new library to demo, asks for approval, then plans and builds it in a sticky monorepo with a Cursor cloud agent. For an… |
| `the-morning-newspaper` | The Morning Newspaper | 1 | 0 |  | A newspaper customized to you. It pulls from your email and calendar, lays it out for you, and prints while you sleep. Created by @karenxcheng |
| `tinkabot` | tinkabot | 3 | 0 | pstack | Wraps an API into a Cursor/Agent Plugin (MCP + skills). Data shape first, smallest scaffold that works, prove locally, then ask once for affiliation and publis… |
| `tradbot-2` | Tradbot | 3 | 5 | Gmail, Google Calendar, Slack | Watches your personal email and calendar so school forms, bills, and RSVPs don't slip. Drafts the reply, catches the pickup clash, and never sends without you. |
| `best-video-editor` | Video Edit Desk | 6 | 1 | slack, notion-workspace, linear, figma | Turns uploaded footage into cut clips, burned-in captions, and platform-sized exports. Works from your notes and never overwrites the original. |
| `video-editor` | Video Editor | 5 | 0 | Remotion, Google Drive | Edits short vertical talking-head videos from your raw footage: picks the best takes, captions what you actually said, and adds B-roll, motion graphics, and mu… |
| `webby` | Webby | 1 | 6 | X | Website admin. Owns a personal site (rebuild + live fallback, exclusive long-form and newsletter) and a public weekday dashboard. Also owns newsletter sends: e… |
| `website-ops` | Website Ops | 8 | 1 | GitHub, Google Drive, Slack, Figma | Ships website changes as pull requests from your site repo with before and after screenshots in chat, and runs evidence backed audits of SEO, content, speed, a… |
| `writing-bot` | Writing Bot | 1 | 0 |  | A writing partner for drafting and revising essays, emails, docs, and other prose. It uses a structured revision workflow so the result is clearer and better o… |
| `wtd` | WTD | 6 | 1 | Notion, Slack, Gmail, Google Drive | WTD is a VIP hospitality planning partner for marketing ops — project-plan and status rhythm across tentpoles and ticket banks, nomination-sheet tracking, mark… |
| `x-brief` | X Brief | 6 | 2 | X, slack, notion-workspace, linear | Turns the accounts and topics you pick on X into one short daily brief. Reads your X connection or handles you paste, and never posts on your behalf. |
