# Claude Agent Framework

This directory contains a multi-agent, phase-based development workflow. The `coordinator` orchestrates specialist agents, collects standardized handoffs, and runs read-only quality gates before shipping.

## How the framework is structured

- `CLAUDE.md`: global rules (pipeline enforcement, model routing, required response formats)
- `agents/*.md`: agent personas (build agents, gate agents, orchestration agents)
- `agents/TECHSTACK.md.template`: template for repo-root `TECHSTACK.md` (includes model routing + optional per-agent defaults)
- `scripts/agent_audit.sh`: repo audit + Phase 6 enforcement (incl. requiring `.claude/history/sessions/` updates when repo changes)
- `evals/`: eval specs used by `evals-agent` (repo-local evals can live in `.claude/evals/` too)
- `history/`: runtime global history store for this machine (`~/.claude/history/`; not part of the distributable framework zip)

Global `~/.claude/` provides defaults across repos. Repo-local `<repo>/.claude/` should override global defaults when both exist.

## Pipeline overview (phases)

The pipeline is phase-based; skipping phases requires explicit approval (see `agents/coordinator.md`).

- **Phase -1: INTAKE** → `intake-agent` (triage, routing, risk level)
- **Phase 0: CLARIFY** → `product-agent` (+ `researcher-agent` as needed)
- **Phase 0.5: DISCOVER** → `context-scout-agent` produces a `context_bundle`
- **Phase 1: PLAN** → `coordinator` assigns work to agents with scoped ownership
- **Phase 1.5: CONTRACT** → `api-contract-agent` (when API/contracts change)
- **Phase 2: FOUNDATION** → `data-agent` + `infra-agent` (when schema/infra changes)
- **Phase 3: BUILD** → `frontend-agent` / `backend-agent` / `ai-agent` (parallel where safe)
- **Phase 3.5: INTEGRATE** → `integration-agent` reconciles drift and prepares for gates
- **Phase 4: GATES (read-only)** → gate agents (testing/qa/security/ai-sast/evals/etc.) return `gate_report`
- **Phase 5: CLEANUP** → `cleanup-agent` (hygiene, de-risking)
- **Phase 6: SHIP** → `context-builder` + `memory-agent` + `history-agent` (+ metrics updates)

## Required response formats (contracts)

### `handoff_note` (required for repo-changing work)

Any agent that **changes repo state** (contracts/foundation/build/cleanup/docs) must end with a fenced `yaml` block containing `handoff_note` (Schema v1). The coordinator includes relevant handoffs verbatim for integration and Phase 4 gates.

```yaml
handoff_note:
  version: 1
  from_agent: ai-agent
  status: done # done|blocked
  summary: "What changed and why"
  files_changed: []
  decisions: []
  commands_run: []
  risks: []
  followups:
    - owner_agent: security-agent
      item: "What should be validated next"
```

### `gate_report` (required for Phase 4 gate agents)

Every Phase 4 gate agent response must end with a fenced `yaml` block containing `gate_report` (Schema v1). Gates are **read-only verifiers**; they do not fix issues directly.

```yaml
gate_report:
  version: 1
  gate: security-agent
  status: pass # pass|fail|warn|skip
  summary: "1-2 sentence outcome summary"

  evidence:
    commands: []
    notes: []

  findings: []
  questions_for_coordinator: []
```

## Model routing + per-agent defaults

Repo-root `TECHSTACK.md` is the source of truth for which model/tool does what. It must include `model_routing`, and may include `agent_work_type_defaults` to set persona defaults (override per task only when necessary).

Defaults (if available):
- **analysis** → Codex (`gpt-5.2-thinking`)
- **execution** → Claude Code (`claude-opus-4.5`)
- **data_processing** → Gemini (`gemini-3`)

See `agents/TECHSTACK.md.template` for the full block.

## Deploy to a new repo

1. Add the framework to the repo as `<repo>/.claude/` (recommended so it is versioned/shared).
   - If starting from `claude-agent-framework.zip`: unzip, then rename `claude-agent-framework/` → `.claude/`.
2. Run the `claude-bootstrap` agent (`agents/claude-bootstrap.md`) to create/update:
   - `<repo>/TECHSTACK.md` (including `model_routing` and optional `agent_work_type_defaults`)
   - `docs/memory/{DECISIONS,LEARNINGS,CONVENTIONS}.md`
   - `.claude/history/` directory structure + `.claude/scripts/agent_audit.sh` (Phase 6 enforcement)
   - optional `.claude/evals/` scaffolding
3. Commit `.claude/` + `TECHSTACK.md` so the whole workflow is reproducible for the team.

## Customizing per repo

- Prefer repo-local overrides under `.claude/agents/` for any project-specific behavior.
- Use overlays by listing `overlays:` in `TECHSTACK.md` and adding `.claude/agents/overlays/<name>.md`.
