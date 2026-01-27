# Multi-Agent Engineering Framework

## 🔥 THE ALGORITHM - Universal Execution Engine

**THE ALGORITHM** provides structured execution for any task, from trivial fixes to complex features.

### Invocation
- "run the algorithm" or "use the algorithm" → Full 7-phase execution
- "algorithm effort [LEVEL]: [task]" → Force effort level

### The 7 Phases
```
1. OBSERVE  → Gather context, understand current state
2. THINK    → Analyze, form hypotheses, identify gaps
3. PLAN     → Create execution strategy with ISC
4. BUILD    → Implement using appropriate agents
5. EXECUTE  → Run, test, integrate
6. VERIFY   → Quality gates, validation
7. LEARN    → Capture insights, improve system
```

### Effort Classification
| Level | Description | Agents | Parallel |
|-------|-------------|--------|----------|
| TRIVIAL | Single-line fix | None | 0 |
| QUICK | Simple bug/feature | Intern | 1 |
| STANDARD | Typical feature | Engineer, QA | 1-3 |
| THOROUGH | Complex feature | + Architect | 3-5 |
| DETERMINED | Critical/complex | All | 10+ |

### ISC (Ideal State Criteria)
Every task creates an ISC table tracking completion:
```
| # | Criterion | Status | Evidence |
|---|-----------|--------|----------|
| 1 | Tests pass | ⏳ | - |
| 2 | No console errors | ⏳ | - |
| 3 | User can complete flow | ⏳ | - |
```

**Skills location:** `.claude/skills/THEALGORITHM/`

---

## ⚠️ MANDATORY PIPELINE ENFORCEMENT

**CRITICAL**: This development pipeline is MANDATORY for ALL work, regardless of perceived scope or complexity. You MUST:

1. **Execute every phase** unless the user explicitly says "skip phase X"
2. **Use the phase checklist** below and mark each phase complete
3. **NEVER assume** a phase is unnecessary - ask first if unclear
4. **Phase 6 (context-builder + documentation + history capture) is ALWAYS required** - no exceptions

```
BEFORE ANY IMPLEMENTATION, output this checklist:
═══════════════════════════════════════════════════════════════
PIPELINE EXECUTION CHECKLIST
═══════════════════════════════════════════════════════════════
[ ] Preflight: BRANCH - create/switch to a dedicated branch (before edits)
[ ] Phase -1: INTAKE - intake-agent (triage, routing, risk level)
[ ] Phase 0: CLARIFY - product-agent (requirements, acceptance criteria)
[ ] Phase 0.5: DISCOVER - context-scout-agent (repo scan, context bundle)
[ ] Phase 1: PLAN - coordinator (implementation analysis, task decomposition)
[ ] Phase 1.5: CONTRACT - api-contract-agent (if API changes)
[ ] Phase 2: FOUNDATION - data-agent + infra-agent (if schema/infra changes)
[ ] Phase 3: BUILD - frontend/backend/ai agents
[ ] Phase 3.5: INTEGRATE - integration-agent (merge parallel work, interface checks)
[ ] Phase 4: QUALITY GATES - testing + qa + security + ai-sast-agent + evals-agent + code-review + logging + sre (+ availability/ui/ux as applicable)
[ ] Phase 5: CLEANUP - cleanup-agent (dead code, imports, debug statements)
[ ] Phase 6: SHIP - agent audit + context-builder (MANDATORY docs) + memory-agent + history-agent (update .claude/history/sessions if present) + metrics-agent + evals-agent + PR
═══════════════════════════════════════════════════════════════
```

**If you want to skip a phase, you MUST:**
1. State which phase you want to skip
2. Explain why
3. Get explicit user approval with "yes, skip phase X"

---

## 🌿 Hard Rule: Branch-Per-Scope (MANDATORY)

Any time you will change files in a repo (code, tests, docs, config), you MUST:

1. **Create a new branch immediately** (before the first edit/commit) to avoid conflicts/collisions.
2. **Keep one branch = one scope**. If scope changes, stop and create a new branch.
3. **Phase 6 is not complete until a PR/MR is OPEN** for the branch (unless the user explicitly says "no PR").
4. **After merge, delete the branch** (remote) and prune/delete the local branch to keep things clean.

**Examples (Git):**
```bash
# Create/switch to a new branch
git checkout -b <branch>

# Push branch + set upstream
git push -u origin HEAD

# After merge: delete remote branch (and prune/delete local if desired)
git push origin --delete <branch>
git branch -d <branch>
```

---

## 🔒 Hard Rule: Delegation Uses Fresh Context Windows

**Assumption:** Every delegated agent/subtask runs in a **fresh, isolated context window**.

- A worker does **not** inherit coordinator chat history, prior plans, or other agents’ outputs unless they are explicitly included in the worker’s first message.
- Delegation must be treated as “this is the only context the worker sees.”

### Delegation Contract (Coordinator / Delegation Agent)
When spawning a worker, include a self-contained brief with:
- Goal, non-goals, and acceptance criteria
- Explicit scope boundaries (files/dirs the worker may and may not edit)
- Inputs: spec excerpts + `context_bundle` (Phase 0.5) + any required decisions
- Verification commands the worker should run

### Worker Contract (All Agents)
If required context is missing or ambiguous:
- Stop and route the missing-input request back to the `coordinator` before editing (do not ask the user directly).
- If you changed repo state, end your response with a `handoff_note` YAML block (Schema v1; see `~/.claude/agents/coordinator.md#standard-build-handoff-note-required`).

### Standard Build Handoff Note (Required: `handoff_note` YAML)
Any agent that completes work which changes repo state (contracts/foundation/build/cleanup/docs) must end with:

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

### Phase 4 Gate Contract (All Gate Agents)
- Run as a **fresh, read-only verifier**: do not use `Write`/`Edit`, do not modify files, and do not “fix” issues directly.
- Treat `handoff_note` blocks (if provided) as required context; if missing for changed areas, request them from the `coordinator` before concluding risk.
- Return a gate report with evidence (commands run, key outputs) and actionable findings.
- Route all fixes back to the `coordinator`, who assigns them to the **owning agent** for the affected files.

### Phase 4 Gate Report Format (Required: `gate_report` YAML)
Every Phase 4 gate agent response must end with a fenced `yaml` block containing `gate_report` (Schema v1).

```yaml
gate_report:
  version: 1
  gate: code-review-agent
  status: pass # pass|fail|warn|skip
  summary: "1-2 sentence outcome summary"

  evidence:
    commands: []
    notes: []

  findings: []
  # findings:
  #   - severity: high # critical|high|medium|low|info
  #     title: "Short title"
  #     affected_paths: ["path/to/file.ext"]
  #     owner_agent: "backend-agent" # or "coordinator" if unclear
  #     recommended_fix: "Concrete remediation in 1-5 sentences"
  #     evidence: "Optional: key log lines, stack trace, or command output excerpt"
  #     repro: "Optional: exact steps/commands to reproduce"
  #     confidence: high # high|medium|low

  questions_for_coordinator: []
```

---

## 🧠 Hard Rule: Model Routing (Defined in `TECHSTACK.md`)

**Source of truth:** Every repo must define a `model_routing` block in `TECHSTACK.md` (see `~/.claude/agents/TECHSTACK.md.template`). Optional: add `agent_work_type_defaults` to set per-agent defaults (persona → work type) so the coordinator can auto-route tasks.

Hard routing rules (current defaults):
- **Analysis / planning / verification reasoning** → **Codex** (`gpt-5.2-thinking`, “heavy”)
- **Coding / task execution** (edits, fixes, running commands) → **Claude Code** (`claude-opus-4.5`)
- **Large data processing** (normalization/chunking/summarization) → **Gemini** (`gemini-3`)

Classification note:
- **Phase 4 gates** are **analysis** work (Codex). If a gate needs command output, have the `coordinator` delegate command execution to the **execution** engine and then evaluate the results in the gate report.

If a task is routed to the wrong engine/model, stop and route it back to the `coordinator` to reassign.

## ⚠️ Hard Guardrail: Deprecation Warnings

- Treat deprecation warnings as regressions in code you touch: fix them or explicitly call out deferral + follow-up.
- During Phase 4 verification, scan test/build output for "deprecat" and address warnings that originate from project code (not third-party tooling).
- Prefer non-deprecated primitives/APIs (example: `time.monotonic()` for elapsed time; avoid deprecated event-loop helpers like `asyncio.get_event_loop()` in new code).

## Agent Framework

Agents are available in `~/.claude/agents/` and provide specialized capabilities:

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| `intake-agent` | Triage, routing, risk level | **Phase -1**: ALWAYS first unless explicitly skipped |
| `product-agent` | Requirements, acceptance criteria | **Phase 0**: After intake, for any work needing clarification |
| `context-scout-agent` | Repo discovery, context bundle | **Phase 0.5**: MANDATORY for any code change |
| `coordinator` | Task decomposition, agent assignment | **Phase 1**: After requirements clear |
| `api-contract-agent` | OpenAPI specs, types, client generation | **Phase 1.5**: Any API changes |
| `memory-agent` | Decisions, learnings, conventions | **Always**: Read at start, write on decisions |
| `data-agent` | Schema design, migrations, queries | **Phase 2**: Any schema changes |
| `infra-agent` | Terraform, Pulumi, IaC | **Phase 2**: Any infrastructure changes |
| `frontend-agent` | Next.js, React, Tailwind, a11y | **Phase 3**: Any UI work |
| `backend-agent` | FastAPI, Pydantic, async Python | **Phase 3**: Any API/service work |
| `ai-agent` | LLM integration, prompts, RAG | **Phase 3**: Any AI features |
| `integration-agent` | Merge parallel work, interface coherence | **Phase 3.5**: After parallel build |
| `testing-agent` | Test generation, coverage | **Phase 4**: MANDATORY |
| `qa-agent` | E2E flows, regression matrix | **Phase 4**: MANDATORY |
| `security-agent` | Threat modeling, OWASP, SAST | **Phase 1-2** (threat model), **Phase 4** (scan) - MANDATORY |
| `ai-sast-agent` | Multi-agent SAST deep scan (code + IaC + APIs + deps) | **Phase 4**: MANDATORY for any code/config/infra changes |
| `evals-agent` | Deterministic behavior enforcement | **Phase 4** (behavioral validation), **Phase 6** (final check) |
| `code-review-agent` | Quality, maintainability, patterns | **Phase 4**: MANDATORY |
| `logging-agent` | Audit trails, observability | **Phase 4**: MANDATORY |
| `sre-agent` | Scalability, reliability, infra review | **Phase 4**: MANDATORY |
| `availability-agent` | Runtime resilience, graceful degradation | **Phase 4**: MANDATORY for frontend/data fetching changes |
| `ui-validation-agent` | Box model, style leakage, visual integrity | **Phase 4**: MANDATORY if frontend changes |
| `ux-audit-agent` | Usability/flow audit, discoverability, friction | **Phase 4**: Run for user-facing changes and periodic UX audits |
| `metrics-agent` | Pipeline analytics, velocity | **Always**: Tracks all events |
| `history-agent` | Captures outputs to `.claude/history/` (if present) and `~/.claude/history/` | **Always**: Capture sessions/learnings; **Phase 6**: mandatory ship capture |
| `cleanup-agent` | Dead code, unused deps, hygiene | **Phase 5**: MANDATORY |
| `delegation-agent` | Parallel execution | Orchestrates phases 2-4 |
| `context-builder` | Documentation maintenance | **Phase 6**: MANDATORY - always update docs |
| `prompt-optimizer` | Context bundling | Complex debugging |
| `claude-bootstrap` | Repo initialization | New projects |

---

## Always-On Development Pipeline (MANDATORY)

**This pipeline is MANDATORY for ALL work.** No exceptions unless user explicitly opts out of specific phases.

### Pipeline Enforcement Rules

```yaml
ENFORCEMENT_POLICY:
  default: "FULL_PIPELINE"  # Always assume full pipeline
  skip_requires: "EXPLICIT_USER_APPROVAL"  # Must say "skip phase X"
  phase_6_skip: "NEVER"  # Documentation update is NEVER skipped

  # Even for "simple" tasks:
  simple_bug_fix: "Run Phases -1, 0 (if unclear), 0.5, then 3-6"
  typo_fix: "Run Phases -1 and 6 (update docs if file structure changed)"
  small_feature: "FULL PIPELINE (Phases -1 to 6) - no shortcuts"
```

### Pipeline Triggers

| Trigger | Pipeline | Can Skip? |
|---------|----------|-----------|
| New feature request | **Full pipeline** (Phases -1 to 6) | Only with explicit approval |
| Bug fix | **Phases -1, 0 (if needed), 0.5, 3-6** | Phase 0 only with explicit approval |
| Refactoring | **Phases -1, 0.5, 1, 3-6** | Need approval for each skip |
| Documentation only | **Phases -1, 6** | Never skip Phase 6 |
| ANY code change | **Phases 0.5, 4-6 MANDATORY** | Quality gates never skipped |

### Pipeline Phases

```
┌─────────────────────────────────────────────────────────────────┐
│  CROSS-CUTTING (always active)                                  │
│  ├─ memory-agent: Read DECISIONS.md, LEARNINGS.md, CONVENTIONS  │
│  ├─ metrics-agent: Track all events and durations               │
│  ├─ history-agent: Capture sessions/learnings/decisions         │
│  └─ security-agent: Threat modeling (Phase 1-2), scanning (4)   │
├─────────────────────────────────────────────────────────────────┤
│  PHASE -1: INTAKE (intake-agent)                    [GATE -1]   │
│  ├─ Classify request, detect ambiguity/risk                    │
│  └─ Output: Intake Report with routing                         │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 0: CLARIFY (product-agent)                     [GATE 0]  │
│  ├─ Parse requirement, ask clarifying questions                 │
│  ├─ memory-agent: Check past decisions on this topic            │
│  └─ Output: Clear spec with acceptance criteria                 │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 0.5: DISCOVER (context-scout-agent)          [GATE 0.5] │
│  ├─ Locate relevant files, patterns, tests                     │
│  └─ Output: Context Bundle                                     │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 1: PLAN (coordinator)                          [GATE 1]  │
│  ├─ Technical decomposition from spec                           │
│  ├─ security-agent: Threat modeling (if security-sensitive)     │
│  ├─ memory-agent: Check LEARNINGS.md for past issues            │
│  └─ Output: Execution plan with dependencies                    │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 1.5: CONTRACT (api-contract-agent)           [SEQUENTIAL]│
│  ├─ Define/update API contracts (OpenAPI, types)                │
│  ├─ Generate TypeScript types from specs                        │
│  └─ Output: Contracts ready for implementation                  │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 2: FOUNDATION (data-agent + infra-agent)     [SEQUENTIAL]│
│  ├─ data-agent: Schema design, migrations                       │
│  └─ infra-agent: Terraform/Pulumi changes (if needed)           │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 3: BUILD (parallel)                            [PARALLEL]│
│  ├─ backend-agent: API endpoints, services                      │
│  ├─ frontend-agent: UI components, pages                        │
│  └─ ai-agent: Prompts, LLM integration (if needed)              │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 3.5: INTEGRATE (integration-agent)          [SEQUENTIAL]│
│  ├─ Reconcile interfaces/types across agents                   │
│  └─ Output: Integration Report                                 │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 4: QUALITY GATES (parallel, mandatory)         [PARALLEL]│
│  ├─ testing-agent: Unit/integration tests, coverage ≥80%        │
│  ├─ qa-agent: E2E user flows, regression matrix                 │
│  ├─ security-agent: OWASP scan, vulnerability check             │
│  ├─ ai-sast-agent: Multi-agent SAST deep scan                    │
│  ├─ evals-agent: Behavioral validation, regression prevention    │
│  ├─ code-review-agent: Quality grade ≥A-                        │
│  ├─ logging-agent: Observability check                          │
│  ├─ sre-agent: Production readiness                             │
│  ├─ availability-agent: Runtime resilience checks               │
│  ├─ ux-audit-agent: Usability/flow audit (user-facing)          │
│  └─ ui-validation-agent: Visual integrity (frontend changes)    │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 5: CLEANUP (cleanup-agent)                   [SEQUENTIAL]│
│  └─ Remove dead code, debug statements, organize imports        │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 6: SHIP                                      [SEQUENTIAL]│
│  ├─ memory-agent: Capture decisions/learnings                   │
│  ├─ metrics-agent: Log completion stats                         │
│  ├─ history-agent: Capture session + key artifacts              │
│  ├─ evals-agent: Final eval run (if applicable)                 │
│  └─ Final tests, update docs, open PR                           │
└─────────────────────────────────────────────────────────────────┘
```

### Parallelization Rules

```yaml
parallel_safe:
  - backend-agent + frontend-agent + ai-agent                    # Phase 3
  - testing + qa + security + ai-sast-agent + evals-agent + code-review + logging + sre + availability + ux-audit + ui-validation # Phase 4

sequential:
  - intake-agent → product-agent → context-scout-agent → coordinator → api-contract-agent → foundation → build → integration-agent → gates → cleanup → ship
  - data-agent + infra-agent can run in parallel within Phase 2

always_active:
  - memory-agent   # Reads context, captures decisions
  - metrics-agent  # Tracks all events
  - history-agent  # Captures sessions/learnings/decisions
  - security-agent # Threat modeling (early), scanning (late)
```

### Failure Handling & Feedback Loops

**When a gate fails, route back to fix:**

| Gate Failure | Routes To |
|--------------|-----------|
| Test failure | Agent that owns the failing file |
| E2E flow failure | qa-agent → frontend-agent or backend-agent |
| Security vuln | backend-agent (injection/auth) or frontend-agent (XSS) |
| Code review B/C/D | Agent that owns the file |
| Missing logs | Agent that owns the file |
| SRE issue | backend-agent or data-agent |
| Infrastructure issue | infra-agent |
| Contract violation | api-contract-agent → backend-agent |
| UI validation failure | frontend-agent (overflow, z-index, style leakage, visual overlap) |

**On ANY failure:**
- memory-agent checks LEARNINGS.md for known fixes
- metrics-agent logs the failure event

**Feedback Protocol:**
1. **Capture** - What failed, why, which files
2. **Route** - Send failure report to responsible agent
3. **Fix** - Agent applies targeted fix + local validation
4. **Revalidate** - Re-run ONLY the failed gate
5. **Escalate** - After 3 retries, escalate to user

```yaml
max_retries_per_gate: 3
max_total_retries: 10
```

---

## Always-On Practices

You are working with Eric, a developer who follows a multi-agent development framework. These practices should be applied automatically to ALL work:

### Context Maintenance (Context Builder)
- After creating new files/directories, update or create relevant `CONTEXT.md` files
- Keep documentation current with code changes
- Maintain `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, and `docs/GLOSSARY.md` when relevant

### Testing Standards (Testing Agent + QA Agent)
- All new code should have corresponding unit/integration tests (testing-agent)
- Critical user flows should have E2E tests (qa-agent)
- Target 80% coverage minimum, 100% for critical paths (auth, payments, data mutations)
- Run tests before considering work complete
- Use appropriate testing patterns: unit, integration, e2e as needed

### Security First (Security Agent)
- **Phase 1-2**: Threat model security-sensitive features (auth, public APIs, AI)
- **Phase 4**: Scan for OWASP Top 10 vulnerabilities
- Check for hardcoded secrets, SQL injection, XSS, and other common issues
- Validate and sanitize all user inputs
- Use parameterized queries for database operations
- Apply principle of least privilege

### API Contracts (API Contract Agent)
- Define API contracts before implementation
- Keep OpenAPI specs in sync with code
- Generate types from specs
- Detect breaking changes before they ship

### Infrastructure (Infra Agent)
- Use Terraform for platform-level infrastructure
- Use Pulumi for service-level infrastructure
- Never make manual cloud console changes
- All infra changes go through IaC

### Logging & Observability (Logging Agent)
- Add structured logging to new features
- Include audit trails for sensitive operations (auth, data mutations, admin actions)
- Implement proper error handling with meaningful error codes
- Never log sensitive data (passwords, tokens, PII)

### Task Coordination (Coordinator)
- For complex features, decompose into focused subtasks
- Identify dependencies and parallelization opportunities
- Track progress and blockers
- Each task should be completable in 15-30 minutes, touch ≤5 files

### Code Quality
- Follow existing codebase patterns and conventions
- Keep functions small and focused
- Use meaningful names
- Add comments only where logic isn't self-evident

### Shell & Prompt Safety
- **Quote paths with brackets**: In zsh/bash, always quote file paths containing `[ ]` (common in Next.js dynamic routes) when using `git add`, `sed`, `rg`, etc.
  ```bash
  # Correct
  git add -- 'apps/web/src/app/workspaces/[workspaceId]/page.tsx'

  # Wrong - brackets interpreted as glob pattern
  git add apps/web/src/app/workspaces/[workspaceId]/page.tsx
  ```
- **Avoid backticks in prompts**: In zsh, backticks trigger command substitution. Use single or double quotes instead.
  ```bash
  # Correct
  echo "Use the 'foo' function"

  # Wrong - zsh tries to execute 'foo' as a command
  echo "Use the `foo` function"
  ```

## Workflow Triggers

### When Starting New Work
1. Create a new branch immediately (before any edits)
2. Check/update context documentation first
3. Plan the approach before coding
4. Consider security implications upfront (threat model if needed)
5. Define API contracts if adding/changing endpoints

### When Writing Code
1. Write tests alongside implementation
2. Add appropriate logging
3. Handle errors gracefully
4. Validate inputs at boundaries

### Before Completing Work
1. Run tests and ensure they pass
2. Quick security review of changes
3. Update context/documentation if needed
4. Verify logging coverage for new code paths

## Explicit Agent Invocation

The pipeline runs automatically, but you can invoke agents directly:

**Requirements & Planning:**
- "Use product-agent to clarify these requirements"
- "Use coordinator to decompose this feature"
- "Use memory-agent to recall past decisions on this topic"

**Contracts & Infrastructure:**
- "Use api-contract-agent to define the API contract"
- "Use infra-agent to set up the infrastructure"

**Core Development:**
- "Use frontend-agent to build this React component"
- "Use backend-agent to create the FastAPI endpoint"
- "Use data-agent to design the database schema"
- "Use ai-agent to implement this AI feature"

**Quality & Security:**
- "Use testing-agent to generate comprehensive tests"
- "Use qa-agent to create E2E tests for this flow"
- "Use security-agent to threat model this feature"
- "Use security-agent to audit this endpoint"
- "Use code-review-agent to review code quality"
- "Use logging-agent to add observability"
- "Use sre-agent to review production readiness"
- "Use ui-validation-agent to check for layout and visual issues"

**Shipping:**
- "Use cleanup-agent to clean up before PR"
- "Use context-builder to update documentation"
- "Use delegation-agent to parallelize this work"

**Analytics & Memory:**
- "Use metrics-agent to show pipeline stats"
- "Use memory-agent to capture this decision"

**Research:**
- "Use researcher-agent to research X"
- "Quick research on Y"
- "Extensive research on Z"

**Continuous Improvement:**
- "Use history-agent to capture this session"
- "Use evals-agent to create eval for this behavior"
- "Use self-improvement-agent to analyze recent patterns"

---

## Enhanced Agent Framework

In addition to the core pipeline agents, these agents provide advanced capabilities:

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| `researcher-agent` | Multi-source parallel research (incl. product/UX patterns) | Research tasks, fact-checking, competitive analysis, product/UX pattern scans |
| `self-improvement-agent` | Framework optimization | Weekly analysis, pattern extraction, agent improvements |

---

## History Capture System (UOCS)

Automatic capture of all valuable work outputs for searchable knowledge across all projects.

### Directory Structure
Project-local (if present): `.claude/history/`  
Global: `~/.claude/history/`

Directory structure (same for both):
```
~/.claude/history/
├── sessions/YYYY-MM/           # Session summaries
├── learnings/YYYY-MM/          # Problem-solving narratives  
├── research/YYYY-MM/           # Research findings
├── decisions/YYYY-MM/          # Architectural decisions
├── features/YYYY-MM/           # Feature implementations
├── bugs/YYYY-MM/               # Bug fixes
└── raw-outputs/YYYY-MM/        # Event logs (JSONL)
```

### File Naming Convention
`YYYY-MM-DD-HHMMSS_[PROJECT]_[TYPE]_[DESCRIPTION].md`

**Types:** SESSION, LEARNING, RESEARCH, DECISION, FEATURE, BUG

### Capture Triggers

| Event | Capture Type | Agent |
|-------|-------------|-------|
| Session ends | SESSION | history-agent |
| Gate failure resolved (2+ retries) | LEARNING | history-agent |
| Research completed | RESEARCH | researcher-agent → history-agent |
| Architecture decision made | DECISION | memory-agent → history-agent |
| Feature shipped | FEATURE | history-agent |
| Bug fixed | BUG | history-agent |

### History Commands

| Command | Description |
|---------|-------------|
| `history search <query>` | Full-text search across all history |
| `history recent [n]` | Show n most recent captures |
| `history project <name>` | All captures for a project |
| `history type <type>` | All captures of specific type |
| `capture session` | Manually capture current session |
| `capture learning` | Capture a learning moment |
| `capture decision` | Capture an architecture decision |

### Integration with memory-agent
- **memory-agent** → Project-specific (docs/DECISIONS.md, docs/LEARNINGS.md)
- **history-agent** → Project-local `.claude/history/` (if present) + global `~/.claude/history/`
- Sync: write to `.claude/history/` when available and copy to global; otherwise write to global only

---

## Research System

Multi-source parallel research with confidence scoring and source attribution.

### Research Modes

| Mode | Timeout | Queries | When to Use |
|------|---------|---------|-------------|
| **Quick** | 2 min | 1-2 | Simple factual questions |
| **Standard** | 5 min | 3-5 parallel | Default for most research |
| **Extensive** | 10 min | 8+ parallel | Deep dives, comprehensive analysis |

### Research Protocol
1. **Decompose** - Break topic into focused sub-questions
2. **Parallel Execute** - Launch queries simultaneously
3. **Cross-Validate** - Compare findings across sources
4. **Synthesize** - Assign confidence levels, attribute sources

### Confidence Levels
- **High (✓✓✓):** 3+ sources agree
- **Medium (✓✓):** 2 sources or 1 authoritative source
- **Low (✓):** Single non-authoritative source
- **Conflicting (⚠️):** Sources disagree

### Research Commands
```
research <topic>              # Standard research (5 min)
quick-research <topic>        # Quick research (2 min)
extensive-research <topic>    # Deep dive (10 min)
fact-check <claim>           # Verify specific claim
compare <A> vs <B>           # Comparative research
```

---

## Evaluation System (Evals)

Lock in deterministic behavior through evaluation suites.

### Eval Directory
```
~/.claude/evals/
├── global/                  # Cross-project evals
│   ├── agent-behaviors/     # Agent output expectations
│   ├── response-formats/    # Format compliance
│   └── security/            # Security behavior checks
├── [project]/               # Project-specific evals
└── regression/              # Auto-generated from failures
```

### Eval Types
1. **Output Evals** - Verify specific outputs match expectations
2. **Behavior Evals** - Verify agents behave correctly in scenarios
3. **Format Evals** - Verify outputs follow required formats
4. **Regression Evals** - Auto-generated from past failures

### Eval Commands

| Command | Description |
|---------|-------------|
| `eval create <name>` | Create new eval |
| `eval run [path]` | Run evals |
| `eval list` | List all evals |
| `eval status` | Pass/fail summary |
| `eval capture-regression` | Create eval from recent failure |

### Eval-First Development
1. Define expected behavior (write eval)
2. Verify eval fails (behavior doesn't exist)
3. Implement (make eval pass)
4. Lock in (eval prevents regression)

---

## Self-Improvement System

Continuous improvement through pattern analysis and framework optimization.

### Analysis Triggers
- **Weekly:** Pattern detection, agent effectiveness report
- **After 10+ gate failures:** Targeted failure analysis
- **On request:** "improve agents", "analyze what's not working"

### What Gets Analyzed
- Gate failure patterns (by agent, by error type)
- Success patterns (high-velocity sessions)
- Agent effectiveness metrics
- Convention violations

### Improvement Outputs
- Updated agent .md files
- New entries in CONVENTIONS.md
- Regression evals from failures
- Pattern reports with recommendations

### Improvement Commands
```
improve analyze              # Full analysis of recent history
improve agent <name>         # Analyze specific agent
improve patterns             # Extract patterns from history
improve suggest              # Generate improvement suggestions
improve conventions          # Update conventions from patterns
```

---

## Observability & Metrics

Enhanced event capture for pipeline visibility.

### Event Types
- `pipeline_start` / `pipeline_complete` - Phase lifecycle
- `gate_pass` / `gate_fail` - Quality gate results
- `agent_invoked` - Agent activations
- `file_changed` - File modifications
- `decision_made` / `learning_captured` - Knowledge events

### Event Log Location
Repo-local (if present): `.claude/history/raw-outputs/YYYY-MM/YYYY-MM-DD_events.jsonl`  
Global: `~/.claude/history/raw-outputs/YYYY-MM/YYYY-MM-DD_events.jsonl`

### Metrics Available
- Pipeline velocity (time per phase)
- Gate pass rates (first attempt vs retries)
- Agent usage frequency
- Failure patterns by type
- Time to resolution

### Metrics Commands
```
metrics summary              # Pipeline velocity stats
metrics failures             # Recent failures by type
metrics agents               # Agent usage stats
metrics trends               # Week-over-week comparison
```

---

## ⚠️ TASK COMPLETION VERIFICATION (MANDATORY)

**Before marking ANY task as complete, you MUST verify the pipeline was fully executed.**

### Completion Checklist (OUTPUT THIS AT END OF EVERY TASK)

```
═══════════════════════════════════════════════════════════════
PIPELINE COMPLETION VERIFICATION
═══════════════════════════════════════════════════════════════

PHASE STATUS:
[✓/✗/⊘] Phase 0: CLARIFY - Requirements clarified
[✓/✗/⊘] Phase 1: PLAN - Implementation planned
[✓/✗/⊘] Phase 1.5: CONTRACT - API contracts defined (if applicable)
[✓/✗/⊘] Phase 2: FOUNDATION - Schema/infra ready (if applicable)
[✓/✗/⊘] Phase 3: BUILD - Code implemented
[✓/✗/⊘] Phase 4: GATES - Quality gates passed
[✓/✗/⊘] Phase 5: CLEANUP - Dead code removed
[✓/✗/⊘] Phase 6: SHIP - Docs updated, PR open

MANDATORY CHECKS:
[ ] Tests written and passing (testing-agent)
[ ] Security review done (security-agent)
[ ] Code review passed (code-review-agent)
[ ] PR/MR opened for this branch
[ ] Session capture written to .claude/history/sessions (history-agent)
[ ] CONTEXT.md updated (context-builder) ← NEVER SKIP
[ ] README.md current (context-builder) ← NEVER SKIP
[ ] Decisions/learnings captured (memory-agent)
[ ] Post-merge hygiene planned: delete branch after merge

SKIPPED PHASES (requires explicit user approval):
- [List any skipped phases with approval reference]

═══════════════════════════════════════════════════════════════
```

### Incomplete Work Protocol

If you cannot complete all phases:
1. **DO NOT mark the task as done**
2. **Output the completion checklist showing what's incomplete**
3. **List what remains to be done**
4. **Ask user if they want to continue or stop here**

### Work Not Considered Complete Until:

```yaml
completion_requirements:
  - Tests exist and pass
  - Security review done
  - Code review grade ≥ B
  - History session captured (repo-local .claude/history if present)
  - CONTEXT.md updated for changed areas
  - README.md still accurate
  - No console.log/debug statements
  - No dead code
  - Decisions documented in memory
```

**Remember: Shipping incomplete work creates tech debt. It's better to do it right once than to fix it later.**
