"""Morpheme recipes: prefix + root + suffix compositions."""

from __future__ import annotations

import itertools
from dataclasses import dataclass

PREFIXES = ("neo", "lumen", "vertex", "north", "sable", "orbit", "cobalt", "kite")
ROOTS = ("forge", "spark", "harbor", "signal", "loom", "peak", "drift", "grid")
SUFFIXES = ("labs", "co", "works", "hq", "studio", "systems", "collective")


@dataclass(slots=True)
class MorphemeRecipe:
    """Generate candidate names from combinatorial morphemes.

    Pure fallback used when the LLM adapter is unavailable or stale.
    Deterministic ordering; callers shuffle if they want variety.
    """

    def compose(self, limit: int = 64) -> list[str]:
        names: list[str] = []
        for pre, root in itertools.product(PREFIXES, ROOTS):
            names.append(f"{pre.capitalize()}{root.capitalize()}")
            if len(names) >= limit:
                return names
        for root, suf in itertools.product(ROOTS, SUFFIXES):
            names.append(f"{root.capitalize()}{suf.capitalize()}")
            if len(names) >= limit:
                return names
        return names