"""Chat use case skeleton."""

from __future__ import annotations

from retailops.core.domain.errors import UseCaseError
from retailops.core.domain.models import ChatRequest, ChatResponse, TraceContext
from retailops.core.ports import KnowledgeBasePort, LLMPort, ObservabilityPort, PromptRegistryPort


def handle_chat(
    request: ChatRequest,
    llm: LLMPort,
    kb: KnowledgeBasePort,
    prompts: PromptRegistryPort,
    obs: ObservabilityPort,
) -> ChatResponse:
    """Handle a chat request using orchestrated ports."""
    trace = TraceContext(
        trace_id=f"trace-{request.session_id}",
        session_id=request.session_id,
        user_id=request.user_id,
    )

    with obs.start_span("use_case.handle_chat", trace):
        obs.log_event("chat.request.received", {"channel": request.channel}, trace)

        with obs.start_span("compose_prompt", trace):
            # TODO: choose prompt strategy by locale/channel/user segment.
            prompt_text, prompt_version = prompts.get("chat.default")
            obs.log_event(
                "chat.prompt.selected",
                {"prompt_key": "chat.default", "prompt_version": prompt_version, "span": "compose_prompt"},
                trace,
            )

        with obs.start_span("retrieve", trace):
            # TODO: refine retrieval strategy and tune k by query complexity.
            chunks = kb.retrieve(query=request.message, k=5, trace=trace)
            obs.log_event("chat.retrieve.done", {"retrieved_count": len(chunks), "span": "retrieve"}, trace)

        with obs.start_span("llm_generate", trace):
            # TODO: build context from retrieved chunks and apply guardrails.
            model_payload = llm.generate(prompt=prompt_text, trace=trace, response_schema=None)
            obs.log_event("chat.llm_generate.done", {"span": "llm_generate"}, trace)

        # TODO: parse model payload via strict schema validation.
        answer = str(model_payload.get("answer", ""))
        if not answer:
            raise UseCaseError("LLM returned empty answer payload")

        return ChatResponse(
            answer=answer,
            confidence=float(model_payload.get("confidence", 0.0)),
            trace_id=trace.trace_id,
            prompt_versions={"chat.default": prompt_version},
            citations=[chunk.source_id for chunk in chunks],
            retrieved_sources=[chunk.source_name for chunk in chunks],
            tool_calls=[],
        )
