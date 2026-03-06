"""Port contract for observability concerns."""

from __future__ import annotations

from contextlib import AbstractContextManager
from typing import Any, Protocol

from retailops.core.domain.models import TraceContext


class ObservabilityPort(Protocol):
    """Provides tracing and event logging interface."""

    def start_span(self, name: str, trace: TraceContext) -> AbstractContextManager[None]:
        """Start and return a span context manager."""

    def log_event(self, name: str, payload: dict[str, Any], trace: TraceContext) -> None:
        """Emit a structured observability event."""
