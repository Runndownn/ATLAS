#!/usr/bin/env python3
"""Deterministically generate a BinReaper ATLAS production TODO family."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from todo_system_lib import (
    OutputConflict,
    RegistryError,
    atomic_write,
    build_outputs,
    load_registry,
    preflight,
    preserve_passed_manifest,
    stale_part_files,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", required=True, type=Path)
    parser.add_argument("--part1-header", required=True, type=Path)
    parser.add_argument("--output-root", required=True, type=Path)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--replace-conflicts", action="store_true")
    args = parser.parse_args()

    registry_path = args.registry.resolve()
    header_path = args.part1_header.resolve()
    output_root = args.output_root.resolve()
    if not registry_path.is_file() or registry_path.is_symlink():
        print(f"Generation blocked: registry must be a regular non-symlink file: {registry_path}", file=sys.stderr)
        return 2
    if not header_path.is_file() or header_path.is_symlink():
        print(f"Generation blocked: PART1 header must be a regular non-symlink file: {header_path}", file=sys.stderr)
        return 2

    lock_path = output_root / ".atlas-production-todo.lock"
    lock_fd: int | None = None
    try:
        registry = load_registry(registry_path)
        header = header_path.read_bytes()
        outputs, _manifest, _blocks = build_outputs(registry, header, "not-run")
        plan_dir = output_root / f"Plan_{registry['slug']}"
        if plan_dir.parent.resolve() != output_root:
            raise RegistryError("plan directory escaped output root")
        preserve_passed_manifest(plan_dir, registry["slug"], outputs)
        create, unchanged, replace = preflight(plan_dir, outputs, args.replace_conflicts)
        stale = stale_part_files(plan_dir, registry["slug"], outputs)
        if stale and not args.replace_conflicts:
            raise OutputConflict("stale PART1 files: " + ", ".join(str(path) for path in stale))

        action = "APPLY" if args.apply else "DRY-RUN"
        print(f"{action}: {plan_dir}")
        print(f"- create: {len(create)}")
        print(f"- unchanged: {len(unchanged)}")
        print(f"- replace: {len(replace)}")
        print(f"- stale part files: {len(stale)}")
        print(f"- canonical tasks: {len(registry['tasks'])}")
        print(f"- PART1 documents: {len(registry['tasks']) // 3}")
        if not args.apply:
            return 0

        output_root.mkdir(parents=True, exist_ok=True)
        try:
            lock_fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            os.write(lock_fd, f"pid={os.getpid()}\n".encode("utf-8"))
            os.fsync(lock_fd)
        except FileExistsError as exc:
            raise OutputConflict(f"generation lock exists: {lock_path}") from exc

        plan_dir.mkdir(parents=True, exist_ok=True)
        for relative_text, data in sorted(outputs.items()):
            atomic_write(plan_dir / Path(relative_text), data)
        for path in stale:
            path.unlink()
        print("Generation applied successfully.")
        return 0
    except (RegistryError, OutputConflict, UnicodeDecodeError, json.JSONDecodeError, OSError) as exc:
        print(f"Generation blocked: {exc}", file=sys.stderr)
        return 2
    finally:
        if lock_fd is not None:
            os.close(lock_fd)
            try:
                lock_path.unlink()
            except FileNotFoundError:
                pass


if __name__ == "__main__":
    raise SystemExit(main())
