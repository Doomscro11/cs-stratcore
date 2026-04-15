# Module Responsibility Map

This map defines ownership boundaries inside `src/cs_stratcore/`.

## Internal Modules

- `api`: ingress and egress contracts at repository boundary (transport layer only in later passes).
- `common`: shared primitives that are stable, lightweight, and explicitly cross-cutting.
- `actor_models`: actor representation, objective framing, and actor-behavior assumptions.
- `scenario_engine`: scenario framing and strategic state projection over curated inputs.
- `payoff_engine`: payoff and utility framing primitives and score component assembly.
- `strategy_engine`: strategic move and countermove estimation coordination.
- `belief_engine`: uncertainty and belief-state framing for partially observed strategic state.
- `recommender`: recommendation candidate generation from bounded strategic outputs.
- `scoring_audit`: explainability payload shape, scoring traceability, and audit-oriented output structure.

## Adapter Modules (Reserved Seams)

- `adapters.openspiel`: seam for strategic search/game foundations.
- `adapters.posggym`: seam for partially observable multi-agent environment modeling.
- `adapters.attack_graphs`: seam for adversary path and attack-route modeling.

Adapters are boundary packages and do not own core doctrine or internal decision semantics.

## Ownership Exclusions

`cs-stratcore` does not own:

- raw data collection pipelines,
- mission-level governance policy,
- global graph persistence/truth authority,
- external system deployment control planes.
