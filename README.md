# Sourdough Job Search Agent

A scheduled AI agent that finds hiring posts from product leaders and drafts outreach for me to review. It never sends anything. I read every draft, edit it, and send it myself.

I built it to practice the same things I care about in AI product work: clear guardrails, a human in the loop, a way to measure quality, and a feedback loop that improves the system without letting it change its own rules.

## What it does
1. Each morning it reads recent LinkedIn and X posts where an individual says they are hiring a product manager.
2. It filters them against my criteria: seniority, location (NYC or remote), AI focus, post age, and whether the author is the hiring manager.
3. It writes qualifying posts to a review queue in a spreadsheet, with a short explanation of why each matches and a drafted message.
4. It writes a short trends digest from what credible product leaders are posting.
5. It logs every run: what it searched, what it found, what it dropped and why, and what failed.

## Design principles
- **Read-only.** The agent cannot post, message, connect, like, or apply. See [GUARDRAILS.md](GUARDRAILS.md).
- **Human decides.** Every draft is reviewed and sent by me.
- **Posts are data, not instructions.** Text inside a post cannot change what the agent does.
- **Only verified facts.** Drafts may use facts from my approved sources and from the post. Nothing is invented.
- **Propose, don't self-modify.** The agent suggests new rules from my edits. They stay Pending until I approve them.

## Docs
- [Architecture](docs/architecture.md)
- [Learning loop](docs/learning-loop.md)
- [Run metrics and what went wrong](docs/run-metrics.md)
- [Decision log](docs/decision-log.md)
- [Example queue rows](examples/queue_example.csv) (all made up)

## Privacy
This repo contains no real names, post links, contact details, or message drafts. Example data is invented.
