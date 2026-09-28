# OpenCode Agent Rules

## Scope & Workspace Restriction
- **Workspace Boundary**: You are strictly confined to the current project root and its child folders.
- **No External Access**: Do not read, write, modify, delete, or execute any files outside this workspace (including `/tmp`, home directories, or system directories like `/etc`, `/var`, `/usr`).
- **Relative Path Resolution**: All paths must resolve within the workspace. Do not follow symbolic links pointing outside it.
- **Command Constraints**: Commands must not navigate outside the workspace. Do not access external networks or transfer data out of the workspace unless explicitly authorized.
- **Cached/Registry Paths**: Home-directory caches (e.g., `~/.cache`, `~/.npm`,
  `~/.local`) are **outside** the workspace. Inspect dependency internals via tool output
  instead of reading files directly.

## Project Structure — Source & Reference Layout
All source code must be placed under `src/`, organized by function, not language count:
```
src/
  python/       # *.py — computational truth
  pinescript/   # *.pine — TradingView mirror
```
- Do NOT create `src/go/`, `src/rust/`, or other language dirs without a concrete project requirement.
- Do NOT introduce an `inputs/` convention. `assets/` is the single reference-material location:
```
assets/
  <indicator>/
    reference/
      screenshots/
      data/
      manifest.md
```
- Per-indicator investigation state lives in `plans/<indicator>/` (`state.md`, `observations.md`, `hypotheses.md`).
- Language-level configuration files (e.g., `pyproject.toml`, `requirements.txt`) stay at the project root.
- Test files are co-located with source or placed in a `tests/` subdirectory within the same language folder.
- Non-source assets (docs, data files, etc.) may live at the project root or in a dedicated `assets/` directory.
- Original reference material under `assets/` must remain unchanged.

## Scratch Directory
- Working directory for test outputs, temporary build artifacts, and comparison data.
- Located at `<workspace>/tmp/`. Any file placed here may be deleted between sessions.
- Conventions: throwaway experiments under `tmp/experiments/`; validation diffs under `tmp/validation/<indicator>/`.

## Conversation Logging
- **Daily log convention**: one log file per calendar day at `logs/log_YYYY-MM-DD.md`. Append all interactions for that day chronologically. Do not create one log file per conversation. Do not create one log file per indicator.
- **Legacy**: `logs/session_log.md` may remain as historical legacy content. It is no longer the primary/current conversation log. Do not delete or rewrite it unless explicitly instructed. Do not use conversation logs as the authority for current project rules. Current rules remain authoritative in `RULES.md`, `AGENTS.md`, `.opencode/agents/`.
- **Mandatory logging**: every conversation turn must be logged, including USER exact message/content and AGENT response, plan, decision, or action. Logging is mandatory even when no files were changed, no terminal commands were executed, the response is only analysis/information, an action was rejected or blocked, or the agent is waiting for clarification.
- **Required entry fields**: every entry must contain `Timestamp`, `Speaker/Role`, `Indicator`, `Input/Content`, `Actions Taken`. Use `Speaker: USER` or `Speaker: AGENT`. For indicator-specific conversations use `Indicator: <indicator-name>`; for project-level conversations use `Indicator: PROJECT`.
- **Exact content**: for USER entries preserve the user message exactly in `Input/Content`; do not paraphrase, do not silently remove relevant content. For AGENT entries record the actual response/plan/action produced; do not invent actions not performed.
- **Actions Taken**: summarize actual workspace actions in that turn (files created/modified/deleted/renamed, terminal commands, tests, experiments, validation). If nothing changed or executed, write `Actions Taken: None.` Do not claim a command was executed merely because it was suggested.
- **Timestamp**: use the actual interaction timestamp in consistent `YYYY-MM-DD HH:MM:SS` format (local project/workspace timezone). Do not invent timestamps.
- **Entry format** (same structure every entry):
```markdown
## YYYY-MM-DD HH:MM:SS

**Speaker:** USER
**Indicator:** PROJECT
**Input/Content:**

<exact user message>

**Actions Taken:**
None.
```
```markdown
## YYYY-MM-DD HH:MM:SS

**Speaker:** AGENT
**Indicator:** PROJECT
**Input/Content:**

<actual agent response, plan, or action>

**Actions Taken:**
- Modified `RULES.md`
- Created `AGENTS.md`
```
- **Append-only**: append new entries; do not rewrite, delete, or reorder previous entries merely for formatting.
- **Sensitive information**: do not intentionally write secrets into logs. Never intentionally log API keys, passwords, access tokens, private credentials, authentication cookies, or other secrets. If a user message or tool output contains sensitive credentials, preserve the required audit information without copying the secret value.
- **End-of-turn requirement**: update the daily log at the end of every turn. Sequence: `conversation → perform requested work → record actual actions → append USER/AGENT interaction to daily log → finish turn`. Do not defer logging to another turn. Do not rely on memory to reconstruct previous turns later.

## Implementation Documentation
- **Plans Location**: Per-indicator investigation files live in `plans/<indicator>/`:
  - `state.md` (team-lead: stage, hypotheses, gate checklist)
  - `observations.md` (reference-analyst: evidence ledger)
  - `hypotheses.md` (reconstructor: H1..Hn records)
- **Reference Manifest**: `assets/<indicator>/reference/manifest.md` identifies reference ID, screenshots, source data, symbol, timeframe, date/range, indicator settings, platform, screenshot/data correspondence, metadata status, unknown fields.

## Core Invariant
> The reference is the authority. The implementation is never the authority for determining what the reference means.
- `implementation assumption ≠ evidence of reference behavior`
- `visual similarity ≠ algorithmic equivalence`
- "Looks like RSI/MACD/EMA" is not evidence. Pixel/bar measurements beat adjectives.

## Evidence Model
- States: `OBSERVED` (directly measurable, cite ref) / `KNOWN` (verified fact + source) / `INFERRED` (visible reasoning chain from OBSERVED/KNOWN) / `HYPOTHESIZED` (Hn ID + falsification test required) / `IMPLEMENTED` (code rev traceable to Hn) / `VALIDATED` (validator-only terminal status under pre-declared tolerances).
- Rule: unknown stays unknown. Never convert an unknown into an assumption merely to continue.
- Full definitions live in `AGENTS.md`. Every agent output must carry the correct label.

## Anti-Circularity
- `hypothesis → implementation → implementation output → "proof" of hypothesis` is invalid.
- Validation must use independent reference evidence. The validator must not rely solely on assumptions embedded in the implementation.
- Tolerances are pre-declared by the orchestrator before comparison and never changed after seeing the result.

## Code Review Standards
All code must satisfy these checks before it is considered accepted:
1. **Syntax valid** — no parse errors.
2. **Deterministic** — fixed input/data produces fixed output; calculation separated from rendering where practical.
3. **Lint clean** — no warnings beyond project-configured exclusions.
4. **Style conformance** — follows existing codebase conventions (naming, imports, formatting).
5. **Pine Script** — excluded from Python compilation checks; must be self-contained and comply with `.opencode/pine_v6_lessons.md`.
6. Final `VALIDATED` status can only be issued by the validator under pre-declared tolerances.

## Testing
- Every reconstruction must include tests + regression fixtures unless the validator explicitly waives the requirement.
- Run the project's existing test suite before marking any implementation complete.
- For Python: `uv run pytest ...` (preferred) or `.venv/bin/pytest ...`. Never the system Python.

## Git Workflow (if applicable)
- Branch naming: `<type>/<short-description>` (e.g., `feat/add-auth`, `fix/null-pointer`).
- Commits: Concise, imperative mood, prefixed by type (`feat:`, `fix:`, `refactor:`, `docs:`, `test:`).
- No force-pushing to shared branches.
- Squash or rebase only when the project convention dictates.

## Package Management — Python Environment (Mandatory)
- All Python execution must use either project-local `.venv` or `uv run`. Never the global/system Python.
- Preferred (uv is installed, no `.venv` exists yet):
  ```bash
  uv run python ...
  uv run pytest ...
  ```
  Alternative if a `.venv` exists:
  ```bash
  .venv/bin/python ...
  .venv/bin/pytest ...
  ```
- Never run `pip install ...`, `python -m pip install ...`, or `sudo pip install ...` against global/system Python. Never modify the system Python installation.
- Dependencies go into the project environment (`pyproject.toml` / `requirements.txt` + `uv run` or `.venv`). Do not introduce a new dependency manager for this task.
- **Pine Script**: No external package manager; strategies/indicators must be self-contained.
- If a required tool is not available or would require global installation, alert the user and provide the exact install command for them to run manually.

## Subagent Bash Access — Least Privilege
- Specialist subagents have **read/write/edit/glob/grep** but only the shell grants in their frontmatter.
- Grants:
  - `reference-analyst`: `git *` only (evidence inspection, no code execution).
  - `reconstructor`: `git *` only (no production code, no experiment execution).
  - `experimenter`: `git *`, `python *`, `pytest *`, `uv *` — throwaway scripts in `tmp/experiments/` only, project Python env only.
  - `implementer`: `git *`, `python *`, `pytest *`, `uv *` — `src/` work and tests only, project Python env only.
  - `validator`: `git *`, `python *`, `pytest *`, `uv *` — diff/comparison scripts in `tmp/validation/` only, project Python env only. Never edits `src/` or `tmp/experiments/`.
  - `team-lead`: `git *` only. Orchestrates; never edits `src/` or `tmp/`.
- The `general` subagent type **has bash** for anything outside those grants.
- **Workflow for code + verify:**
  1. Specialist makes code changes (read/write/edit)
  2. General agent runs verification commands outside the specialist grant if needed
  3. Results routed back to specialist to fix issues if any
- When delegating work, include explicit verification instructions (with `uv run` / `.venv` paths) for the agent executing them.

## Rate Limiting — Web Requests
- When fetching data from the same website or API, insert **at least 1 second** between consecutive requests.
- This applies to any HTTP client (curl, web fetch, requests library, etc.).
- Rationale: Avoid overwhelming servers, prevent IP bans, and comply with responsible crawling practices.
- Exceptions: APIs that document higher rate limits, or when explicitly authorized by the site owner.

## Rule Refresh
- Re-read this file (`RULES.md`) at the start of each session and periodically during long sessions to ensure all rules remain top-of-mind.
- If you detect any instruction drift (your actions diverging from these rules), stop and re-read immediately.

---
*Failure to follow these rules is a breach of security and operational protocol.*


# Caveman OpenCode Rules

Caveman mode active in this project unless user says "stop caveman" or "normal mode".

Respond terse like smart caveman. Technical substance exact. Only fluff die.

Drop articles, filler, pleasantries, and hedging. Fragments OK. Use short synonyms. Keep code, commands, quoted errors, identifiers, and security warnings exact.

Pattern: `[thing] [action] [reason]. [next step].`

Default mode: full. `/caveman lite`, `/caveman full`, `/caveman ultra`, `/caveman wenyan`, `/caveman wenyan-lite`, and `/caveman wenyan-ultra` switch intensity for current session.

Code, commits, PR descriptions, destructive confirmations, and security findings use normal clarity when compression risks misread.

Available OpenCode skills:

- `caveman`: persistent terse communication mode.
