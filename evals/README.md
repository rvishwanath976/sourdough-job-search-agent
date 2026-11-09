# Draft evals

A rule checker for the outreach drafts. It verifies the rules a script can check. Rules that need judgment are scored separately.

## Run it
```
python test_checker.py                                   # self-tests, invented drafts
python checker.py drafts.json --facts facts.json         # check real drafts
python checker.py drafts.json --facts facts.json --kind connection   # 300 character limit
```

`drafts.json` is a list of `{"id", "label", "text"}`. `facts.json` lists the numbers a draft may contain. The real one is git-ignored. `facts.example.json` shows the format.

## What it checks
**Critical (never send):** a number not in the approved facts, a projection without "expected", JPMorgan mentioned before Boostlingo, pointing out a gap, mentioning pay, a placeholder left in, claiming direct reports, Boostlingo in present tense.

**Standard (breaks a style rule):** the exact opener, length, no dashes, parentheses or emoji, a low-pressure close, at least one concrete result.

**Warn:** hype words, the LLM-as-a-judge framework without "first of its kind", no Boostlingo mention.

## What it does not check yet
Whether a draft ties to what the post asks for, whether the opener fits the role type, and whether each result is attributed to the right company. Those need a rubric scored by a person or a judge model. It also does not check that the greeting name matches the author.

## Why a script and not just the model
A rule written in a prompt is a request. A check is a measurement. Running the same checks before and after every prompt change shows whether quality moved.
