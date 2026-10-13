"""GenerationRequest schema."""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator


class GenerationRequest(BaseModel):
    """Validated input for a single forge call."""

    brief: str = Field(min_length=3, max_length=400)
    count: int = Field(default=12, ge=1, le=200)
    style: str = Field(default="modern")
    tld: str = Field(default="com")

    @field_validator("style")
    @classmethod
    def _style_known(cls, value: str) -> str:
        allowed = {"modern", "classic", "playful", "technical", "abstract"}
        if value not in allowed:
            raise ValueError(f"style must be one of {sorted(allowed)}")
        return value

    @field_validator("tld")
    @classmethod
    def _tld_shape(cls, value: str) -> str:
        if not value.isalpha() or len(value) > 12:
            raise ValueError("tld must be alphabetic and <= 12 chars")
        return value.lower()