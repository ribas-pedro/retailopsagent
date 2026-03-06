"""Observability adapter based on OTel + structured logger."""

from __future__ import annotations

from contextlib import AbstractContextManager
from typing import Any

from retailops.core.domain.models import TraceContext
from retailops.core.ports.observability import ObservabilityPort
from retailops.observability.logger import log_event
from retailops.observability.otel import span


class OTelObservabilityAdapter(ObservabilityPort):
    """Implements observability port using logger and OTel spans."""

    def start_span(self, name: str, trace: TraceContext) -> AbstractContextManager[None]:
        """Start a named span."""
        return span(name, trace)

    def log_event(self, name: str, payload: dict[str, Any], trace: TraceContext) -> None:
        """Log structured observability event."""
        log_event(name=name, payload=payload, trace=trace)
