#!/usr/bin/env python3
"""Validate a generated BinReaper ATLAS production TODO family."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from todo_system_lib import (
    RegistryError,
    load_registry,
    mark_manifest_passed,
    validate_plan_dir,
    validate_registry,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", required=True, type=Path)
    parser.add_argument("--plan-dir", required=True, type=Path)
    parser.add_argument("--part1-header", required=True, type=Path)
    parser.add_argument("--write-validation", action="store_true")
    args = parser.parse_args()

    registry_path = args.registry.resolve()
    plan_dir = args.plan_dir.resolve()
    header_path = args.part1_header.resolve()
    try:
        if registry_path.is_symlink() or header_path.is_symlink():
            raise RegistryError("registry and PART1 header must not be symlinks")
        registry = load_registry(registry_path)
        validate_registry(registry)
        if plan_dir.name != f"Plan_{registry['slug']}":
            raise RegistryError(f"plan directory must be Plan_{registry['slug']}")
        header = header_path.read_bytes()
        header.decode("utf-8")
        errors = validate_plan_dir(registry, header, plan_dir)
    except (RegistryError, OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        print(f"Validation failed during setup: {exc}", file=sys.stderr)
        return 2

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    if args.write_validation:
        mark_manifest_passed(plan_dir, registry)
        errors = validate_plan_dir(registry, header, plan_dir)
        if errors:
            print("Validation failed after marking manifest:")
            for error in errors:
                print(f"- {error}")
            return 1

    print(
        "Validation passed: "
        f"{len(registry['tasks'])} canonical tasks, "
        f"{len(registry['tasks'])} v1.2 tasks, "
        f"{len(registry['tasks'])} v2.1 TODOs, "
        f"{len(registry['tasks']) // 3} PART1 documents, "
        "exactly three TODOs per PART1 document."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
