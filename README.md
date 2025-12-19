# Agent Framework (Model-Agnostic)

This repository is a **model/runtime-agnostic, multi-agent development workflow** extracted from my local Claude setup (`~/.claude/`) and repackaged as a distributable template.

It’s designed to be:

- **Tool-agnostic**: the core ideas are phases, contracts, gates, and handoffs.
- **Adapter-based**: you “install” the framework into a repo in the format your agent runtime expects.
- **Safe to publish**: it intentionally does **not** include local chat history, telemetry, or settings.

## What’s included

- `templates/claude/` – a ready-to-copy template for a repo that uses:
  - `CLAUDE.md` at the repo root
  - `.claude/agents/` personas
  - `.claude/evals/` eval specs
  - `.claude/scripts/agent_audit.sh` enforcement helper

## What is intentionally NOT included

Do **not** publish or commit these (they often contain sensitive data):

- `~/.claude/history*`, `~/.claude/projects/`, `~/.claude/file-history/`
- `~/.claude/settings.json`, `~/.claude/session-env/`, `~/.claude/telemetry/`
- Any repo-local `.claude/history/` contents containing real session transcripts

If you’re using this repo to update the template from your own machine, use the export script (below), not a raw copy.

## Quickstart (Claude adapter)

Install the template into an existing git repo:

```bash
python3 tools/install.py --adapter claude --target /path/to/your/repo
```

That will:

- copy `templates/claude/CLAUDE.md` → `/path/to/your/repo/CLAUDE.md` (if missing)
- copy `templates/claude/.claude/` → `/path/to/your/repo/.claude/` (if missing)

Then:

1. Create/update `/path/to/your/repo/TECHSTACK.md` (see `.claude/agents/TECHSTACK.md.template`).
2. Commit `CLAUDE.md`, `.claude/`, and `TECHSTACK.md`.

## Keeping it model-agnostic

The framework is written so you can run it in many environments. The key primitives are:

- **Phases** (intake → clarify → plan → build → gates → ship)
- **Agent roles** (coordinator + specialists)
- **Contracts** (`handoff_note`, `gate_report`)
- **Model routing** (declared in `TECHSTACK.md`, but adaptable to any runtime)

The `templates/claude/` folder is one adapter. If you want to support another runtime, add a new folder under `templates/<runtime>/` and map the same concepts into that runtime’s configuration format.

## Updating the template from your local `~/.claude`

If you maintain your framework in `~/.claude` and want to refresh this repo safely:

```bash
python3 tools/export_from_claude_home.py --out ./export/claude
```

This export script is **allowlist-based** (copies only `agents/`, `evals/`, `scripts/`, and safe docs) and then runs a lightweight secret scan.

## Attribution

If you reuse this framework, please retain the copyright/license notices and link back to this repo.

## License

Apache-2.0 (see `LICENSE` and `NOTICE`).
