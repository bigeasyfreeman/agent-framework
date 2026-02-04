# Claude Parallel Agents

**Agents with embedded maximum parallelism enforcement.**

These are Claude Code agents with the PARALLEL directive embedded directly in each agent's prompt, ensuring parallel-first execution is enforced automatically.

## What's Different

Each agent in `.claude/agents/` has the following directive embedded after "Core Identity":

```markdown
## 🚀 PARALLEL-FIRST EXECUTION (MANDATORY)

**Before ANY multi-step task:**
1. **Decompose** into atomic subtasks
2. **Check independence** — Can B start without A's output?
3. **If YES → Parallel** (single message, multiple Task calls)
4. **If NO → Sequential** (only when truly dependent)

**Threshold:** 3+ independent subtasks = MUST parallelize. No exceptions.

**Model Selection:**
- `haiku` — Simple checks, file reads (10-20x faster)
- `sonnet` — Standard analysis, implementation  
- `opus` — Deep reasoning only

**After parallel work:** Launch spotcheck agent to verify consistency.

**FORBIDDEN:**
- "Let me do these one at a time" — NO
- "For clarity, I'll handle sequentially" — NO
- Launching 1 agent when 5 could run parallel — NO

*Parallel is not optional. Parallel is the default.*
```

## Included Agents

Core agents with parallel enforcement:
- `Architect.md` — System design with parallel analysis
- `Engineer.md` — Implementation with parallel task execution
- `Intern.md` — Parallel grunt work specialist
- `Designer.md` — UX/UI with parallel review patterns
- `Pentester.md` — Security testing with parallel attack vectors
- `QATester.md` — QA with parallel test execution
- `ClaudeResearcher.md` / `GeminiResearcher.md` / `GrokResearcher.md` / `CodexResearcher.md` — Research with parallel topic coverage
- Plus: `coordinator`, `backend-agent`, `frontend-agent`, `infra-agent`, `plan-agent`, `qa-agent`, `researcher-agent`, `review-agent`, `security-agent`, `testing-agent`, `delegation-agent`, `context-builder`, `intake-agent`

## Installation

Copy `.claude/` to your project root:

```bash
cp -r templates/claude-parallel/.claude ~/your-project/
```

Or merge with existing `.claude/agents/`:

```bash
cp templates/claude-parallel/.claude/agents/* ~/.claude/agents/
```

## Standalone Directive

The directive is also available standalone at `.claude/directives/PARALLEL.md` for:
- Adding to CLAUDE.md as a global include
- Embedding in custom agents
- Reference documentation

## Usage

The agents will automatically enforce parallel execution. When given a multi-step task, they will:

1. Identify independent subtasks
2. Launch them in parallel (single message, multiple Task calls)
3. Use appropriate models (haiku for speed, sonnet for balance)
4. Run spotcheck after parallel completion

No additional configuration needed — parallelism is baked in.

---

*Based on PAI agent templates with parallel-first execution enforcement.*
