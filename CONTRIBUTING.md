# Contributing to ai-business-name-forge

Thanks for wanting to forge names with us. This is a hobbyist project —
keep it scrappy, keep it tested.

## Dev setup

```bash
git clone https://github.com/forge-labs/ai-business-name-forge
cd ai-business-name-forge
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -e ".[dev]"
pre-commit install
```

## Layout

- `forge_app/` — entry + bootstrap
- `forge_core/` — naming engine, scoring, phonetics
- `forge_handlers/` — thin CLI/IPC handlers
- `forge_services/` — business logic services
- `forge_models/` — dataclasses + pydantic schemas
- `forge_adapters/` — platform + backend adapters
- `forge_utils/` — helpers, no business logic
- `config/` — TOML configs
- `tests/` — pytest suite

## Standards

- Format with `ruff format`. Lint with `ruff check`.
- Type hints everywhere. `mypy --strict` must pass on `forge_core/`.
- New name patterns go in `forge_core/patterns/` with a matching test.
- Commit messages: `forge: <area>: <what>`.

## PRs

1. Branch from `main`.
2. One logical change per PR.
3. Tests required for new behavior.
4. Update `config/default.toml` if you add tunables.