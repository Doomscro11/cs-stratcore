"""Strategic assessment aggregate container schema."""

from pydantic import Field

from cs_stratcore.belief_engine import Claim, Observation
from cs_stratcore.common import ModelBase
from cs_stratcore.recommender import RecommendationCandidate
from cs_stratcore.scoring_audit import AssessmentAuditMetadata, RiskAssessment
from cs_stratcore.strategy_engine.models import Countermove, Move, Outcome


class StrategicAssessment(ModelBase):
    """Typed aggregate output for bounded strategic assessment state."""

    assessment_id: str = Field(min_length=1)
    scenario_id: str = Field(min_length=1)
    observations: list[Observation] = Field(default_factory=list)
    claims: list[Claim] = Field(default_factory=list)
    candidate_moves: list[Move] = Field(default_factory=list)
    candidate_countermoves: list[Countermove] = Field(default_factory=list)
    projected_outcomes: list[Outcome] = Field(default_factory=list)
    risk_assessment: RiskAssessment | None = None
    recommendation_candidates: list[RecommendationCandidate] = Field(default_factory=list)
    audit_metadata: AssessmentAuditMetadata | None = None
