# PARALLEL.md — Maximum Parallelism Directive

**This directive enforces parallel-first execution. Embed in agents or include in CLAUDE.md.**

---

## 🚀 PARALLEL-FIRST EXECUTION (MANDATORY)

**Before executing ANY multi-step task, you MUST:**

1. **Decompose** — Break the task into atomic subtasks
2. **Identify Independence** — Which subtasks have NO dependencies on each other?
3. **Parallelize** — Launch ALL independent subtasks simultaneously via Task tool
4. **Sequence Only When Required** — Only execute sequentially if output of A is input to B

### The Parallel Test

For every task, ask:
> "Can I start subtask B without waiting for subtask A to complete?"

If YES → Launch them in parallel (single message, multiple Task calls)
If NO → They must be sequential

### Minimum Parallel Threshold

**If a task has 3+ independent subtasks, you MUST parallelize.**

No exceptions. No "I'll do them one by one for clarity." Parallel is the default.

---

## Execution Pattern

### ❌ WRONG — Sequential (Slow)

```
Task 1: Research competitor A → wait → 
Task 2: Research competitor B → wait → 
Task 3: Research competitor C → wait → 
Synthesize
```

### ✅ RIGHT — Parallel (Fast)

```
[Single message with 3 Task calls]:
  Task 1: Research competitor A
  Task 2: Research competitor B  
  Task 3: Research competitor C
→ All complete →
Synthesize
```

---

## Model Selection for Parallel Work

**Speed matters in parallel execution. Choose wisely:**

| Subtask Type | Model | Rationale |
|--------------|-------|-----------|
| Simple checks, file reads, lookups | `haiku` | 10-20x faster |
| Standard analysis, implementation | `sonnet` | Balanced |
| Deep reasoning, architecture | `opus` | When intelligence > speed |

**5 haiku agents > 1 opus agent doing sequential work** (faster AND cheaper)

---

## Spotcheck Pattern (REQUIRED)

After parallel work completes, ALWAYS launch a spotcheck agent:

```typescript
Task({
  prompt: "Verify consistency and completeness across all outputs: [results]",
  subagent_type: "Intern",
  model: "haiku"
})
```

---

## Common Parallelizable Patterns

| Task Type | Parallel Approach |
|-----------|-------------------|
| Research N topics | N agents, one per topic |
| Analyze N files | N agents, one per file |
| Test N approaches | N agents, one per approach |
| Process N items | N agents (or batched if >10) |
| Multi-perspective analysis | N agents with different viewpoints |
| Competitive analysis | N agents, one per competitor |

---

## Anti-Patterns (FORBIDDEN)

1. **"Let me do these one at a time"** — NO. Parallelize.
2. **"For clarity, I'll handle each sequentially"** — NO. Clarity comes from synthesis, not sequencing.
3. **"I'll start with X, then move to Y"** — ONLY if Y depends on X's output.
4. **Launching 1 agent when you could launch 5** — FORBIDDEN.

---

## Verification Checklist

Before completing any task, confirm:

- [ ] I identified all subtasks
- [ ] I checked dependencies between subtasks
- [ ] I launched independent subtasks in parallel (single message, multiple Task calls)
- [ ] I used appropriate models (haiku for grunt work)
- [ ] I ran a spotcheck after parallel completion

**If you executed 3+ subtasks sequentially that could have been parallel, you failed this directive.**

---

*Parallel is not optional. Parallel is the default.*
