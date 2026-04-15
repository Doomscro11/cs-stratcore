# Architecture Rules

These rules are mandatory for subsequent implementation passes.

## 1) Packaging and Namespace

- Keep a single top-level Python project.
- Keep unified namespace rooted at `cs_stratcore`.
- Keep one top-level `pyproject.toml`; do not introduce multi-package managers.
- Avoid import path hacks and runtime `sys.path` mutation.

## 2) Boundary Discipline

- Core modules must not depend on concrete external adapter internals.
- Adapters must depend inward on stable seams, never reverse.
- Keep transport-facing API concerns separate from strategic core logic.
- Keep shared code in `common` minimal and purpose-driven.

## 3) Doctrine and Auditability

- Treat all consequential outputs as structured and explainable artifacts.
- Preserve deterministic execution posture where feasible; deterministic mode is a later mandatory capability.
- Keep assumptions explicit and bounded; avoid implicit global state.

## 4) Implementation Sequence

Follow this progression:

1. executable foundation and orchestration skeleton,
2. canonical schema definitions,
3. internal strategic logic,
4. adapter integrations,
5. hardening and promotion controls.

## 5) Non-Goals for Early Passes

Until explicitly introduced, do not add:

- route handlers or API feature surfaces,
- substantive strategy/scenario/payoff solver logic,
- external integration logic,
- database/deployment/auth infrastructure.
