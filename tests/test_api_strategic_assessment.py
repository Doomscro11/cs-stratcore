"""Pass 4 API flow tests for strategic assessment orchestration."""

from importlib import import_module

from fastapi.testclient import TestClient

from cs_stratcore.api.main import app
from cs_stratcore.scoring_audit import RiskLevel
from cs_stratcore.strategy_engine import StrategicAssessment

ASSESSMENT_PATH = "/strategic-assessment"


def _request_payload() -> dict[str, object]:
    return {
        "scenario": {
            "scenario_id": "scn-101",
            "name": "Contain privileged access probing",
            "description": "Bounded pass-4 orchestration scenario",
            "actor_ids": ["actor-blue", "actor-red"],
            "objectives": [],
            "constraints": [],
            "environment": None,
        },
        "environment_state": {
            "environment_id": "env-101",
            "scenario_id": "scn-101",
            "summary": "Heightened monitoring with constrained change window.",
            "operational_conditions": ["heightened_monitoring", "change_window_constrained"],
        },
        "actors": [
            {
                "actor_id": "actor-blue",
                "name": "Blue Team",
                "role": "defender",
                "objectives": [],
                "constraints": [],
                "capabilities": [],
            },
            {
                "actor_id": "actor-red",
                "name": "Red Team",
                "role": "adversary",
                "objectives": [],
                "constraints": [],
                "capabilities": [],
            },
        ],
        "observations": [
            {
                "observation_id": "obs-101",
                "scenario_id": "scn-101",
                "source_kind": "upstream_system",
                "source_ref": "event-991",
                "statement": "Repeated privileged login failures detected.",
            }
        ],
        "claims": [
            {
                "claim_id": "clm-101",
                "scenario_id": "scn-101",
                "statement": "Credential abuse attempt likely underway.",
                "confidence": "high",
                "derivation_kind": "analytic_inference",
                "supporting_observation_ids": ["obs-101"],
            }
        ],
    }


def test_strategic_assessment_route_module_importable() -> None:
    module = import_module("cs_stratcore.api.main")
    assert hasattr(module, "app")


def test_post_strategic_assessment_returns_valid_response() -> None:
    client = TestClient(app)

    response = client.post(ASSESSMENT_PATH, json=_request_payload())

    assert response.status_code == 200

    body = response.json()
    parsed = StrategicAssessment.model_validate(body)

    assert parsed.assessment_id == "scn-101-assessment-v1"
    assert parsed.scenario_id == "scn-101"
    assert len(parsed.candidate_moves) == 2
    assert len(parsed.candidate_countermoves) == 2
    assert len(parsed.projected_outcomes) == 2
    assert parsed.risk_assessment is not None
    assert parsed.risk_assessment.risk_level == RiskLevel.HIGH
    assert len(parsed.recommendation_candidates) == 1


def test_post_strategic_assessment_is_deterministic() -> None:
    client = TestClient(app)
    payload = _request_payload()

    first_response = client.post(ASSESSMENT_PATH, json=payload)
    second_response = client.post(ASSESSMENT_PATH, json=payload)

    assert first_response.status_code == 200
    assert second_response.status_code == 200
    assert first_response.json() == second_response.json()
