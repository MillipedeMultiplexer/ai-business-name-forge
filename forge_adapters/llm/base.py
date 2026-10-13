"""LLMAdapter protocol — the only contract core code depends on."""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class LLMAdapter(Protocol):
    """Anything that can turn a brief into candidate names."""

    def generate_names(self, *, brief: str, style: str, count: int) -> list[str]:
        """Return up to `count` raw candidate names."""
        ...