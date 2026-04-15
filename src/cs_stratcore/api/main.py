"""Minimal FastAPI application shell for cs_stratcore."""

from fastapi import FastAPI

app = FastAPI(
    title="cs-stratcore",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"service": "cs-stratcore", "status": "ok"}
