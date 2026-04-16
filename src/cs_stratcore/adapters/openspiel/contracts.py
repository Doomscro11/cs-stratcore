"""OpenSpiel adapter seam contracts.

This seam defines future strategic-search integration points while keeping
internal model ownership inside cs_stratcore.
"""

from dataclasses import dataclass
from typing import Protocol

from cs_stratcore.scenario_engine import Scenario
from cs_stratcore.strategy_engine import Move


@dataclass(frozen=True)
class OpenSpielCapability:
    """Descriptor for deferred OpenSpiel-backed capability."""

    provider: str = "openspiel"
    supports_strategic_search: bool = True
    supports_equilibrium_analysis: bool = True
    integrated: bool = False


class OpenSpielStrategicSearchAdapter(Protocol):
    """Contract for future strategic search against canonical scenario state.

    Consumes canonical `Scenario` and actor identifiers.
    Emits canonical `Move` candidates.
    """

    def propose_moves(self, *, scenario: Scenario, actor_ids: list[str]) -> list[Move]:
        """Produce candidate moves from canonical strategic state."""


class DeferredOpenSpielAdapter:
    """Pass 5 placeholder implementation for the OpenSpiel seam.

    Explicitly deferred:
    - importing OpenSpiel runtime packages
    - game construction and solving
    - policy/equilibrium extraction
    """

    capability = OpenSpielCapability()

    def propose_moves(self, *, scenario: Scenario, actor_ids: list[str]) -> list[Move]:
        raise NotImplementedError(
            "OpenSpiel integration is deferred. This seam is a Pass 5 stub."
        )
