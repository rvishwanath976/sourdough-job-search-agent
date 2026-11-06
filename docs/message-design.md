# Message design

How the agent drafts outreach, and why. Every message is a draft for me to review. The agent never sends anything.

## Goal
A short, human message that earns a reply. It should read like I wrote it, not like a template or a pitch.

## Structure
Every draft follows the same four parts, in this order:

1. **Opener in my own words.** A fixed, simple greeting that names the role. It does not paraphrase or praise a line from the post. Early drafts did that, and I rewrote them because they sounded like AI-written LinkedIn copy.
2. **What I have done that matches what the post asks for.** The agent picks the one or two requirements in the post that line up with my strongest experience and builds on those, using the post's own key terms. It skips requirements I cannot speak to instead of mentioning them.
3. **A concrete result.** Every draft includes at least one business result, not only a description of work. Projections are labeled as projections ("expected to").
4. **A low-pressure close.** A single line saying I would like to learn more about the role. No asks for a call, no deadlines.

Length: 50 to 85 words on LinkedIn, 40 to 60 on X.

## Adapting by role type
The most recent experience always goes first. How it starts depends on the role:

| Role looks like | Lead with |
|---|---|
| Leadership (Group PM, Head, Director) | Scope: owning AI products across a whole company |
| Very technical or evaluation-heavy | Evaluation and accuracy work, with its business result |
| Growth or turnaround | An adoption turnaround, with numbers |
| Broad or unrelated domain | A general message: recent AI product work and its result, then older experience, then stop |

Older experience comes second, either as a second result or to show big-company scale.

## What the agent must not do
- **Point out gaps.** No "I haven't worked in X." Highlight what is relevant and leave out the rest.
- **Imply experience I do not have.** For example, claiming to have managed people when I led products and cross-functional work.
- **Invent connections.** No fake mutual contacts, prior conversations, or enthusiasm I have not stated.
- **Use unverified numbers.** Only figures from my approved sources, copied exactly. No placeholders.
- **Mention pay.**
- **Use a style that reads as machine-written.** No emoji, em dashes, parentheses, or hype words.

These connect to the hard rules in [GUARDRAILS.md](../GUARDRAILS.md). The guardrails say what is forbidden. This document explains what a good message looks like inside those limits.

## Approved sources
The agent may only use facts that appear in my current resume, my published work, and my own interview stories, plus what the author wrote in their post. If nothing I have maps closely to the stated need, it ties to the nearest real overlap and claims no more.

## Example of an edit and what it taught
Everything below is invented.

**Draft**
> Hi Sam, your focus on a trusted assistant is what stood out in your post. I'm an AI product manager with experience in AI products. I haven't worked in retail. Open to a quick chat?

**My edit**
> Hi Sam! Pleasure to meet you. I wanted to reach out to express interest in the Senior Product Manager role you're hiring for. I led AI products at [recent company] and [result]. Before that, I launched LLM products at [earlier company] that [result]. I'd love to learn more about this role.

**What changed, and the rule it became**
- Weak opener, so the opener is now fixed and in my voice.
- A line about a gap was removed, so the agent no longer mentions gaps.
- Results were added, so every draft needs at least one concrete result.
- Recent experience moved first, so the most recent role always leads.

## How drafts are checked
Rules that can be checked by a script are the next step: word count, banned characters, required result, and whether every number matches an approved source. I track what I edit in each draft using dropdowns, which feeds the [learning loop](learning-loop.md).
