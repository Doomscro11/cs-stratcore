# Architecture Overview

## Purpose

`cs-stratcore` is the bounded strategic interaction subsystem for CounterSec / SAVANT. It exists to transform curated governed state into structured strategic assessments and recommendation candidates with clear auditability and explainability posture.

## Scope of This Repository

This repository owns strategic interaction orchestration and internal reasoning module boundaries. It is intentionally isolated from direct collection, mission governance, and graph truth-authority responsibilities.

## Non-Goals

This repository does not:

- act as global truth authority,
- ingest uncontrolled raw text as primary reasoning substrate,
- replace upstream state-governance systems,
- provide deployment platform concerns,
- implement external adapter internals in this pass.

## Lifecycle Posture

This pass freezes architecture and package shape only. Future passes add:

1. executable foundations and service flow,
2. canonical schemas,
3. adapter implementation and integration behavior,
4. determinism and hardening controls for production promotion.

## Ecosystem Position

- Upstream dependencies (conceptual): `cs-darkweb`, `CounterSecAI`, `engraphify`, `cs-mirocore`, `ASH`, `SAVANT`.
- Planned adapter seams: OpenSpiel, POSGGym, attack-graphs.
- Integration posture: internal modules remain sovereign; adapters remain replaceable seams at boundaries.
