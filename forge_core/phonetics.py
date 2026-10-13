"""Phonetic scoring — pronounceability, syllable balance, phonotactics."""

from __future__ import annotations

import re
from dataclasses import dataclass

_VOWELS = set("aeiouy")
_CLUSTER_RE = re.compile(r"[bcdfghjklmnpqrstvwxz]{4,}")


@dataclass(slots=True)
class PhoneticScorer:
    """Scores how easily a name rolls off the tongue.

    Scale: 0.0 (unpronounceable) to 1.0 (smooth).
    Deterministic — no randomness, safe for batch jobs.
    """

    def syllable_count(self, name: str) -> int:
        """Approximate English syllable count via vowel-group heuristic."""
        word = name.lower()
        groups = 0
        prev_vowel = False
        for ch in word:
            is_vowel = ch in _VOWELS
            if is_vowel and not prev_vowel:
                groups += 1
            prev_vowel = is_vowel
        if word.endswith("e") and groups > 1:
            groups -= 1
        return max(1, groups)

    def score(self, name: str) -> float:
        """Blend syllable fit and consonant-cluster penalties."""
        if not name:
            return 0.0
        syllables = self.syllable_count(name)
        # 2-3 syllables is the sweet spot for a business name.
        if syllables in (2, 3):
            syllable_score = 1.0
        elif syllables == 1:
            syllable_score = 0.75
        elif syllables == 4:
            syllable_score = 0.55
        else:
            syllable_score = 0.3

        clusters = _CLUSTER_RE.findall(name.lower())
        cluster_penalty = min(0.6, 0.2 * len(clusters))

        length = len(name)
        length_score = 1.0 if 4 <= length <= 12 else (0.7 if length <= 16 else 0.4)

        raw = (syllable_score * 0.5) + (length_score * 0.3) + (1.0 - cluster_penalty) * 0.2
        return round(min(1.0, max(0.0, raw)), 4)