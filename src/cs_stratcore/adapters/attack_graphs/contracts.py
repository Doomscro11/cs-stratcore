"""attack-graphs adapter seam contracts.

This seam defines future adversary route/path modeling points while preserving
canonical output ownership inside cs_stratcore.
"""

from dataclasses import dataclass
from typing import Protocol

from cs_stratcore.scenario_engine import Scenario
from cs_stratcore.scoring_audit import RiskAssessment


@dataclass(frozen=True)
class AttackGraphsCapability:
    """Descriptor for deferred attack-graphs-backed capability."""

    provider: str = "attack_graphs"
    supports_attack_path_modeling: bool = True
    supports_route_risk_signals: bool = True
    integrated: bool = False


class AttackGraphsRouteAdapter(Protocol):
    """Contract for future route-modeling over canonical scenario state.

    Consumes canonical `Scenario`.
    Emits canonical `RiskAssessment` signals usable by internal services.
    """

    def assess_route_risk(self, *, scenario: Scenario) -> RiskAssessment:
        """Assess adversary route risk using canonical model outputs."""


class DeferredAttackGraphsAdapter:
    """Pass 5 placeholder implementation for the attack-graphs seam.

    Explicitly deferred:
    - importing attack-graphs runtime packages
    - graph construction/traversal
    - route scoring integration
    """

    capability = AttackGraphsCapability()

    def assess_route_risk(self, *, scenario: Scenario) -> RiskAssessment:
        raise NotImplementedError(
            "attack-graphs integration is deferred. This seam is a Pass 5 stub."
        )
