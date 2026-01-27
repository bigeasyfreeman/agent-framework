# Multi-Agent Engineering Framework

A **high-velocity, multi-agent development pipeline** with 86 specialized agents, quality gates, and continuous learning. Takes work from intake to ship with systematic validation at every phase.

## What This Is

This framework provides:

- **86 specialized agents** coordinated across 8 development phases
- **THE ALGORITHM** - A universal 7-phase execution engine (OBSERVE → THINK → PLAN → BUILD → EXECUTE → VERIFY → LEARN)
- **Quality gates** that catch issues before they ship
- **Parallel execution** for maximum velocity
- **Continuous learning** that improves the system over time

## Pipeline Overview

```
Phase -1    Phase 0      Phase 1       Phase 2        Phase 3         Phase 3.5      Phase 4           Phase 5      Phase 6
INTAKE  →   SPEC    →    PLAN     →   FOUNDATION  →   BUILD      →   INTEGRATE  →   QUALITY GATES  →  CLEANUP  →   SHIP
   ↓          ↓            ↓             ↓              ↓               ↓               ↓               ↓           ↓
intake    product      context      data-quality    engineer      integration    code-review      cleanup     context-builder
prior     devil        plan         migration       frontend      delta          security         flag        metrics
scope     judge        architect    infra-policy    backend       review-coord   testing          deps        history
                       api-contract                 coordinator   file-reserve   qa, a11y, perf              learning
                                                    delegation                   availability                 self-improve
```

## Quick Start

### Installation

Install the framework into an existing repo:

```bash
python3 tools/install.py --adapter claude --target /path/to/your/repo
```

This copies:
- `CLAUDE.md` → Your repo root (agent instructions)
- `.claude/agents/` → 86 specialized agents
- `.claude/skills/` → THE ALGORITHM and supporting skills
- `.claude/workflows/` → Delegation patterns

### Usage

The pipeline activates automatically based on work type:

| Work Type | Pipeline | Agents Activated |
|-----------|----------|------------------|
| New feature | Full (Phases -1 to 6) | All applicable |
| Bug fix | Phases -1, 0.5, 3-6 | context-scout, engineer, gates, cleanup |
| Refactor | Phases -1, 0.5, 1, 3-6 | context-scout, plan, engineer, gates |
| Docs only | Phases -1, 6 | intake, context-builder |

### THE ALGORITHM

For complex tasks, THE ALGORITHM provides structured execution:

```
1. OBSERVE  → Gather context, understand state
2. THINK    → Analyze, form hypotheses
3. PLAN     → Create execution strategy
4. BUILD    → Implement with appropriate agents
5. EXECUTE  → Run, test, integrate
6. VERIFY   → Quality gates, validation
7. LEARN    → Capture insights, improve
```

Invoke with: "run the algorithm" or "algorithm effort STANDARD: [task]"

## Phase Details

### Phase -1: INTAKE & TRIAGE
- **intake-agent**: Classifies requests, detects risk
- **prior-work-agent**: Prevents duplicate effort
- **scope-analyzer-agent**: Right-sizes the pipeline

### Phase 0: SPEC CLARIFICATION
- **product-agent**: Defines requirements, acceptance criteria
- **devil-agent**: Adversarial review, finds gaps
- **judge-agent**: Synthesizes final spec

### Phase 1: PLANNING & CONTRACTS
- **context-scout-agent**: Discovers relevant code/patterns
- **plan-agent**: Creates implementation plan
- **architect**: System design, constitutional principles
- **api-contract-agent**: Defines API interfaces

### Phase 2: FOUNDATION
- **data-quality-agent**: Data invariants, validation
- **migration-agent**: Schema migrations, rollback plans
- **infra-policy-agent**: Infrastructure guardrails

### Phase 3: PARALLEL BUILD
- **coordinator**: Orchestrates all build agents
- **delegation-agent**: Manages parallel execution
- **engineer**: Core implementation (TDD)
- **frontend-agent**: UI components, accessibility
- **backend-agent**: APIs, services, data access
- **ai-agent**: LLM integration, prompts

### Phase 3.5: INTEGRATION
- **integration-agent**: Merges parallel work
- **delta-compiler-agent**: Reconciles changes
- **review-coordinator**: Aggregates findings

### Phase 4: QUALITY GATES (12+ parallel)
- **code-review-agent**: Quality, maintainability
- **security-agent**: Threat modeling, OWASP
- **ai-sast-agent**: Static analysis
- **testing-agent**: Tests, coverage
- **qa-agent**: E2E validation
- **availability-agent**: Error handling, resilience
- **a11y-agent**: Accessibility
- **perf-agent**: Performance
- **dependency-agent**: License, vulnerabilities
- **privacy-agent**: PII, data handling
- **self-healing-agent**: Auto-fix failures

### Phase 5: CLEANUP
- **cleanup-agent**: Dead code, stale files
- **flag-cleanup-agent**: Old feature flags
- **deps-cleanup-agent**: Unused dependencies

### Phase 6: SHIP & LEARN
- **context-builder**: Documentation updates
- **metrics-agent**: Pipeline analytics
- **history-agent**: Session capture
- **learning-capture-agent**: Extract insights
- **compound-learning-agent**: Pattern synthesis
- **self-improvement-agent**: System evolution

## Agent Model Selection

Choose the right model for the task:

| Task Type | Model | Why |
|-----------|-------|-----|
| Grunt work, verification | `haiku` | 10-20x faster |
| Implementation, analysis | `sonnet` | Balanced |
| Architecture, reasoning | `opus` | Maximum intelligence |

## Delegation Patterns

### Parallel Execution
```typescript
// Launch multiple agents in ONE message
Task({ prompt: "Build auth UI", subagent_type: "frontend-agent", model: "sonnet" })
Task({ prompt: "Build auth API", subagent_type: "backend-agent", model: "sonnet" })
Task({ prompt: "Build auth tests", subagent_type: "testing-agent", model: "haiku" })
```

### Spotcheck Pattern
Always verify parallel work:
```typescript
Task({
  prompt: "Verify auth implementation is complete and consistent",
  subagent_type: "qa-agent",
  model: "haiku"
})
```

## What's Included

```
templates/claude/
├── CLAUDE.md                    # Agent framework instructions
├── .claude/
│   ├── agents/                  # 86 specialized agents
│   │   ├── intake-agent.md
│   │   ├── product-agent.md
│   │   ├── engineer.md
│   │   ├── ... (83 more)
│   │   └── overlays/            # Stack-specific customizations
│   ├── skills/
│   │   ├── THEALGORITHM/        # Universal execution engine
│   │   ├── _CREATE_PLAN/        # Planning skill
│   │   ├── _DEBUG/              # Debugging skill
│   │   └── Agents/              # Agent composition
│   ├── workflows/
│   │   └── Delegation.md        # Parallel execution patterns
│   ├── evals/                   # Behavioral evaluations
│   └── scripts/
│       └── agent_audit.sh       # Audit helper
├── ENGINEERING_PIPELINE.md      # Complete pipeline documentation
tools/
├── install.py                   # Installation script
└── export_from_claude_home.py   # Safe export utility
```

## What's NOT Included (Intentionally)

For safety, these are excluded:
- Chat history (`~/.claude/history*`, `~/.claude/projects/`)
- Settings (`~/.claude/settings.json`)
- Telemetry (`~/.claude/telemetry/`)
- Session transcripts

Use `tools/export_from_claude_home.py` for safe exports.

## Extending the Framework

### Adding Stack Overlays
Create stack-specific customizations in `.claude/agents/overlays/`:
```
overlays/
├── nextjs.md      # Next.js patterns
├── fastapi.md     # FastAPI patterns
└── README.md      # Overlay documentation
```

### Creating New Agents
Add new agents to `.claude/agents/` following the pattern:
```markdown
---
name: my-agent
description: What this agent does
model: sonnet
---

# Agent Instructions

## When to Use
- Trigger conditions

## How to Work
- Methodology

## Outputs
- Expected deliverables
```

### Adding Adapters
For non-Claude runtimes, add `templates/<runtime>/` mapping the same concepts.

## Key Principles

1. **Right-size the pipeline** - scope-analyzer prevents over-engineering
2. **Spec before build** - devil-agent catches gaps early
3. **Contracts before code** - api-contract-agent ensures alignment
4. **Parallel where possible** - delegation-agent maximizes throughput
5. **Gates are mandatory** - no skipping quality validation
6. **Learn from everything** - compound-learning improves the system

## Attribution

If you reuse this framework, please retain copyright/license notices and link back.

## License

Apache-2.0 (see `LICENSE` and `NOTICE`)

---

*Ship high-quality code with confidence through systematic validation and continuous improvement.*
