import json

from retailops.core.domain.models import TraceContext
from retailops.observability.logger import log_event


def test_log_event_includes_trace_and_event(capsys) -> None:
    trace = TraceContext(trace_id="trace-123", session_id="s-1", user_id="u-1")

    log_event("unit.test.event", {"foo": "bar"}, trace)

    captured = capsys.readouterr().out.strip().splitlines()
    assert captured
    payload = json.loads(captured[-1])
    assert payload["event"] == "unit.test.event"
    assert payload["trace_id"] == "trace-123"
    assert payload["session_id"] == "s-1"
    assert payload["user_id"] == "u-1"
    assert payload["payload"]["foo"] == "bar"
