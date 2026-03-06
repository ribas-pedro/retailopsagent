"""Port contract for LLM providers."""

from __future__ import annotations

from typing import Any, Protocol

from retailops.core.domain.models import TraceContext


class LLMPort(Protocol):
    """Generates model output from a prompt."""

    def generate(
        self,
        prompt: str,
        trace: TraceContext,
        response_schema: dict[str, Any] | None,
    ) -> dict[str, Any]:
        """Generate structured response payload."""
