# PAI Engineering Pipeline: Phases -1 to 6

A complete multi-agent development pipeline that takes work from intake to ship with quality gates, parallel execution, and continuous learning.

---

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

---

## Phase -1: INTAKE & TRIAGE

**Purpose:** Receive work requests, classify them, prevent duplicate effort, and right-size the pipeline.

### Agents

| Agent | Role | Outputs |
|-------|------|---------|
| **intake-agent** | First-touch triage and routing | Request classification, risk detection, pipeline entry point |
| **prior-work-agent** | Checks git history, merged PRs, existing code | Duplicate detection, regression prevention |
| **scope-analyzer-agent** | Analyzes task scope to determine which phases/agents needed | Pipeline right-sizing, prevents over-engineering |

### Flow
```
Request → intake-agent → prior-work-agent → scope-analyzer-agent → Phase 0
                ↓                ↓                    ↓
         Classification    Duplicate check      Pipeline config
```

### Key Outputs
- Request type (feature, bug, refactor, research)
- Risk level (low, medium, high)
- Duplicate/overlap detection
- Recommended pipeline phases to activate

---

## Phase 0: SPEC CLARIFICATION

**Purpose:** Ensure we build the right thing through adversarial review and spec finalization.

### Agents

| Agent | Role | Outputs |
|-------|------|---------|
| **product-agent** | Clarifies requirements, defines acceptance criteria | PRD, acceptance criteria, edge cases |
| **devil-agent** | Adversarial critic that challenges assumptions | Gaps, risks, stress-tested criteria |
| **judge-agent** | Synthesizes Product + Devil inputs into final spec | Implementable specification |

### Flow
```
                    ┌─────────────────┐
                    │  product-agent  │ ──→ Initial PRD
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │   devil-agent   │ ──→ Challenges & Gaps
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │   judge-agent   │ ──→ Final Spec
                    └─────────────────┘
```

### Key Outputs
- Product Requirements Document (PRD)
- Acceptance criteria (testable)
- Edge cases and error states
- Final implementable specification

---

## Phase 1: PLANNING & CONTRACTS

**Purpose:** Understand context, design architecture, define contracts, create implementation plan.

### Agents

| Agent | Role | Outputs |
|-------|------|---------|
| **context-scout-agent** | Mandatory repo discovery | Relevant files, patterns, tests, bounded context bundle |
| **plan-agent** | Creates implementation plans | Step-by-step plan with research and best practices |
| **architect** | System design with PhD-level expertise | Constitutional principles, feature specs, task breakdown |
| **api-contract-agent** | Owns API/interface contracts | API specs, data models, versioning |

### Flow
```
Spec → context-scout → plan-agent → architect → api-contract-agent → Phase 2
              ↓             ↓            ↓              ↓
        Context bundle    Plan      Architecture    Contracts
```

### Key Outputs
- Bounded context bundle (relevant code, patterns, tests)
- Implementation plan with phases
- Architectural decisions and principles
- API contracts (OpenAPI, TypeScript interfaces)
- Task breakdown with [P] parallelization markers

---

## Phase 2: FOUNDATION & SAFETY

**Purpose:** Establish data integrity, migration safety, and infrastructure guardrails before building.

### Agents

| Agent | Role | Outputs |
|-------|------|---------|
| **data-quality-agent** | Defines data invariants and validation | Data validation rules, consistency checks |
| **migration-agent** | Plans schema/data migrations | Migration scripts, rollback plans, cutover steps |
| **infra-policy-agent** | Reviews IaC for risk, cost, safety | Infrastructure guardrails, policy compliance |

### Flow
```
Contracts → data-quality → migration-agent → infra-policy → Phase 3
                 ↓               ↓               ↓
           Invariants      Migration plan    IaC review
```

### Key Outputs
- Data validation rules and invariants
- Migration scripts with rollback capability
- Infrastructure policy compliance
- Safety guardrails for build phase

---

## Phase 3: PARALLEL BUILD

**Purpose:** Implement the feature with specialized agents working in parallel where possible.

### Agents

| Agent | Role | Outputs |
|-------|------|---------|
| **coordinator** | Central orchestrator for pipeline | Task decomposition, agent assignment, feedback loops |
| **delegation-agent** | Manages parallel agent sessions | Parallel work distribution, maximum throughput |
| **engineer** | Elite principal engineer (TDD, constitutional) | Implementation code, tests |
| **frontend-agent** | UI/components/state management/accessibility | Frontend code, components |
| **backend-agent** | API/services/async patterns/data access | Backend code, services |
| **api-client-agent** | Generates API clients from contracts | Type-safe API clients |
| **feature-flag-agent** | Implements feature flags and rollout controls | Flag configuration, kill switches |
| **observability-agent** | Adds logs, metrics, traces | Instrumentation code |
| **ux-design-agent** | Ensures UI for every endpoint | User flows, frontend components |

### Flow
```
                              ┌──→ frontend-agent ──┐
                              │                     │
Plan + Contracts → coordinator ├──→ backend-agent  ──┼──→ Phase 3.5
        │                     │                     │
        ↓                     ├──→ api-client-agent ┤
   delegation-agent           │                     │
        │                     └──→ observability   ──┘
        ↓
   [Parallel Sessions]
```

### Parallelization Strategy
- **Independent components** run simultaneously
- **Dependent components** run sequentially
- **Spotcheck pattern** verifies parallel work
- **File reservation** prevents conflicts

### Key Outputs
- Implementation code (frontend + backend)
- Tests (contract, integration, e2e)
- API clients (type-safe)
- Feature flags
- Instrumentation (logs, metrics, traces)

---

## Phase 3.5: INTEGRATION & RECONCILIATION

**Purpose:** Merge parallel work, resolve conflicts, ensure interface alignment.

### Agents

| Agent | Role | Outputs |
|-------|------|---------|
| **integration-agent** | Merges parallel work, checks interfaces | Integrated codebase, resolved conflicts |
| **delta-compiler-agent** | Processes ADD/EDIT/KILL operations | Merged document changes |
| **review-coordinator** | Orchestrates multi-agent review | Aggregated findings, confidence scores |
| **file-reservation-agent** | Provides advisory locks for parallel editing | Lock coordination, conflict prevention |

### Flow
```
Parallel Outputs → file-reservation → delta-compiler → integration-agent → review-coordinator → Phase 4
                         ↓                 ↓                  ↓                   ↓
                   Lock resolution    Merge changes     Interface check    Confidence score
```

### Key Outputs
- Merged codebase from parallel work
- Resolved conflicts
- Interface/type alignment verification
- Confidence score for quality gates

---

## Phase 4: QUALITY GATES (Parallel)

**Purpose:** Comprehensive validation across 12+ dimensions before declaring work complete.

### Agents

| Agent | Focus Area | Gate |
|-------|------------|------|
| **code-review-agent** | Code quality, maintainability, readability | Mandatory |
| **ai-sast-agent** | Multi-category static analysis (taint, deps, OWASP, crypto) | Mandatory |
| **security-agent** | Threat modeling, OWASP Top 10, dependency patching | Mandatory |
| **testing-agent** | Test generation, coverage, CI/CD validation | Mandatory |
| **qa-agent** | E2E testing, user flow validation | Mandatory |
| **availability-agent** | Error boundaries, retry logic, graceful degradation | Mandatory |
| **a11y-agent** | Keyboard navigation, semantics, contrast | Mandatory |
| **perf-agent** | Latency, throughput, resource regressions | Mandatory |
| **dependency-agent** | License compliance, vulnerability checks | Mandatory |
| **privacy-agent** | PII exposure, logging redaction | Mandatory |
| **ui-validation-agent** | Layout, visual integrity, UX consistency | Frontend only |
| **ux-audit-agent** | Usability, discoverability, friction | User-facing only |
| **self-healing-agent** | Auto-retry and fix validation failures | On gate failure |

### Flow
```
                    ┌──→ code-review ──────┐
                    ├──→ ai-sast ──────────┤
                    ├──→ security ─────────┤
                    ├──→ testing ──────────┤
Integrated Code → ──├──→ qa ───────────────┼──→ Gate Results → Phase 5
                    ├──→ availability ─────┤         ↓
                    ├──→ a11y ─────────────┤    (if failures)
                    ├──→ perf ─────────────┤         ↓
                    ├──→ dependency ───────┤  self-healing-agent
                    ├──→ privacy ──────────┤         ↓
                    └──→ ui-validation ────┘    Retry (max N)
```

### Gate Failure Protocol
1. **self-healing-agent** attempts automatic fix (up to N iterations)
2. If auto-fix fails, route back to appropriate Phase 3 agent
3. Document failure pattern for learning capture

### Key Outputs
- Quality scores across all dimensions
- Security vulnerability report
- Test coverage report
- Accessibility compliance
- Performance benchmarks
- PASS/FAIL determination per gate

---

## Phase 5: CLEANUP

**Purpose:** Remove tech debt, dead code, unused dependencies before shipping.

### Agents

| Agent | Role | Outputs |
|-------|------|---------|
| **cleanup-agent** | Removes dead code, stale files, updates docs | Clean codebase |
| **flag-cleanup-agent** | Removes stale feature flags after rollout | Flag removal |
| **deps-cleanup-agent** | Removes unused dependencies, tidies lockfiles | Clean dependencies |

### Flow
```
Quality Gates Passed → cleanup-agent → flag-cleanup → deps-cleanup → Phase 6
                            ↓              ↓              ↓
                      Dead code        Old flags      Unused deps
                       removed          removed         removed
```

### Key Outputs
- Removed dead code and unused files
- Cleaned up feature flags
- Pruned unused dependencies
- Updated documentation (PRDs, READMEs)

---

## Phase 6: SHIP & LEARN

**Purpose:** Document the work, capture learnings, update metrics, enable continuous improvement.

### Agents

| Agent | Role | Outputs |
|-------|------|---------|
| **context-builder** | Maintains CONTEXT.md, README, docs | Updated documentation |
| **metrics-agent** | Tracks pipeline performance, gate failures, velocity | Analytics dashboard |
| **history-agent** | Captures session summaries, learnings, decisions | Searchable knowledge base |
| **learning-capture-agent** | Detects learnings from agent outputs | Learning entries |
| **compound-learning-agent** | Synthesizes patterns across learnings | Rule candidates |
| **self-improvement-agent** | Analyzes patterns to improve agent instructions | System improvements |

### Flow
```
                              ┌──→ context-builder ──→ Docs
                              │
Cleaned Code → history-agent ─┼──→ metrics-agent ────→ Analytics
                              │
                              └──→ learning-capture ──→ compound-learning ──→ self-improvement
                                                              ↓
                                                        Agent improvements
```

### Continuous Improvement Loop
1. **learning-capture-agent** extracts learnings from session
2. **compound-learning-agent** synthesizes patterns (triggers at 50+ learnings)
3. **self-improvement-agent** updates agent instructions
4. Improved agents perform better in future phases

### Key Outputs
- Updated CONTEXT.md and README files
- Session history and summaries
- Captured learnings
- Synthesized patterns
- Agent instruction improvements
- Pipeline performance metrics

---

## Cross-Phase Patterns

### Handoff Protocol
Each phase produces artifacts that the next phase consumes:
```
Phase N Output → Validation → Phase N+1 Input
```

### Truth Anchors
- **Phase 0:** Final spec from judge-agent
- **Phase 1:** API contracts from api-contract-agent
- **Phase 3.5:** Confidence score from review-coordinator
- **Phase 4:** Gate results (PASS/FAIL)

### Parallel vs Sequential
- **Parallel:** Independent agents within same phase
- **Sequential:** Phase dependencies (must complete Phase N before Phase N+1)

### Error Recovery
1. Gate failure → self-healing-agent attempts fix
2. Self-healing fails → route to appropriate build agent
3. Pattern captured → compound-learning updates system

---

## Agent Model Selection

| Phase | Recommended Model | Reason |
|-------|-------------------|--------|
| Phase -1 | haiku | Fast triage |
| Phase 0 | sonnet/opus | Spec quality matters |
| Phase 1 | opus | Architectural decisions |
| Phase 2 | sonnet | Standard work |
| Phase 3 | sonnet | Balanced build |
| Phase 3.5 | sonnet | Integration work |
| Phase 4 | haiku/sonnet | Parallel gates |
| Phase 5 | haiku | Cleanup tasks |
| Phase 6 | haiku | Documentation |

---

## Quick Start

### Minimal Pipeline (Small Tasks)
```
intake → scope-analyzer → engineer → testing → cleanup
```

### Standard Pipeline (Features)
```
intake → product → plan → engineer + frontend + backend → integration → quality gates → cleanup → context-builder
```

### Full Pipeline (Complex Features)
All phases activated, all agents engaged.

---

## Key Principles

1. **Right-size the pipeline** - scope-analyzer prevents over-engineering
2. **Spec before build** - devil-agent catches gaps early
3. **Contracts before code** - api-contract-agent ensures alignment
4. **Parallel where possible** - delegation-agent maximizes throughput
5. **Gates are mandatory** - no skipping quality validation
6. **Learn from everything** - compound-learning improves the system

---

*This pipeline enables teams to ship high-quality code with confidence through systematic validation and continuous improvement.*
