# Pass 5 Adapter Seams

Pass 5 introduces explicit external adapter seams only. No runtime integration
with OpenSpiel, POSGGym, or attack-graphs is included in this pass.

## Purpose

- Define stable seam contracts for future capability capture.
- Keep canonical model ownership inside `cs_stratcore` modules.
- Preserve existing deterministic Pass 4 API and service behavior.

## Non-Goals

- No external package imports.
- No solver or simulation execution.
- No attack-graph execution.
- No changes to API routes or schema semantics.

## Seam Packages

- `cs_stratcore.adapters.openspiel`: strategic search/game foundations seam.
- `cs_stratcore.adapters.posggym`: partially observable environment seam.
- `cs_stratcore.adapters.attack_graphs`: adversary path modeling seam.

Each seam exposes:

- a capability descriptor dataclass,
- a narrow protocol contract over canonical model types,
- a deferred stub class raising `NotImplementedError` at execution points.
