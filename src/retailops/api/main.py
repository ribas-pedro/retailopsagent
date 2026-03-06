"""FastAPI application entrypoint."""

from __future__ import annotations

import time
from uuid import uuid4

from fastapi import FastAPI, Request

from retailops.core.domain.models import TraceContext
from retailops.observability import log_event, setup_tracer

app = FastAPI(title="RetailOps Agent", version="0.1.0")
setup_tracer(service_name="retailops-agent")


@app.middleware("http")
async def trace_middleware(request: Request, call_next):
    """Create and propagate trace context for each request."""
    start = time.perf_counter()
    trace = TraceContext(
        trace_id=str(uuid4()),
        session_id=request.headers.get("x-session-id", "http-session"),
        user_id=request.headers.get("x-user-id", "anonymous"),
    )
    request.state.trace = trace

    log_event(
        name="api.request.start",
        payload={"method": request.method, "path": request.url.path, "span": "api"},
        trace=trace,
    )

    response = await call_next(request)

    latency_ms = round((time.perf_counter() - start) * 1000, 2)
    response.headers["x-trace-id"] = trace.trace_id
    log_event(
        name="api.request.end",
        payload={
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "latency_ms": latency_ms,
            "span": "api",
        },
        trace=trace,
    )
    return response


@app.get("/health")
def health(request: Request) -> dict[str, str]:
    """Health check endpoint."""
    trace = request.state.trace
    return {"status": "ok", "trace_id": trace.trace_id}
