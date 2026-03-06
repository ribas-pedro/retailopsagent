"""FastAPI application entrypoint."""

from fastapi import FastAPI

app = FastAPI(title="RetailOps Agent", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}
