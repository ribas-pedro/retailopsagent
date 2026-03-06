from dataclasses import asdict

from retailops.core.domain.models import ChatRequest, ChatResponse, RetrievedChunk, TraceContext


def test_chat_request_defaults() -> None:
    request = ChatRequest(user_id="u1", session_id="s1", message="oi")

    assert request.locale == "pt-BR"
    assert request.channel == "api"


def test_chat_response_serialization_and_defaults() -> None:
    response = ChatResponse(answer="Olá", trace_id="t1")
    as_dict = response.to_dict()

    assert as_dict["answer"] == "Olá"
    assert as_dict["trace_id"] == "t1"
    assert as_dict["citations"] == []
    assert as_dict["prompt_versions"] == {}
    assert as_dict["retrieved_sources"] == []
    assert as_dict["tool_calls"] == []


def test_retrieved_chunk_and_trace_context_serialization() -> None:
    chunk = RetrievedChunk(
        source_id="doc-1",
        source_name="policy.md",
        text="texto",
        metadata={"section": "returns"},
        score=0.87,
    )
    trace = TraceContext(trace_id="trace-1", session_id="s1", user_id="u1", span_id="span-1")

    assert asdict(chunk)["metadata"]["section"] == "returns"
    assert asdict(trace)["span_id"] == "span-1"
