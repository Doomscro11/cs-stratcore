# cs-stratcore

`cs-stratcore` is the sovereign strategic interaction subsystem in the CounterSec / SAVANT ecosystem.

This repository is currently in a doctrine-first scaffold phase. The objective of this pass is to freeze architecture, package boundaries, and repository shape before introducing service flow, canonical schemas, or solver logic.

## Mission

`cs-stratcore` provides bounded strategic assessment over governed state, including actor-model framing, objective-conflict analysis, move/countermove estimation, scenario scoring, escalation-aware risk framing, and recommendation candidate generation.

## Design Doctrine

- Not a generic game-theory playground.
- Not a truth authority.
- Does not use raw uncontrolled text as the primary reasoning substrate.
- Consumes curated structured state from sovereign upstream systems.
- Emits structured, explainable, auditable strategic assessments and recommendation candidates.

## Repository Scope (This Pass)

- Single Python project with `src/` layout.
- Unified namespace: `cs_stratcore`.
- Internal module scaffolding and architectural docs.
- CI workflow scaffold for lint, type-check, and tests.

No substantive API implementation, business logic, canonical schemas, or adapter integrations are included in this pass.

## Planned Ecosystem Relationships

`cs-stratcore` is designed to operate alongside:

- `cs-darkweb` (collection operations)
- `CounterSecAI` (AI-native operational interaction)
- `engraphify` (governed relational intelligence / graph state)
- `cs-mirocore` (environment and scenario-state construction)
- `ASH` (assurance, policy, audit, replay, promotion)
- `SAVANT` (mission-level federated operating system)

Future adapter seams are reserved for:

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

Scaffold and doctrine are intentionally ahead of implementation. Later passes should add executable foundations without changing the structural contract defined here.
