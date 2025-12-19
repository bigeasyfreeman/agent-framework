#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$REPO_ROOT"

fail=0
warn=0

say_ok() { printf "OK   %s\n" "$1"; }
say_warn() {
  printf "WARN %s\n" "$1"
  warn=1
}
say_fail() {
  printf "FAIL %s\n" "$1"
  fail=1
}

check_file() {
  local path="$1"
  if [[ -f "$path" ]]; then
    say_ok "$path"
  else
    say_fail "Missing file: $path"
  fi
}

check_dir() {
  local path="$1"
  if [[ -d "$path" ]]; then
    say_ok "$path/"
  else
    say_fail "Missing dir: $path/"
  fi
}

echo "AGENT AUDIT"
echo "repo_root: $REPO_ROOT"
echo

check_file "CLAUDE.md"
check_file "TECHSTACK.md"
check_file ".claude/agents/coordinator.md"
check_file ".claude/agents/history-agent.md"

echo
check_dir ".claude/history"
check_dir ".claude/history/sessions"
check_dir ".claude/history/learnings"
check_dir ".claude/history/decisions"
check_dir ".claude/history/features"
check_dir ".claude/history/bugs"
check_dir ".claude/history/research"
check_dir ".claude/history/raw-outputs"

echo
if command -v git >/dev/null 2>&1 && git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  base_ref=""
  if git show-ref --verify --quiet refs/remotes/origin/main; then
    base_ref="origin/main"
  elif git show-ref --verify --quiet refs/remotes/origin/master; then
    base_ref="origin/master"
  elif git show-ref --verify --quiet refs/heads/main; then
    base_ref="main"
  elif git show-ref --verify --quiet refs/heads/master; then
    base_ref="master"
  fi

  if [[ -z "$base_ref" ]]; then
    say_warn "No origin/main, origin/master, main, or master ref found; skipping history capture enforcement"
  else
    # Enforce that any shippable change includes a session capture under .claude/history/sessions/.
    # This checks committed changes (vs base), staged changes, unstaged changes, and untracked files.
    all_changes="$(
      {
        git diff --name-only "$base_ref"...HEAD || true
        git diff --name-only --cached || true
        git diff --name-only || true
        git ls-files --others --exclude-standard || true
      } 2>/dev/null \
        | sed '/^$/d' \
        | sort -u
    )"

    if [[ -z "$all_changes" ]]; then
      say_ok "No repo changes detected (history capture not required)"
    else
      non_history_changes="$(printf '%s\n' "$all_changes" | grep -Ev '^\\.claude/history/' || true)"
      session_changes="$(printf '%s\n' "$all_changes" | grep -E '^\\.claude/history/sessions/' || true)"

      if [[ -n "$non_history_changes" && -z "$session_changes" ]]; then
        say_fail "Repo changes detected but no session capture in .claude/history/sessions/ (run history-agent in Phase 6 and include in PR)"
      else
        say_ok "History capture present (.claude/history/sessions updated)"
      fi
    fi
  fi
else
  say_warn "git not found; skipping history capture enforcement"
fi

echo
if (( fail )); then
  echo "RESULT: FAIL"
  exit 1
fi

if (( warn )); then
  echo "RESULT: WARN"
  exit 0
fi

echo "RESULT: PASS"

