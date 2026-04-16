"""Shared canonical schema models used across domain packages."""

from pydantic import BaseModel, ConfigDict, Field


class ModelBase(BaseModel):
    """Common base with explicit validation and serialization behavior."""

    model_config = ConfigDict(extra="forbid")


class Objective(ModelBase):
    """Strategic objective modeled for an actor or scenario."""

    objective_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    description: str | None = None
    priority: int | None = Field(default=None, ge=1)


class Constraint(ModelBase):
    """Bound or limitation relevant to decision making."""

    constraint_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    description: str | None = None
    severity: int | None = Field(default=None, ge=1, le=5)


class Capability(ModelBase):
    """Declared capability available to an actor."""

    capability_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    description: str | None = None
    maturity_level: int | None = Field(default=None, ge=1, le=5)
