#!/usr/bin/env python3
"""Deterministic generator/validator library for the BinReaper ATLAS TODO family."""

from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any

GENERATOR_VERSION = "2.0.0"
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TASK_ID_RE = re.compile(r"^T[1-9][0-9]*(?:\.[1-9][0-9]*){2,}$")
DOMAIN_RE = re.compile(r"^\{[A-Z0-9_]+\}$")
TAG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
VALID_PRIORITIES = {"P0", "P1", "P2", "P3"}
VALID_MODES = {"ACTIVE-WORKSPACE", "CONNECTED-REPOSITORY", "ATTACHED-SNAPSHOT", "SOURCE-ONLY"}
VALID_DISPOSITIONS = {"reuse", "extend", "refactor", "create", "migrate", "retire"}
V21_SECTIONS = [
    ("purpose", "Purpose / Why this exists"),
    ("where", "Where this applies"),
    ("repository_evidence", "Repository and authority evidence"),
    ("current_state", "Current-state assessment and gap analysis"),
    ("design", "Design and integration strategy"),
    ("implementation", "Implementation requirements"),
    ("security", "Security and safety requirements"),
    ("edge_cases", "Edge cases and outliers to handle"),
    ("acceptance", "Acceptance criteria (“done” definition)"),
    ("testing", "Testing plan"),
    ("validation", "Validation and completion evidence"),
    ("debugging", "Debugging checklist"),
]
SECTION_MINIMUMS = {
    "purpose": 3, "where": 3, "repository_evidence": 3, "current_state": 3,
    "design": 3, "implementation": 4, "security": 4, "edge_cases": 4,
    "acceptance": 4, "testing": 6, "validation": 3, "debugging": 4,
}
TODO_RE = re.compile(r"(?m)^\* \[([ xX])\] TODO ([1-9][0-9]*): (.+)$")
V12_RE = re.compile(r"(?m)^\* \[([ xX])\] - (T[1-9][0-9]*(?:\.[1-9][0-9]*){2,}) (.+)$")


class RegistryError(ValueError):
    pass


class OutputConflict(RuntimeError):
    pass


def canonical_json_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_registry(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise RegistryError("registry root must be an object")
    return data


def require_text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise RegistryError(f"{label} must be a non-empty string")
    return value


def require_list(value: Any, label: str, minimum: int = 0) -> list[Any]:
    if not isinstance(value, list) or len(value) < minimum:
        raise RegistryError(f"{label} must contain at least {minimum} item(s)")
    return value


def validate_registry(registry: dict[str, Any]) -> None:
    required = {
        "schema_version", "generator_version", "slug", "title", "evidence_mode",
        "target_repository", "target_plan_path", "planning_root", "part1_header_source",
        "source_repositories", "authorities", "domains", "epics", "assumptions",
        "conflicts", "master_plan", "tasks",
    }
    missing = sorted(required - set(registry))
    extra = sorted(set(registry) - required)
    if missing or extra:
        raise RegistryError(f"top-level fields mismatch; missing={missing}, extra={extra}")
    if registry["schema_version"] != "2.0.0":
        raise RegistryError("schema_version must be 2.0.0")
    slug = require_text(registry["slug"], "slug")
    if not SLUG_RE.fullmatch(slug):
        raise RegistryError("slug must be lowercase hyphen-case")
    if registry["evidence_mode"] not in VALID_MODES:
        raise RegistryError("invalid evidence mode")
    for key in ("title", "target_repository", "target_plan_path", "planning_root", "part1_header_source"):
        require_text(registry[key], key)

    repos = require_list(registry["source_repositories"], "source_repositories", 1)
    for index, repo in enumerate(repos):
        if not isinstance(repo, dict):
            raise RegistryError(f"source_repositories[{index}] must be an object")
        for key in ("repository", "commit", "role", "access_mode"):
            require_text(repo.get(key), f"source_repositories[{index}].{key}")
        if not re.fullmatch(r"[0-9a-f]{40}", repo["commit"]):
            raise RegistryError(f"source_repositories[{index}].commit must be a 40-character SHA")
        if repo["access_mode"] not in {"local", "connector", "snapshot", "source-only"}:
            raise RegistryError(f"invalid source repository access mode: {repo['access_mode']}")

    authorities = require_list(registry["authorities"], "authorities")
    auth_ids: set[str] = set()
    for index, authority in enumerate(authorities):
        if not isinstance(authority, dict):
            raise RegistryError(f"authorities[{index}] must be an object")
        aid = require_text(authority.get("id"), f"authorities[{index}].id")
        if aid in auth_ids:
            raise RegistryError(f"duplicate authority ID {aid}")
        auth_ids.add(aid)
        for key in ("class", "repository", "commit", "path", "decision", "status", "limitations"):
            if key in {"repository", "commit", "limitations"}:
                if not isinstance(authority.get(key), str):
                    raise RegistryError(f"{aid}.{key} must be a string")
            else:
                require_text(authority.get(key), f"{aid}.{key}")
        if authority["status"] not in {"found", "unresolved", "conflicting"}:
            raise RegistryError(f"{aid} has invalid status")

    domains = require_list(registry["domains"], "domains", 1)
    domain_tokens: list[str] = []
    for index, domain in enumerate(domains):
        token = require_text(domain.get("token"), f"domains[{index}].token")
        if not DOMAIN_RE.fullmatch(token):
            raise RegistryError(f"invalid domain token {token}")
        domain_tokens.append(token)
        require_text(domain.get("name"), f"domains[{index}].name")
        require_text(domain.get("description"), f"domains[{index}].description")
    if len(domain_tokens) != len(set(domain_tokens)):
        raise RegistryError("domain tokens must be unique")
    domain_set = set(domain_tokens)

    epics = require_list(registry["epics"], "epics", 1)
    epic_ids: set[str] = set()
    epic_order: list[str] = []
    for index, epic in enumerate(epics):
        eid = require_text(epic.get("epic_id"), f"epics[{index}].epic_id")
        if eid in epic_ids:
            raise RegistryError(f"duplicate epic ID {eid}")
        epic_ids.add(eid)
        require_text(epic.get("name"), f"{eid}.name")
        require_text(epic.get("objective"), f"{eid}.objective")
        epic_order.extend(require_list(epic.get("task_ids"), f"{eid}.task_ids", 1))

    tasks = require_list(registry["tasks"], "tasks", 3)
    if len(tasks) % 3:
        raise RegistryError(f"task count must be divisible by three; got {len(tasks)}")
    sequences = [task.get("sequence") for task in tasks]
    if sequences != list(range(1, len(tasks) + 1)):
        raise RegistryError("task sequences must be contiguous from one")
    task_ids = [require_text(task.get("task_id"), f"tasks[{i}].task_id") for i, task in enumerate(tasks)]
    if any(not TASK_ID_RE.fullmatch(task_id) for task_id in task_ids):
        raise RegistryError("one or more task IDs are invalid")
    if len(task_ids) != len(set(task_ids)):
        raise RegistryError("task IDs must be unique")
    titles = [require_text(task.get("title"), task_ids[i] + ".title") for i, task in enumerate(tasks)]
    if len(titles) != len(set(titles)):
        raise RegistryError("task titles must be unique")
    if epic_order != task_ids:
        raise RegistryError("epic task order must equal canonical task order")

    positions = {task_id: index for index, task_id in enumerate(task_ids)}
    task_by_id = {task["task_id"]: task for task in tasks}
    for task in tasks:
        task_id = task["task_id"]
        if task.get("epic_id") not in epic_ids:
            raise RegistryError(f"{task_id} references unknown epic")
        if task.get("priority") not in VALID_PRIORITIES:
            raise RegistryError(f"{task_id} has invalid priority")
        hours = task.get("estimated_hours")
        if not isinstance(hours, int) or not 1 <= hours <= 16:
            raise RegistryError(f"{task_id}.estimated_hours must be 1-16")
        require_text(task.get("owner"), f"{task_id}.owner")
        if not isinstance(task.get("raci"), dict) or set(task["raci"]) != {"R", "A", "C", "I"}:
            raise RegistryError(f"{task_id}.raci must contain exactly R, A, C, I")
        task_domains = require_list(task.get("domains"), f"{task_id}.domains", 1)
        if set(task_domains) - domain_set:
            raise RegistryError(f"{task_id} uses unknown domain")
        deps = require_list(task.get("dependencies"), f"{task_id}.dependencies")
        for dep in deps:
            if dep not in positions or positions[dep] >= positions[task_id]:
                raise RegistryError(f"{task_id} has unknown or forward dependency {dep}")
        for key in ("source_plan_mapping", "repository_evidence", "tags"):
            require_list(task.get(key), f"{task_id}.{key}", 1)
        acceptance = require_list(task.get("acceptance_criteria"), f"{task_id}.acceptance_criteria", 2)
        if len(acceptance) > 5:
            raise RegistryError(f"{task_id}.acceptance_criteria exceeds five")
        steps = require_list(task.get("steps"), f"{task_id}.steps", 1)
        if len(steps) > 5:
            raise RegistryError(f"{task_id}.steps exceeds five")
        if any(not TAG_RE.fullmatch(tag) for tag in task["tags"]):
            raise RegistryError(f"{task_id} has invalid tag")
        require_text(task.get("risk"), f"{task_id}.risk")
        require_text(task.get("mitigation"), f"{task_id}.mitigation")
        components = require_list(task.get("affected_components"), f"{task_id}.affected_components", 1)
        for component in components:
            require_text(component.get("path_or_symbol"), f"{task_id}.component.path_or_symbol")
            if component.get("disposition") not in VALID_DISPOSITIONS:
                raise RegistryError(f"{task_id} has invalid disposition")
            require_text(component.get("reason"), f"{task_id}.component.reason")
        security = task.get("security_knowledge")
        if not isinstance(security, list):
            raise RegistryError(f"{task_id}.security_knowledge must be an array")
        for mapping in security:
            if mapping.get("classification") not in {
                "EVIDENCED", "INFERRED", "DEFENSIVE-SCENARIO", "RAW-CHALLENGE",
                "EXTERNAL-STANDARD", "UNRESOLVED",
            }:
                raise RegistryError(f"{task_id} has invalid security classification")
            for key in ("source", "claim", "application"):
                require_text(mapping.get(key), f"{task_id}.security.{key}")
            if not isinstance(mapping.get("limitation"), str):
                raise RegistryError(f"{task_id}.security.limitation must be a string")
        completion = task.get("completion")
        if not isinstance(completion, dict) or completion.get("state") not in {"complete", "incomplete"}:
            raise RegistryError(f"{task_id}.completion is invalid")
        evidence = require_list(completion.get("evidence"), f"{task_id}.completion.evidence")
        if completion["state"] == "complete" and not evidence:
            raise RegistryError(f"{task_id} is complete without evidence")
        v21 = task.get("v21")
        if not isinstance(v21, dict) or set(v21) != {key for key, _ in V21_SECTIONS}:
            raise RegistryError(f"{task_id}.v21 keys do not match contract")
        for key, minimum in SECTION_MINIMUMS.items():
            entries = require_list(v21.get(key), f"{task_id}.v21.{key}", minimum)
            for entry in entries:
                require_text(entry, f"{task_id}.v21.{key} item")
        validation_text = "\n".join(v21["validation"])
        for marker in ("Commands to run:", "Expected evidence:", "Completion record:"):
            if marker not in validation_text:
                raise RegistryError(f"{task_id}.validation missing {marker}")

    assumption_ids: set[str] = set()
    targets: list[str] = []
    for assumption in require_list(registry["assumptions"], "assumptions"):
        aid = require_text(assumption.get("id"), "assumption.id")
        if aid in assumption_ids:
            raise RegistryError(f"duplicate assumption {aid}")
        assumption_ids.add(aid)
        require_text(assumption.get("statement"), f"{aid}.statement")
        require_list(assumption.get("evidence_searched"), f"{aid}.evidence_searched", 1)
        require_text(assumption.get("resolving_artifact"), f"{aid}.resolving_artifact")
        target = require_text(assumption.get("validation_task_id"), f"{aid}.validation_task_id")
        if target not in task_by_id:
            raise RegistryError(f"{aid} references unknown validation task")
        if aid not in task_by_id[target].get("assumption_refs", []):
            raise RegistryError(f"{target} must reference {aid}")
        targets.append(target)
    duplicate_targets = [target for target, count in Counter(targets).items() if count > 1]
    if duplicate_targets:
        raise RegistryError(f"each assumption requires a unique validation task: {duplicate_targets}")
    for task in tasks:
        for aid in require_list(task.get("assumption_refs"), f"{task['task_id']}.assumption_refs"):
            if aid not in assumption_ids:
                raise RegistryError(f"{task['task_id']} references unknown assumption {aid}")

    for conflict in require_list(registry["conflicts"], "conflicts"):
        cid = require_text(conflict.get("id"), "conflict.id")
        require_list(conflict.get("sources"), f"{cid}.sources", 2)
        require_text(conflict.get("statement"), f"{cid}.statement")
        require_text(conflict.get("safest_interpretation"), f"{cid}.safest_interpretation")
        if conflict.get("resolution_task_id") not in task_by_id:
            raise RegistryError(f"{cid} has unknown resolution task")

    master = registry.get("master_plan")
    if not isinstance(master, dict):
        raise RegistryError("master_plan must be an object")
    require_text(master.get("objective"), "master_plan.objective")
    for key in ("scope", "architecture", "trust_boundaries", "delivery_sequence"):
        require_list(master.get(key), f"master_plan.{key}", 1)
    for key in ("constraints", "unresolved_decisions"):
        require_list(master.get(key), f"master_plan.{key}")

    visiting: set[str] = set()
    visited: set[str] = set()
    def visit(task_id: str) -> None:
        if task_id in visiting:
            raise RegistryError(f"dependency cycle at {task_id}")
        if task_id in visited:
            return
        visiting.add(task_id)
        for dep in task_by_id[task_id]["dependencies"]:
            visit(dep)
        visiting.remove(task_id)
        visited.add(task_id)
    for task_id in task_ids:
        visit(task_id)


def bullets(items: list[str], indent: str = "") -> str:
    return "\n".join(f"{indent}* {item}" for item in items)


def checkbox(task: dict[str, Any]) -> str:
    return "x" if task["completion"]["state"] == "complete" else " "


def render_master_plan(registry: dict[str, Any]) -> str:
    master = registry["master_plan"]
    atlas = next((repo["commit"] for repo in registry["source_repositories"] if repo["repository"].endswith("/ATLAS")), "UNRESOLVED")
    ygg = next((repo["commit"] for repo in registry["source_repositories"] if repo["repository"].endswith("/Yggdrasil")), "UNRESOLVED")
    lines = [
        f"# Plan-MASTER — {registry['title']}", "",
        "## Plan metadata", "",
        f"* Evidence mode: `{registry['evidence_mode']}`",
        f"* Target repository: `{registry['target_repository']}`",
        f"* Target plan: `{registry['target_plan_path']}`",
        f"* Frozen ATLAS ref: `{atlas}`",
        f"* Frozen Yggdrasil ref: `{ygg}`",
        f"* Canonical task authority: `TODO_{registry['slug']}-registry.json`",
        "* Status: `PROPOSED / NOT IMPLEMENTED`", "",
        "## Objective", "", master["objective"], "",
        "## Scope", "", bullets(master["scope"]), "",
        "## Architecture and system boundaries", "", bullets(master["architecture"]), "",
        "## Trust boundaries", "", bullets(master["trust_boundaries"]), "",
        "## Constraints", "", bullets(master["constraints"] or ["None recorded."]), "",
        "## Evidence and authority map", "",
    ]
    for authority in registry["authorities"]:
        lines.append(
            f"* `{authority['id']}` — `{authority['status']}` — "
            f"`{authority['repository']}@{authority['commit'] or 'UNRESOLVED'}:{authority['path']}` — "
            f"{authority['decision']} Limitation: {authority['limitations']}"
        )
    lines.extend(["", "## Assumptions", ""])
    if registry["assumptions"]:
        for assumption in registry["assumptions"]:
            lines.append(f"* `{assumption['id']}` → `{assumption['validation_task_id']}` — {assumption['statement']}")
    else:
        lines.append("* None recorded.")
    lines.extend(["", "## Conflicts and safest interpretations", ""])
    if registry["conflicts"]:
        for conflict in registry["conflicts"]:
            lines.append(
                f"* `{conflict['id']}` → `{conflict['resolution_task_id']}` — {conflict['statement']} "
                f"Safest interpretation: {conflict['safest_interpretation']}"
            )
    else:
        lines.append("* None recorded.")
    lines.extend(["", "## Intended delivery sequence", ""])
    for index, item in enumerate(master["delivery_sequence"], start=1):
        lines.append(f"{index}. {item}")
    lines.extend(["", "## Unresolved decisions", "", bullets(master["unresolved_decisions"] or ["None recorded."]), ""])
    task_map = {task["task_id"]: task for task in registry["tasks"]}
    for epic in registry["epics"]:
        lines.extend([f"## {epic['epic_id']}. {epic['name']}", "", epic["objective"], ""])
        for task_id in epic["task_ids"]:
            task = task_map[task_id]
            dependencies = ", ".join(task["dependencies"]) if task["dependencies"] else "None"
            lines.append(
                f"* [{checkbox(task)}] `{task_id}` — {task['title']} "
                f"(`{task['priority']}`, {task['estimated_hours']}h; dependencies: {dependencies})"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def epic_summary(registry: dict[str, Any]) -> str:
    task_map = {task["task_id"]: task for task in registry["tasks"]}
    rows = [
        "| Epic name | P0 | P1 | P2 | P3 | Total estimated hours | Three highest-risk tasks |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for epic in registry["epics"]:
        tasks = [task_map[task_id] for task_id in epic["task_ids"]]
        counts = Counter(task["priority"] for task in tasks)
        risks = "; ".join(f"{task['task_id']}: {task['risk']}" for task in tasks[:3]).replace("|", "\\|")
        rows.append(
            f"| {epic['epic_id']} — {epic['name']} | {counts['P0']} | {counts['P1']} | "
            f"{counts['P2']} | {counts['P3']} | {sum(task['estimated_hours'] for task in tasks)} | {risks} |"
        )
    return "\n".join(rows)


def v12_json_record(task: dict[str, Any]) -> dict[str, Any]:
    return {
        "task_id": task["task_id"],
        "title": task["title"],
        "priority": task["priority"],
        "estimated_hours": f"{task['estimated_hours']}h",
        "owner": task["owner"],
        "dependencies": task["dependencies"],
        "evidence": task["repository_evidence"],
        "acceptance_criteria": task["acceptance_criteria"],
        "tags": task["tags"],
    }


def render_v12_task(task: dict[str, Any]) -> str:
    dependencies = ", ".join(task["dependencies"]) if task["dependencies"] else "None"
    raci = task["raci"]
    source = "; ".join(task["source_plan_mapping"])
    evidence = "; ".join(task["repository_evidence"])
    acceptance = "; ".join(f"{index}) {item}" for index, item in enumerate(task["acceptance_criteria"], start=1))
    return (
        f"* [{checkbox(task)}] - {task['task_id']} {task['title']}\n"
        f"  * Priority: `{task['priority']}`\n"
        f"  * Est. Effort: `{task['estimated_hours']}h`\n"
        f"  * Owner: `{task['owner']}` | R: {raci['R']} | A: {raci['A']} | C: {raci['C']} | I: {raci['I']}\n"
        f"  * Domains: {' '.join(task['domains'])}\n"
        f"  * Dependencies: {dependencies}\n"
        f"  * Evidence: {evidence}; source mapping: {source}\n"
        f"  * Acceptance Criteria: {acceptance}\n"
        f"  * Steps / Subtasks:\n{bullets(task['steps'], '    ')}\n"
        f"  * Risks & Mitigations: {task['risk']} / {task['mitigation']}.\n"
        f"  * Tags: {' '.join(f'[{tag}]' for tag in task['tags'])}"
    )


def render_v12(registry: dict[str, Any]) -> str:
    lines = [
        f"# Flagship Production Engineering TODO Plan — {registry['title']}", "",
        f"Evidence and assumption note: evidence mode is `{registry['evidence_mode']}`. "
        "The latest ZIP is authoritative for architecture and macro tasks. Repository behavior is limited to frozen cited evidence; "
        "unsupported conclusions use stable assumption IDs and exactly one validation task.", "",
        epic_summary(registry), "", "## Domain Registry", "",
    ]
    for domain in registry["domains"]:
        lines.append(f"* `{domain['token']}` — {domain['name']}: {domain['description']}")
    lines.append("")
    task_map = {task["task_id"]: task for task in registry["tasks"]}
    for epic in registry["epics"]:
        lines.extend([f"## {epic['epic_id']}. {epic['name']}", "", epic["objective"], ""])
        for task_id in epic["task_ids"]:
            lines.extend([render_v12_task(task_map[task_id]), ""])
    lines.extend([
        "Implementation notes: execute evidence and authority resolution before path-dependent changes; preserve the six phase barriers, "
        "one authoritative state owner, exact-byte lineage, fail-closed safety, replay/idempotency semantics, observability, migration, "
        "rollout, rollback, documentation, and completion evidence. P2/P3 adapters must not bypass unresolved P0/P1 foundations.",
        "", "## Machine-Readable Task Index", "", "```json",
        json.dumps([v12_json_record(task) for task in registry["tasks"]], indent=2, ensure_ascii=False),
        "```", "",
    ])
    return "\n".join(lines)


def required_authority_text(registry: dict[str, Any]) -> str:
    found = [authority["path"] for authority in registry["authorities"] if authority["status"] == "found"]
    unresolved = [authority["path"] for authority in registry["authorities"] if authority["status"] != "found"]
    text = "; ".join(found) if found else "UNRESOLVED"
    if unresolved:
        text += "; unresolved: " + "; ".join(unresolved)
    return text


def render_v21_block(task: dict[str, Any], registry: dict[str, Any]) -> str:
    dependencies = ", ".join(task["dependencies"]) if task["dependencies"] else "None"
    scope = "; ".join(f"{component['path_or_symbol']} ({component['disposition']})" for component in task["affected_components"])
    lines = [
        f"* [{checkbox(task)}] TODO {task['sequence']}: {task['title']}", "",
        f"  1.2 source task(s): `{task['task_id']}`",
        f"  Priority: `{task['priority']}`",
        f"  Estimated effort: `{task['estimated_hours']} hours`",
        f"  Dependencies: `{dependencies}`",
        f"  Evidence basis: `{registry['evidence_mode']}`",
        f"  Repository scope: `{scope}`",
        f"  Required authorities: `{required_authority_text(registry)}`",
    ]
    if task["completion"]["state"] == "complete":
        lines.extend(["", "  Completion evidence:", bullets(task["completion"]["evidence"], "  ")])
    for key, heading in V21_SECTIONS:
        lines.extend(["", f"  {heading}", "", bullets(task["v21"][key], "  ")])
    return "\n".join(lines).rstrip()


def render_v21(registry: dict[str, Any]) -> tuple[str, list[str]]:
    blocks = [render_v21_block(task, registry) for task in registry["tasks"]]
    return "## TODO\n\n" + "\n\n".join(blocks) + "\n", blocks


def render_parts(slug: str, header: str, blocks: list[str]) -> dict[str, str]:
    prefix = header.rstrip("\n") + "\n\n## TODO\n\n"
    result: dict[str, str] = {}
    for offset in range(0, len(blocks), 3):
        number = offset // 3 + 1
        result[f"TODO_{slug}-PART1/TODO_{slug}-PART1-{number}.md"] = (
            prefix + "\n\n".join(blocks[offset:offset + 3]) + "\n"
        )
    return result


def build_outputs(
    registry: dict[str, Any],
    header_bytes: bytes,
    validation_status: str = "not-run",
) -> tuple[dict[str, bytes], dict[str, Any], list[str]]:
    validate_registry(registry)
    registry_bytes = canonical_json_bytes(registry)
    header = header_bytes.decode("utf-8")
    if not header_bytes.strip():
        raise RegistryError("PART1 header must not be empty")
    slug = registry["slug"]
    v21_text, blocks = render_v21(registry)
    outputs: dict[str, bytes] = {
        f"Plan-MASTER_{slug}.md": render_master_plan(registry).encode("utf-8"),
        f"TODO_{slug}-registry.json": registry_bytes,
        f"TODO-MASTER_{slug}-v2.1/TODO-MASTER_{slug}-v2.1.md": v21_text.encode("utf-8"),
        f"TODO_{slug}-v1.2/TODO_{slug}-v1.2.md": render_v12(registry).encode("utf-8"),
    }
    outputs.update({path: text.encode("utf-8") for path, text in render_parts(slug, header, blocks).items()})
    complete = sum(task["completion"]["state"] == "complete" for task in registry["tasks"])
    output_hashes = {path: sha256_bytes(data) for path, data in sorted(outputs.items())}
    manifest = {
        "schema_version": "1.0.0",
        "generator_version": GENERATOR_VERSION,
        "slug": slug,
        "plan_directory": f"Plan_{slug}",
        "evidence_mode": registry["evidence_mode"],
        "source_repositories": registry["source_repositories"],
        "part1_header_sha256": sha256_bytes(header_bytes),
        "registry_sha256": sha256_bytes(registry_bytes),
        "input_fingerprint": sha256_bytes(
            registry_bytes + b"\0" + header_bytes + b"\0" + GENERATOR_VERSION.encode("utf-8")
        ),
        "counts": {
            "canonical_tasks": len(registry["tasks"]),
            "v12_tasks": len(registry["tasks"]),
            "v21_tasks": len(registry["tasks"]),
            "part1_documents": len(registry["tasks"]) // 3,
            "tasks_per_part1": 3,
            "complete": complete,
            "incomplete": len(registry["tasks"]) - complete,
        },
        "outputs": output_hashes,
        "validation": {"status": validation_status, "validator_version": GENERATOR_VERSION},
    }
    outputs[f"TODO_{slug}-manifest.json"] = canonical_json_bytes(manifest)
    return outputs, manifest, blocks


def ensure_safe_relative(relative: Path) -> None:
    if relative.is_absolute() or any(part in {"", ".", ".."} for part in relative.parts):
        raise RegistryError(f"unsafe relative path: {relative}")


def ensure_no_symlink_ancestors(root: Path, relative: Path) -> None:
    ensure_safe_relative(relative)
    current = root.resolve()
    for part in relative.parts[:-1]:
        current = current / part
        if current.exists() and current.is_symlink():
            raise RegistryError(f"refusing to traverse symlink component: {current}")


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


def preserve_passed_manifest(plan_dir: Path, slug: str, outputs: dict[str, bytes]) -> None:
    relative = f"TODO_{slug}-manifest.json"
    target = plan_dir / relative
    if not target.is_file() or target.is_symlink():
        return
    try:
        actual = json.loads(target.read_text(encoding="utf-8"))
        expected = json.loads(outputs[relative].decode("utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return
    if (actual.get("validation") or {}).get("status") != "passed":
        return
    actual_compare = dict(actual)
    expected_compare = dict(expected)
    actual_compare.pop("validation", None)
    expected_compare.pop("validation", None)
    if actual_compare == expected_compare:
        outputs[relative] = canonical_json_bytes(actual)


def preflight(plan_dir: Path, outputs: dict[str, bytes], replace_conflicts: bool) -> tuple[list[Path], list[Path], list[Path]]:
    create: list[Path] = []
    unchanged: list[Path] = []
    replace: list[Path] = []
    for relative_text, expected in sorted(outputs.items()):
        relative = Path(relative_text)
        ensure_no_symlink_ancestors(plan_dir, relative)
        target = plan_dir / relative
        if target.exists() and target.is_symlink():
            raise RegistryError(f"refusing to replace symlink: {target}")
        if not target.exists():
            create.append(target)
        elif target.read_bytes() == expected:
            unchanged.append(target)
        elif replace_conflicts:
            replace.append(target)
        else:
            raise OutputConflict(f"conflict at {target}; review before --replace-conflicts")
    return create, unchanged, replace


def stale_part_files(plan_dir: Path, slug: str, outputs: dict[str, bytes]) -> list[Path]:
    part_dir = plan_dir / f"TODO_{slug}-PART1"
    expected = {
        (plan_dir / relative).resolve()
        for relative in outputs
        if relative.startswith(f"TODO_{slug}-PART1/")
    }
    if not part_dir.is_dir():
        return []
    return sorted(
        path for path in part_dir.glob(f"TODO_{slug}-PART1-*.md")
        if path.resolve() not in expected
    )


def extract_blocks(text: str, regex: re.Pattern[str]) -> list[tuple[re.Match[str], str]]:
    matches = list(regex.finditer(text))
    return [
        (match, text[match.start():(matches[index + 1].start() if index + 1 < len(matches) else len(text))].strip())
        for index, match in enumerate(matches)
    ]


def normalize_block(block: str) -> str:
    return "\n".join(line.rstrip() for line in block.strip().splitlines())


def validate_plan_dir(
    registry: dict[str, Any],
    header_bytes: bytes,
    plan_dir: Path,
) -> list[str]:
    errors: list[str] = []
    slug = registry["slug"]
    expected, _manifest_template, master_blocks = build_outputs(registry, header_bytes, "not-run")
    expected_non_manifest = {path: data for path, data in expected.items() if not path.endswith("-manifest.json")}
    for relative, data in expected_non_manifest.items():
        target = plan_dir / relative
        if not target.is_file():
            errors.append(f"missing output: {relative}")
        elif target.is_symlink():
            errors.append(f"output is symlink: {relative}")
        elif target.read_bytes() != data:
            errors.append(f"content differs from canonical projection: {relative}")

    v21_path = plan_dir / f"TODO-MASTER_{slug}-v2.1" / f"TODO-MASTER_{slug}-v2.1.md"
    parsed_master_blocks: list[str] = []
    if v21_path.is_file():
        text = v21_path.read_text(encoding="utf-8")
        if not text.startswith("## TODO\n"):
            errors.append("v2.1 must begin with exactly '## TODO'")
        if len(re.findall(r"(?m)^## TODO\s*$", text)) != 1:
            errors.append("v2.1 must contain exactly one TODO section")
        blocks = extract_blocks(text, TODO_RE)
        parsed_master_blocks = [block for _, block in blocks]
        numbers = [int(match.group(2)) for match, _ in blocks]
        if numbers != list(range(1, len(registry["tasks"]) + 1)):
            errors.append("v2.1 numbering/order mismatch")
        for (match, block), task in zip(blocks, registry["tasks"]):
            if match.group(3).strip() != task["title"]:
                errors.append(f"v2.1 title mismatch for TODO {task['sequence']}")
            positions = [block.find(heading) for _, heading in V21_SECTIONS]
            if any(position < 0 for position in positions) or positions != sorted(positions):
                errors.append(f"v2.1 section order mismatch for TODO {task['sequence']}")

    v12_path = plan_dir / f"TODO_{slug}-v1.2" / f"TODO_{slug}-v1.2.md"
    if v12_path.is_file():
        text = v12_path.read_text(encoding="utf-8")
        ids = [match.group(2) for match, _ in extract_blocks(text, V12_RE)]
        expected_ids = [task["task_id"] for task in registry["tasks"]]
        if ids != expected_ids:
            errors.append("v1.2 Markdown task IDs/order mismatch")
        index_match = re.search(
            r"## Machine-Readable Task Index\s*\n+\s*```json\s*\n(\[.*\])\s*\n```",
            text,
            re.DOTALL,
        )
        if not index_match:
            errors.append("v1.2 final JSON task index is missing")
        else:
            try:
                payload = json.loads(index_match.group(1))
            except json.JSONDecodeError as exc:
                errors.append(f"v1.2 task index invalid: {exc}")
            else:
                if payload != [v12_json_record(task) for task in registry["tasks"]]:
                    errors.append("v1.2 task index differs from registry")
            if text[index_match.end():].strip():
                errors.append("v1.2 contains commentary after final JSON index")

    prefix = header_bytes.rstrip(b"\n") + b"\n\n## TODO\n\n"
    coverage: list[int] = []
    part_dir = plan_dir / f"TODO_{slug}-PART1"
    expected_count = len(registry["tasks"]) // 3
    expected_names = [f"TODO_{slug}-PART1-{index}.md" for index in range(1, expected_count + 1)]
    actual_files = sorted(
        part_dir.glob(f"TODO_{slug}-PART1-*.md") if part_dir.is_dir() else [],
        key=lambda path: int(re.search(r"-(\d+)\.md$", path.name).group(1)) if re.search(r"-(\d+)\.md$", path.name) else 10**9,
    )
    if [path.name for path in actual_files] != expected_names:
        errors.append("PART1 filename set/order mismatch")
    for index, path in enumerate(actual_files, start=1):
        data = path.read_bytes()
        if not data.startswith(prefix):
            errors.append(f"{path.name}: header or TODO marker differs")
        blocks = extract_blocks(data.decode("utf-8"), TODO_RE)
        if len(blocks) != 3:
            errors.append(f"{path.name}: expected three TODOs, found {len(blocks)}")
        numbers = [int(match.group(2)) for match, _ in blocks]
        expected_numbers = list(range((index - 1) * 3 + 1, index * 3 + 1))
        if numbers != expected_numbers:
            errors.append(f"{path.name}: TODO sequence mismatch")
        coverage.extend(numbers)
        if parsed_master_blocks:
            for (_, actual_block), expected_block in zip(blocks, parsed_master_blocks[(index - 1) * 3:index * 3]):
                if normalize_block(actual_block) != normalize_block(expected_block):
                    errors.append(f"{path.name}: TODO body differs from v2.1 master")
    if coverage != list(range(1, len(registry["tasks"]) + 1)):
        errors.append("PART1 coverage differs from canonical TODO sequence")

    manifest_path = plan_dir / f"TODO_{slug}-manifest.json"
    if not manifest_path.is_file():
        errors.append("manifest missing")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"manifest invalid: {exc}")
        else:
            if manifest.get("part1_header_sha256") != sha256_bytes(header_bytes):
                errors.append("manifest header hash mismatch")
            registry_bytes = canonical_json_bytes(registry)
            if manifest.get("registry_sha256") != sha256_bytes(registry_bytes):
                errors.append("manifest registry hash mismatch")
            counts = {
                "canonical_tasks": len(registry["tasks"]),
                "v12_tasks": len(registry["tasks"]),
                "v21_tasks": len(registry["tasks"]),
                "part1_documents": len(registry["tasks"]) // 3,
                "tasks_per_part1": 3,
                "complete": sum(task["completion"]["state"] == "complete" for task in registry["tasks"]),
                "incomplete": sum(task["completion"]["state"] != "complete" for task in registry["tasks"]),
            }
            if manifest.get("counts") != counts:
                errors.append("manifest counts mismatch")
            output_hashes = manifest.get("outputs")
            if not isinstance(output_hashes, dict) or set(output_hashes) != set(expected_non_manifest):
                errors.append("manifest output path set mismatch")
            else:
                for relative, expected_data in expected_non_manifest.items():
                    target = plan_dir / relative
                    if target.is_file():
                        actual_hash = sha256_bytes(target.read_bytes())
                        if output_hashes.get(relative) != actual_hash:
                            errors.append(f"manifest hash mismatch: {relative}")
                        if actual_hash != sha256_bytes(expected_data):
                            errors.append(f"canonical hash mismatch: {relative}")
            if (manifest.get("validation") or {}).get("status") not in {"not-run", "passed"}:
                errors.append("manifest validation status invalid")
    return errors


def mark_manifest_passed(plan_dir: Path, registry: dict[str, Any]) -> None:
    path = plan_dir / f"TODO_{registry['slug']}-manifest.json"
    manifest = json.loads(path.read_text(encoding="utf-8"))
    manifest["validation"] = {"status": "passed", "validator_version": GENERATOR_VERSION}
    atomic_write(path, canonical_json_bytes(manifest))
