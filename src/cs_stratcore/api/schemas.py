"""API request schemas for strategic assessment routes."""

from pydantic import Field

from cs_stratcore.actor_models import Actor
from cs_stratcore.belief_engine import Claim, Observation
from cs_stratcore.common import ModelBase
from cs_stratcore.scenario_engine import EnvironmentState, Scenario


class StrategicAssessmentRequest(ModelBase):
    """Structured request payload for strategic assessment orchestration."""

    scenario: Scenario
    environment_state: EnvironmentState | None = None
    actors: list[Actor] = Field(min_length=1)
    observations: list[Observation] = Field(default_factory=list)
    claims: list[Claim] = Field(default_factory=list)
