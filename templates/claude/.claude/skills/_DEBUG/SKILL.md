---
name: debug
description: Start a systematic debugging session with structured diagnostic protocol
argument-hint: "<error or symptom description>"
---

# Debugging Session

Start a systematic debugging session following a structured diagnostic protocol.

## What This Skill Does

1. **Gathers symptoms** and error information
2. **Forms hypotheses** based on evidence
3. **Tests systematically** to isolate root cause
4. **Documents findings** for future reference

## Initial Interaction

```
Let's debug this systematically. Tell me:

1. **What's happening?** (Symptom/error message)
2. **What should happen?** (Expected behavior)
3. **When did it start?** (Recent changes?)
4. **How often?** (Always / Sometimes / Once)

What's the error or symptom you're seeing?
```

## Debugging Protocol

### Phase 1: Gather Evidence
- Exact error message (copy/paste)
- Stack trace if available
- Steps to reproduce
- Environment details (dev/prod, versions)
- Recent changes (git log, deploys)

### Phase 2: Form Hypotheses
Based on evidence, list likely causes:
1. Most likely: [hypothesis]
2. Possible: [hypothesis]
3. Less likely: [hypothesis]

### Phase 3: Test Hypotheses
For each hypothesis:
- Define test that would confirm/reject
- Execute test
- Record result
- Move to next if rejected

### Phase 4: Fix and Verify
- Implement fix
- Verify fix resolves issue
- Check for regressions
- Document root cause

## Output Format

```markdown
# Debugging Session: [Brief Description]

**Started**: [timestamp]
**Status**: Investigating / Root cause found / Resolved

---

## Symptoms

**Error**:
```
[Exact error message]
```

**Expected**: [What should happen]
**Actual**: [What happens instead]
**Reproducibility**: Always / Sometimes / Once
**Environment**: [Dev/Staging/Prod, versions]

---

## Recent Changes

| When | What Changed | Relevant? |
|------|--------------|-----------|
| [Date] | [Change] | Yes/No/Maybe |

---

## Hypotheses

### H1: [Most likely cause] - [TESTING/REJECTED/CONFIRMED]
**Why suspect**: [Reasoning]
**Test**: [How to verify]
**Result**: [What we found]

### H2: [Second possibility] - [TESTING/REJECTED/CONFIRMED]
**Why suspect**: [Reasoning]
**Test**: [How to verify]
**Result**: [What we found]

### H3: [Third possibility] - [TESTING/REJECTED/CONFIRMED]
**Why suspect**: [Reasoning]
**Test**: [How to verify]
**Result**: [What we found]

---

## Investigation Log

### [Timestamp] - [Action taken]
**Finding**: [What we learned]
**Next**: [What to try next]

### [Timestamp] - [Action taken]
**Finding**: [What we learned]
**Next**: [What to try next]

---

## Root Cause

**Identified**: [Yes/No/Partial]

[Description of root cause]

**Evidence**:
- [Evidence 1]
- [Evidence 2]

---

## Fix

**Approach**: [How we'll fix it]

**Changes**:
- [File:line] - [Change description]

**Verification**:
- [ ] Fix applied
- [ ] Original error no longer occurs
- [ ] No regressions introduced
- [ ] Tests pass

---

## Learnings

**Root Cause Pattern**: [What caused this]
**Prevention**: [How to prevent in future]
**Detection**: [How to catch earlier next time]

---

## Time Spent

| Phase | Duration |
|-------|----------|
| Gathering evidence | Xm |
| Forming hypotheses | Xm |
| Testing | Xm |
| Fixing | Xm |
| **Total** | **Xm** |
```

## Common Debug Patterns

### "It works on my machine"
- Check environment variables
- Check dependency versions
- Check file permissions
- Check network/firewall

### "It worked yesterday"
- `git log --since="yesterday"`
- Check deploy history
- Check dependency updates
- Check external service changes

### "It works sometimes"
- Race condition?
- Caching issue?
- External dependency flakiness?
- Resource limits?

### "No error, just wrong"
- Check input data
- Check business logic
- Check edge cases
- Add logging to trace flow

## Tools to Use

### Quick Checks
```bash
# Recent changes
git log --oneline -20

# What changed in a file
git diff HEAD~5 -- path/to/file

# Find where something is used
grep -r "functionName" --include="*.py"

# Check running processes
ps aux | grep [process]

# Check ports
lsof -i :8000
```

### Add Debugging Output
- Console.log / print statements
- Structured logging
- Debugger breakpoints
- Network inspection

## When to Escalate

- Debugging > 30 minutes without progress
- Issue involves external services you can't access
- Security implications discovered
- Need access/permissions you don't have

## Post-Debug

After resolving, consider:
- [ ] Add test to prevent regression
- [ ] Document root cause in code comment
- [ ] Update monitoring/alerting
- [ ] Share learning with team
- [ ] `/remember` the pattern for future
