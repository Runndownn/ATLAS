"""Analysis phase — deep understanding and pattern detection.

Maps to Yggdrasil Phase E: Deep Understanding.
Extensible analysis phase — provides built-in pattern detection and
a plugin interface for custom analyzers.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Protocol

from atlas.core.job_store import JobRecord, PhaseRecord
from atlas.core.orchestrator import PipelineConfig
from atlas.phases.base import Phase
from atlas.storage.hash_store import HashStore

logger = logging.getLogger("atlas.phases.analysis")


class AnalyzerPlugin(Protocol):
    """Protocol for analysis plugin modules."""

    name: str

    async def analyze(
        self,
        file_path: str,
        job: JobRecord,
    ) -> dict:
        """Analyze a file and return findings."""
        ...


class AnalysisPhase(Phase):
    """Phase E — Deep Understanding.

    Runs analysis plugins against discovered artifacts. Built-in
    plugins include file type detection, hash lookup, and pattern matching.
    """

    name = "deep_understanding"
    retryable = True

    def __init__(
        self,
        hash_store: HashStore | None = None,
        plugins: list[AnalyzerPlugin] | None = None,
    ):
        super().__init__()
        self._hash_store = hash_store or HashStore()
        self._plugins = plugins or []

    async def execute(
        self,
        job: JobRecord,
        config: PipelineConfig,
        phase_record: PhaseRecord,
    ) -> None:
        """Execute analysis phase."""
        # Get discovery + fingerprinting results from job metadata
        discovery = job.metadata.get("discovery", {})
        risky_files = discovery.get("risky_files", [])

        if not risky_files:
            await self.emit_event(job, "no_files_to_analyze")
            self.update_progress(percent=100.0, message="No files to analyze")
            return

        total = len(risky_files)
        processed = 0
        findings: list[dict] = []

        await self.emit_event(job, "analysis_started", {"total_files": total})

        for file_path in risky_files:
            path = Path(file_path)

            # Built-in analysis
            file_findings = {
                "path": file_path,
                "name": path.name,
                "extension": path.suffix.lower(),
                "size": path.stat().st_size if path.exists() else 0,
                "analyzers": [],
            }

            # Run each plugin
            for plugin in self._plugins:
                try:
                    result = await plugin.analyze(file_path, job)
                    file_findings["analyzers"].append({
                        "plugin": plugin.name,
                        "result": result,
                    })
                except Exception as exc:
                    logger.warning("Plugin %s failed on %s: %s", plugin.name, file_path, exc)

            findings.append(file_findings)
            processed += 1

            if processed % 100 == 0:
                self.update_progress(
                    percent=(processed / total) * 100 if total > 0 else 100,
                    processed=processed,
                    total=total,
                )

        await self.emit_event(job, "analysis_complete", {
            "total_files": total,
            "findings_count": len(findings),
        })

        job.metadata["analysis"] = {
            "total_files": total,
            "findings": findings[:50],  # Truncate for metadata
        }

        self.update_progress(
            percent=100.0,
            processed=processed,
            total=total,
            message=f"Analyzed {processed} files",
        )


def create_handler(
    hash_store: HashStore | None = None,
    plugins: list[AnalyzerPlugin] | None = None,
) -> AnalysisPhase:
    """Create a phase handler factory."""
    return AnalysisPhase(hash_store=hash_store, plugins=plugins)
