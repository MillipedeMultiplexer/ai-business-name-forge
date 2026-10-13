"""Brandability scoring — memorability, distinctiveness, brevity."""

from __future__ import annotations

from dataclasses import dataclass

from forge_models.name_candidate import NameCandidate


@dataclass(frozen=True, slots=True)
class ScoredName:
    """A candidate paired with its final brandability score."""

    candidate: NameCandidate
    brandability: float


@dataclass(slots=True)
class BrandabilityScorer:
    """Weighted blend of dimensions that predict a name's stickiness.

    Weights come from `config/default.toml` under `[scoring]` and must
    sum to 1.0; the constructor normalizes defensively.
    """

    weights: dict[str, float]

    def score(self, candidate: NameCandidate, *, phonetic: float) -> float:
        """Return a 0-100 brandability score for one candidate."""
        brevity = self._brevity(candidate.display)
        distinctiveness = self._distinctiveness(candidate.display)
        memorability = self._memorability(candidate.display)

        total_weight = sum(self.weights.values()) or 1.0
        blended = (
            self.weights.get("phonetic", 0.35) * phonetic
            + self.weights.get("brevity", 0.25) * brevity
            + self.weights.get("distinctiveness", 0.25) * distinctiveness
            + self.weights.get("memorability", 0.15) * memorability
        ) / total_weight
        return round(blended * 100, 2)

    def _brevity(self, name: str) -> float:
        n = len(name)
        if n <= 6:
            return 1.0
        if n <= 10:
            return 0.85
        if n <= 14:
            return 0.6
        return 0.35

    def _distinctiveness(self, name: str) -> float:
        # Rare letters (q, x, z, j, v, k) lift distinctiveness.
        rare = sum(1 for c in name.lower() if c in "qxzjvk")
        return min(1.0, 0.5 + rare * 0.08)

    def _memorability(self, name: str) -> float:
        # Alliteration + repeated letters help recall.
        words = name.lower().split()
        if len(words) >= 2 and words[0][:1] == words[1][:1]:
            return 0.9
        return 0.7