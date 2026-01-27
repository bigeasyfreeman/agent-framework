# Delegation Workflow

Comprehensive guide to delegating tasks to agents for parallel and specialized work.

## Agent Types

| Type | Definition | Best For |
|------|------------|----------|
| **Named Agents** | Pre-configured specialists (Engineer, Architect, QATester) | Recurring work, specialized expertise |
| **Dynamic Agents** | Task-specific agents composed from traits | One-off tasks, novel combinations, parallel grunt work |

## Named Agents

| Agent | Specialty | Use When... |
|-------|-----------|-------------|
| Engineer | TDD, implementation | "implement", "build", "code" |
| Architect | System design | "design the system", "architecture" |
| QATester | Browser validation | "test", "validate", "verify" |
| Intern | General-purpose | Parallel tasks, grunt work |
| Explore | Codebase navigation | "find", "search", "explore code" |

## Dynamic Agent Composition

When you need a specific expertise combination, compose from traits:

**Expertise** (domain knowledge):
- security, legal, finance, medical, technical
- research, creative, business, data, communications

**Personality** (behavior style):
- skeptical, enthusiastic, cautious, bold, analytical
- creative, empathetic, contrarian, pragmatic, meticulous

**Approach** (work style):
- thorough, rapid, systematic, exploratory
- comparative, synthesizing, adversarial, consultative

**Example Compositions:**

| Need | Traits |
|------|--------|
| Security architecture review | security, skeptical, thorough, adversarial |
| Legal contract review | legal, cautious, meticulous, systematic |
| Quick business assessment | business, pragmatic, rapid, comparative |
| Red team critique | contrarian, skeptical, adversarial, bold |

---

## Model Selection (CRITICAL FOR SPEED)

| Task Type | Model | Why |
|-----------|-------|-----|
| Deep reasoning, architecture | `opus` | Maximum intelligence |
| Standard implementation, analysis | `sonnet` | Balanced |
| Simple checks, parallel grunt work | `haiku` | 10-20x faster |

```typescript
// WRONG - defaults to expensive/slow
Task({ prompt: "Check if file exists", subagent_type: "Intern" })

// RIGHT - Haiku for simple task
Task({ prompt: "Check if file exists", subagent_type: "Intern", model: "haiku" })
```

**Rule of Thumb:**
- Grunt work or verification → `haiku`
- Implementation or research → `sonnet`
- Strategic/architectural → `opus`

---

## Foreground Delegation

Standard blocking delegation - waits for agent to complete.

### Single Agent

```typescript
Task({
  description: "Research competitor",
  prompt: "Investigate Acme Corp's recent product launches...",
  subagent_type: "Engineer",
  model: "sonnet"
})
// Blocks until complete, returns result
```

### Parallel Agents

**ALWAYS use a single message with multiple Task calls for parallel work:**

```typescript
// Send as SINGLE message with multiple tool calls
Task({
  description: "Research company A",
  prompt: "Investigate Company A...",
  subagent_type: "Intern",
  model: "haiku"
})
Task({
  description: "Research company B",
  prompt: "Investigate Company B...",
  subagent_type: "Intern",
  model: "haiku"
})
Task({
  description: "Research company C",
  prompt: "Investigate Company C...",
  subagent_type: "Intern",
  model: "haiku"
})
// All run in parallel, all results returned together
```

### Spotcheck Pattern

**ALWAYS launch a spotcheck agent after parallel work:**

```typescript
// After parallel agents complete
Task({
  description: "Spotcheck parallel results",
  prompt: "Review these results for consistency and completeness: [results]",
  subagent_type: "Intern",
  model: "haiku"
})
```

---

## Background Delegation

Non-blocking delegation - agents run while you continue working.

```typescript
Task({
  description: "Background research",
  prompt: "Research X...",
  subagent_type: "Intern",
  model: "haiku",
  run_in_background: true  // Returns immediately
})
// Returns { agent_id: "abc123", status: "running" }

// Check later
TaskOutput({ agentId: "abc123", block: false })

// Retrieve when ready
TaskOutput({ agentId: "abc123", block: true })
```

---

## Decision Matrix

### Foreground vs Background

| Situation | Choice | Reason |
|-----------|--------|--------|
| Need results immediately | Foreground | Blocking is fine |
| Have other work to do | Background | Don't want to wait |
| 3+ parallel tasks | Background | More flexible |
| Single quick task | Foreground | Simpler |

---

## Full Context Requirements

When delegating, ALWAYS include:

1. **WHY** - Business context, why this matters
2. **WHAT** - Current state, existing implementation
3. **EXACTLY** - Precise actions, file paths, patterns
4. **SUCCESS CRITERIA** - What good output looks like

```typescript
Task({
  description: "Audit auth security",
  prompt: `
    ## Context
    We're preparing for SOC 2 audit. Need to verify our auth implementation.

    ## Current State
    Auth is in src/auth/, uses JWT with refresh tokens.

    ## Task
    1. Review all auth-related code
    2. Check for OWASP Top 10 vulnerabilities
    3. Verify token handling is secure
    4. Check for timing attacks in password comparison

    ## Success Criteria
    - Comprehensive security assessment
    - Specific file:line references for any issues
    - Severity ratings for each finding
    - Remediation recommendations
  `,
  subagent_type: "Engineer",
  model: "sonnet"
})
```
