from pathlib import Path
import re

ROOT = Path(__file__).parents[1]
TEXT = (ROOT / "SKILL.md").read_text(encoding="utf-8")


def test_frontmatter_and_publication_safety():
    assert TEXT.startswith("---\n")
    assert "name: durable-context-management" in TEXT
    assert "version: 0.1.0" in TEXT
    assert len(re.search(r"description: (.+)", TEXT).group(1)) <= 60
    assert "/home/" not in TEXT
    assert "/mnt/" not in TEXT
    assert "minec" not in TEXT.lower()


def test_routing_contract_is_present():
    for token in (
        "ADMIT", "REJECT_INITIAL", "REJECT_TARGET", "ACCEPT_TARGET",
        "AMBIGUOUS_TARGET", "EXCEPTION_TARGET", "reclassification",
        "Write once, verify", "discussion-only",
    ):
        assert token in TEXT
