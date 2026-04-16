"""Scenario and environment canonical models."""

from pydantic import Field

from cs_stratcore.common import Constraint, ModelBase, Objective


class EnvironmentState(ModelBase):
    """Structured contextual conditions surrounding a scenario."""

    environment_id: str = Field(min_length=1)
    scenario_id: str = Field(min_length=1)
    summary: str = Field(min_length=1)
    operational_conditions: list[str] = Field(default_factory=list)


class Scenario(ModelBase):
    """Bounded problem frame for strategic assessment."""

    scenario_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    description: str | None = None
    actor_ids: list[str] = Field(default_factory=list)
    objectives: list[Objective] = Field(default_factory=list)
    constraints: list[Constraint] = Field(default_factory=list)
    environment: EnvironmentState | None = None
