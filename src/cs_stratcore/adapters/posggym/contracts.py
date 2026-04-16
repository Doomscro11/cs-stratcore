"""POSGGym adapter seam contracts.

This seam defines future partially observable environment interaction points
without introducing runtime simulation integration in Pass 5.
"""

from dataclasses import dataclass
from typing import Protocol

from cs_stratcore.scenario_engine import EnvironmentState, Scenario


@dataclass(frozen=True)
class PosgGymCapability:
    """Descriptor for deferred POSGGym-backed capability."""

    provider: str = "posggym"
    supports_partial_observability: bool = True
    supports_multi_agent_step: bool = True
    integrated: bool = False


class PosgGymEnvironmentAdapter(Protocol):
    """Contract for future environment rollout over canonical scenario context.

    Consumes canonical `Scenario` plus optional `EnvironmentState`.
    Emits canonical `EnvironmentState` projections.
    """

    def project_environment_state(
        self,
        *,
        scenario: Scenario,
        environment_state: EnvironmentState | None,
        horizon_steps: int,
    ) -> EnvironmentState:
        """Project an updated environment state."""


class DeferredPosgGymAdapter:
    """Pass 5 placeholder implementation for the POSGGym seam.

    Explicitly deferred:
    - importing POSGGym runtime packages
    - environment execution and stepping
    - policy-driven observation rollout
    """

    capability = PosgGymCapability()

    def project_environment_state(
        self,
        *,
        scenario: Scenario,
        environment_state: EnvironmentState | None,
        horizon_steps: int,
    ) -> EnvironmentState:
        raise NotImplementedError(
            "POSGGym integration is deferred. This seam is a Pass 5 stub."
        )
