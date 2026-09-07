"""The radar suite is pytest-only; keep unittest discovery out of it.

Every module here is written against pytest fixtures and imports pytest at the
top. The release-policy archive preflight runs `python -B -m unittest discover
-s tests` on a runner that installs only `requirements-test.txt`, which this
repository does not ship, so without this hook that discovery imports
`tests/radar/test_monitor.py`, fails on `import pytest` and blocks the release
(the v0.1.4 tag). unittest collects nothing from these function-style tests
anyway, so withholding the package from it loses no coverage: `ci.yml` runs
the radar half under pytest on every push.
"""

from __future__ import annotations

import unittest


def load_tests(
    loader: unittest.TestLoader,
    standard_tests: unittest.TestSuite,
    pattern: str | None,
) -> unittest.TestSuite:
    """Return the package's own suite and stop discovery from recursing into it."""
    del loader, pattern
    return standard_tests
