"""Pydantic schemas aligned with chat domain models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class ChatRequestSchema(BaseModel):
    """API request schema for chat endpoint."""

    user_id: str
    session_id: str
    message: str
    locale: str = "pt-BR"
    channel: str = "api"


class ChatResponseSchema(BaseModel):
    """API response schema for chat endpoint."""

    answer: str
    citations: list[str] = Field(default_factory=list)
    confidence: float = 0.0
    trace_id: str
    prompt_versions: dict[str, str] = Field(default_factory=dict)
    retrieved_sources: list[str] = Field(default_factory=list)
    tool_calls: list[dict[str, Any]] = Field(default_factory=list)
