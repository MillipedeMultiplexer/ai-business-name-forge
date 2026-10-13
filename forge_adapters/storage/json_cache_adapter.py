"""JsonCacheAdapter: single-file JSON cache with TTL expiry."""

from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

log = logging.getLogger("forge.adapters.storage.json")


@dataclass(slots=True)
class JsonCacheAdapter:
    """Simple file-backed cache. Not thread-safe; single-process use only."""

    path: Path
    _loaded: dict[str, dict[str, Any]] = field(default_factory=dict, init=False)

    def __post_init__(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if self.path.exists():
            try:
                self._loaded = json.loads(self.path.read_text("utf-8"))
            except json.JSONDecodeError:
                log.warning("corrupt cache at %s, starting fresh", self.path)
                self._loaded = {}

    def get(self, key: str) -> Any | None:
        entry = self._loaded.get(key)
        if entry is None:
            return None
        if entry.get("expires_at", 0) < time.time():
            del self._loaded[key]
            return None
        return entry["value"]

    def set(self, key: str, value: Any, *, ttl_hours: int = 72) -> None:
        self._loaded[key] = {
            "value": value,
            "expires_at": time.time() + ttl_hours * 3600,
        }
        self._flush()

    def _flush(self) -> None:
        self.path.write_text(json.dumps(self._loaded, indent=2), encoding="utf-8")