"""Observability setup package."""

from retailops.observability.logger import get_logger, log_event
from retailops.observability.otel import setup_tracer, span

__all__ = ["get_logger", "log_event", "setup_tracer", "span"]
