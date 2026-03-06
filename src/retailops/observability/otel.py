"""OpenTelemetry tracing setup and span helpers."""

from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator

from retailops.core.domain.models import TraceContext

_TRACER = None


def setup_tracer(service_name: str = "retailops-agent"):
    """Configure and return a tracer with console exporter."""
    global _TRACER
    if _TRACER is not None:
        return _TRACER

    try:
        from opentelemetry import trace
        from opentelemetry.sdk.resources import Resource
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
    except ImportError:
        _TRACER = False
        return None

    provider = TracerProvider(resource=Resource.create({"service.name": service_name}))
    provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
    trace.set_tracer_provider(provider)
    _TRACER = trace.get_tracer(service_name)
    return _TRACER


@contextmanager
def span(name: str, trace: TraceContext) -> Iterator[None]:
    """Create an OTel span and attach common attributes."""
    tracer = setup_tracer()
    if not tracer:
        yield
        return

    with tracer.start_as_current_span(name) as current_span:
        current_span.set_attribute("trace_id", trace.trace_id)
        current_span.set_attribute("session_id", trace.session_id)
        current_span.set_attribute("user_id", trace.user_id)
        if trace.span_id:
            current_span.set_attribute("span_id", trace.span_id)
        yield
