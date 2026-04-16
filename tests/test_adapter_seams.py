"""Pass 5 tests for explicit external adapter seams."""

import pytest

from cs_stratcore.adapters.attack_graphs import (
    AttackGraphsCapability,
    DeferredAttackGraphsAdapter,
)
from cs_stratcore.adapters.openspiel import (
    DeferredOpenSpielAdapter,
    OpenSpielCapability,
)
from cs_stratcore.adapters.posggym import (
    DeferredPosgGymAdapter,
    PosgGymCapability,
)
from cs_stratcore.scenario_engine import Scenario


def _scenario_fixture() -> Scenario:
    return Scenario(
        scenario_id="scn-pass5",
        name="Pass 5 seam validation",
        actor_ids=["actor-a", "actor-b"],
        objectives=[],
        constraints=[],
        environment=None,
    )


def test_adapter_modules_import_cleanly() -> None:
    assert DeferredOpenSpielAdapter.__name__ == "DeferredOpenSpielAdapter"
    assert DeferredPosgGymAdapter.__name__ == "DeferredPosgGymAdapter"
    assert DeferredAttackGraphsAdapter.__name__ == "DeferredAttackGraphsAdapter"


def test_capability_descriptors_are_explicit_and_deferred() -> None:
    open_spiel = OpenSpielCapability()
    posg_gym = PosgGymCapability()
    attack_graphs = AttackGraphsCapability()

    assert open_spiel.provider == "openspiel"
    assert posg_gym.provider == "posggym"
    assert attack_graphs.provider == "attack_graphs"

    assert open_spiel.integrated is False
    assert posg_gym.integrated is False
    assert attack_graphs.integrated is False


def test_open_spiel_stub_raises_not_implemented() -> None:
    adapter = DeferredOpenSpielAdapter()

    with pytest.raises(NotImplementedError):
        adapter.propose_moves(scenario=_scenario_fixture(), actor_ids=["actor-a", "actor-b"])


def test_posggym_stub_raises_not_implemented() -> None:
    adapter = DeferredPosgGymAdapter()

    with pytest.raises(NotImplementedError):
        adapter.project_environment_state(
            scenario=_scenario_fixture(),
            environment_state=None,
            horizon_steps=3,
        )


def test_attack_graphs_stub_raises_not_implemented() -> None:
    adapter = DeferredAttackGraphsAdapter()

    with pytest.raises(NotImplementedError):
        adapter.assess_route_risk(scenario=_scenario_fixture())
