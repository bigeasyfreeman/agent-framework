# Stack Overlays

This directory holds **stack‑specific supplements** to the core, tech‑agnostic agents.

## How to Use
1. Core agents avoid assuming any framework.
2. When `TECHSTACK.md` lists overlays (e.g., `nextjs`, `fastapi`), the coordinator and relevant agents must read the matching overlay file and apply its rules.
   - Prefer project-local overlays at `.claude/agents/overlays/<name>.md`
   - Fall back to global overlays at `~/.claude/agents/overlays/<name>.md`

## Overlay Rules
- Only include stack‑specific patterns, commands, and red flags.
- Never duplicate core guidance.
- Keep overlays small and additive.

## Example

`TECHSTACK.md`:
```yaml
overlays:
  - nextjs
  - fastapi
```

Agents then read:
- `.claude/agents/overlays/nextjs.md` (preferred)
- `.claude/agents/overlays/fastapi.md` (preferred)
- `~/.claude/agents/overlays/nextjs.md` (fallback)
- `~/.claude/agents/overlays/fastapi.md` (fallback)
