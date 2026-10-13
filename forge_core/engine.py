"""NamingEngine: orchestrates generation, dedupe, and scoring."""

from __future__ import annotations

import re
from dataclasses import dataclass

from forge_adapters.llm.base import LLMAdapter
from forge_core.phonetics import PhoneticScorer
from forge_core.scoring import BrandabilityScorer, ScoredName
from forge_models.name_candidate import NameCandidate
from forge_models.generation_request import GenerationRequest

_SLUG_RE = re.compile(r"[^a-z0-9]+")


@dataclass(slots=True)
class NamingEngine:
    """Pure orchestration: prompt -> candidates -> scored, deduped names.

    Side effects: none (LLM adapter owns its own I/O).
    Complexity: O(n log n) for the final sort across `n` candidates.
    """

    llm: LLMAdapter
    phonetics: PhoneticScorer
    scorer: BrandabilityScorer

    def forge(self, request: GenerationRequest) -> list[ScoredName]:
        """Run the full forge pipeline for one request.

        Returns up to `request.count` names, best-first. Empty list when
        the adapter yields nothing usable — callers treat that as a soft
        failure, not an exception.
        """
        raw = self.llm.generate_names(
            brief=request.brief,
            style=request.style,
            count=request.count * 3,  # oversample, dedupe later
        )
        seen: set[str] = set()
        scored: list[ScoredName] = []

        for candidate_name in raw:
            slug = _SLUG_RE.sub("-", candidate_name.strip().lower()).strip("-")
            if not slug or slug in seen:
                continue
            seen.add(slug)

            candidate = NameCandidate(
                display=candidate_name.strip(),
                slug=slug,
                tld=request.tld,
            )
            phonetic = self.phonetics.score(candidate.display)
            brand = self.scorer.score(candidate, phonetic=phonetic)
            scored.append(ScoredName(candidate=candidate, brandability=brand))

        scored.sort(key=lambda s: s.brandability, reverse=True)
        return scored[: request.count]