# ISC Methodology — Think Before Acting

For significant tasks (multi-step, unclear requirements, spawning sub-agents), use this framework.

---

## When to Use

**USE IT:**
- Multi-step tasks (3+ steps)
- Building or creating something new
- Unclear or complex requirements
- Tasks Eric says are important

**SKIP IT:**
- Quick questions / lookups
- One-shot commands
- Status checks
- Casual conversation
- Tasks completable in <30 seconds

---

## The Process

### 1. OBSERVE — Extract Criteria
Parse the request into **Ideal State Criteria (ISC)**:
- Each criterion: 4-8 words, YES/NO answer
- Single fact per criterion
- Include **anti-criteria** (what we DON'T want)

**Format:**
```
[C1] API returns 200 status
[C2] Tests pass on CI
[A1] No hardcoded credentials
[A2] No breaking changes to public API
```

### 2. PLAN — Map to Actions
- Which criteria need sub-agents?
- Which can you handle directly?
- Dependencies? Parallel vs sequential?

### 3. EXECUTE — Track Progress
- Work through criteria
- Update status: PENDING → IN_PROGRESS → VERIFIED
- Discover new criteria → add them

### 4. VERIFY — Binary Check
Each criterion: YES or NO with evidence.
Report: X/Y criteria satisfied.

### 5. LEARN — Capture
Write significant learnings to `memory/YYYY-MM-DD.md`.

---

## Good vs Bad Criteria

**Good (granular, binary):**
```
[C1] Install script creates config file
[C2] Uninstall removes all artifacts
[A1] No manual editing required
```

**Bad (vague, multi-part):**
```
[C1] Everything works correctly     ← Not testable
[C2] System is fully integrated     ← Too vague
[C3] All features work properly     ← Multi-part
```

**The test:** Can I answer YES/NO in 1 second with evidence?

---

## ISC Tracker (optional)

For complex tasks, include at the end:
```
ISC TRACKER
Criteria:  4/6 satisfied
Anti:      2/2 avoided
Remaining: [C3] Tests pass, [C5] Docs updated
```
