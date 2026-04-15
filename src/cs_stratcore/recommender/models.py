"""Recommendation candidate canonical models."""

from enum import StrEnum

from pydantic import Field

from cs_stratcore.belief_engine import ConfidenceLevel
from cs_stratcore.common import ModelBase


class RecommendationType(StrEnum):
    """Recommendation proposal categories."""

    IMMEDIATE_ACTION = "immediate_action"
    PREPARATORY_ACTION = "preparatory_action"
    MONITORING_ACTION = "monitoring_action"


class RecommendationCandidate(ModelBase):
    """Structured recommendation proposal produced by assessment flow."""

    recommendation_id: str = Field(min_length=1)
    scenario_id: str = Field(min_length=1)
    recommendation_type: RecommendationType
    rationale: str = Field(min_length=1)
    confidence: ConfidenceLevel
    linked_move_ids: list[str] = Field(default_factory=list)
