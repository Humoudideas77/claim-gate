from claim_gate import lint


def test_unsourced_claims_flagged():
    assert lint("Revenue grew 39% in 2026.")
    assert lint("The market hit $2B last year.")
    assert lint('It "changed everything overnight" for users.')


def test_sourced_claims_pass():
    assert not lint("Revenue grew 39%, per https://example.com/10-k")
    assert not lint("Adoption tripled https://example.com/report this quarter.")


def test_opinions_pass():
    assert not lint("This approach is cleaner and easier to maintain.")
    assert not lint("Good infrastructure is invisible when it works.")
