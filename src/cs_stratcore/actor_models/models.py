"""Actor-oriented canonical models."""

from enum import StrEnum

from pydantic import Field

from cs_stratcore.belief_engine import ConfidenceLevel
from cs_stratcore.common import Capability, Constraint, ModelBase, Objective


class RelationshipType(StrEnum):
    """Structured relationship categories between modeled actors."""

    ALLY = "ally"
    ADVERSARY = "adversary"
    PARTNER = "partner"
    DEPENDENCY = "dependency"
    COMPETITOR = "competitor"


class Actor(ModelBase):
    """Decision-capable participant in a strategic scenario."""

    actor_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    role: str | None = None
    objectives: list[Objective] = Field(default_factory=list)
    constraints: list[Constraint] = Field(default_factory=list)
    capabilities: list[Capability] = Field(default_factory=list)


class Relationship(ModelBase):
    """Typed relationship between source and target actors."""

    relationship_id: str = Field(min_length=1)
    source_actor_id: str = Field(min_length=1)
    target_actor_id: str = Field(min_length=1)
    relationship_type: RelationshipType
    confidence: ConfidenceLevel
    description: str | None = None
