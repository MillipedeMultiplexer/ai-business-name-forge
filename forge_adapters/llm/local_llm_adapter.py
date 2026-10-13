"""LocalLLMAdapter: llama.cpp backend with a deterministic stub fallback."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path

from forge_core.patterns.morpheme_recipe import MorphemeRecipe

log = logging.getLogger("forge.adapters.llm.local")


@dataclass(slots=True)
class LocalLLMAdapter:
    """Wraps a local GGUF model. Falls back to MorphemeRecipe when absent.

    The fallback is intentional and load-bearing: a fresh clone must be
    usable offline. Never raise on missing weights — log and degrade.
    """

    model_path: str | None = None
    temperature: float = 0.9
    top_p: float = 0.95
    _recipe: MorphemeRecipe = field(default_factory=MorphemeRecipe)

    def generate_names(self, *, brief: str, style: str, count: int) -> list[str]:
        if self.model_path and Path(self.model_path).exists():
            return self._generate_with_model(brief=brief, style=style, count=count)
        log.info("no local model at %r, using morpheme fallback", self.model_path)
        return self._recipe.compose(limit=count)

    def _generate_with_model(self, *, brief: str, style: str, count: int) -> list[str]:
        try:
            from llama_cpp import Llama  # type: ignore[import-not-found]
        except ImportError:
            log.warning("llama-cpp-python not installed, falling back")
            return self._recipe.compose(limit=count)

        llm = Llama(model_path=self.model_path, n_ctx=2048, verbose=False)
        prompt = (
            f"Generate {count} business names for a {style} business described as: "
            f"{brief}. One name per line. No numbering, no explanation."
        )
        out = llm(prompt, max_tokens=512, temperature=self.temperature, top_p=self.top_p)
        text = out["choices"][0]["text"]
        return [line.strip(" -•\t") for line in text.splitlines() if line.strip()][:count]