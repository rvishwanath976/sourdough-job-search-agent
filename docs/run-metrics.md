# Run metrics and what went wrong

## What I track per run
Searches run, posts found, rows added, posts dropped and the reason, and failures.

## Common drop reasons
Recruiters and staffing posts, job-aggregator accounts, roles outside the US, non-product roles, junior or contract roles, location outside NYC or remote, no AI mention, and duplicates.

## What I learned
- **Past-week searches returned very few usable posts.** Moving to a 30-day window and pressing "Load more" raised output from about 1 row a run to 5 to 8.
- **Search pages do not expose post permalinks reliably.** Rows often link to the job listing or the author's profile instead, and the Notes column says so.
- **Many posts do not state a location.** The agent includes them but flags the location for me to confirm.
- **Some sources fail.** One run had no browser access, so it logged the error and skipped the browser steps. Another run found X returned an empty timeline. Both were logged as failures instead of reported as "no results".
- **Web search is a weak substitute.** It returns job boards, not dated personal posts.

## Principle
A failed source is logged as a failure, never as "nothing found".
