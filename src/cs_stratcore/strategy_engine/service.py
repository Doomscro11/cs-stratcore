"""Deterministic Pass 4 service orchestration for strategic assessment."""

from cs_stratcore.actor_models import Actor
from cs_stratcore.belief_engine import Claim, ConfidenceLevel, Observation
from cs_stratcore.recommender import RecommendationCandidate, RecommendationType
from cs_stratcore.scenario_engine import EnvironmentState, Scenario
from cs_stratcore.scoring_audit import (
    AssessmentAuditMetadata,
    RiskAssessment,
    RiskLevel,
)
from cs_stratcore.strategy_engine.assessment import StrategicAssessment
from cs_stratcore.strategy_engine.models import Countermove, Move, MoveType, Outcome


def build_strategic_assessment(
    *,
    scenario: Scenario,
    actors: list[Actor],
    observations: list[Observation],
    claims: list[Claim],
    environment_state: EnvironmentState | None = None,
) -> StrategicAssessment:
    """Assemble a deterministic placeholder strategic assessment."""

    scenario_id = scenario.scenario_id
    assessment_id = f"{scenario_id}-assessment-v1"
    context_summary = _context_summary(scenario=scenario, environment_state=environment_state)

    candidate_moves = _build_moves(scenario_id=scenario_id, actors=actors)
    candidate_countermoves = _build_countermoves(
        scenario_id=scenario_id,
        actors=actors,
        moves=candidate_moves,
    )
    projected_outcomes = _build_outcomes(
        scenario_id=scenario_id,
        moves=candidate_moves,
        countermoves=candidate_countermoves,
        context_summary=context_summary,
    )
    risk_assessment = _build_risk_assessment(
        scenario_id=scenario_id,
        claims=claims,
        observations=observations,
        context_summary=context_summary,
    )
    recommendation_candidates = _build_recommendations(
        scenario_id=scenario_id,
        moves=candidate_moves,
    )
    audit_metadata = AssessmentAuditMetadata(
        assessment_id=assessment_id,
        schema_version="1.0.0",
        generated_at="deterministic-pass4",
        explanation_note="Deterministic placeholder orchestration for Pass 4.",
    )

    return StrategicAssessment(
        assessment_id=assessment_id,
        scenario_id=scenario_id,
        observations=observations,
        claims=claims,
        candidate_moves=candidate_moves,
        candidate_countermoves=candidate_countermoves,
        projected_outcomes=projected_outcomes,
        risk_assessment=risk_assessment,
        recommendation_candidates=recommendation_candidates,
        audit_metadata=audit_metadata,
    )


def _context_summary(*, scenario: Scenario, environment_state: EnvironmentState | None) -> str:
    if environment_state is not None:
        return environment_state.summary
    if scenario.environment is not None:
        return scenario.environment.summary
    return f"Scenario context: {scenario.name}"


def _build_moves(*, scenario_id: str, actors: list[Actor]) -> list[Move]:
    moves: list[Move] = []

    for index, actor in enumerate(actors, start=1):
        moves.append(
            Move(
                move_id=f"{scenario_id}-move-{index}",
                scenario_id=scenario_id,
                actor_id=actor.actor_id,
                move_type=MoveType.DEFENSIVE,
                description=f"Placeholder defensive action by {actor.name}.",
            )
        )

    return moves


def _build_countermoves(
    *,
    scenario_id: str,
    actors: list[Actor],
    moves: list[Move],
) -> list[Countermove]:
    countermoves: list[Countermove] = []

    actor_ids = [actor.actor_id for actor in actors]
    fallback_actor_id = actor_ids[0]

    for index, move in enumerate(moves, start=1):
        responder_actor_id = _next_actor_id(
            actor_ids=actor_ids,
            current_actor_id=move.actor_id,
            fallback_actor_id=fallback_actor_id,
        )
        countermoves.append(
            Countermove(
                countermove_id=f"{scenario_id}-countermove-{index}",
                scenario_id=scenario_id,
                actor_id=responder_actor_id,
                responds_to_move_id=move.move_id,
                move_type=MoveType.OFFENSIVE,
                description=f"Placeholder countermove responding to {move.move_id}.",
            )
        )

    return countermoves


def _next_actor_id(
    *,
    actor_ids: list[str],
    current_actor_id: str,
    fallback_actor_id: str,
) -> str:
    if len(actor_ids) <= 1:
        return fallback_actor_id

    current_index = actor_ids.index(current_actor_id)
    next_index = (current_index + 1) % len(actor_ids)
    return actor_ids[next_index]


def _build_outcomes(
    *,
    scenario_id: str,
    moves: list[Move],
    countermoves: list[Countermove],
    context_summary: str,
) -> list[Outcome]:
    outcomes: list[Outcome] = []

    for index, move in enumerate(moves, start=1):
        countermove = countermoves[index - 1]
        outcomes.append(
            Outcome(
                outcome_id=f"{scenario_id}-outcome-{index}",
                scenario_id=scenario_id,
                description=(
                    "Placeholder outcome from "
                    f"{move.move_id} and {countermove.countermove_id}. "
                    f"Context: {context_summary}."
                ),
                affected_actor_ids=[move.actor_id, countermove.actor_id],
            )
        )

    return outcomes


def _build_risk_assessment(
    *,
    scenario_id: str,
    claims: list[Claim],
    observations: list[Observation],
    context_summary: str,
) -> RiskAssessment:
    risk_level = _derive_risk_level(claims=claims, observations=observations)

    risk_factors: list[str] = []
    if claims:
        risk_factors.append("claim_presence")
    if observations:
        risk_factors.append("observation_presence")
    if not risk_factors:
        risk_factors.append("limited_signal")

    return RiskAssessment(
        risk_assessment_id=f"{scenario_id}-risk-v1",
        scenario_id=scenario_id,
        risk_level=risk_level,
        summary=f"Deterministic placeholder risk framing for context: {context_summary}.",
        primary_risk_factors=risk_factors,
    )


def _derive_risk_level(
    *,
    claims: list[Claim],
    observations: list[Observation],
) -> RiskLevel:
    if any(claim.confidence == ConfidenceLevel.HIGH for claim in claims):
        return RiskLevel.HIGH
    if claims:
        return RiskLevel.MEDIUM
    if observations:
        return RiskLevel.LOW
    return RiskLevel.LOW


def _build_recommendations(
    *,
    scenario_id: str,
    moves: list[Move],
) -> list[RecommendationCandidate]:
    if not moves:
        return []

    primary_move = moves[0]
    return [
        RecommendationCandidate(
            recommendation_id=f"{scenario_id}-recommendation-1",
            scenario_id=scenario_id,
            recommendation_type=RecommendationType.IMMEDIATE_ACTION,
            rationale=(
                "Deterministic placeholder recommendation to execute "
                f"{primary_move.move_id} first."
            ),
            confidence=ConfidenceLevel.MEDIUM,
            linked_move_ids=[primary_move.move_id],
        )
    ]
