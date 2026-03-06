"""Port contract for knowledge base operations."""

from __future__ import annotations

from typing import Protocol

from retailops.core.domain.models import RetrievedChunk, TraceContext


class KnowledgeBasePort(Protocol):
    """Ingests and retrieves knowledge documents."""

    def ingest(self) -> None:
        """Ingest documents into retrieval store."""

    def retrieve(self, query: str, k: int, trace: TraceContext) -> list[RetrievedChunk]:
        """Retrieve top-k chunks relevant to query."""
