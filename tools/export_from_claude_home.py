#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path


ALLOWLIST_DIRS = [
    "agents",
    "evals",
    "scripts",
]
ALLOWLIST_FILES = [
    "README.md",
    "CLAUDE.md",
]


SECRET_PATTERNS: list[re.Pattern[str]] = [
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9]{30,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"(?i)ANTHROPIC_API_KEY"),
    re.compile(r"(?i)OPENAI_API_KEY"),
    re.compile(r"(?i)api[_-]?key\s*=\s*['\"][^'\"]+['\"]"),
]


def scan_for_secrets(root: Path) -> list[str]:
    findings: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        # Best-effort: treat as UTF-8 text; skip binary-ish files.
        try:
            data = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for pat in SECRET_PATTERNS:
            if pat.search(data):
                findings.append(str(path))
                break
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Export a safe, publishable subset of ~/.claude into an output directory.",
    )
    parser.add_argument(
        "--home",
        default=str(Path.home() / ".claude"),
        help="Path to the source ~/.claude directory (default: ~/.claude).",
    )
    parser.add_argument(
        "--out",
        required=True,
        help="Output directory (will be replaced if it exists).",
    )
    args = parser.parse_args()

    src = Path(args.home).expanduser().resolve()
    if not src.exists() or not src.is_dir():
        raise SystemExit(f"Source does not exist or is not a directory: {src}")

    out_root = Path(args.out).expanduser().resolve()
    if out_root.exists():
        shutil.rmtree(out_root)
    out_root.mkdir(parents=True)

    # Produce a Claude adapter-shaped export.
    adapter_root = out_root
    dot_claude = adapter_root / ".claude"
    dot_claude.mkdir(parents=True)

    for d in ALLOWLIST_DIRS:
        src_dir = src / d
        if src_dir.exists() and src_dir.is_dir():
            shutil.copytree(src_dir, dot_claude / d)

    for f in ALLOWLIST_FILES:
        src_file = src / f
        if src_file.exists() and src_file.is_file():
            shutil.copy2(src_file, adapter_root / f)

    findings = scan_for_secrets(adapter_root)
    if findings:
        print("Potential secrets detected in export (refusing to proceed):", file=sys.stderr)
        for p in findings:
            print(f"- {p}", file=sys.stderr)
        return 2

    print(f"Exported to: {adapter_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
