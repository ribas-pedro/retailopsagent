"""Structured JSON logging helpers."""

from __future__ import annotations

import json
import logging
import sys
from datetime import datetime, timezone
from typing import Any

from retailops.core.domain.models import TraceContext

_LOGGER_NAME = "retailops"


class _JsonFormatter(logging.Formatter):
    """Format records as JSON payloads."""

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "event": getattr(record, "event", record.getMessage()),
            "trace_id": getattr(record, "trace_id", None),
            "session_id": getattr(record, "session_id", None),
            "user_id": getattr(record, "user_id", None),
            "payload": getattr(record, "payload", {}),
        }
        for optional_field in ("span", "latency_ms", "prompt_version"):
            if hasattr(record, optional_field):
                payload[optional_field] = getattr(record, optional_field)
        return json.dumps(payload, ensure_ascii=False)


def get_logger() -> logging.Logger:
    """Return configured JSON logger instance."""
    logger = logging.getLogger(_LOGGER_NAME)
    if logger.handlers:
        return logger

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(_JsonFormatter())
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    return logger


def log_event(name: str, payload: dict[str, Any], trace: TraceContext) -> None:
    """Emit a structured JSON event with standardized fields."""
    logger = get_logger()
    extra = {
        "event": name,
        "trace_id": trace.trace_id,
        "session_id": trace.session_id,
        "user_id": trace.user_id,
        "payload": payload,
    }
    if trace.span_id is not None:
        extra["span"] = trace.span_id
    if "latency_ms" in payload:
        extra["latency_ms"] = payload["latency_ms"]
    if "prompt_version" in payload:
        extra["prompt_version"] = payload["prompt_version"]
    logger.info(name, extra=extra)
