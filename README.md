# claim-gate

> No source, no claim. A tiny linter that fails any sentence making a checkable claim (a number, percentage, currency figure, year, quote, or authority phrase) without an inline source URL.

MIT-licensed. Zero dependencies. Does one thing well.

## Why

The most common way written content goes wrong is a confident, specific, unsourced claim — a number or a "studies show" with nothing behind it. `claim-gate` makes that fail loudly, so it never ships. Drop it in a pre-commit hook or CI step for docs, posts, reports, or model output.

## Install

```sh
# no install needed — single file, stdlib only
curl -O https://raw.githubusercontent.com/<you>/claim-gate/main/claim_gate.py
```

## Use

```sh
python claim_gate.py README.md docs/*.md     # exits nonzero if any claim is unsourced
python claim_gate.py --selftest
```

```python
from claim_gate import lint
lint("Revenue grew 39% in 2026.")                       # -> ["Revenue grew 39% in 2026."]
lint("Revenue grew 39%, per https://example.com/10-k")  # -> []
```

## What counts as a claim

A sentence is flagged when it contains any of: a percentage, a currency figure, a 3+ digit number, a year, a quoted phrase, or an authority cue ("according to", "study shows", "benchmark", "SOTA") — and has no `http(s)://` URL in the same sentence. Plain opinions pass.

## License

MIT
