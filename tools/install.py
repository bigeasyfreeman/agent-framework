#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def copy_tree(src: Path, dst: Path, *, force: bool) -> None:
    if dst.exists():
        if not force:
            raise FileExistsError(f"Refusing to overwrite existing path: {dst}")
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def copy_file(src: Path, dst: Path, *, force: bool) -> None:
    if dst.exists() and not force:
        raise FileExistsError(f"Refusing to overwrite existing file: {dst}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install an agent framework template into an existing repo.",
    )
    parser.add_argument(
        "--adapter",
        required=True,
        help="Template adapter to use (e.g. 'claude').",
    )
    parser.add_argument(
        "--target",
        required=True,
        help="Path to the target repo directory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files/directories if present.",
    )
    args = parser.parse_args()

    repo_root = Path(args.target).expanduser().resolve()
    if not repo_root.exists() or not repo_root.is_dir():
        raise SystemExit(f"Target does not exist or is not a directory: {repo_root}")

    templates_root = Path(__file__).resolve().parents[1] / "templates"
    adapter_root = templates_root / args.adapter
    if not adapter_root.exists() or not adapter_root.is_dir():
        raise SystemExit(f"Unknown adapter '{args.adapter}'. Expected directory: {adapter_root}")

    src_claude_md = adapter_root / "CLAUDE.md"
    src_dot_claude = adapter_root / ".claude"

    if src_claude_md.exists():
        copy_file(src_claude_md, repo_root / "CLAUDE.md", force=args.force)
        print(f"Installed: {repo_root / 'CLAUDE.md'}")

    if src_dot_claude.exists():
        copy_tree(src_dot_claude, repo_root / ".claude", force=args.force)
        print(f"Installed: {repo_root / '.claude'}")

    print("Done.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except FileExistsError as e:
        print(str(e), file=sys.stderr)
        print("Tip: re-run with --force to overwrite.", file=sys.stderr)
        raise SystemExit(2)
