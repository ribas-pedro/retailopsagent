"""Port contract for prompt registry."""

from __future__ import annotations

from typing import Protocol


class PromptRegistryPort(Protocol):
    """Fetches prompt text and version by key."""

    def get(self, key: str) -> tuple[str, str]:
        """Return prompt text and prompt version."""
