"""Canonical schema coverage tests for Pass 3."""

import pytest
from pydantic import ValidationError

from cs_stratcore.actor_models import Actor, Relationship, RelationshipType
from cs_stratcore.belief_engine import Claim, ConfidenceLevel, Observation
from cs_stratcore.common import (
    Capability,
    Constraint,
    DerivationKind,
    Objective,
    SourceKind,
)
from cs_stratcore.recommender import (
    RecommendationCandidate,
    RecommendationType,
)
from cs_stratcore.scenario_engine import EnvironmentState, Scenario
from cs_stratcore.scoring_audit import (
    AssessmentAuditMetadata,
    RiskAssessment,
    RiskLevel,
)
from cs_stratcore.strategy_engine import (
    Countermove,
    Move,
    MoveType,
    Outcome,
    StrategicAssessment,
)


def test_required_models_import_stably() -> None:
    assert Actor.__name__ == "Actor"
    assert Objective.__name__ == "Objective"
    assert Constraint.__name__ == "Constraint"
    assert Capability.__name__ == "Capability"
    assert Relationship.__name__ == "Relationship"
    assert Observation.__name__ == "Observation"
    assert Claim.__name__ == "Claim"
    assert Scenario.__name__ == "Scenario"
    assert EnvironmentState.__name__ == "EnvironmentState"
    assert Move.__name__ == "Move"
    assert Countermove.__name__ == "Countermove"
    assert Outcome.__name__ == "Outcome"
    assert RiskAssessment.__name__ == "RiskAssessment"
    assert RecommendationCandidate.__name__ == "RecommendationCandidate"
    assert StrategicAssessment.__name__ == "StrategicAssessment"


def test_representative_model_instantiation() -> None:
    objective = Objective(objective_id="obj-1", name="Maintain service continuity", priority=1)
    constraint = Constraint(constraint_id="con-1", name="Limited response window", severity=3)
    capability = Capability(capability_id="cap-1", name="Incident response team", maturity_level=4)

    actor = Actor(
        actor_id="actor-1",
        name="Blue Team",
        role="defender",
        objectives=[objective],
        constraints=[constraint],
        capabilities=[capability],
    )
    relationship = Relationship(
        relationship_id="rel-1",
        source_actor_id="actor-1",
        target_actor_id="actor-2",
        relationship_type=RelationshipType.ALLY,
        confidence=ConfidenceLevel.MEDIUM,
    )

    environment = EnvironmentState(
        environment_id="env-1",
        scenario_id="scn-1",
        summary="Elevated threat activity in production environment.",
        operational_conditions=["heightened_monitoring", "limited_change_window"],
    )
    scenario = Scenario(
        scenario_id="scn-1",
        name="Contain lateral movement risk",
        actor_ids=["actor-1", "actor-2"],
        objectives=[objective],
        constraints=[constraint],
        environment=environment,
    )

    observation = Observation(
        observation_id="obs-1",
        scenario_id="scn-1",
        source_kind=SourceKind.UPSTREAM_SYSTEM,
        source_ref="event-447",
        statement="Multiple failed privileged logins detected.",
    )
    claim = Claim(
        claim_id="clm-1",
        scenario_id="scn-1",
        statement="Adversary is probing privileged access paths.",
        confidence=ConfidenceLevel.MEDIUM,
        derivation_kind=DerivationKind.ANALYTIC_INFERENCE,
        supporting_observation_ids=["obs-1"],
    )

    move = Move(
        move_id="mov-1",
        scenario_id="scn-1",
        actor_id="actor-1",
        move_type=MoveType.DEFENSIVE,
        description="Enforce temporary privilege escalation controls.",
    )
    countermove = Countermove(
        countermove_id="cmov-1",
        scenario_id="scn-1",
        actor_id="actor-2",
        responds_to_move_id="mov-1",
        move_type=MoveType.OFFENSIVE,
        description="Shift to alternate credential theft channel.",
    )
    outcome = Outcome(
        outcome_id="out-1",
        scenario_id="scn-1",
        description="Privilege abuse opportunity reduced within monitoring window.",
        affected_actor_ids=["actor-1", "actor-2"],
    )

    risk_assessment = RiskAssessment(
        risk_assessment_id="risk-1",
        scenario_id="scn-1",
        risk_level=RiskLevel.HIGH,
        summary="Elevated risk of account compromise if controls are delayed.",
        primary_risk_factors=["credential_stuffing", "stale_privileges"],
    )
    recommendation = RecommendationCandidate(
        recommendation_id="rec-1",
        scenario_id="scn-1",
        recommendation_type=RecommendationType.IMMEDIATE_ACTION,
        rationale="Immediate privilege hardening reduces exploitability.",
        confidence=ConfidenceLevel.HIGH,
        linked_move_ids=["mov-1"],
    )
    audit = AssessmentAuditMetadata(
        assessment_id="assess-1",
        schema_version="1.0.0",
        explanation_note="Canonical schema pass fixture.",
    )

    assessment = StrategicAssessment(
        assessment_id="assess-1",
        scenario_id="scn-1",
        observations=[observation],
        claims=[claim],
        candidate_moves=[move],
        candidate_countermoves=[countermove],
        projected_outcomes=[outcome],
        risk_assessment=risk_assessment,
        recommendation_candidates=[recommendation],
        audit_metadata=audit,
    )

    assert actor.actor_id == "actor-1"
    assert relationship.relationship_type == RelationshipType.ALLY
    assert scenario.environment is not None
    assert assessment.risk_assessment is not None
    recommendation_type = assessment.recommendation_candidates[0].recommendation_type
    assert recommendation_type == RecommendationType.IMMEDIATE_ACTION


def test_structural_validation_is_lightweight_and_enforced() -> None:
    with pytest.raises(ValidationError):
        Objective(objective_id="", name="Invalid")

    with pytest.raises(ValidationError):
        Actor(actor_id="actor-1", name="Blue Team", unknown_field="x")
