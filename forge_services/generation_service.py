"""GenerationService: end-to-end name generation with trademark checks."""

from __future__ import annotations

import logging
from dataclasses import dataclass

from forge_core.engine import NamingEngine
from forge_core.scoring import ScoredName
from forge_models.generation_request import GenerationRequest
from forge_services.trademark_service import TrademarkService

log = logging.getLogger("forge.services.generation")


@dataclass(slots=True)
class GenerationService:
    """Public service for name generation.

    Wraps the engine with trademark screening and result filtering.
    Handlers must call this, not the engine directly — trademark
    screening is a compliance requirement for shipped results.
    """

    engine: NamingEngine
    trademark: TrademarkService

    def generate(self, request: GenerationRequest) -> list[ScoredName]:
        """Forge names, screen against the trademark cache, drop collisions."""
        candidates = self.engine.forge(request)
        if not candidates:
            log.warning("engine returned no candidates for brief=%r", request.brief)
            return []

        accepted: list[ScoredName] = []
        for scored in candidates:
            hit = self.trademark.check(scored.candidate.slug, tld=request.tld)
            if hit.found:
                log.info("trademark collision, dropping: %s", scored.candidate.slug)
                continue
            accepted.append(scored)
        return accepted