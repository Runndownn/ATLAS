"""Review phase — evidence recording and artifact promotion.

Maps to Yggdrasil Phase F: Review/Promotion.
Records analysis results as evidence and promotes artifacts
to downstream knowledge systems.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path

from atlas.core.job_store import JobRecord, PhaseRecord
from atlas.core.orchestrator import PipelineConfig
from atlas.phases.base import Phase

logger = logging.getLogger("atlas.phases.review")


@dataclass
class EvidenceRecord:
    """A piece of evidence recorded during review."""

    evidence_id: str
    job_id: str
    observation: str
    evidence_type: str  # "observed_fact" | "parsed_fact" | "inferred_relationship" | "classification_hypothesis"
    confidence: float = 1.0
    source: str = ""
    related_evidence: list[str] = field(default_factory=list)
    promoted: bool = False
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))


@dataclass
class PromotionRecord:
    """Record of an artifact promoted from pipeline to knowledge."""

    promotion_id: str
    job_id: str
    content_hash: str
    source_path: str
    artifact_type: str
    risk_level: str = "general"
    evidence: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))


class ReviewPhase(Phase):
    """Phase F — Review & Promotion.

    Records evidence from prior phases, generates a summary report,
    and identifies artifacts suitable for promotion to knowledge stores.
    """

    name = "review_promotion"
    retryable = False  # Non-retryable: evidence recording should be idempotent

    def __init__(self):
        super().__init__()

    async def execute(
        self,
        job: JobRecord,
        config: PipelineConfig,
        phase_record: PhaseRecord,
    ) -> None:
        """Execute review phase."""
        discovery = job.metadata.get("discovery", {})
        fingerprinting = job.metadata.get("fingerprinting", {})
        analysis = job.metadata.get("analysis", {})
        extraction = job.metadata.get("extraction", {})

        # Generate evidence summary
        evidence = self._compile_evidence(job, discovery, fingerprinting, analysis, extraction)

        # Generate promotion candidates
        promotions = self._compile_promotion_candidates(job, discovery, fingerprinting, analysis)

        await self.emit_event(job, "review_complete", {
            "evidence_count": len(evidence),
            "promotion_candidates": len(promotions),
            "summary": {
                "files_discovered": discovery.get("total_files", 0),
                "bytes_discovered": discovery.get("total_bytes", 0),
                "archives_found": discovery.get("archive_count", 0),
                "duplicates": fingerprinting.get("duplicates", 0),
                "unique_hashes": len(fingerprinting.get("content_ids", [])),
                "risky_files": len(discovery.get("risky_files", [])),
                "extraction_errors": len(extraction.get("errors", [])),
                "analysis_findings": analysis.get("total_files", 0),
            },
        })

        job.metadata["review"] = {
            "evidence_count": len(evidence),
            "promotion_candidates": len(promotions),
            "timestamp": datetime.now(UTC).isoformat(),
            "evidence_sample": evidence[:10],
            "promotion_sample": [p.__dict__ for p in promotions[:5]],
        }

        await self.emit_event(job, "pipeline_ready_for_promotion", {
            "job_id": job.job_id,
            "promotion_count": len(promotions),
        })

        self.update_progress(
            percent=100.0,
            message=f"Reviewed {len(evidence)} evidence items, {len(promotions)} promotion candidates",
        )

    def _compile_evidence(
        self,
        job: JobRecord,
        discovery: dict,
        fingerprinting: dict,
        analysis: dict,
        extraction: dict,
    ) -> list[EvidenceRecord]:
        """Compile evidence records from phase metadata."""
        evidence: list[EvidenceRecord] = []

        # Evidence: files discovered
        if discovery.get("total_files", 0) > 0:
            evidence.append(EvidenceRecord(
                evidence_id=f"disc-{job.job_id}-001",
                job_id=job.job_id,
                observation=f"Discovered {discovery['total_files']} files ({discovery['total_bytes']} bytes)",
                evidence_type="observed_fact",
                confidence=1.0,
                source="reconnaissance",
            ))

        # Evidence: archives found
        if discovery.get("archive_count", 0) > 0:
            evidence.append(EvidenceRecord(
                evidence_id=f"arch-{job.job_id}-001",
                job_id=job.job_id,
                observation=f"Found {discovery['archive_count']} archive(s)",
                evidence_type="observed_fact",
                confidence=1.0,
                source="reconnaissance",
            ))

        # Evidence: duplicates detected
        if fingerprinting.get("duplicates", 0) > 0:
            evidence.append(EvidenceRecord(
                evidence_id=f"dup-{job.job_id}-001",
                job_id=job.job_id,
                observation=f"Detected {fingerprinting['duplicates']} duplicate file(s)",
                evidence_type="inferred_relationship",
                confidence=0.95,
                source="fingerprinting",
            ))

        # Evidence: risky files
        risky = discovery.get("risky_files", [])
        if risky:
            evidence.append(EvidenceRecord(
                evidence_id=f"risk-{job.job_id}-001",
                job_id=job.job_id,
                observation=f"Found {len(risky)} file(s) with risk flags",
                evidence_type="classification_hypothesis",
                confidence=0.8,
                source="reconnaissance",
            ))

        # Evidence: extraction errors
        errors = extraction.get("errors", [])
        if errors:
            evidence.append(EvidenceRecord(
                evidence_id=f"err-{job.job_id}-001",
                job_id=job.job_id,
                observation=f"Encountered {len(errors)} extraction error(s)",
                evidence_type="observed_fact",
                confidence=1.0,
                source="extraction",
                related_evidence=[f"arch-{job.job_id}-001"],
            ))

        return evidence

    def _compile_promotion_candidates(
        self,
        job: JobRecord,
        discovery: dict,
        fingerprinting: dict,
        analysis: dict,
    ) -> list[PromotionRecord]:
        """Identify artifacts suitable for promotion."""
        import uuid

        candidates = []
        content_ids = fingerprinting.get("content_ids", [])
        risky_files = discovery.get("risky_files", [])

        for i, content_id in enumerate(content_ids):
            candidate = PromotionRecord(
                promotion_id=str(uuid.uuid4()),
                job_id=job.job_id,
                content_hash=content_id,
                source_path="",
                artifact_type="file",
                risk_level="reviewed",
                evidence=[f"disc-{job.job_id}-001"],
            )
            candidates.append(candidate)

        return candidates


def create_handler() -> ReviewPhase:
    """Create a review phase handler."""
    return ReviewPhase()
