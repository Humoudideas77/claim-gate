#!/usr/bin/env python3
"""
claim_gate.py — the no-source-no-claim linter.

Any sentence containing a number, percentage, currency figure, year, quote, or an
authority phrase ("according to", "study shows") MUST carry an inline source URL,
or it fails. Catches the most common way written content goes wrong: confident,
specific, unsourced claims.

  python claim_gate.py FILE [FILE ...]      # lint files, nonzero exit on any fail
  python claim_gate.py --selftest

Zero dependencies. MIT.
"""
import re, sys, pathlib

CLAIM = re.compile(
    r"(\b\d+(\.\d+)?\s?%|[$€£]\s?\d|\b\d{3,}\b|"
    r"\b(18|19|20)\d{2}\b|"
    r"benchmark|SOTA|study (shows|finds)|according to|\"[^\"]{8,}\")", re.I)
URL = re.compile(r"https?://\S+")


def split_sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n", text) if s.strip()]


def lint(text):
    """Return list of (sentence) that make a checkable claim without a source URL."""
    fails = []
    for s in split_sentences(text):
        if CLAIM.search(s) and not URL.search(s):
            fails.append(s)
    return fails


def lint_file(path):
    return lint(pathlib.Path(path).read_text())


def selftest():
    bad = "Revenue grew 39% and the market hit $2B in 2026."
    good = "Revenue grew 39%, per the filing https://example.com/10-k"
    assert lint(bad), "should flag unsourced 39% / $2B / 2026"
    assert not lint(good), "sourced claim should pass"
    assert not lint("This is a plain opinion with no checkable claim."), "no claim, no flag"
    print("SELFTEST PASS — unsourced claims flagged, sourced + opinion pass.")


def main(argv):
    if not argv or argv[0] == "--selftest":
        selftest(); return 0
    total = 0
    for path in argv:
        fails = lint_file(path)
        total += len(fails)
        status = "PASS" if not fails else f"FAIL ({len(fails)})"
        print(f"{status}  {path}")
        for f in fails:
            print(f"  unsourced claim: {f}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
