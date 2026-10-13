"""Bootstrap: wires config, adapters, services, and handlers together."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

from forge_adapters.llm.local_llm_adapter import LocalLLMAdapter
from forge_adapters.storage.json_cache_adapter import JsonCacheAdapter
from forge_core.engine import NamingEngine
from forge_core.phonetics import PhoneticScorer
from forge_core.scoring import BrandabilityScorer
from forge_services.generation_service import GenerationService
from forge_services.trademark_service import TrademarkService
from forge_utils.config_loader import load_config

log = logging.getLogger("forge.bootstrap")


@dataclass(slots=True)
class Container:
    """Resolved dependency graph handed to handlers."""

    generation: GenerationService
    trademark: TrademarkService
    config: dict


def build_container(config_path: Path | None = None) -> Container:
    """Construct the full dependency graph.

    Config is loaded from `config/default.toml` unless overridden.
    LLM adapter falls back to a deterministic stub when no local
    weights are present — the CLI must never hard-fail on a fresh clone.
    """
    cfg = load_config(config_path)
    log.debug("config loaded: %s", cfg.get("meta", {}).get("profile"))

    cache = JsonCacheAdapter(Path(cfg["cache"]["path"]))
    llm = LocalLLMAdapter(
        model_path=cfg["llm"].get("model_path"),
        temperature=float(cfg["llm"]["temperature"]),
        top_p=float(cfg["llm"]["top_p"]),
    )

    engine = NamingEngine(
        llm=llm,
        phonetics=PhoneticScorer(),
        scorer=BrandabilityScorer(weights=cfg["scoring"]),
    )
    trademark = TrademarkService(cache=cache, ttl_hours=int(cfg["trademark"]["ttl_hours"]))

    return Container(
        generation=GenerationService(engine=engine, trademark=trademark),
        trademark=trademark,
        config=cfg,
    )