---
name: overlay-fastapi
description: Stack overlay for FastAPI/Pydantic/SQLAlchemy (async). Additive rules for agents working on Python APIs.
tools: Read
---

# FastAPI Overlay

Applies when `TECHSTACK.md` includes `fastapi` in `overlays`.

## Patterns
- Prefer Pydantic models at API boundaries; avoid untyped `dict` request bodies.
- Keep route handlers thin; move business logic into services.
- Validate path/query parameters with types/enums; avoid manual parsing.
- Use explicit timeouts for outbound HTTP (`httpx`) and handle retries intentionally.

## Red Flags
- Returning raw ORM models without serialization control.
- Blocking I/O in async endpoints (file reads, network calls) without `await`.
- Global mutable state in `api/` modules (non-idempotent imports).
- Catch-all `except Exception` without re-raising or structured error envelope.

## Verification
- Run the smallest relevant pytest scope (e.g., `pytest py-backend/tests/test_*.py -k <keyword>`).
- Confirm FastAPI validation errors return 422 with the expected envelope (if customized).

