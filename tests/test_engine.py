"""End-to-end tests for the naming engine pipeline."""

from __future__ import annotations

import pytest

from forge_core.engine import NamingEngine
from forge_core.phonetics import PhoneticScorer
from forge_core.scoring import BrandabilityScorer
from forge_models.generation_request import GenerationRequest


class _StubLLM:
    """Deterministic LLM stub — returns a fixed corpus."""

    def generate_names(self, *, brief: str, style: str, count: int) -> list[str]:
        corpus = ["CobaltForge", "CobaltForge", "LumenGrid", "VertexLabs", "SableHQ"]
        return corpus[:count]


@pytest.fixture()
def engine() -> NamingEngine:
    weights = {"phonetic