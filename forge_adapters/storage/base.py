"""CacheAdapter protocol."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class CacheAdapter(Protocol):
    """Minimal key-value cache contract with TTL."""

    def get(self, key: str) -> Any | None: ...
    def set(self, key: str, value: Any, *, ttl_hours: int = 72) -> None: ...