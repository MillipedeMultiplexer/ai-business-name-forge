"""TrademarkHit schema."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TrademarkHit:
    """Result of a trademark screening lookup."""

    found: bool
    slug: str
    tld: str
    source: str