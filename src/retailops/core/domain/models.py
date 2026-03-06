"""Core domain models for chat orchestration."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(slots=True)
class ChatRequest:
    """Input message request for the support agent."""

    user_id: str
    session_id: str
    message: str
    locale: str = "pt-BR"
    channel: str = "api"


@dataclass(slots=True)
class RetrievedChunk:
    """Knowledge chunk retrieved from search."""

    source_id: str
    source_name: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)
    score: float = 0.0


@dataclass(slots=True)
class TraceContext:
    """Trace context propagated across layers."""

    trace_id: str
    session_id: str
    user_id: str
    span_id: str | None = None


@dataclass(slots=True)
class ChatResponse:
    """Final answer payload returned by the use case."""

    answer: str
    citations: list[str] = field(default_factory=list)
    confidence: float = 0.0
    trace_id: str = ""
    prompt_versions: dict[str, str] = field(default_factory=dict)
    retrieved_sources: list[str] = field(default_factory=list)
    tool_calls: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Serialize response to plain dictionary."""
        return asdict(self)
