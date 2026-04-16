"""Risk and audit metadata canonical models."""

from enum import StrEnum

from pydantic import Field

from cs_stratcore.common import ModelBase


class RiskLevel(StrEnum):
    """Risk severity labels for bounded risk framing."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class RiskAssessment(ModelBase):
    """Bounded risk framing object."""

    risk_assessment_id: str = Field(min_length=1)
    scenario_id: str = Field(min_length=1)
    risk_level: RiskLevel
    summary: str = Field(min_length=1)
    primary_risk_factors: list[str] = Field(default_factory=list)


class AssessmentAuditMetadata(ModelBase):
    """Lightweight placeholder metadata for auditability."""

    assessment_id: str = Field(min_length=1)
    schema_version: str = Field(min_length=1)
    generated_at: str | None = None
    explanation_note: str | None = None
