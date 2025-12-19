---
name: overlay-nextjs
description: Stack overlay for Next.js App Router + React + Tailwind. Additive rules for frontend work.
tools: Read
---

# Next.js Overlay

Applies when `TECHSTACK.md` includes `nextjs` in `overlays`.

## Patterns
- Prefer server components by default; add `"use client"` only when needed.
- Keep data fetching patterns consistent (follow existing `apps/web` conventions).
- Use stable component boundaries: UI components in `apps/web/src/components`, route/page in `apps/web/src/app`.
- Prefer Tailwind utility classes + `clsx`/`tailwind-merge` over ad-hoc CSS.

## Red Flags
- Nested layout shells (duplicate wrappers) in App Router.
- Client components that accidentally pull server-only modules.
- Missing loading/error states for async UI flows.
- Silent catch blocks that hide user-visible failures.

## Verification
- Run `pnpm --filter @compass/web test` for changed UI logic.
- Run `pnpm --filter @compass/web lint` for Next.js lint rules.

