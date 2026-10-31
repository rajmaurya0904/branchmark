"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import branchmark


def test_version_is_set() -> None:
    assert branchmark.__version__
