"""Config loader with sane defaults and shallow merge."""

from __future__ import annotations

import logging
from pathlib import Path

try:
    import tomllib  # py3.11+
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib  # type: ignore[no-redef]

log = logging.getLogger("forge.utils.config")

DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[2] / "config" / "default.toml"

_FALLBACK = {
    "meta": {"profile": "default"},
    "llm": {"model_path": None, "temperature": 0.9, "top_p": 0.95},
    "cache": {"path": "cache/forge_cache.json"},
    "trademark": {"ttl_hours": 72},
    "scoring": {"phonetic": 0.35, "brevity": 0.25, "distinctiveness": 0.25, "memorability": 0.15},
}


def load_config(path: Path | None = None) -> dict:
    """Load TOML config, merging over defaults.

    Missing file is not an error — defaults are returned so the CLI
    always has a working config.
    """
    target = path or DEFAULT_CONFIG_PATH
    if not target.exists():
        log.warning("config not found at %s, using defaults", target)
        return _FALLBACK

    with target.open("rb") as fh:
        loaded = tomllib.load(fh)

    merged = {**_FALLBACK, **loaded}
    for section, values in _FALLBACK.items():
        if isinstance(values, dict):
            merged[section] = {**values, **merged.get(section, {})}
    return merged