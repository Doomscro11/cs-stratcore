"""Minimal FastAPI application shell for cs_stratcore."""

from fastapi import FastAPI

from cs_stratcore.api.schemas import StrategicAssessmentRequest
from cs_stratcore.strategy_engine import StrategicAssessment
from cs_stratcore.strategy_engine.service import build_strategic_assessment

app = FastAPI(
    title="cs-stratcore",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"service": "cs-stratcore", "status": "ok"}


@app.post("/strategic-assessment")
def strategic_assessment(request: StrategicAssessmentRequest) -> StrategicAssessment:
    return build_strategic_assessment(
        scenario=request.scenario,
        actors=request.actors,
        observations=request.observations,
        claims=request.claims,
        environment_state=request.environment_state,
    )
