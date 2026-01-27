---
name: Agents
description: Dynamic agent composition and management system. USE WHEN you need specialized agents, parallel work, or custom expertise combinations.
---

# Agents - Agent Composition System

## Overview

The Agents skill manages agent composition and orchestration:
- Compose dynamic agents from traits (expertise + personality + approach)
- Spawn parallel agents for divide-and-conquer work
- Select appropriate models for task complexity

## Agent Types

| Type | Definition | Best For |
|------|------------|----------|
| **Named Agents** | Pre-configured specialists (Engineer, Architect, QATester) | Recurring work, specialized expertise |
| **Dynamic Agents** | Task-specific agents composed from traits | One-off tasks, novel combinations |

## Using Named Agents

```typescript
Task({
  subagent_type: "Engineer",
  prompt: "Implement the user authentication feature...",
  model: "sonnet"
})
```

**Available Agents:**
- `Engineer` - TDD implementation, battle-tested patterns
- `Architect` - System design, trade-off analysis
- `QATester` - Browser validation, quality gates
- `backend-agent` - API design, services
- `frontend-agent` - UI components, state
- `security-agent` - AppSec, OWASP Top 10
- `data-agent` - Database design, migrations
- `sre-agent` - Infrastructure, reliability

## Composing Dynamic Agents

When you need a specific expertise combination:

**Traits Available:**

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
| Creative content development | creative, enthusiastic, exploratory |
| Red team critique | contrarian, skeptical, adversarial, bold |
| Quick business assessment | business, pragmatic, rapid, comparative |

## Model Selection (CRITICAL)

| Task Type | Model | Speed |
|-----------|-------|-------|
| Grunt work, verification | `haiku` | 10-20x faster |
| Standard implementation | `sonnet` | Balanced |
| Deep reasoning, architecture | `opus` | Maximum intelligence |

**Rule:** Parallel agents especially benefit from `haiku` for speed.

## Parallel Execution

Spawn multiple agents in ONE message for parallel work:

```typescript
// All run simultaneously
Task({ subagent_type: "Intern", prompt: "Research company A...", model: "haiku" })
Task({ subagent_type: "Intern", prompt: "Research company B...", model: "haiku" })
Task({ subagent_type: "Intern", prompt: "Research company C...", model: "haiku" })
```

**Spotcheck Pattern:** Always launch a spotcheck agent after parallel work to verify consistency.

## Task Prompt Requirements

When delegating, ALWAYS include:

1. **WHY** - Business context, why this matters
2. **WHAT** - Current state, existing implementation
3. **EXACTLY** - Precise actions, file paths, patterns
4. **SUCCESS CRITERIA** - What good output looks like

```typescript
Task({
  subagent_type: "Engineer",
  prompt: `
    ## Context
    We're adding dark mode. Users have requested this feature.

    ## Current State
    Theme is in src/theme/, uses CSS variables.

    ## Task
    1. Add dark mode toggle to settings page
    2. Persist preference to localStorage
    3. Apply theme on page load

    ## Success Criteria
    - Toggle works in browser
    - Theme persists across refresh
    - No flash of wrong theme on load
  `,
  model: "sonnet"
})
```
