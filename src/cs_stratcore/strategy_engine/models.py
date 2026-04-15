"""Move, countermove, and outcome canonical models."""

from enum import StrEnum

from pydantic import Field

from cs_stratcore.common import ModelBase


class MoveType(StrEnum):
    """Candidate move categories for strategic analysis."""

    DEFENSIVE = "defensive"
    OFFENSIVE = "offensive"
    DIPLOMATIC = "diplomatic"
    ECONOMIC = "economic"


class Move(ModelBase):
    """Candidate action proposed by an actor."""

    move_id: str = Field(min_length=1)
    scenario_id: str = Field(min_length=1)
    actor_id: str = Field(min_length=1)
    move_type: MoveType
    description: str = Field(min_length=1)


class Countermove(ModelBase):
    """Response candidate to a move."""

    countermove_id: str = Field(min_length=1)
    scenario_id: str = Field(min_length=1)
    actor_id: str = Field(min_length=1)
    responds_to_move_id: str = Field(min_length=1)
    move_type: MoveType
    description: str = Field(min_length=1)


class Outcome(ModelBase):
    """Structured possible result state for a move/countermove path."""

    outcome_id: str = Field(min_length=1)
    scenario_id: str = Field(min_length=1)
    description: str = Field(min_length=1)
    affected_actor_ids: list[str] = Field(default_factory=list)
