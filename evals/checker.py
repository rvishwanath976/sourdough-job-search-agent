"""Rule checker for outreach drafts.

Checks the rules a script can verify. Rules that need judgment (does the draft tie
to what the post asks for, is the opener right for the role type) are scored
separately by a person or a judge model.

Usage:
    python checker.py drafts.json --facts facts.json [--kind legacy]

drafts.json is a list of {"id": ..., "label": "draft" or "final", "text": "..."}.
facts.json holds the numbers a draft is allowed to contain (see facts.example.json).
Severity: CRITICAL = never send. STANDARD = breaks a style rule. WARN = worth a look.
"""
import argparse, json, re, sys
from collections import Counter

NUM = re.compile(r"\$?\d[\d,]*(?:\.\d+)?(?:\s?(?:million|billion))?[kKmMbBxX%]?\+?")
YEAR = re.compile(r"^(19|20)\d\d$")

def norm(tok: str) -> str:
    return re.sub(r"\s+", "", tok.lower()).rstrip(",.")

def numbers_in(text: str):
    return [norm(m.group(0)) for m in NUM.finditer(text)]

def sentences(text: str):
    return [s for s in re.split(r"(?<=[.!?])\s+", text) if s]

def check(text: str, allowed: set, kind: str = "legacy"):
    """Return a list of (severity, check_name, detail)."""
    out = []
    # ---- CRITICAL ----
    bad = [n for n in numbers_in(text) if n not in allowed and not YEAR.match(n)]
    if bad:
        out.append(("CRITICAL", "unapproved_number", ", ".join(sorted(set(bad)))))
    for s in sentences(text):
        if re.search(r"\bdoubl(e|ing)\b|\b2x\b|\$100m", s, re.I) and not re.search(r"expected|projected", s, re.I):
            out.append(("CRITICAL", "projection_without_expected", s[:80]))
    jp, bl = text.find("JPMorgan"), text.find("Boostlingo")
    if jp != -1 and bl != -1 and jp < bl:
        out.append(("CRITICAL", "jpmorgan_before_boostlingo", ""))
    if re.search(r"\bI haven'?t\b|\bI have not\b|\bno experience\b|\bI lack\b|\bnever (worked|built)\b|\bdon'?t have (any )?experience\b", text, re.I):
        out.append(("CRITICAL", "points_out_a_gap", ""))
    if re.search(r"\bsalary\b|\bcompensation\b|\bpay\b|\$\d+\s?[kK]\b", text, re.I):
        out.append(("CRITICAL", "mentions_pay", ""))
    if re.search(r"\bX{1,}\+?\b|\[|\]|\bTBD\b", text):
        out.append(("CRITICAL", "placeholder_left_in", ""))
    if re.search(r"direct reports?|people manager", text, re.I):
        out.append(("CRITICAL", "claims_direct_reports", ""))
    if re.search(r"\bcurrently\b|at Boostlingo I (lead|manage|am)\b", text, re.I):
        out.append(("CRITICAL", "boostlingo_in_present_tense", ""))
    # ---- STANDARD ----
    if not re.match(r"^Hi [^!]+! Pleasure to meet you\. I wanted to reach out to express interest in the [^.]*you're hiring for", text):
        out.append(("STANDARD", "opener_not_exact", ""))
    if re.search(r"stood out|I saw your", text, re.I):
        out.append(("STANDARD", "paraphrases_the_post", ""))
    words, chars = len(text.split()), len(text)
    if kind == "legacy" and not 50 <= words <= 85:
        out.append(("STANDARD", "word_count_50_to_85", f"{words} words"))
    if kind == "connection" and chars >= 300:
        out.append(("STANDARD", "connection_note_300_chars", f"{chars} chars"))
    if kind == "inmail" and chars >= 1900:
        out.append(("STANDARD", "inmail_1900_chars", f"{chars} chars"))
    if re.search(r"[—–]|-->|[()]", text) or re.search("[☀-➿\U0001F300-\U0001FAFF]", text):
        out.append(("STANDARD", "banned_punctuation_or_emoji", ""))
    if not re.search(r"learn more|love to hear", text, re.I):
        out.append(("STANDARD", "no_low_pressure_close", ""))
    if not [n for n in numbers_in(text) if n not in ("0", "1")]:
        out.append(("STANDARD", "no_concrete_result", ""))
    # ---- WARN ----
    if "LLM-as-a-judge" in text and not re.search(r"\bfirst\b", text):
        out.append(("WARN", "judge_framework_missing_first_of_its_kind", ""))
    if re.search(r"\b(excited|passionate|thrilled|leverage|delve|genuinely|honestly|truly)\b", text, re.I):
        out.append(("WARN", "hype_word", ""))
    if jp != -1 and bl == -1:
        out.append(("WARN", "no_boostlingo_mention", ""))
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("drafts"); ap.add_argument("--facts", required=True)
    ap.add_argument("--kind", default="legacy", choices=["legacy", "connection", "inmail"])
    a = ap.parse_args()
    allowed = {norm(x) for x in json.load(open(a.facts))["allowed_numbers"]}
    items = json.load(open(a.drafts))
    results, counts = [], Counter()
    for it in items:
        f = check(it["text"], allowed, it.get("kind", a.kind))
        sev = {s for s, _, _ in f}
        status = "FAIL-CRITICAL" if "CRITICAL" in sev else "FAIL" if "STANDARD" in sev else "WARN" if "WARN" in sev else "PASS"
        results.append((it, status, f))
        for _, name, _ in f: counts[name] += 1
    for it, status, f in results:
        print(f"{it['id']:>4} {it['label']:<6} {status:<14} " + "; ".join(f"{n}" + (f" [{d}]" if d else "") for _, n, d in f))
    total = len(results)
    clean = sum(1 for _, s, _ in results if s in ("PASS", "WARN"))
    crit = sum(1 for _, s, _ in results if s == "FAIL-CRITICAL")
    print(f"\n{clean}/{total} pass all critical and standard checks; {crit} have a critical failure")
    for name, n in counts.most_common(): print(f"  {n:>3}  {name}")

if __name__ == "__main__":
    main()
