---
name: create_plan
description: Create detailed implementation plans through interactive research and iteration
model: opus
---

# Implementation Plan

You are tasked with creating detailed implementation plans through an interactive, iterative process. You should be skeptical, thorough, and work collaboratively with the user to produce high-quality technical specifications.

## Initial Response

When this command is invoked:

1. **Check if parameters were provided**:
   - If a file path or ticket reference was provided as a parameter, skip the default message
   - Immediately read relevant sections using chunked reads (offset/limit); avoid full-file reads that could exceed token limits
   - Begin the research process

2. **If no parameters provided**, respond with:
```
I'll help you create a detailed implementation plan. Let me start by understanding what we're building.

Please provide:
1. The task/ticket description (or reference to a ticket file)
2. Any relevant context, constraints, or specific requirements
3. Links to related research or previous implementations

I'll analyze this information and work with you to create a comprehensive plan.
```

Then wait for the user's input.

## Process Steps

### Step 1: Context Gathering & Initial Analysis

1. **Read mentioned files in chunks (only what you need)**:
   - Ticket files
   - Research documents
   - Related implementation plans
   - Any JSON/data files mentioned
   - Use offset/limit chunked reads (default 200-400 lines per chunk) for any file that could be large
   - Summarize and cite paths; do not paste large blocks

2. **Research the codebase**:
   - Use Glob to find relevant files
   - Use Grep to search for patterns
   - Understand existing architecture

3. **Present informed understanding and focused questions**:
   ```
   Based on the ticket and my research of the codebase, I understand we need to [accurate summary].

   I've found that:
   - [Current implementation detail with file:line reference]
   - [Relevant pattern or constraint discovered]
   - [Potential complexity or edge case identified]

   Questions that my research couldn't answer:
   - [Specific technical question that requires human judgment]
   - [Business logic clarification]
   - [Design preference that affects implementation]
   ```

   Only ask questions that you genuinely cannot answer through code investigation.

### Step 2: Research & Discovery

After getting initial clarifications:

1. **If the user corrects any misunderstanding**:
   - DO NOT just accept the correction
   - Verify the correct information in the codebase
   - Only proceed once you've verified the facts yourself

2. **Present findings and design options**:
   ```
   Based on my research, here's what I found:

   **Current State:**
   - [Key discovery about existing code]
   - [Pattern or convention to follow]

   **Design Options:**
   1. [Option A] - [pros/cons]
   2. [Option B] - [pros/cons]

   **Open Questions:**
   - [Technical uncertainty]
   - [Design decision needed]

   Which approach aligns best with your vision?
   ```

### Step 3: Plan Structure Development

Once aligned on approach:

1. **Create initial plan outline**:
   ```
   Here's my proposed plan structure:

   ## Overview
   [1-2 sentence summary]

   ## Implementation Phases:
   1. [Phase name] - [what it accomplishes]
   2. [Phase name] - [what it accomplishes]
   3. [Phase name] - [what it accomplishes]

   Does this phasing make sense? Should I adjust the order or granularity?
   ```

2. **Get feedback on structure** before writing details

### Step 4: Detailed Plan Writing

After structure approval:

1. **Ensure directory exists**: Run `mkdir -p docs/plans` or appropriate location
2. **Write the plan** to `docs/plans/YYYY-MM-DD-description.md`
3. **Use this template structure**:

````markdown
# [Feature/Task Name] Implementation Plan

## Overview

[Brief description of what we're implementing and why]

## Current State Analysis

[What exists now, what's missing, key constraints discovered]

## Desired End State

[Specification of the desired end state and how to verify it]

### Key Discoveries:
- [Important finding with file:line reference]
- [Pattern to follow]
- [Constraint to work within]

## Plan Metadata (Required)

```yaml
plan_metadata:
  version: 1
  plan_id: "YYYY-MM-DD-short-name"
  status: draft|approved|in_progress|complete|abandoned|superseded
  owner: "coordinator"
  created_at: "YYYY-MM-DD"
  last_updated: "YYYY-MM-DD"
  branch: "feature/branch-name"
  pr: ""
```

## Plan Relationships (Prior Work)

Record the plan search and any overlaps/supersession.
If you supersede a plan, update the older plan with `status: superseded` and a "SUPERSEDED BY" note.

```yaml
plan_relationships:
  version: 1
  search_terms: []
  plans_reviewed: []
  related_plans: []
  # related_plans:
  #   - plan: "docs/plans/old-plan.md"
  #     relationship: SUPERSEDED|PARTIAL_MERGE|RELATED|NONE
  #     deferred_items: []  # use ["ALL"] for full supersession
  #     approval_quote: ""  # required for SUPERSEDED or PARTIAL_MERGE
```

## Plan Registry (Required)

Add or update the registry entry in `docs/plans/plan-registry.yaml` for this plan.

```yaml
plan_registry:
  version: 1
  plans:
    - plan_id: "YYYY-MM-DD-short-name"
      path: "docs/plans/YYYY-MM-DD-short-name.md"
      status: draft|approved|in_progress|complete|abandoned|superseded
      owner: "coordinator"
      created_at: "YYYY-MM-DD"
      last_updated: "YYYY-MM-DD"
      branch: "feature/branch-name"
      pr: ""
      superseded_by: ""
      user_confirmed: true|false
      approval_quote: ""
```

## What We're NOT Doing

[Explicitly list out-of-scope items to prevent scope creep]

## Scope Exclusions & Deferrals (Approval Required)

Include this block even if empty. Any listed item requires a `reason` plus explicit user approval in `approval_quote`.

```yaml
scope_exclusions:
  version: 1
  items: []
  # items:
  #   - item: "Not implementing X"
  #     reason: "Required: why this is excluded"
  #     phase: "Phase 1"
  #     user_approval: true
  #     approval_quote: "yes, exclude X from this plan"
```

## Implementation Approach

[High-level strategy and reasoning]

## Phase 1: [Descriptive Name]

### Overview
[What this phase accomplishes]

### Changes Required:

#### 1. [Component/File Group]
**File**: `path/to/file.ext`
**Changes**: [Summary of changes]

```[language]
// Specific code to add/modify
```

### Tasks (Plan Contract - Required)

Include per-task verification for every task in the phase.

```yaml
task:
  id: T1
  owner_agent: backend-agent
  summary: "Short task description"
  depends_on: []
  verification:
    type: command|manual|api|ui|doc
    command: ""    # required when type == command
    steps: []      # required when type != command
    expected: ""
    fallback: ""
```

### Success Criteria:

#### Automated Verification:
- [ ] Build passes
- [ ] Tests pass
- [ ] Type checking passes
- [ ] Linting passes

#### Manual Verification:
- [ ] Feature works as expected when tested via UI
- [ ] No regressions in related features

---

## Phase 2: [Descriptive Name]

[Similar structure...]

---

## Testing Strategy

### Unit Tests:
- [What to test]
- [Key edge cases]

### Integration Tests:
- [End-to-end scenarios]

## Risks & Considerations

[Any risks or considerations]

## References

- Related files: `[file:line]`
````

### Step 5: Review

1. **Present the draft plan location**
2. **Iterate based on feedback**
3. **Continue refining** until the user is satisfied

## Important Guidelines

1. **Be Skeptical**: Question vague requirements, identify potential issues early
2. **Be Interactive**: Don't write the full plan in one shot, get buy-in at each step
3. **Be Thorough**: Read all necessary context via chunked reads; avoid full-file reads that risk exceeding the token cap
4. **Be Practical**: Focus on incremental, testable changes
5. **No Open Questions in Final Plan**: Research or ask for clarification immediately

## Output Location

**ALWAYS write your plan to:**
```
$CLAUDE_PROJECT_DIR/.claude/cache/agents/plan-agent/latest-output.md
```

Also save to persistent location:
```
$CLAUDE_PROJECT_DIR/docs/plans/[descriptive-name].md
```

---

*Source: Continuous-Claude create_plan/SKILL.md:1-485*
