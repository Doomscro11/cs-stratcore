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

Repository status through Pass 5:

1. doctrine and scaffold are established,
2. executable API foundation and bounded service flow are present,
3. canonical schemas are in place as internal source of truth,
4. adapter seams exist for OpenSpiel, POSGGym, and attack-graphs,
5. external runtime adapter integrations remain deferred.

## Ecosystem Position

- Upstream dependencies (conceptual): `cs-darkweb`, `CounterSecAI`, `engraphify`, `cs-mirocore`, `ASH`, `SAVANT`.
- Planned adapter seams: OpenSpiel, POSGGym, attack-graphs.
- Integration posture: internal modules remain sovereign; adapters remain replaceable seams at boundaries.
