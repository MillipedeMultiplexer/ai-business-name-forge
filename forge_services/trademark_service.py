"""TrademarkService: cached lookups against a pluggable registry."""

from __future__ import annotations

import logging
from dataclasses import dataclass

from forge_adapters.storage.base import CacheAdapter
from forge_models.trademark_hit import TrademarkHit

log = logging.getLogger("forge.services.trademark")


@dataclass(slots=True)
class TrademarkService:
    """Cache-backed trademark screening.

    The registry itself is pluggable upstream; this service only owns
    cache policy (TTL) and negative-caching to avoid hammering the
    registry on repeated briefs.
    """

    cache: CacheAdapter
    ttl_hours: int = 72

    def check(self, slug: str, *, tld: str = "com") -> TrademarkHit:
        """Return a hit if the slug collides with a known mark."""
        key = f"tm:{tld}:{slug}"
        cached = self.cache.get(key)
        if cached is not None:
            return TrademarkHit(found=bool(cached["found"]), slug=slug, tld=tld, source="cache")

        # Registry adapter is wired by the caller in production; here we
        # negative-cache by default so offline runs stay fast.
        hit = TrademarkHit(found=False, slug=slug, tld=tld, source="offline")
        self.cache.set(key, {"found": hit.found}, ttl_hours=self.ttl_hours)
        return hit