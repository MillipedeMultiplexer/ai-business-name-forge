"""NameCandidate schema."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class NameCandidate:
    """A single forged name with its canonical slug and TLD."""

    display: str
    slug: str
    tld: str

    def fqdn(self) -> str:
        return f"{self.slug}.{self.tld}"