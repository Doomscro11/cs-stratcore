"""Belief and confidence models for canonical strategic schemas."""

from enum import StrEnum

from pydantic import Field

from cs_stratcore.common import DerivationKind, ModelBase, SourceKind


class ConfidenceLevel(StrEnum):
    """Bounded confidence labels used across claims and assessments."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Observation(ModelBase):
    """Raw or semi-processed fact/event reported by sovereign systems."""

    observation_id: str = Field(min_length=1)
    scenario_id: str = Field(min_length=1)
    source_kind: SourceKind
    source_ref: str | None = None
    statement: str = Field(min_length=1)


class Claim(ModelBase):
    """Structured assertion derived from observation or analysis."""

    claim_id: str = Field(min_length=1)
    scenario_id: str = Field(min_length=1)
    statement: str = Field(min_length=1)
    confidence: ConfidenceLevel
    derivation_kind: DerivationKind
    supporting_observation_ids: list[str] = Field(default_factory=list)
