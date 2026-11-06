# Learning loop

For each draft I record whether it was a good match, whether I edited it, and what changed, using dropdowns. The agent compares the draft with my final message and looks for patterns.

## Rule: propose only
If the same change shows up in at least three rows, the agent appends one plain-English rule with its evidence and sets the status to **Pending**. I approve or retire rules. Only approved rules affect future runs. The agent never approves its own rules.

## Examples of rules that came out of review (paraphrased)
- Open every message in my own voice instead of paraphrasing the post.
- Always include at least one concrete business result.
- Do not mention what I have not done. Build on the strongest matching requirement.
- Only include roles in NYC or remote.
- Treat a plain "Product Manager" title as possibly senior at startups and frontier labs.

## Why this design
Letting a system rewrite its own rules removes the person who is accountable for the output. Proposing keeps me in control while still turning my edits into improvements.
