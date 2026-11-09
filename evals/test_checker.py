"""Self-tests for checker.py using invented drafts. Run: python test_checker.py"""
import json
from checker import check, norm

ALLOWED = {norm(x) for x in json.load(open("facts.example.json"))["allowed_numbers"]}
GOOD = ("Hi Sam! Pleasure to meet you. I wanted to reach out to express interest in the Senior Product "
        "Manager role you're hiring for. At Acme I led AI products and grew a new tool from zero adoption to "
        "30 customers in one quarter. A model change I led brought in $2M in revenue in under two weeks. "
        "At Beta I launched products that generated $10M+ in revenue. I'd love to learn more about this role.")

def names(text, kind="legacy"):
    return {n for _, n, _ in check(text, ALLOWED, kind)}

def run():
    cases = [
        ("good draft passes", GOOD, set()),
        ("invented number is caught", GOOD.replace("$2M", "$9M"), {"unapproved_number"}),
        ("projection needs 'expected'", GOOD.replace("$10M+ in revenue", "5x in revenue, doubling revenue"), {"projection_without_expected"}),
        ("gap phrase is caught", GOOD.replace("I'd love", "I haven't worked in this area. I'd love"), {"points_out_a_gap"}),
        ("em dash is caught", GOOD.replace("At Beta", "At Beta — earlier,"), {"banned_punctuation_or_emoji"}),
        ("wrong opener is caught", GOOD.replace("Hi Sam! Pleasure to meet you.", "Hi Sam, I saw your post."), {"opener_not_exact", "paraphrases_the_post"}),
        ("too short is caught", "Hi Sam! Pleasure to meet you. I wanted to reach out to express interest in the PM role you're hiring for. I'd love to learn more about this role.", {"word_count_50_to_85", "no_concrete_result"}),
    ]
    failed = 0
    for label, text, expected in cases:
        got = names(text)
        ok = expected <= got and (expected or not got)
        print(("ok   " if ok else "FAIL ") + label + ("" if ok else f"  expected {expected}, got {got}"))
        failed += not ok
    # order check
    order = GOOD.replace("At Acme", "At JPMorgan").replace("At Beta", "At Boostlingo")
    ok = "jpmorgan_before_boostlingo" in names(order)
    print(("ok   " if ok else "FAIL ") + "JPMorgan-before-Boostlingo is caught"); failed += not ok
    # two-version length limits
    base = "Hi Sam! Pleasure to meet you. I wanted to reach out to express interest in the Senior PM role you're hiring for. "
    def kn(t, k): return {n for _, n, _ in check(t, {"$2M+"}, k)}
    long_note = base + "I led AI products at Boostlingo. " * 12 + "I'd love to learn more."
    long_mail = base + "I led AI products at Boostlingo. " * 70 + "I'd love to learn more."
    short_ok = base + "I led AI products at Boostlingo, including a model change that brought in $2M+ in revenue in under two weeks. I'd love to learn more."
    for label, t, k, want, absent in [
        ("connection note over 300 chars is caught", long_note, "connection", "connection_note_300_chars", None),
        ("InMail over 1900 chars is caught", long_mail, "inmail", "inmail_1900_chars", None),
        ("short connection note passes the length rules", short_ok, "connection", None, "connection_note_300_chars"),
    ]:
        g = kn(t, k)
        ok = (want in g) if want else (absent not in g and "word_count_50_to_85" not in g)
        print(("ok   " if ok else "FAIL ") + label); failed += not ok
    raise SystemExit(1 if failed else 0)

if __name__ == "__main__":
    run()

