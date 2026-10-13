"""Slug helpers used across core and services."""

from __future__ import annotations

import re

_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def slugify(name: str) -> str:
    """Return a URL-safe slug. Never returns an empty string."""
    slug = _NON_ALNUM.sub("-", name.strip().lower()).strip("-")
    return slug or "unnamed"