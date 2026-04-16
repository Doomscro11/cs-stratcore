"""Shared low-level schema types for canonical models."""

from enum import StrEnum


class SourceKind(StrEnum):
    """Origin category for reported observations."""

    UPSTREAM_SYSTEM = "upstream_system"
    ANALYST_REPORT = "analyst_report"
    SENSOR_FEED = "sensor_feed"


class DerivationKind(StrEnum):
    """How a claim was derived from available state."""

    DIRECT_OBSERVATION = "direct_observation"
    ANALYTIC_INFERENCE = "analytic_inference"
    FUSED_ASSESSMENT = "fused_assessment"
