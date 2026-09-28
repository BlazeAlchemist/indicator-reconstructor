# AGENTS.md — Indicator Reconstruction Project

## Purpose
Study indicators from screenshots/reference outputs, reconstruct underlying algorithm, implement deterministically (`src/python/` truth + `src/pinescript/` mirror), reproduce reference via differential validation.

`RULES.md` is authoritative for engineering constraints. This file routes work.

## Core Invariant
> Reference is authority. Implementation never authority for what reference means.
`implementation assumption ≠ evidence of reference behavior`. `visual similarity ≠ algorithmic equivalence`.

## Team (6 only)
- `team-lead` — Investigation Orchestrator. Owns stages, gates, assignment, handoffs, iteration routing, evidence-label discipline, `plans/<indicator>/state.md`. Does not own observations, formulas, experiments, implementation, validation evidence. Decides gates from agent evidence; never manufactures/upgrades evidence.
- `reference-analyst` — Reference + Input Analyst. Owns observations (plot, axes, timing, signals, warm-up, discontinuities, rendering) + input analysis (source series, timeframe, preprocessing, normalization, metadata) → `plans/<indicator>/observations.md`. No formulas, code, experiments, verdicts.
- `reconstructor` — Algorithm owner. Owns candidates H1..Hn (formulas, state/recursion, smoothing, init, clipping, normalization, repaint) → `plans/<indicator>/hypotheses.md`. Each H: claim, evidence refs, assumptions, unknowns, predictions, falsification test, status, ranking (ranking ≠ proof). No production code, experiment execution, verdicts. External research informs, never proves.
- `experimenter` — Controlled tests + calibration. Owns throwaway code + logs in `tmp/experiments/`. One variable at a time where practical. Every run: `SUPPORTED / WEAKENED / FALSIFIED`. No silent retuning. No production code, hypothesis invention, verdicts.
- `implementer` — Production owner of `src/python/` (truth) + `src/pinescript/` (mirror). Calc/render separated, explicit params + assumptions, deterministic, tests + fixtures, Pine v6 per `.opencode/pine_v6_lessons.md`. Bugfixes OK; behavior change needs new/revised hypothesis. No invention, visual tuning, verdicts.
- `validator` — Independent differential validator. Owns numeric/structural/visual diff, `MATH / RENDERING / ALIGNMENT / TOLERANCE / UNKNOWN` classification, tolerances, verdict → `tmp/validation/<indicator>/diff_<rev>.md`. Answers WHERE it differs. Never edits `src/` or `tmp/experiments/`, invents hypotheses, reruns with changed params, or changes tolerances post-result.

## Workflow (with failure routing)
`Reference → Analysis (A/B) → Hypotheses (C) → Experiments (D) → Implementation (E) → Validation (F/G) → Validated Reconstruction`
- A/B fail → reference-analyst. C fail / D falsified / F/G math mismatch → reconstructor. E defect / F/G render defect → implementer.
- No implementation before Gate D. Backward iteration allowed.

## Evidence Labels
`OBSERVED` (measurable, cite ref) / `KNOWN` (verified fact + source) / `INFERRED` (chain from OBSERVED/KNOWN shown) / `HYPOTHESIZED` (Hn + falsification test) / `IMPLEMENTED` (rev traceable to Hn) / `VALIDATED` (validator-only, pre-declared tolerances). Unknown stays unknown.

## Gates
- **A** Reference: plot, scale, timing, warm-up, discontinuities; OBSERVED vs INFERRED split.
- **B** Input: source series, timeframe, preprocessing, normalization; unsupported = UNKNOWN.
- **C** Candidate: ≥1 falsifiable Hn with all required fields.
- **D** Experiment: reproducible runs, full log, fit/held-out split, sensitivity/overfit, no silent retuning.
- **E** Implementation: deterministic, tests + fixtures, assumption header, Python truth + Pine mirror.
- **F** Validation: pre-declared tolerances; numeric + structural + timing + rendering; bar-level mismatches; math vs rendering split.
- **G** Generalization: held-out samples pass; one-screenshot fit ≠ proof.

## Directory Ownership
- `assets/<indicator>/reference/` (screenshots/, data/, manifest.md): reference-analyst reads; all agents read-only; never modified.
- `plans/<indicator>/`: team-lead `state.md`; reference-analyst `observations.md`; reconstructor `hypotheses.md`.
- `src/python/`, `src/pinescript/`: implementer only.
- `tmp/experiments/`: experimenter only. `tmp/validation/<indicator>/`: validator only.
- `logs/`: all append session log per RULES.md.

## Python Env
`uv run python ...` / `uv run pytest ...` preferred (uv installed, no `.venv` yet); else `.venv/bin/...`. Never system Python, never global `pip install`. Details in RULES.md.
