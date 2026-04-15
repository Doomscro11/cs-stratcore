# cs-stratcore

`cs-stratcore` is the sovereign strategic interaction subsystem in the CounterSec / SAVANT ecosystem.

This repository has completed bounded implementation through Pass 5:

- doctrine and scaffold,
- executable foundation,
- canonical schemas,
- bounded strategic assessment API flow,
- explicit external adapter seams (deferred, not integrated).

## Mission

`cs-stratcore` provides bounded strategic assessment over governed state, including actor-model framing, objective-conflict analysis, move/countermove estimation, scenario scoring, escalation-aware risk framing, and recommendation candidate generation.

## Design Doctrine

- Not a generic game-theory playground.
- Not a truth authority.
- Does not use raw uncontrolled text as the primary reasoning substrate.
- Consumes curated structured state from sovereign upstream systems.
- Emits structured, explainable, auditable strategic assessments and recommendation candidates.

## Repository Scope (Current State)

- Single Python project with `src/` layout.
- Unified namespace: `cs_stratcore`.
- FastAPI app entrypoint at `src/cs_stratcore/api/main.py` with:
  - `GET /health` returning `{"service": "cs-stratcore", "status": "ok"}`
  - deterministic `POST /strategic-assessment`
- Canonical internal schemas across actor, scenario, belief, strategy, recommendation, and scoring/audit domains.
- Deterministic placeholder service orchestration for strategic assessment.
- Adapter seam contracts for OpenSpiel, POSGGym, and attack-graphs with deferred stubs (`NotImplementedError`).
- CI workflow for lint, type-check, and tests.

No external runtime integration is included yet for OpenSpiel, POSGGym, or attack-graphs.

## Planned Ecosystem Relationships

`cs-stratcore` is designed to operate alongside:

- `cs-darkweb` (collection operations)
- `CounterSecAI` (AI-native operational interaction)
- `engraphify` (governed relational intelligence / graph state)
- `cs-mirocore` (environment and scenario-state construction)
- `ASH` (assurance, policy, audit, replay, promotion)
- `SAVANT` (mission-level federated operating system)

Adapter seams are present for:

- OpenSpiel
- POSGGym
- attack-graphs

## Structure

```text
cs-stratcore/
  .github/workflows/ci.yml
  docs/architecture/
    overview.md
    module_map.md
    rules.md
  src/cs_stratcore/
    api/
    common/
    actor_models/
    scenario_engine/
    payoff_engine/
    strategy_engine/
    belief_engine/
    recommender/
    scoring_audit/
    adapters/
      openspiel/
      posggym/
      attack_graphs/
  tests/
  pyproject.toml
```

## Status

`cs-stratcore` is structurally complete through Pass 5. The architecture is stable, canonical model ownership remains internal, service behavior is deterministic and bounded, and external capability seams are explicit but deferred.
