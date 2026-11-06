# Architecture

```
Scheduler (daily)
   |
   v
Agent run
   |-- reads settings (pause, sends off, limits)
   |-- reads context: watchlist, past rows, contacted list, approved rules
   |-- searches LinkedIn and X in a browser (read-only)
   |-- qualifies each post against written criteria
   |-- drafts a message from approved sources
   |-- writes rows to the review sheet
   |-- writes a trends digest
   |-- logs the run
   v
Review sheet  -->  Me (read, edit, send manually, give feedback)
                        |
                        v
               Feedback columns feed the learning loop
```

## Sheet tabs
Queue, Contacted, Learned Rules, Watchlist, Run Log, Settings, People, Trends, Trend sources.

## Why a spreadsheet
It is easy to read, edit and filter, it keeps a visible history, and my feedback columns sit next to each draft so the agent can learn from them.

## Qualification criteria (summary)
Individual author who is plausibly the hiring manager; senior product role; AI mentioned in the post or role; NYC or US-remote; posted within 30 days; not a duplicate; pay and contract checks.
