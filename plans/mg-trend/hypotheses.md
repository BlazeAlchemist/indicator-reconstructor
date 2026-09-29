# mg-trend — Hypotheses (reconstructor)

> Scope: `plans/mg-trend/observations.md` (Gates A/B ledger) + 21 PNGs in `assets/mg-trend/reference/screenshots/`. No `manifest.md`, no `data/` at time of writing.
> Evidence discipline: every candidate below is labeled `HYPOTHESIZED`. Relative ranking is provisional prioritization only — **ranking ≠ proof**. New evidence must be able to kill H1. No formula anchoring. External formulas cited as HYPOTHESIZED only, never validation.
> Gate C requirement: ≥1 explicit falsifiable candidate with all required fields — met by H1..H4 below + H5/H2b (Gate-D revision).
> Pixel-test absorption 2026-09-28 (reconstructor, no code/experiments run — verdicts absorbed from `tmp/experiments/mg-trend/gate_d_pixel_log.md` + `exp_h4_census.md` + `exp_symmetry.md` + `exp_gaps.md` + `exp_h3_steps.md`, deviation IDs D1..D5 cited inline): H2-P2.5-flip FALSIFIED→secondary variant; H4-P4.2 violated twice (D2)→E1/E2 exceptions; H3 core pixel-FALSIFIED (kill record kept); H1 P1.1/P1.4/P1.5/P1.6 pixel-SUPPORTED, P1.3 OHLCV-gated. Every claim below stays `HYPOTHESIZED`-labeled; ranking ≠ proof restated; only validator can mark VALIDATED.
> Gate D held-out + diagnostics absorption 2026-09-28 (reconstructor, NO code, NO experiments run — verdicts absorbed from `tmp/experiments/mg-trend/heldout_results.md` §Results/§Verdicts/§Diagnostics D1–D5 EXECUTED + `gate_d_full_log.md` + `fit_mcd_nke.md`): H1-P1.3 KILLED (fit KILL 2 + held-out KILL 19); H2-P2.2 WEAKENED (18/18 sweep but RMSE 3/6 + whipsaw median 4.0x). D3–D5 apportion central-identical vs width-discriminator; D1 MSFT gap-cause; D2 earliest-window misses. New H5 HYBRID + H2b variant tabled below (all HYPOTHESIZED). Ranking ≠ proof restated; only validator can mark VALIDATED.

## Global constraints every Hn must explain (from ledger)

- G1: overlay 3-trace, shared price scale, no fill, no pane (§1, §3: all 21 PNGs).
- G2: thick central red/green + 2 thin purple dashed, purple never changes color (§1: e.g. `META_Screenshot_2026-09-28_14-42-53.png`, `CRM_Screenshot_2026-09-28_14-44-58.png`).
- G3: legend `TREND LINE1..12`, LINE7-12 always blank; red state LINE1==LINE3, green LINE2==LINE4, LINE5=upper, LINE6=lower (§1: e.g. `BE_Screenshot_2026-09-28_14-27-36-1.png` 259.945/259.945, `Dell_Screenshot_2026-09-28_14-30-06.png` 127.945/127.945, `MU_Screenshot_2026-09-28_14-47-14.png` 196.928/196.928).
- G4: LINE5 > central > LINE6 always; sampled symmetry exact to 3dp (§1, §6: BE ±15.432, Dell 8.200/8.201, MRNA 9.335/9.334, MSFT Sep-09, META Sep-25, MU Nov-25, NKE Jul-08).
- G5: central trails (red below price in ups, green above in downs) but price extends far beyond bands for weeks (§6: `MRNA_Screenshot_2026-09-28_14-33-03.png` price ~110-202 vs upper ~65-130; `MSFT_Screenshot_2026-09-28_14-40-40.png` gap above upper; `MCD_Screenshot_2026-09-28_14-44-21.png` below lower).
- G6: sparse triangles (0-8/view) not 1:1 with flips; red-up below lows near lower/restart, green-down above highs during green (§2, §5: `MU_Screenshot_2026-09-28_14-47-14.png`, `NKE_Screenshot_2026-09-28_14-46-47.png`, `Dell_Screenshot_2026-09-28_14-30-06.png`, `MRNA_Screenshot_2026-09-28_14-32-27.png`).
- G7: central gaps ≥7 views (1-5 bars, no thick line) while bands continuous through gaps (§4: `BE_Screenshot_2026-09-28_14-27-36.png`, `MRNA_Screenshot_2026-09-28_14-34-05.png`, `MSFT_Screenshot_2026-09-28_14-40-40.png`, `MSFT_Screenshot_2026-09-28_14-41-55.png`, `META_Screenshot_2026-09-28_14-42-53.png`).
- G8: all traces smooth through price gaps (§3: `MRNA_Screenshot_2026-09-28_14-33-03.png`, `MRNA_Screenshot_2026-09-28_14-38-31.png`, `MSFT_Screenshot_2026-09-28_14-40-40.png`).
- G9: no warm-up visible, traces present at left edge (§4: `MU_Screenshot_2026-09-28_14-47-14.png`, `Dell_Screenshot_2026-09-28_14-31-21.png`, `MRNA_Screenshot_2026-09-28_14-32-27.png`); Daily (15) + 2h (6) (§7).
- G10: small Chinese labels `机构进/机构出/筑顶/筑底` near bands/extremes (§2); large bottom captions are video overlays, not indicator (§2).

---

## H1 — Symmetric ATR-envelope midline + close-cross state machine (Supertrend-variant, mid-plotted)

**Current status:** `HYPOTHESIZED` + pixel-SUPPORTED display math BUT P1.3 flip rule KILLED (fit KILL 2 per `tmp/experiments/mg-trend/fit_mcd_nke.md` §Results/§Verdicts + held-out KILL 19 per `tmp/experiments/mg-trend/heldout_results.md` §Results/§Verdicts (d) — do NOT implement band-break rule; kill record below — only validator can mark VALIDATED)

### Claim

Central is a moving-average midline; bands are symmetric ATR offsets of that midline; color state is a close-vs-opposite-band state machine; duplicates are display copies.

Formulas (all HYPOTHESIZED, params UNKNOWN):

- Source `S_t ∈ {close, hl2, hlc3}` UNKNOWN.
- `basis_t = MA_w(S)_t`, `w` UNKNOWN (candidate 20–60; SMA or EMA UNKNOWN).
- `TR_t = max(H_t − L_t, |H_t − C_{t−1}|, |L_t − C_{t−1}|)`; `ATR_t = RMA_N(TR)_t` (Wilder) or `SMA_N`, `N` UNKNOWN.
- `W_t = m · ATR_t`, `m` UNKNOWN.
- `upper_t = basis_t + W_t` (= LINE5); `lower_t = basis_t − W_t` (= LINE6); `mid_t = basis_t`.
- State recursion with gap state `0`:
  - if `state_{t−1} = +1` (red) and `close_t < lower_t` → `state_t = 0` for `g ≥ 1` bars then `−1`; if `close_t` reclaims `mid_t` within `g` bars → remain `+1` (whipsaw guard, HYPOTHESIZED).
  - if `state_{t−1} = −1` (green) and `close_t > upper_t` → `state_t = 0` then `+1` (symmetric).
  - else `state_t = state_{t−1}`.
- Display mapping: `LINE1_t = LINE3_t = mid_t` iff `state_t = +1` else `na`; `LINE2_t = LINE4_t = mid_t` iff `state_t = −1` else `na`; `LINE5_t = upper_t`, `LINE6_t = lower_t` always defined; LINE7–12 unassigned (`na`).
- Smoothing: via `MA_w` + `RMA_N`; no extra smoothing HYPOTHESIZED.
- Init: first `max(w,N)` bars `na`, hidden by left-edge truncation (chart loads more history than displayed) → explains G9.
- Clipping/thresholds: none; no fixed levels (§2 OBSERVED absence).
- Normalization: none; price units, shared scale (§3).
- Repaint: HYPOTHESIZED no intrabar repaint beyond standard confirmed-close state; 2h views may update intrabar — UNKNOWN.

This is a Supertrend-variant in the external-research sense (cf. Seban Supertrend basic/final bands + direction state — cited as HYPOTHESIZED only, not equivalence): classic Supertrend plots the active band edge; H1 instead plots the basis midline and keeps both bands, which is the structural symmetry explanation.

### Supporting evidence refs

- G3/G4 symmetry: §1 + §6 legends (BE 275.377>259.945>244.513 ±15.432 exact; MSFT 471.514>453.472>435.430; META 662.279>616.393>570.507; MU 227.016>196.928>166.840; NKE 47.908>45.252>42.597) — structural `mid ± W` predicts exactly this; tooltips §1 (`LINE3` on central red, `LINE4` on central green, `LINE6` on lower, `LINE5` on upper) match display mapping.
- G7 gaps with continuous bands: §4 (`MSFT_Screenshot_2026-09-28_14-40-40.png` Jul-28–Aug-3 central absent while dashes continue ~416/~373; `MRNA_Screenshot_2026-09-28_14-34-05.png` mid-Jul gap) — predicted by `state=0 → na` while `upper/lower` always defined.
- G5 trailing + far extension: §6 (Dell Jun–Sep 2026 price above central ~100; MRNA weeks 40–70 above upper) — slow `MA_w` + lagged `ATR_t` trails in trends yet lets gap-driven price escape bands for weeks without forcing an immediate flip until opposite-band close.
- G8 smoothness: §3 (MRNA Aug 2026 ~60→110 gap, central ~58→110 smooth) — MA + RMA smooth through single-bar gaps.
- Duplicates + blanks: §1 (LINE1==LINE3 / LINE2==LINE4 at every crosshair; LINE7–12 always blank) — two `plot()` calls of same series per color (thick + edge) + 6 reserved/unused slots; purple invariant (§1) = bands have no state.

### Assumptions

1. Bands are computed from central (`upper/lower = central ± W`), not central from bands.
2. Flip trigger is close-vs-opposite-band, not MA cross, not mid-cross.
3. Gap = explicit `na` transition state (1+ bars), not missing data.
4. Duplicates are display copies for thickness/edge, not separate math.
5. Left-edge values are post-warm-up (hidden history).

### Unknowns

- `S`, `MA` type/length `w`, `ATR` type/length `N`, multiplier `m`, gap length `g` and reclaim rule, 2h session definition (§7/§9 UNKNOWN), triangle sub-rule (see below), whether black segment in `MSFT_Screenshot_2026-09-28_14-41-55.png` is selection vs state (§2/§9).

### Predictions

- P1.1 (symmetry): at every bar, `LINE5 − central == central − LINE6` within rounding (±0.002); digitizing any view yields zero-mean asymmetry. [pixel-SUPPORTED per `tmp/experiments/mg-trend/exp_symmetry.md` + `gate_d_pixel_log.md` run 2: 21/21 resid ≤0.001, mean 0.000; D5 caveat sub-0.001 structural asymmetry unexcluded without data/]
- P1.2 (ordering): `LINE5 > central > LINE6` strictly at every bar including gaps (bands persist). [pixel-SUPPORTED same run: 21/21 ordering holds]
- P1.3 (flip bars): every red→green flip is preceded on the flip bar by `close < lower`; every green→red by `close > upper`; flips never occur on bars where close stays inside bands. [`HYPOTHESIZED` + KILLED at Gate D fit + held-out per `tmp/experiments/mg-trend/fit_mcd_nke.md` §Results/§Verdicts (KILL-PANEL=2 NKE 2026-02-20 −1→+1 C65.40 in [60.93,67.51] + 2026-02-25 +1→−1 C63.40 in [60.66,67.67]) + `tmp/experiments/mg-trend/heldout_results.md` §Results/§Verdicts (d) (KILL-PANEL held-out total=19 ≥2: CRM 4 dated 2026-02-20-style list 2025-11-10/2026-06-02/2026-06-10/2026-07-30 + MU 3 + SNOW 1 + DELL 3 + MRNA 6 + MSFT 0 + META 2; fires 6/7 tickers, 5 tickers EACH ≥2; each kill bar = in-window best-H2 cross-dated flip with close strictly inside best-H1 bands at first-new-state bar — ledger-consistent flip dates H1's rule forbids). Mechanism confirmation via §Diagnostics D2 EXECUTED: H1 MISSES DELL W1 [2025-09-01..09-30] + MRNA W1 [2026-05-01..06-30] (both earliest windows) where H2 hits all (DELL W1 H2 2025-09-04+09-16; MRNA W1 H2 05-01/05-11/05-20/06-15) — H1 silence exactly where inside-band ledger motion occurs. Do NOT revive band-break rule.]
- P1.4 (gaps): gaps occur only at flips (transition `na`), length `g` small (1–5 bars); no gap mid-trend without flip. [pixel-SUPPORTED per `tmp/experiments/mg-trend/exp_gaps.md` + `gate_d_pixel_log.md` run 3: 8/8 gaps at flips, 0 mid-trend gaps in 21 views, lengths 1–5 bars, bands continuous 8/8; D1 caveat gap-vs-tight is partly zoom/resolution-dependent, gap-vs-tight selection rule stays UNKNOWN]
- P1.5 (smoothness): central and bands have bounded bar-to-bar slope (no single-bar steps > `W_t`); price gaps do not spike traces. [pixel-SUPPORTED per `tmp/experiments/mg-trend/exp_h3_steps.md` cross-check + `gate_d_pixel_log.md` run 4: 0 exact flats, smooth unimodal curvature in MU+NKE primary + 4 supporting views; D3 caveat eye-not-digitizer, numeric slope histogram stays OHLCV-gated]
- P1.6 (triangles — SECONDARY model): red-up arrows lag green→red flips by ≥0 bars and sit at/near `lower` touch or post-flip pullback; green-down arrows occur mid-green-state at `upper` touch, not at flips. Specifically: NOT every flip has an arrow same-bar; arrows never precede flips. Flip-signal model predicts 1:1 same-bar coincidence — H1 predicts this fails. [pixel-SUPPORTED per `tmp/experiments/mg-trend/exp_h4_census.md` + `gate_d_pixel_log.md` run 1: arrows-with-flip 21/99 raw (21%), de-dup 17/82 (21%); flips-with-arrow 19/57 raw (33%), de-dup 14/40 (35%); fit 23% vs held-out 19% — P4.4 <50% met; D2/D4 caveats apply — see H4-P4.2 revision for the two exception bars; D4 ±1 bar-index uncertainty]

### Falsification experiment

- **Exp-H1 (pixel pre-tests DONE 2026-09-28 + Gate-D OHLCV EXECUTED — P1.3 KILLED, do NOT re-run to revive):** sourced Daily OHLCV fit MCD+NKE (`fit_mcd_nke.md`) + held-out CRM/MU/SNOW/DELL/MRNA/MSFT/META scoring-only (`heldout_results.md`). Grid `w,N,m` families (SMA/EMA × Wilder/SMA-ATR) fitting `LINE5/central/LINE6` at legend snapshots (§6 values). **H1 KILLED by:** (b) fit KILL-PANEL=2 (NKE 2026-02-20/02-25 inside-band) + held-out KILL-PANEL=19 (≥2 fires 6/7 tickers, 5 tickers EACH ≥2; §Verdicts (d)) + D2 mechanism confirmation (H1 MISSES DELL W1 Sep2025 + MRNA W1 May-Jun2026 earliest windows where H2 hits all — silence where inside-band ledger motion occurs). Pixel pre-tests per `exp_symmetry.md` (21/21 SUPPORTS P1.1) + `exp_gaps.md` (8/8 SUPPORTS P1.4) stand for display math only; flip rule dead. Do NOT revive band-break rule without new evidence.

**Current status:** `HYPOTHESIZED` + pixel-SUPPORTED display math (P1.1/P1.2/P1.4/P1.5/P1.6 pixel-SUPPORTED) BUT P1.3 band-break flip rule KILLED — fit KILL 2 (boundary, `fit_mcd_nke.md`) + held-out KILL 19 (non-boundary cross-regime, `heldout_results.md` §Verdicts (d)) + D2 earliest-window mechanism confirmation. Do NOT implement band-break rule; do NOT revive without new evidence. Only validator can mark VALIDATED.

### Kill record (Gate D fit + held-out, 2026-09-28 — DO NOT DELETE, do NOT revive band-break rule)

- Pre-registered kill criterion (P1.3): ≥2 ledger flips occur with close strictly inside both bands (on OHLCV, not pixels).
- Fit-stage: KILL-PANEL=2 (NKE 2026-02-20 −1→+1 C65.40 in best-H1 band [60.93,67.51] + 2026-02-25 +1→−1 C63.40 in [60.66,67.67]; both deep-inside, both directions, both in pre-declared NKE-Feb padded window) → H1-P1.3 FALSIFIED fit-stage (boundary + model-dependent caveats logged in `fit_mcd_nke.md` §Adjudication-2, not hidden).
- Held-out CONFIRMATION (scoring-only, locked BEST-H1 `hl2/EMA60/SMA10/1.5 2-bar gap`): KILL-PANEL held-out total=19 (≈10× threshold ≥2): CRM 4 (2025-11-10, 2026-06-02, 2026-06-10, 2026-07-30) + MU 3 + SNOW 1 + DELL 3 + MRNA 6 + MSFT 0 + META 2 — fires 6/7 tickers; five tickers (CRM/MU/DELL/MRNA/META) EACH independently ≥2; MRNA heaviest (6, gap regime obs §4); MSFT alone clean (H1's best ticker: RMSE pass both, 2/2 windows, KILL 0 — still doesn't save the family). Cross-regime (chop CRM obs §4/#18, persistent-red MU, tight DELL, gap MRNA, extension META) ⇒ not a one-ticker/one-regime artifact. Fit boundary caveats SUPERSEDED. Windows H1 16/18 vs H2 18/18; RMSE<5 H1 5/6 (all but META 14.60) — value-leg passes but kill-leg fails ⇒ no overturn (overturn required ALL of RMSE≥5/6 + windows≥13/18 + KILL≤1 + anchors≥6/7 per `heldout_results.md` §Verdicts). Overflip: H1 held-out total 71 vs pixel 31 (overall 2.29×, median 3.0×) — H1 is NOT the sparse side held-out; fit-silence (1/3) BROKEN held-out side (16/18) via trends/gaps supplying outside-band closes, but kills show H1 fires while still missing ledger flips ⇒ mechanism MORE falsified, not revived (silence → killed-with-hits per §Verdicts overfit verdict).
- Mechanism confirmation via §Diagnostics D2 EXECUTED: H1 MISSES DELL W1 [2025-09-01..09-30] + MRNA W1 [2026-05-01..06-30] (both earliest windows; which-calendar-window identity recorded, NOT invented) where H2 hits all (DELL W1 H2 2025-09-04+09-16; MRNA W1 H2 05-01/05-11/05-20/06-15) — H1 silence exactly where inside-band ledger motion occurs (NKE Feb-whipsaw fit analogue). H2 ⊇ H1 on windows.
- Display math (P1.1/P1.2/P1.4/P1.5/P1.6-secondary) SURVIVES as structural reference (symmetry 21/21, ordering, gaps-at-flips 8/8, smoothness, secondary sparsity) — only the flip rule P1.3 dies. H1 retained as width-reference (ATR-envelope V rule reused by H5) + kill-record anchor, NOT as live trigger candidate. P1.3 stays KILLED.

**Relative ranking:** KILLED — no longer #1; retained only as display-math reference + H4 composite partner superseded by H5/H2b (see ranking below). Ranking ≠ proof; H1 dies on P1.3 (killed twice).

---

## H2 — Dual-MA ribbon-select + volatility envelope (central = winning MA)

**Current status:** `HYPOTHESIZED` + WEAKENED at Gate D held-out (NOT killed, NOT supported) — width-cause identified via §Diagnostics D3–D5 + gap-cause D1 + path to H2b/H5 below. [Absorbed from `tmp/experiments/mg-trend/heldout_results.md` §Results/§Verdicts + §Diagnostics D1–D5 EXECUTED + `tmp/experiments/mg-trend/gate_d_full_log.md`; pixel pre-history per `tmp/experiments/mg-trend/gate_d_pixel_log.md` runs 1–2 + `exp_h4_census.md` + `exp_symmetry.md`: P2.1 SUPPORTED, OLD P2.5-flip FALSIFIED→secondary variant. Do NOT implement old-H2 envelope yet — see H2b/H5. Only validator can mark VALIDATED.]

### Claim

Central is the selected leg of a two-MA ribbon; bands are volatility offsets of the selected leg; color = ribbon order; triangles are a SECONDARY conditional layer (H4-compatible, REVISED 2026-09-28 — no longer flip/cross markers).

Formulas (all HYPOTHESIZED, params UNKNOWN):

- `MAf_t = MA_{wf}(S)_t`, `MAs_t = MA_{ws}(S)_t`, types (EMA/SMA/HMA) + lengths UNKNOWN.
- `V_t = k · ATR_N(t)` or `k · Stdev_N(t)`, `k,N` UNKNOWN.
- `state_t = +1` iff `MAf_t > MAs_t` (red), `−1` iff `MAf_t < MAs_t` (green), `0` (na gap) iff `|MAf_t − MAs_t| < eps` (cross-confirmation zone).
- `central_t = MAs_t` (or `MAf_t` — variant; must pick one per experiment; default HYPOTHESIZED `MAs_t` i.e. slow leg, explaining heavy trailing + far extension).
- `upper_t = central_t + V_t` (= LINE5); `lower_t = central_t − V_t` (= LINE6); same display duplication as H1 (LINE1/LINE3 red copy, LINE2/LINE4 green copy, LINE7–12 blank).
- Smoothing: inherent in both MAs + `V_t`; predicts extra-smooth traces even through gaps.
- Init: `max(wf,ws,N)` bars `na`, hidden by truncation → G9.
- Clipping/thresholds: none except `eps` flat-zone HYPOTHESIZED.
- Normalization: none; repaint: HYPOTHESIZED none beyond cross-confirmation delay (1-bar).

Differs from H1 only in flip rule: MA-vs-MA cross, not price-vs-band. Otherwise same symmetric display math, so also structurally explains G4.

### Supporting evidence refs

- G4 symmetry + G2/G3 display: same §1/§6 legend facts as H1 — `central ± V` predicts exact symmetry identically.
- G8 smoothness + G5 far extension: §3 MRNA/MSFT gap smoothness; §6 MU May–Jul 2026 price ~700–1200 vs central ~500–880, Dell Jun–Sep 2026 price ~100 above central — slow-leg central lags fast price surges for weeks, matching a long `ws`.
- G6/G7 mixed: §5 CRM Nov 2025–Feb 2026 price oscillates through central ~242–253 with multiple flips (ribbon whipsaw zone); §4 tight joints without empty gaps in MCD/CRM/SNOW/NKE/MU (cross without `eps` trigger) vs gapped flips in BE/MRNA/MSFT/META (cross inside `eps` → `na` gap). §5 Dell Jan-29 arrows lagging central (Dec–Jan downs during later green) fits cross-confirm delay.
- Chinese labels near extremes (§2: `筑顶` at highs/upper, `筑底` at lows/lower) fit envelope-touch readings of a ribbon envelope.

### Assumptions

1. Two MAs exist; only the selected one is plotted (other is hidden, explaining why only 3 traces visible despite 12 slots).
2. `eps` flat-zone produces `na` gaps; without it all joints would be tight (explains gapped vs tight flip dichotomy §4).
3. Slow leg is plotted (not fast); fast leg never displayed.
4. LINE7–12 blank = hidden second MA + unused signal slots.

### Unknowns

- MA types/lengths, `V` basis (ATR vs SD), `k,N`, `eps`, which leg plotted, source `S`, 2h handling; same black/wick anomalies as H1; exact cross-vs-arrow timing (§5 bar precision day/2h only).

### Predictions

- P2.1 (symmetry + ordering): same as P1.1/P1.2 — symmetric, strictly ordered. [pixel-SUPPORTED per `tmp/experiments/mg-trend/exp_symmetry.md` + `gate_d_pixel_log.md` run 2: 21/21 resid ≤0.001, mean 0.000; D5 caveat sub-0.001 unexcluded]
- P2.2 (flip bars — ribbon rule): every flip coincides with `MAf` crossing `MAs` within ±1 bar, REGARDLESS of where close sits vs bands; flips can occur with close inside bands (directly contradicts H1-P1.3). [Gate-D HELD-OUT: date-leg SUPPORTED — 18/18 windows (100%, all 7 tickers) + ≥1 inside-band cross (73 total, 19 in-window KILL subset per `heldout_results.md` §Results/§Verdicts (d): CRM 4 dated 2025-11-10/2026-06-02/2026-06-10/2026-07-30 + MU 3 + SNOW 1 + DELL 3 + MRNA 6 + MSFT 0 + META 2) + H2 ⊇ H1 on windows (every H1-hit window also H2-hit; H2 adds the 2 H1-missed D2 earliest windows). BUT family WEAKENED on value/whipsaw legs — see Gate-D diagnosis below. Core date claim survives; envelope sub-claim does not.]
- P2.3 (pinch): band width `V_t` need not pinch at flips (unlike Bollinger); central slope kinks at cross while bands stay smooth. [untested without data/; consistent with smooth pixel curvature per `exp_h3_steps.md` cross-check]
- P2.4 (gaps): gaps occur only when `|MAf−MAs|<eps` at cross; choppy CRM-type whipsaws show alternating tight joints, trending flips show clean single joints or short gaps. [consistent with `tmp/experiments/mg-trend/exp_gaps.md` 8/8 gaps-at-flips + ~30 tight joints; gap-vs-tight selection rule stays UNKNOWN; D1 resolution caveat]
- P2.5 (triangles — SECONDARY model, REVISED 2026-09-28 after pixel falsification of flip variant): OLD flip-variant ("every flip has ±1 triangle and vice versa") is FALSIFIED at pixel level per `tmp/experiments/mg-trend/exp_h4_census.md` + `gate_d_pixel_log.md` run 1 + D4 (±1 uncertainty): arrows-with-flip 21/99 raw (21%), de-dup 17/82 (21%); flips-with-arrow 19/57 (33%), de-dup 14/40 (35%) vs predicted ~100%; documented arrows-without-flips (MRNA Aug-gap red while already red `MRNA_Screenshot_2026-09-28_14-32-27.png`, MU Nov reds along persistent red, NKE 6 greens/0 post-Mar flips, Dell-14-31-21 7 reds/0 flips) and flips-without-arrows (MRNA-mid-Jul gap, SNOW Dec R→G, NKE Jan-Feb, MU Aug inserts). REVISED claim adopts the H4-compatible secondary-signal layer: triangles read ribbon state + bands/price but do not mark crosses — red-up iff `state=+1` (or flipped to `+1` within last `k` bars) AND (`low ≤ lower` touch/penetration OR post-flip pullback reclaim of central); green-down iff `state=−1` AND (`high ≥ upper` OR rejection at central); hence lag/multiplicity (Dell Dec–Jan lagged greens, MU/CRM/NKE multiples) and low two-way coincidence (<50%) are PREDICTED, not anomalies. Ribbon core (P2.2) + display math unchanged; only the triangle sub-claim changed. [HYPOTHESIZED; D2 exceptions inherited from H4-P4.2 revision apply — rare pre-flip/contrarian prints allowed, see H4]

### Falsification experiment

- **Exp-H2 (needs OHLCV; pixel pre-test DONE + Gate-D held-out EXECUTED):** same sourced windows as Exp-H1. Fit `wf,ws` (EMA/SMA grid) to reproduce flip DATES from pixel census (§4–§5: BE Aug 26–28, MRNA mid-Jul/early-Aug, MSFT Jul-28–Aug-3, META Jul gaps) independent of bands; then check central VALUES match slow leg. Pixel pre-test on OLD P2.5-flip already executed: arrow-flip coincidence census across all 21 views per `tmp/experiments/mg-trend/exp_h4_census.md` — coincidence 21%/35% vs predicted ~100% → OLD P2.5-flip FALSIFIED (sub-claim only, core alive). Gate-D held-out EXECUTED per `tmp/experiments/mg-trend/heldout_results.md` §Results/§Verdicts (H1-P1.3 KILLED KILL 19; H2-P2.2 WEAKENED: RMSE<5 3/6 vs required ≥5/6 + whipsaw median 4.0× > 3× cap + MSFT H2 gap_viol=2). **Kills H2-core (ribbon P2.2) if:** (a) no `(wf,ws,type)` pair reproduces ≥80% of ledger flip dates within ±1 bar on data while H1's band-break rule does; OR (c) flip bars show no MA-cross but clear opposite-band close-break. **Kills REVISED P2.5-secondary if:** (b′) on sourced OHLCV, ≥3 triangle bars show no same-side band touch/penetration AND no local extreme within `k` bars post-flip AND no central-reclaim (i.e. mid-channel arrows with no trigger — violating the revised secondary rule); OR two-way arrow↔flip coincidence ≈ 1.0 on full series (flip-marker revival, secondary dead). D4 ±1 bar-index uncertainty applies to all timing checks. **Gate-D diagnosis (LOCKED numbers, do NOT refit — width-cause + gap-cause identified):** D3–D5 apportion central-IDENTICAL vs width-discriminator — central shared slow EMA60 so central miss IDENTICAL per ticker both families (diag verbatim): META +14.569 both, MU +0.298 both, MRNA +2.301 both; width is the discriminator: META hw_err H1 +1.137 vs H2 +53.022 (H2 model_hw 98.908 vs legend_hw 45.886; RMSE 45.68 vs 14.60 ≈ 3× worse); MU hw_err H1 −2.112 vs H2 +6.175 (RMSE 5.05 vs 1.75; MU +0.05 over the <5 line = envelope-scaling fragility, not only extension regime per §Verdicts (c)); MRNA hw_err H1 −0.673 vs H2 +9.843 (RMSE 8.36 vs 2.37). H1 ATR-envelope (SMA-N=10/m=1.5) nails all three widths; H2 Stdev10 k=2.5 blows all three (all hw_err positive = systematic over-width). Whipsaw: H2 median 4.0× / total 107 vs pixel 31 (overall 3.45×) vs H1 median 3.0× / total 71 (overall 2.29×) — BOTH over-flip, H2 worse; MU single-ticker 5.5× exceeds collapse rate (recorded). D1 gap-cause: MSFT H2 gap_viol idx 220/221 dates 2024-11-14/15 — 2-bar na mid-down-state, state −1 both sides (217–219 before, 222–224 after), no flip ±2b, nearest flips 212 (2024-11-04) and 230 (2026-11-29 per diag flip list 2024-11-29); cross bars list includes 220/221 but no flips emitted there (verbatim D1 stdout) — breaks H2's clean sheet on its otherwise cleanest ticker (MSFT: KILL 0, 2/2 windows, RMSE pass both). Candidate mechanism (UNCONFIRMED HYPOTHESIZED): mid-whipsaw zero-runs or diff==0 touch-without-cross bars; whipsaw 18 vs 4 pixel makes whipsaw-runs plausible. Path forward = H2b (envelope replaced + whipsaw guard) + H5 (hybrid), NOT old-H2 implementation.

**Current status:** `HYPOTHESIZED` + WEAKENED (held-out) — ribbon date-core (P2.2) survives via 18/18 sweep + 19 in-window inside-band crosses + H2 ⊇ H1 on windows; width-cause (Stdev10 k=2.5 systematic over-width D3–D5) + gap-cause (D1 MSFT 2024-11-14/15 zero-run) identified; OLD flip-signal triangle sub-claim stays pixel-FALSIFIED (secondary variant adopted). Do NOT implement old-H2 envelope; test H2b/H5 next. Only validator can mark VALIDATED.

**Relative ranking:** old-H2 core demoted off the lead (WEAKENED, width-killed envelope) — live test-priority passes to H2b + H5 (see ranking below). Ranking ≠ proof; P2.2 date-core is the surviving asset, Stdev envelope is the killed liability.

---

## H2b — Cross-trigger + rescaled/ATR-family envelope + whipsaw guard (H2 repair variant)

**Current status:** `HYPOTHESIZED` + UNTESTED repair variant of H2-core (tabled 2026-09-28 post-held-out; absorbs H2-P2.2 date-core, replaces width + gap sub-mechanisms). Test-priority candidate. Only validator can mark VALIDATED.

### Claim

`HYPOTHESIZED`: Same cross-trigger flip rule (H2-P2.2: `MAf×MAs` cross) on the same shared slow-leg central (`MAs`, slow EMA ~60 on `hl2`) that explains §Diagnostics D3–D5 central-identical misses — BUT the Stdev10/k=2.5 envelope (systematic over-width per D3–D5) is REPLACED by a rescaled/ATR-family envelope hypothesis (`V` basis UNKNOWN among ATR-SMA / ATR-Wilder / rescaled-Stdev; `k,N` UNKNOWN) PLUS a whipsaw guard (`HYPOTHESIZED`, e.g. eps-confirm / min-hold / reclaim rule) that suppresses MAf=5 chatter to median ≤3× WITHOUT breaking the 18/18 sweep, and resolves the D1 MSFT 2024-11-14/15 mid-state zero-run to 0 gap_viol. One-liner: cross dates kept, envelope rescaled, chatter guarded.

Formulas (all HYPOTHESIZED, params UNKNOWN):

- `S_t ∈ {hl2, close, hlc3}` UNKNOWN (start-grid center `hl2` HYPOTHESIZED from BEST-H2, NOT locked).
- `MAf_t = MA_{wf}(S)_t`, `MAs_t = MA_{ws}(S)_t`, type ∈ {EMA, SMA} UNKNOWN, `wf, ws` UNKNOWN (start-grid center `wf~5, ws~60` HYPOTHESIZED from BEST-H2 date-sweep, NOT locked; `ws` = slow leg explains D3–D5 shared central).
- `central_t = MAs_t` (`HYPOTHESIZED` slow leg; fast-leg variant explicitly NOT tabled unless slow-leg width grid fails — cf. D-F4 precedent).
- Envelope (REPLACED — `V` basis UNKNOWN, three-way HYPOTHESIZED family, experiment must decide):
  - (i) `V_t = m · ATR^{SMA}_N(t)` (H1-style SMA-ATR; start center `N~10, m~1.5` HYPOTHESIZED from BEST-H1 width wins, NOT locked); OR
  - (ii) `V_t = m · ATR^{Wilder}_N(t)` (Wilder/RMA variant); OR
  - (iii) `V_t = c · k · Stdev_N(t)` (rescaled-Stdev: old-H2 Stdev with rescale `c < 1` HYPOTHESIZED, `c,k,N` UNKNOWN — admits old-H2 was right shape, wrong scale).
- `upper_t = central_t + V_t` (= LINE5); `lower_t = central_t − V_t` (= LINE6); same display duplication as H1/H2 (LINE1/LINE3 red copy, LINE2/LINE4 green copy, LINE7–12 blank).
- State recursion with guard (HYPOTHESIZED guard family — params `eps, h, g` all UNKNOWN; experiment must pre-declare one before scoring):
  - raw cross: `MAf` crosses `MAs` at bar `x` (direction `d`);
  - confirm: `|MAf_x − MAs_x| > eps` (eps-confirm) AND no opposite raw cross within last `h` bars (min-hold `h`, HYPOTHESIZED e.g. 2–5 bars) — else suppress (chatter filtered, no flip, no gap);
  - on confirmed cross: `state = 0` (na gap) for 1 bar (HYPOTHESIZED; `g=1` start center from BEST-H2, NOT locked) then `d`; reclaim variant: if close reclaims `central` within `g` bars against `d`, revert (HYPOTHESIZED alternative, experiment picks one).
  - D1 mechanism: MSFT 2024-11-14/15 idx 220/221 (diff≈0 touch-without-cross or unconfirmed micro-cross) FAILS eps-confirm → NO gap, state stays `−1` through 220/221 → gap_viol 0 (see P2b.4).
- Smoothing: inherent in both MAs + `V_t`. Init: `max(wf,ws,N)` bars `na`, hidden by truncation → G9 (§4 OBSERVED left-edge presence). Clipping/thresholds: none except guard `eps/h/g` HYPOTHESIZED. Normalization: none (§3). Repaint: HYPOTHESIZED none beyond 1-bar confirm delay.

### Supporting evidence refs

- Date-core inheritance: `heldout_results.md` §Results/§Verdicts (H2 18/18 sweep all 7 tickers; H2 ⊇ H1 on windows; 73 total / 19 in-window inside-band crosses; §Verdicts (d) cross-regime KILL distribution CRM 4 + MU 3 + SNOW 1 + DELL 3 + MRNA 6 + META 2, MSFT 0) + §Diagnostics D2 EXECUTED (H1 MISSES DELL W1 [2025-09-01..09-30] + MRNA W1 [2026-05-01..06-30] earliest windows; H2 HITS all: DELL W1 2025-09-04+09-16, MRNA W1 05-01/05-11/05-20/06-15) — cross-trigger is the surviving asset; H2b keeps it verbatim.
- Width-cause (why Stdev replaced): §Diagnostics D3–D5 EXECUTED (verbatim): central miss IDENTICAL both families per ticker (META +14.569 both; MU +0.298 both; MRNA +2.301 both) → central shared slow EMA60 is CORRECT, width is the SOLE discriminator; hw_err H1 (ATR-SMA10/1.5) +1.137 / −2.112 / −0.673 (nails all three) vs H2 (Stdev10/2.5) +53.022 / +6.175 / +9.843 (blows all three, all positive = systematic over-width); RMSE META 45.68 vs 14.60 (~3× worse), MU 5.05 vs 1.75 (§Verdicts (c) MU-boundary +0.05 = envelope-scaling fragility not only extension regime), MRNA 8.36 vs 2.37. §Verdicts (a) META extension (close 751.66 vs central 616.39, half-width 45.886 ~14.9% per obs §6) + (e) date/value tension (H1 wins values 5/6 vs 3/6, H2 wins dates 18/18 vs 16/18) jointly motivate decoupling trigger from envelope — exactly the H2b/H5 swap.
- Gap-cause (why guard added): §Diagnostics D1 EXECUTED (verbatim): MSFT H2 gap_viol idx 220/221 dates 2024-11-14/15 — 2-bar na mid-down-state, state −1 both sides (217–219 before per-bar central ~421.4–421.5, 222–224 after ~421.3–420.8), no flip ±2b, nearest flips 212 (2024-11-04) and 230 (2024-11-29); cross bars list includes 220/221 but no flips emitted there (cross-list ≠ flip-list already in old-H2 code: 20 crosses → 18 flips). MSFT is otherwise H2's cleanest ticker (KILL 0, 2/2 windows, RMSE pass both per §Results/§Verdicts (b)) yet gap_viol breaks its clean sheet — guard predicts this zero-run away. Whipsaw context: MSFT H2 nflip 18 vs pixel 4 (4.5×) makes whipsaw-run mechanism plausible (UNCONFIRMED per §Verdicts (b)).
- Whipsaw budget (why guard target ≤3×): §Results aggregates — H2 median 4.0× / total 107 vs pixel 31 (3.45× overall) vs H1 median 3.0× / total 71 (2.29×); MU single-ticker 5.5× exceeds collapse rate (recorded §Verdicts + `gate_d_full_log.md` sensitivity/overfit). Reference texture per obs §4 (tight joints ~30, gaps 1–5 bars, 0 mid-trend gaps) + §5 (CRM Nov–Feb chops, MU/NKE multiples) tolerates SOME chop but not 4× median — guard must land ≤3× (H1's held-out level) without losing windows.
- Display math unchanged: obs §1 (LINE1==LINE3 red / LINE2==LINE4 green / LINE5>central>LINE6 all 21) + §6 (symmetry exact to 3dp BE ±15.432 etc.) — `central ± V` structural, same as H1/H2.

### Assumptions

1. Slow leg (`MAs`) is plotted central; fast leg hidden (same as old-H2 assumption 3; explains D3–D5 identical central).
2. Trigger and envelope are DECOUPLED sub-mechanisms (cross decides WHEN, ATR-family decides HOW WIDE) — the core H2b/H5 architectural bet, HYPOTHESIZED.
3. Guard filters chatter, never creates flips (guard-suppressed bars stay in prior state, no na) — explains D1 zero-run removal + tight-joint texture obs §4 (MCD/CRM/SNOW/NKE/MU tight joints = unconfirmed-or-sub-eps crosses held, not gapped).
4. Duplicates/blanks display mapping same as H1/H2 (obs §1 tooltips); LINE7–12 blank = hidden fast leg + unused slots.
5. Left-edge post-warm-up (hidden history) → G9 obs §4.

### Unknowns

- `S`, `wf/ws/type`, `V` basis (ATR-SMA vs ATR-Wilder vs rescaled-Stdev three-way UNKNOWN), `N`, `m/k/c`, guard family choice (eps-confirm vs min-hold vs reclaim) + guard params (`eps`, `h`, `g`), gap length (1 vs 2 bars), leg choice fallback (slow assumed; fast only if slow-width grid fails), 2h session (obs §7/§9 UNKNOWN), triangle sub-rule (inherits H4-secondary, NOT redefined here), black-segment anomaly (obs §9 UNKNOWN).
- Grid scope below is HYPOTHESIZED scope for experimenter to pre-declare (NOT locked params, NOT instruction to fit silently — new params need new grid justification with fit/held-out split + sensitivity/overfit per Gate D).

### Predictions (fresh, distinct from old-H2 — all HYPOTHESIZED)

- P2b.1 (symmetry + ordering): same structural `mid ± V`, `LINE5 > central > LINE6` strictly incl. gaps; resid ≤0.001. [Same as P2.1 — display math unchanged; distinguishes vs H3-option-A only.]
- P2b.2 (dates retained): guard does NOT break the sweep — 18/18 held-out windows still hit (±5td padded per `heldout_results.md` §Inputs), H2b ⊇ H1 preserved, D2 earliest-window hits retained (DELL W1 ≥1 flip Sep 2025, MRNA W1 ≥1 flip May–Jun 2026). [Distinct from old-H2: predicts sweep SURVIVES guard; guard that loses ≥2 windows is a failed guard.]
- P2b.3 (widths fixed — per-regime hw_err bands): with ATR-family/rescaled envelope, single-bar hw_err returns to H1-like bands — HYPOTHESIZED: META hw_err ∈ [−5,+5] (vs old-H2 +53.022), MU ∈ [−4,+4] (vs +6.175), MRNA ∈ [−3,+3] (vs +9.843); RMSE<5 on ≥5/6 scored triples (vs old-H2 3/6). Central miss stays slow-leg-like (≈ +14.6 META / +0.3 MU / +2.3 MRNA at those anchors — shared-leg prediction, NOT a fix claim). [OHLCV-detectable on the SAME three anchors + SNOW-date-unknown excluded per D-H2; pixel extension regime obs §6 (MRNA weeks 40–70 above upper, MSFT gap above upper) stays extension-tolerant.]
- P2b.4 (gap-zero): on MSFT Daily full series under H2b guard, idx 220/221 (2024-11-14 C426.89 / 2024-11-15 C415.00) are NON-na state −1 continuation (same-side −1 at 217–219 and 222–224 per D1 verbatim context), gap_viol(MSFT,H2b) = 0, and 220/221 drop out of the flip list (cross-list ≠ flip-list by guard design); nearest flips stay 212 (2024-11-04) and 230 (2024-11-29) within ±2 bars. No NEW mid-state na runs appear on any held-out ticker (gap_viol = 0 all 7 tickers both families). [OHLCV-detectable, D1-resolving; old-H2 predicts gap_viol=2 persists.]
- P2b.5 (whipsaw guarded): held-out full-series flip totals drop to guard-suppressed range — HYPOTHESIZED: total ∈ [50,90] (vs old-H2 107, vs H1 71, vs pixel 31) AND per-ticker median ≤3.0× (vs old-H2 4.0×); single-ticker caps MU ≤4.0× (vs 5.5×), MSFT ≤3.5× (vs 4.5×), META ≤3.0× (vs 4.0×). Floor: total ≥40 (guard that collapses to ≤ pixel 31 has over-smoothed into H1-silence failure — D2 W1 hits would break first). [OHLCV-countable; pixel texture obs §4 tight-joints stay tight (held, not gapped), gapped flips (BE/MRNA/MSFT/META obs §4) stay gapped 1–5 bars.]
- P2b.6 (V-basis discriminator): ATR-SMA vs Wilder vs rescaled-Stdev decided by width-regime slope — HYPOTHESIZED: if hw_err bands (P2b.3) are met by ATR-SMA `m∈[1.0,2.0]` with `N∈{10,14}` while rescaled-Stdev needs `c` varying >2× across META-extension vs MU-calm regimes, ATR-SMA wins parsimony (single `m` both regimes). [Grid-decided; no basis pre-picked here.]

### Falsification experiment

- **Exp-H2b (needs NEW OHLCV grid — NOT a locked-triple rescore; locked BEST-H1/BEST-H2 params do NOT score H2b):** HYPOTHESIZED grid scope (experimenter must pre-declare + log every combo, fit/held-out split, sensitivity/overfit per Gate D — NOT silent fit): `S{hl2,close,hlc3} × MAf{3,5,8} × MAs{50,60} × type{EMA,SMA} × V-basis{ATR-SMA, ATR-Wilder, Stdev-rescaled} × N{10,14,21} × m{1.0,1.5,2.0,2.5} (or k{1.5,2.0,2.5}+c{0.4,0.6,0.8} for rescaled-Stdev branch) × guard{eps-confirm, min-hold h∈{2,3,5}, reclaim}` with pre-declared tolerances: RMSE<5 on ≥5/6 scored triples + 18/18 windows (±5td) + gap_viol 0 + median ≤3×. Fit on MCD+NKE (same 3 windows/padded rule per `fit_mcd_nke.md`), confirm scoring-only on held-out 7 (same 18 windows per `heldout_results.md` §Inputs). **Kills H2b if:** (envelope) no `(V-basis,N,m/c)` reproduces P2b.3 hw_err bands + RMSE ≥5/6 while holding dates (width/date joint fail); OR (guard) every guard reaching median ≤3× loses ≥2/18 windows (sweep/guard trade-off fatal — P2b.2 vs P2b.5 mutually exclusive); OR (gap) D1 220/221 zero-run persists under ALL guard variants (gap_viol ≥1 MSFT) or new mid-state na runs appear elsewhere; OR (basis) rescaled-Stdev needs regime-varying `c` AND both ATR branches miss P2b.3 (family exhausted). D4 ±1 bar-index uncertainty applies. Pixel pre-checks (symmetry/gaps/steps census) already DONE — do not re-run; this is an OHLCV-grid test.
- HYPOTHESIZED grid scope above is a hypothesis about where to look, NOT evidence and NOT permission to retune silently — every combo logged, negatives kept, MAf-fragility re-tested (MAf≥8 must be scored held-out this time per `gate_d_full_log.md` open item).

**Current status:** `HYPOTHESIZED` + UNTESTED (repair variant; inherits P2.2 date-core SUPPORTS + P2.1 display SUPPORTS; replaces width + guard). Do not implement until Exp-H2b passes pre-declared tolerances. Only validator can mark VALIDATED.

**Relative ranking:** test-priority tier (H2b+H4 vs H5+H4 — see ranking below). Ranking ≠ proof; guard/width joint win must survive the pre-declared grid or H2b dies with old-H2.

---

## H5 — HYBRID: cross-trigger (H2 dates) + ATR-envelope width (H1 widths) on shared slow-leg central

**Current status:** `HYPOTHESIZED` + UNTESTED new falsifiable Hn (tabled 2026-09-28 post-held-out; minimal decoupling hypothesis — dates from H2, widths from H1). Test-priority candidate. Only validator can mark VALIDATED.

### Claim

`HYPOTHESIZED` one-liner: H5 = cross-trigger flip rule (H2-P2.2, `MAf×MAs`) + ATR-envelope width (H1-V rule, SMA-`N`/`m`) on the shared slow-leg central that D3–D5 proves identical — i.e. H2's dates with H1's widths, no new central.

Formulas (all HYPOTHESIZED, params UNKNOWN):

- `S_t ∈ {hl2, close, hlc3}` UNKNOWN (start-grid center `hl2` HYPOTHESIZED from BEST-H1/BEST-H2 agreement `hl2/EMA60`, NOT locked).
- `central_t = EMA_{60}(hl2)_t` (`HYPOTHESIZED` shared slow leg; `wf/ws/type` UNKNOWN beyond start center `MAf~5/MAs~60/EMA` from BEST-H2 date-sweep, NOT locked; leg choice UNKNOWN — slow assumed because D3–D5 central-identical, fast only if slow-width grid fails).
- `TR_t = max(H_t − L_t, |H_t − C_{t−1}|, |L_t − C_{t−1}|)`; `ATR_t = SMA_N(TR)_t` (`HYPOTHESIZED` SMA variant from BEST-H1 `SMA10`; Wilder variant UNKNOWN alternative — experiment decides, cf. H2b three-way).
- `W_t = m · ATR_t`, `m,N` UNKNOWN (start-grid center `N~10, m~1.5` HYPOTHESIZED from BEST-H1 `hl2/EMA60/SMA10/1.5 2-bar gap`, NOT locked).
- `upper_t = central_t + W_t` (= LINE5); `lower_t = central_t − W_t` (= LINE6); `mid_t = central_t`.
- State recursion (`HYPOTHESIZED`, guard TBD UNKNOWN): `state_t = +1` (red) iff `MAf_t > MAs_t`, `−1` iff `MAf_t < MAs_t` (H2-P2.2 cross rule verbatim); gap `na` length `g` UNKNOWN (BEST-H1 2-bar vs BEST-H2 1-bar both HYPOTHESIZED start points, NOT locked); whipsaw guard (eps-confirm/min-hold/reclaim) UNKNOWN — H5-minimal leaves guard OPEN by design (see P5.4: gap/whipsaw inherited as diagnostic, not kill).
- Display mapping: `LINE1_t = LINE3_t = mid_t` iff `+1` else `na`; `LINE2_t = LINE4_t = mid_t` iff `−1` else `na`; `LINE5_t = upper_t`, `LINE6_t = lower_t` always; LINE7–12 `na` (same as H1/H2; obs §1).
- Smoothing via slow-EMA + SMA-ATR; Init `max(ws,N)` bars `na` hidden → obs §4 G9; no clipping/normalization (obs §3); repaint HYPOTHESIZED none beyond confirm delay.

### Supporting evidence refs (WHY H5 is motivated — dates from H2 + widths from H1, D3–D5 apportionment)

- Date-leg from H2 (cross wins dates): `heldout_results.md` §Results/§Verdicts — H2 18/18 windows (100%, all 7 tickers) vs H1 16/18; H2 ⊇ H1 on windows (every H1-hit window also H2-hit); 73 total / 19 in-window inside-band crosses (§Verdicts (d): CRM 4 dated 2025-11-10/2026-06-02/2026-06-10/2026-07-30 + MU 3 + SNOW 1 + DELL 3 + MRNA 6 + MSFT 0 + META 2; fires 6/7 tickers, 5 tickers EACH ≥2; cross-regime chop CRM obs §4/#18 + persistent-red MU + tight DELL + gap MRNA + extension META); §Diagnostics D2 EXECUTED — H1 MISSES DELL W1 [2025-09-01..09-30] + MRNA W1 [2026-05-01..06-30] (both earliest windows) where H2 hits all (DELL W1 H2 2025-09-04+09-16; MRNA W1 H2 05-01/05-11/05-20/06-15). Band-break cannot see these ledger flips; cross can. H5 keeps the cross.
- Width-leg from H1 (ATR wins values): §Diagnostics D3–D5 EXECUTED (verbatim, LOCKED — do NOT refit): central miss IDENTICAL both families per ticker (META +14.569 both; MU +0.298 both; MRNA +2.301 both) → central shared slow EMA60 is CORRECT, trigger/envelope must decouple; width is the SOLE discriminator: META hw_err H1 +1.137 vs H2 +53.022 (model_hw 98.908 vs legend_hw 45.886; RMSE 45.68 vs 14.60 ≈ 3× worse); MU hw_err H1 −2.112 vs H2 +6.175 (RMSE 5.05 vs 1.75; §Verdicts (c) MU-boundary +0.05 = envelope-scaling fragility); MRNA hw_err H1 −0.673 vs H2 +9.843 (RMSE 8.36 vs 2.37). H1 ATR-envelope (SMA10/m=1.5) nails all three (all |hw_err| ≤2.2); H2 Stdev10/k=2.5 blows all three (all hw_err positive = systematic over-width). Obs §6 grounds the targets: legend half-widths META 45.886 (~14.9%) / MU 30.088 (~30.6% per obs §6 MU Nov-25 60.176/196.928) / MRNA 9.334 (~34.9%) + symmetry exact to 3dp (BE ±15.432 etc. obs §1/§6) + far-extension texture (MRNA weeks 40–70 above upper, MSFT gap above upper, MCD below lower obs §6) + smooth gap traversal obs §3. H5 keeps the ATR width.
- Tension resolved by decoupling (§Verdicts (e)): fit H1 wins values by a hair (0.378 vs 0.391) + loses dates badly (1/3 vs 3/3); held-out H1 wins values clearly (RMSE<5 5/6 vs 3/6) + loses dates narrowly (16/18 vs 18/18). Neither family wins both legs — H5 predicts the joint win comes from MIXING legs (cross WHEN + ATR HOW-WIDE), HYPOTHESIZED.
- Gap/whipsaw context (informs H5 boundary with H2b): §Diagnostics D1 EXECUTED — MSFT H2 gap_viol idx 220/221 dates 2024-11-14/15, 2-bar na mid-down-state, state −1 both sides (217–219 before, 222–224 after), no flip ±2b, nearest flips 212 (2024-11-04) and 230 (2024-11-29); cross bars list includes 220/221 but no flips emitted there (verbatim D1 stdout). MSFT is otherwise cleanest (KILL 0, 2/2, RMSE pass both per §Results/§Verdicts (b)) yet gap_viol breaks its clean sheet. Whipsaw medians H2 4.0× / H1 3.0×, totals H2 107 vs H1 71 vs pixel 31 (obs §4 tight-joint vs gap texture + obs §5 CRM chops/MU multiples). H5-minimal does NOT claim gap/whipsaw fixed — that is H2b's guard job (see P5.4 discriminator).

### Assumptions

1. Trigger and envelope DECOUPLE (cross decides WHEN, ATR decides HOW-WIDE) — the H5 architectural bet, HYPOTHESIZED.
2. Slow leg is plotted central (same as H2 assumption 3; explains D3–D5 identical central + obs §6 trailing: Dell Jun–Sep price ~100 above central, MU May–Jul price ~700–1200 vs central ~500–880, META Sep price above central).
3. `mid ± W` structural symmetry + strict ordering (obs §1/§6) + bands continuous through gaps (obs §4: MSFT Jul-28–Aug-3 dashes ~416/~373 continue while central absent; MRNA mid-Jul gap) hold for H5 unchanged.
4. Duplicates/blanks display mapping same as H1/H2 (obs §1 tooltips: LINE3/LINE4 on central, LINE5/LINE6 on dashes); LINE7–12 blank = hidden fast leg + unused slots.
5. Left-edge post-warm-up (hidden history) → obs §4 G9; Daily (15) + 2h (6) per obs §7 — 2h handling UNKNOWN.

### Unknowns

- `S`, `wf/ws/type`, `V` basis (ATR-SMA assumed start center; ATR-Wilder vs rescaled-Stdev UNKNOWN alternatives — three-way lives in H2b, H5-minimal starts ATR-SMA), `N`, `m`, gap length `g` (1 vs 2 bars), guard params (`eps`, `h`, reclaim) + guard family (OPEN in H5 by design), leg-choice fallback, `k_pre/k` triangle lookbacks (inherit H4-secondary, NOT redefined), 2h session, black-segment anomaly (obs §9 UNKNOWN), SNOW legend date UNKNOWN (D-H2, no date invented).
- Grid scope below is HYPOTHESIZED scope for experimenter to pre-declare (NOT locked params, NOT instruction to fit silently — new `(m,N)` needs new grid justification with fit/held-out split + sensitivity/overfit per Gate D).

### Predictions (all HYPOTHESIZED; OHLCV-detectable unless noted)

- P5.1 (display): `LINE5 − central == central − LINE6` (±0.002) + `LINE5 > central > LINE6` strictly incl. gaps; same as P1.1/P1.2/P2.1 (structural `mid±W`). [Pixel already SUPPORTED 21/21 — distinguishes vs H3-option-A only.]
- P5.2 (dates = H2 leg): 18/18 held-out windows hit (±5td padded per `heldout_results.md` §Inputs) + D2 earliest-window hits retained (DELL W1 ≥1 Sep-2025, MRNA W1 ≥1 May–Jun-2026) + KILL-distribution reproduced (in-window cross-dated flips with close inside H1-bands ≥15 total — HYPOTHESIZED band, vs observed 19). [If H5 loses ≥2/18 windows, its cross leg fails identically to H1-silence.]
- P5.3 (widths = H1 leg): single-bar hw_err returns to H1-like bands — HYPOTHESIZED: META ∈ [−5,+5] (vs old-H2 +53.022), MU ∈ [−4,+4] (vs +6.175), MRNA ∈ [−3,+3] (vs +9.843); RMSE<5 on ≥5/6 scored triples (vs old-H2 3/6; SNOW excluded per D-H2); central miss stays slow-leg-like (≈ +14.6 META / +0.3 MU / +2.3 MRNA — shared-leg prediction, NOT a fix claim). [Same three anchors D3–D5; pixel extension obs §6 stays extension-tolerant.]
- P5.4 (gap/whipsaw BOUNDARY with H2b — discriminator, HYPOTHESIZED): H5-minimal (cross+ATR, guard OPEN) predicts dates+widths JOINTLY but does NOT promise gap-zero or ≤3× whipsaw — MSFT 2024-11-14/15 zero-run MAY persist (gap_viol ≥0) and whipsaw MAY stay ~4×/107-total-like. If P5.2+P5.3 pass while gap_viol ≥1 or median >3×, H5-minimal is CONFIRMED as width/date fix and the residual routes to guard → H2b (guarded ATR-SMA ≡ H5+guard). If P5.2+P5.3 pass AND gap_viol=0 AND median ≤3× without any guard, H5-minimal subsumes H2b (guard unnecessary — prefer H5 parsimony).
- P5.5 (flip-vs-secondary unchanged): triangles stay H4-secondary (P4.4 <50% coincidence; obs §5 sparsity 0–8/view, lag/multiplicity Dell Dec–Jan/MU/CRM/NKE) — H5 predicts NO change to arrow census (21%/35% regime). [Pixel already SUPPORTED — H5 must not revive flip-markers.]

### Falsification experiment

- **Exp-H5 (needs NEW OHLCV grid — NOT a locked-triple rescore; BEST-H1/BEST-H2 locked params do NOT score H5):** HYPOTHESIZED grid scope (experimenter must pre-declare + log every combo, fit/held-out split, sensitivity/overfit per Gate D — NOT silent fit): `S{hl2,close} × MAf{5,8} × MAs{60} × type{EMA} × V{ATR-SMA} × N{10,14} × m{1.0,1.5,2.0}` minimal-first (Wilder/rescaled-Stdev + wider `wf/ws` live in H2b, NOT H5-minimal), cross-trigger with gap `g∈{1,2}` pre-declared, guard OFF (minimal). Fit on MCD+NKE (same 3 windows/padded rule per `fit_mcd_nke.md`), confirm scoring-only on held-out 7 (same 18 windows per `heldout_results.md` §Inputs) with pre-declared tolerances: 18/18 windows (P5.2) AND RMSE ≥5/6 + hw_err bands P5.3. **Kills H5 if:** (joint fail) no `(m,N)` reproduces dates AND widths simultaneously within tolerances (i.e. every `(m,N)` hitting 18/18 misses P5.3 bands, and every `(m,N)` hitting P5.3 loses ≥2/18 windows — width/date trade-off fatal); OR (central fail) shared slow-leg central cannot hold P5.3 central-miss pattern (≈ slow-leg-like) while any fast-leg central does (leg assumption wrong — route to fast-leg variant, H5-minimal dead); OR (split fail) H5 passes fit 3/3 + RMSE but collapses held-out (<13/18 or RMSE <4/6 — overfit, same verdict logic as `heldout_results.md` §Verdicts). Gap/whipsaw does NOT kill H5-minimal (P5.4 boundary — residual routes to H2b guard test). D4 ±1 bar-index uncertainty applies. Pixel pre-checks already DONE — do not re-run pixel census.
- HYPOTHESIZED grid scope above is a hypothesis about where to look, NOT evidence and NOT permission to retune silently — every combo logged, negatives kept, fit/held-out split + sensitivity/overfit required (Gate D).

**Current status:** `HYPOTHESIZED` + UNTESTED (new Hn; inherits H2-P2.2 date SUPPORTS + H1 width WINS as motivation, proves neither). Do not implement until Exp-H5 passes pre-declared joint tolerances. Only validator can mark VALIDATED.

**Relative ranking:** test-priority tier — H5+H4 (minimal hybrid, parsimony-first) vs H2b+H4 (guarded repair, robustness-first); H5 tested FIRST (smaller grid), H2b second (guard sweep). Ranking ≠ proof; joint date+width win must survive the pre-declared grid or H5 dies.

---

## H3 — Donchian / Chandelier trailing-stop family (N-bar extreme + ATR ratchet)

**Current status:** `HYPOTHESIZED` + pixel-FALSIFIED (core falsified at pixel level per `tmp/experiments/mg-trend/gate_d_pixel_log.md` runs 2+4 + `exp_symmetry.md` + `exp_h3_steps.md`; kill record kept below — revival requires a new smoothed-extreme variant with fresh pixel-detectable predictions. Only validator can mark VALIDATED; this status is not validated.)

### Claim

Central is a ratcheted trailing stop off N-bar extremes; bands are Donchian extremes (or stop ± width). State flips when price takes out the stop.

Formulas (all HYPOTHESIZED, params UNKNOWN):

- `HH_t = highest(H, N)`, `LL_t = lowest(L, N)`, `midD_t = (HH_t + LL_t)/2`, `N` UNKNOWN (candidate 20–55).
- Chandelier variant: `stopLong_t = max(stopLong_{t−1}, HH_t − m·ATR_N(t))` in up state; `stopShort_t = min(stopShort_{t−1}, LL_t + m·ATR_N(t))` in down state (ratchet: only moves favorably).
- `state_t`: `+1` until `close_t < stopLong_t` (or `low_t < LL_{t−1}` in pure Donchian-break variant) → `−1`; symmetric reverse. Gap `na` for 1 bar at flip (HYPOTHESIZED).
- Display option A (edge-plotted, classic): `central = stopLong` in up / `stopShort` in down; `upper/lower = HH/LL` — predicts ASYMMETRY (central == one edge). Display option B (mid-plotted): `central = midD`, bands = `HH/LL` — predicts exact symmetry by construction (`HH−mid == mid−LL`) but predicts stepped/flat bands.
- Smoothing: none beyond `ATR_N`; extremes are unsmoothed → predicts stair-steps/flats.
- Init: `N` bars `na`, hidden → G9. No normalization, no fixed thresholds, repaint HYPOTHESIZED none (stops confirm on close).

External research (HYPOTHESIZED only): Donchian channels, Chandelier exit (LeBeau), ZigZag stops — inform the family, prove nothing about `mg-trend`.

### Supporting evidence refs

- G5 trailing placement: §6 up-red below price / down-green above price matches a trailing stop; §6 MCD/CRM/NKE down-trend central above price fits `stopShort` ratchet.
- G7 gaps: §4 flip gaps fit stop-flip `na` while `HH/LL` persist continuously.
- G6 arrows: §5 arrows at local highs/lows fit N-bar breakout triggers (e.g. BE Sep-3 low, MSFT late-Jul gap-low, META Aug-26–28 lows).
- Counter-evidence noted (why ranked lower): G8 smoothness §3 (smooth curves through MRNA/MSFT gaps) contradicts unsmoothed extreme steps; G4 exact symmetry (BE ±15.432 to 3dp across 7+ samples §6) contradicts edge-plotted option A and forces option B, which then predicts visible flats/steps not observed.

### Assumptions

1. An N-bar extreme (not an MA) anchors the system.
2. Ratchet (stop never moves adversely within a state).
3. Symmetry samples are either structural (option B mid-plot) or coincidental (option A) — experiment must decide.

### Unknowns

- `N`, `m`, ATR vs pure-break variant, edge- vs mid-plot, `S`, session/2h, triangle/break vs secondary, warm-up length.

### Predictions

- P3.1 (steps): `upper/lower` (and central under option A) show multi-bar flats (equal values to 3dp across ≥3 consecutive bars) at `HH/LL` plateaus, and vertical jumps when a new extreme forms; digitized slope histogram is bimodal (0 vs jump), unlike H1/H2 smooth unimodal. [pixel-FALSIFIED per `tmp/experiments/mg-trend/exp_h3_steps.md` + `gate_d_pixel_log.md` run 4 + D3 (eye-not-digitizer caveat): 0 exact flats on any track in MU+NKE primary + Dell-red/SNOW/MCD/MRNA supporting views; smooth unimodal curvature everywhere — H1-P1.5/H2-smooth passes the same views]
- P3.2 (asymmetry under option A): `LINE5−central ≠ central−LINE6` generally; observed 3dp equalities are sampling luck and break on full series. Under option B symmetry holds but P3.1 steps must appear. [option A pixel-FALSIFIED per `tmp/experiments/mg-trend/exp_symmetry.md` + `gate_d_pixel_log.md` run 2: 21/21 resid ≤0.001, mean 0.000 — systematic symmetry ≠ luck; D5 sub-0.001 caveat. Option B then owes P3.1 steps, which failed above — both display options closed at pixel level]
- P3.3 (flip bars): flips coincide with `close` taking out prior `LL`/`HH` (or stop), not with MA cross and not necessarily with opposite symmetric-band penetration. [OHLCV-gated UNTESTED without data/ per `gate_d_pixel_log.md` §What remains OHLCV-gated item 1 — but core already pixel-FALSIFIED via P3.1/P3.2, so a P3.3 match alone cannot revive H3 without a smoothed-extreme variant]
- P3.4 (far extension): after a gap breakout (MRNA Aug, MSFT late-Jul §3/§6) the stop ratchets quickly to the breakout extreme, so price should re-touch the stop within few bars — prolonged weeks-long extension without flip contradicts tight-ratchet variant, forcing large `N`/`m`. [untested without data/; visual extension weeks-long already strains tight-ratchet variant]
- P3.5 (triangles — BREAKOUT model, a FLIP subtype): arrows mark `HH/LL` breaks; central need not flip same bar if break is against ratchet direction (e.g. upside break during green = green arrow without flip). Secondary band-touch arrows without any N-bar break falsify H3-triangle. [WEAKENED as 1:1 rule per `tmp/experiments/mg-trend/exp_h4_census.md` + `gate_d_pixel_log.md` run 1: same 21%/35% non-coincidence counts; breakout-without-flip allowance keeps isolated cases (e.g. MCD R→G-bar red) alive but as a general predictor it fails]

### Kill record (pixel level, 2026-09-28 — DO NOT DELETE)

- Pre-registered kill criterion (see Falsification experiment below): smooth curvature with no flats at pixel resolution AND symmetric ordering bar-for-bar → option A dead + option B step prediction dead. Criterion MET: `exp_h3_steps.md` 0 flats + `exp_symmetry.md` 21/21 symmetry + smooth gap traversal.
- H3 core (N-bar extreme + ATR ratchet as generator of central/bands) is therefore FALSIFIED at pixel level. Status stays `HYPOTHESIZED` + pixel-FALSIFIED (label discipline: only validator can mark VALIDATED or close a candidate; this record is the experimenter pixel verdict absorbed by reconstructor).
- Revival requires a NEW smoothed-extreme variant (reconstructor call, not yet tabled): e.g. heavily smoothed `HH/LL` or extreme-fed MA converging toward H1/H2 behavior, WITH fresh pixel-detectable predictions distinct from H1-P1.5/H2-smooth (e.g. predicted residual step signature at digitized resolution, or asymmetric response to gap bars). Numeric slope-histogram confirmation on sourced OHLCV stays OHLCV-gated.

### Falsification experiment

- **Exp-H3 (pixel-first, then OHLCV):** (i) digitize `LINE5/LINE6`/central pixel tracks from 2 long Daily views (MU Sep 2025–Oct 2026, NKE Dec 2025–Oct 2026 §7) and test flat-step frequency: ≥5 multi-bar exact flats SUPPORTS Donchian, near-zero flats FALSIFIES H3 (smooth MA families win). (ii) On sourced OHLCV, compute `HH_N/LL_N` grid and check flip-date match vs H1/H2 rules. **Kills H3 if:** smooth curvature with no flats persists at pixel resolution AND symmetric ordering holds bar-for-bar (option A dead, option B step prediction dead) — i.e. P3.1 fails while H1-P1.5/H2-P2.3 pass.

**Current status:** `HYPOTHESIZED` + pixel-FALSIFIED — kill record above; unsmoothed-extreme core dead at pixel level; revival requires smoothed-extreme variant (not yet tabled). Gate-D held-out adds NOTHING for/against H3 (H3 never gridded fit/held-out; no arrow dates invented for P3.5; no OHLCV H3 run). Kill record KEPT, no revival. Do not implement.

**Relative ranking:** LAST (behind H5+H4, H2b+H4, and killed-H1-as-width-reference). Ranking ≠ proof; promotion requires a new smoothed-extreme variant with fresh pixel-detectable predictions that survive digitized slope-histogram test.

---

## H4 — Two-layer signal model (central flips = primary state; triangles + 机构进/出/筑顶/筑底 = secondary filter)

**Current status:** `HYPOTHESIZED` + pixel-SUPPORTED (core secondary claim SUPPORTED per `tmp/experiments/mg-trend/gate_d_pixel_log.md` run 1 + `exp_h4_census.md`; P4.1/P4.3/P4.4 pixel-SUPPORTED, P4.2 violated twice → REVISED 2026-09-28 with documented exceptions — only validator can mark VALIDATED)

### Claim

Orthogonal to H1–H3 core: whatever generates central/bands, the sparse triangles and small Chinese labels are a SECONDARY conditional layer, not flip markers. LINE7–12 blank because shapes/text do not occupy legend number slots in this chart app (or are reserved).

HYPOTHESIZED secondary rules (params UNKNOWN; P4.2 REVISED 2026-09-28 — exceptions documented, not hidden):

- Red-up `▲` (+ magenta `机构进`): printed iff `state=+1` (or flips to `+1` within last `k` bars) AND (`low_t ≤ lower_t` touch/penetration OR `close_t` reclaims `central_t` after pullback). Hence arrows at lows/lower-band (§5) and the MRNA Aug gap-bar arrow while already red (§5 `MRNA_Screenshot_2026-09-28_14-32-27.png`).
- Green-down `▼` (+ grey `机构出`): iff `state=−1` AND (`high_t ≥ upper_t` OR rejection at `central_t` from below). Hence mid-green arrows lagging flips (Dell Dec–Jan §5) and multiples per trend (CRM ~15, MU ~5 §2/§5).
- `筑底` (red, near lows/lower) / `筑顶` (cyan, near highs/upper) mark extreme-extension touches, independent of arrows.
- Placement 1–2% beyond wick, same bar (§4 OBSERVED) = render offset, not data offset; no legend value because shapes carry no series value.
- REVISED exceptions to strict color-conditional (P4.2 violated twice per `tmp/experiments/mg-trend/exp_h4_census.md` + `gate_d_pixel_log.md` D2 — core secondary claim unaffected, rule widened with new pixel-detectable prediction below):
  - E1 early-warning/lookahead print: `META_Screenshot_2026-09-28_14-43-42.png` first red (~Aug-21, below ~543) prints DURING green ~5 days BEFORE the Aug-26 G→R flip. HYPOTHESIZED allowance: secondary layer may print an opposite-side touch signal up to `k_pre` bars before the flip (early lower-band touch anticipating the turn) — i.e. color-conditional holds for ≥~95% of arrows, with rare pre-flip opposite-side touches permitted.
  - E2 opposite-side touch at flip bar: `MCD_Screenshot_2026-09-28_14-44-21.png` red-up prints AT the R→G flip bar (wrong direction for the new green state). HYPOTHESIZED allowance: at a flip bar both sides' touch conditions may evaluate on the same bar (low touches lower even as state resolves green), printing a contrarian arrow that the next-bar state immediately supersedes.

### Supporting evidence refs

- Sparsity + non-coincidence: §2 (0–8 arrows/view while color persists dozens of bars); §5 (Dell reds continue Oct–Nov while greens print Dec–Jan; MRNA red since Jun yet arrow at Aug gap; MU red Sep–Jul with ~5 arrows; NKE green Feb–Sep with ~6 arrows) — flip-model (1:1) fails these cases; secondary-model predicts exactly this lag/multiplicity. Pixel census per `tmp/experiments/mg-trend/exp_h4_census.md` + `gate_d_pixel_log.md` run 1 + D4 (±1 uncertainty): arrows-with-flip 21/99 raw (21%), de-dup 17/82 (21%); flips-with-arrow 19/57 raw (33%), de-dup 14/40 (35%); fit 13/56 (23%) vs held-out 8/43 (19%) — same low regime both halves, no split artifact; P4.1 multiplicity CONFIRMED (Dell-14-31-21 7 reds/0 flips; NKE 6 greens/0 post-Mar flips; CRM ≥5 greens one run; MU 5 reds/4 flips; MCD 6 greens one run).
- Location: §5 reds at/near lower + restart, greens during green near upper; §2 labels cluster at bands/extremes (`机构进` lower, `机构出` upper, `筑顶` highs/upper, `筑底` lows/lower) across Dell/MSFT/META/SNOW/MU/MCD/CRM/NKE examples.
- LINE7–12 blank at every crosshair in all 21 (§1) — shapes/text layer carries no legend values; consistent with secondary annotation layer.

### Assumptions

1. Signal layer reads central/bands/price but does not feed back into state.
2. Offsets are render-only; signal bar = trigger bar (no shift).
3. Labels and triangles share trigger logic (label = regime context, triangle = trigger bar).

### Unknowns

- Exact touch tolerance, lookback `k`, whether volume/momentum filter gates signals (Volume shown in OHLC box §7 but no signal-volume link OBSERVED), label dictionary completeness, why 12 slots when 6 suffice.

### Predictions

- P4.1: arrow count ≪ trend-bar count in every view; ≥1 trend shows ≥3 same-direction arrows without intervening flip (MU, CRM, NKE §2/§5 already suggest this — confirm by census). [pixel-SUPPORTED per `tmp/experiments/mg-trend/exp_h4_census.md` + `gate_d_pixel_log.md` run 1: CONFIRMED in Dell-14-31-21 (7 reds/0 flips), NKE (6 greens/0 post-Mar flips), MU, CRM (≥5 greens one green run), MCD (6 greens one run)]
- P4.2 (REVISED 2026-09-28 — strict color-conditional VIOLATED twice, rule widened): OLD strict form ("no arrow precedes its trend flip; red only during/after red, green only during/after green") violated by 2/82 de-dup arrows per `tmp/experiments/mg-trend/exp_h4_census.md` + `gate_d_pixel_log.md` D2: (i) `META_Screenshot_2026-09-28_14-43-42.png` first red ~Aug-21 during green ~5 days pre-flip; (ii) `MCD_Screenshot_2026-09-28_14-44-21.png` red-up AT the R→G flip bar (wrong direction). REVISED form: ≥~95% of arrows are color-conditional (red during/after red, green during/after green), with two documented exception classes permitted — E1 early-warning/lookahead opposite-side touch up to `k_pre` bars pre-flip, E2 contrarian touch print at the flip bar itself. NEW pixel-detectable prediction: on full-series digitization, pre-flip/contrarian arrows (a) are rare (≤~5% of arrows), (b) coincide with an opposite-side band touch on the arrow bar (low ≤ lower for pre-flip reds, high ≥ upper for pre-flip greens), and (c) are followed by a flip in the arrow's direction within `k_pre` bars (E1) or resolve against the arrow same-bar (E2). [HYPOTHESIZED; core secondary claim unaffected — 80/82 arrows conform]
- P4.3: arrow bars touch/penetrate the same-side band OR sit at local extreme within `k` bars post-flip; arrows mid-channel without band touch or extreme are rare/absent. [location-consistent per obs §5; numeric touch test OHLCV-gated without data/ — extended by revised-P4.2 prediction (b) above to cover exception bars]
- P4.4: flips without arrows are common; arrows without flips are common; same-bar flip+arrow coincidence rate is low (<50%) — the quantitative flip-vs-secondary discriminator for H1/H2/H3 triangle sub-claims. [pixel-SUPPORTED per `tmp/experiments/mg-trend/exp_h4_census.md` + `gate_d_pixel_log.md` run 1: 21% arrows-with-flip, 33–35% flips-with-arrow both directions; threshold met raw and de-dup, fit and held-out]

### Falsification experiment

- **Exp-H4 (pixel-only, EXECUTED 2026-09-28 — see `tmp/experiments/mg-trend/exp_h4_census.md` + `gate_d_pixel_log.md` run 1 + D2/D4):** census of all 21 PNGs recorded (color, band-touch y/n, days-since-last-flip sign) per triangle and arrow-within-±1-bar per flip. Result: coincidence 21%/33–35% (raw), 21%/35% (de-dup), fit 23% vs held-out 19% — far from ≈1.0 both ways, so H4-secondary SURVIVES and flip-signal sub-claims (OLD H2-P2.5, H3-P3.5 as 1:1) are FALSIFIED/WEAKENED as 1:1 rules; H1-P1.6-secondary SUPPORTED. **Kills REVISED H4-secondary if (new test):** on sourced OHLCV full series, EITHER (a) two-way arrow↔flip same-bar (±1) coincidence ≈ 1.0 (flip-marker revival); OR (b) ≥3 triangle bars show no same-side band touch AND no local extreme within `k` bars post-flip AND no central-reclaim AND no E1/E2 exception signature (opposite-side touch + flip within `k_pre`); OR (c) pre-flip/contrarian arrows exceed ~10% of arrows or lack opposite-side band touch (exception rate blows the ≤~5% + touch requirements of revised P4.2). D4 ±1 bar-index uncertainty applies.

### P4.5 numeric 筑底/筑顶 label rule (HYPOTHESIZED, UNTESTED — tabled 2026-09-29, Moomoo Daily preferred)

**Claim (one-liner, HYPOTHESIZED):** `筑底` fires iff Daily `low` touches `lower` (`low_t <= lower_t + 0.10·W_t`) AND 11-bar local-low extreme (`k=5`) or central-reclaim AND green/gap/just-flipped-or-E1 state from locked H5; `筑顶` is the mirror (`high_t >= upper_t − 0.10·W_t`, local-high, red/gap/just-flipped-or-E1). Ranking ≠ proof; only validator can mark VALIDATED.

**Trigger inputs (all from locked H5, NO refit):** Moomoo Daily OHLCV + `run_h5` outputs under locked BEST-H5 `hl2/MAf5/MAs60/EMA/ATR-SMA10/1.5/g1` (same bytes VALIDATED per `tmp/validation/mg-trend/diff_rev1.md`; scoring-only, no grid, no param change — H5 stays locked). Per bar `t` (Daily, H5-ready, bands defined; warm-up `max(maf,mas,N)=60` bars `na` excluded): `state_t ∈ {+1,−1,0}`, `central_t`, `upper_t (=LINE5)`, `lower_t (=LINE6)`, `W_t = (upper_t − lower_t)/2`, `tol_t = 0.10 · W_t`. Daily preferred to match VALIDATED scope (`diff_rev1.md` Gate F/G Daily-only, no arrows; all `筑底/筑顶` cited examples in obs §2 fall in Daily windows: Dell Aug-2026, MSFT Jun-2026, SNOW Feb-2026, MU Jul-2026 top `1255.000`, MSFT Jun-2026 / MCD May+Aug-2026 / CRM May-2026 / NKE Jul-2026 bottoms). 2h (BE/MSFT-2h/META-2h) ONLY if Daily insufficient — i.e. digitized label dates fall in 2h-only views with no Daily counterpart, or Moomoo Daily anchor mismatch forces a session check (obs §9 2h-bar session UNKNOWN) — state why in log if invoked.

**Exact inequalities (HYPOTHESIZED params pre-declared, no tuning):** `k=5` (extreme lookback ±5td), `k_pre=5` (E1 lookahead), `tol=0.10·W_t` (≈0.7–1.7% of price given half-widths 7–17% per obs §6 — matches 1–2% render offset obs §4 + 3dp rounding + half-cent prints per `data/PROVENANCE.md`).
- `B_t (bottom-touch) := low_t <= lower_t + tol_t`; `T_t (top-touch) := high_t >= upper_t − tol_t`.
- `BE_t := low_t == min{Low[max(0,t−5) .. min(N−1,t+5)]}` (edge-truncated); `TE_t := high_t == max{High[t−5 .. t+5]}`.
- `Reclaim_B(t) := close_t > central_t AND exists j∈[1..5] with B_{t−j}` (pullback touch then same-bar reclaim above mid); `Reclaim_T(t) := close_t < central_t AND exists j∈[1..5] with T_{t−j}`.
- `cond_extreme_or_reclaim_底 := BE_t OR Reclaim_B(t)`; `cond_extreme_or_reclaim_顶 := TE_t OR Reclaim_T(t)`.
- `cond_state_底 := (state_t ∈ {−1,0}) OR (state_t==+1 AND first-new-state +1 ∈ [t−5,t]) OR E1: (state_t==−1 AND flip to +1 ∈ (t+1..t+5])`; `cond_state_顶 := (state_t ∈ {+1,0}) OR (state_t==−1 AND first-new-state −1 ∈ [t−5,t]) OR E1-mirror`. Gap-bar `state 0` covers E2 (contrarian touch at flip bar, e.g. MCD R→G red-up per `exp_h4_census.md` #17).
- **P4.5-底 fires iff `B_t AND cond_extreme_or_reclaim_底 AND cond_state_底`; P4.5-顶 iff `T_t AND cond_extreme_or_reclaim_顶 AND cond_state_顶`.** D4 ±1 bar-index uncertainty applies to all timing checks.

**Supporting evidence refs:** obs §2 labels cluster at bands/extremes (`机构进` lower, `机构出` upper, `筑顶` highs/upper, `筑底` lows/lower across Dell/MSFT/META/SNOW/MU/MCD/CRM/NKE) + obs §5 reds at/near lower+restart, greens during green near upper + obs §4 1–2% same-bar placement (render offset) + H4 P4.1/P4.4 sparsity/non-coincidence (21%/35% per `exp_h4_census.md`) + E1 META-2h `14-43-42.png` pre-flip red ~Aug-21 + E2 MCD `14-44-21.png` red-up at R→G flip bar + `state.md` Gate D PASS H5 / Gate F/G Daily-only + `diff_rev1.md` VALIDATED scope (Daily-only, no arrows) + `tmp/experiments/mg-trend/` has NO H4 OHLCV work (only `exp_h4_census.md` pixel-only + `heldout_results.md` §Verdicts P4.2 DEFERRED — no arrow/label dates invented).

**Assumptions (inherit H4 1–3 + new):** 4. Signal layer reads locked-H5 outputs only, no feedback into state. 5. `tol=0.10·W`, `k=k_pre=5` are pre-declared hypotheses, not fits. 6. Label bar = trigger bar (no shift); digitized pixel dates carry ±1 uncertainty. 7. Labels and triangles share state/bands but labels test extreme-touch path (P4.5), triangles test pullback-reclaim path (P4.2/P4.3) — one rule, two label directions.

**Unknowns:** label dictionary completeness (only `筑底/筑顶` + `机构进/出` OBSERVED); label counts per view (no census yet — Exp-H4-numeric stage 1); whether volume/momentum gates labels (Volume in OHLC box obs §7, no signal-volume link OBSERVED); 2h session definition (obs §9); why 12 slots.

**Quantitative predictions (all HYPOTHESIZED, Moomoo Daily, locked H5, ±1):** (i) touch rate ≥80% (`筑底` satisfy `B_t`, `筑顶` satisfy `T_t`); (ii) extreme-or-reclaim ≥70% (`BE/TE` or `Reclaim`); (iii) state-context ≥95% (≤5% E1/E2); (iv) every E1/E2 shows opposite-side touch 100% (`B_t`/`T_t` true on exception bar); (v) label↔flip same-bar (±1) coincidence <50% both directions (same discriminator as P4.4 — labels are NOT flip markers); (vi) sparsity: label count ≪ trend-bar count per window (0–8/view regime per obs §2).

### Kill criteria P4.5 (explicit, OHLCV-measurable — any one kills P4.5, H4-core reverts to pixel-only)

- **K1 (trigger failure):** ≥3 digitized label bars (Moomoo Daily, locked H5, ±1) show NO same-side touch AND NO local extreme within `k=5` AND NO reclaim AND NO E1/E2 signature (opposite-side touch + flip within `k_pre=5`).
- **K2 (flip-marker revival):** two-way label↔flip same-bar (±1) coincidence ≈1.0, defined verbatim as ≥85% labels-with-flip AND ≥85% flips-with-label on full series.
- **K3 (exception-budget blown):** `(E1+E2)/N_labels > 10%` (2× the ≤5% budget) OR ≥2 E1/E2 bars lack opposite-side touch (`B_t`/`T_t` false).
- D4 ±1 applies; SNOW date-UNKNOWN excluded from rate denominators where date undigitizable (D-H2 precedent); BE 2h never scores Daily rule.

### Exp-H4-numeric (for experimenter — HYPOTHESIZED scope, NOT silent-fit, NO H5 refit)

- **Stage 1 pixel label census (no OHLCV):** digitize every `筑底`/`筑顶` bar date per 21 PNGs to day precision (±1; 2h views to 2h stamp where legible) + record state color at bar + visual band-touch y/n; publish counts (no dates invented beyond ±1). Do NOT re-run `exp_h4_census.md` triangle census (DONE 21%/35%).
- **Stage 2 Moomoo Daily OHLCV (preferred source per USER directive):** fetch Daily 2024-01-01→2026-09-28 (≥12mo warm-up before Sep-2025 left edge) for the SAME 7 held-out tickers / SAME 18 windows per `heldout_results.md` §Inputs (CRM 2: [2025-11-01..2026-02-28]+[2026-03-01..2026-08-31]; MU 3: [2026-03-01..03-31]+[2026-03-15..04-30]+[2026-08-01..08-31]; SNOW 2: [2025-12-01..12-31]+[2026-05-01..05-31]; DELL 3: [2025-09-01..09-30]+[2025-11-01..11-30]+[2026-03-01..03-31]; MRNA 3: [2026-05-01..06-30]+[2026-07-10..07-31]+[2026-08-01..08-20]; MSFT 2: [2026-06-01..06-30]+[2026-07-28..08-03]; META 3: [2026-07-01..07-15]+[2026-07-10..07-31]+[2026-09-01..09-15]; total 18). Moomoo symbols: US-equities CRM/MU/SNOW/DELL/MRNA/MSFT/META (verify vs header-last on fetch; mismatch = STOP that ticker). Fit MCD/NKE + BE 2h QUARANTINED (never score). Run locked `run_h5` (BEST-H5 verbatim) scoring-only.
- **Provenance/sha (required):** record provider (Moomoo OpenD quote API vs app export — state which), query timestamps UTC, ticker→symbol mapping, exchange/currency, split/dividend-adjustment flags, per-window anchor-bar match vs `PROVENANCE.md` 8 anchors (tolerance ±0.01 + half-cent notes; SNOW no anchor; BE quarantined), raw CSVs `tmp/experiments/mg-trend/data/moomoo_*_daily.csv` + append `CHECKSUMS.sha256`; NEVER under `assets/`; ≥1s between requests; `sha256sum -c` before scoring, MISMATCH = STOP that ticker, no substitution.
- **Metrics to log (per digitized label bar + aggregates):** date, type (底/顶), `state_t`, `central/upper/lower`, `W_t/tol_t`, `low/high`, touch bool + margin (`low−lower`, `high−upper`), extreme bool (window min/max values), reclaim bool, E1/E2 flag, bars-to-nearest-flip, coincidence flags; aggregates: touch rate 底/顶, extreme-or-reclaim rate, state-context rate, exception rate, label↔flip coincidence both directions, sparsity. Apply tolerances verbatim: `k=5`, `k_pre=5`, `tol=0.10·W`, `B_t/T_t/BE/TE/Reclaim/cond_state` as above, D4 ±1, kill thresholds K1 ≥3 / K2 ≥85% both / K3 >10%.
- **No H5 refit:** locked BEST-H5 `hl2/MAf5/MAs60/EMA/ATR-SMA10/1.5/g1` only; no grid, no tweaking; H5 VALIDATED scope untouched (`diff_rev1.md` Daily-only, no arrows). Verdict per label bar: SUPPORTED / WEAKENED / FALSIFIED for P4.5; negatives kept; fit/held-out split inherited (18 windows are held-out; no fit on labels).

**Current status:** `HYPOTHESIZED` + pixel-SUPPORTED (core P4.1/P4.4 stand; P4.2 E1/E2 revised) + P4.5 numeric label rule UNTESTED (tabled 2026-09-29, Moomoo Daily, locked H5, kill K1/K2/K3 pre-declared) — signal-layer modifier compatible with H5 (preferred composite H5+H4), H2b (guarded composite H2b+H4), and killed-H1 display reference. P4.2 triangles + P4.5 labels DEFERRED until Exp-H4-numeric (no arrow/label dates invented beyond ±1 digitization). Only validator can mark VALIDATED.

**Relative ranking:** co-lead as signal layer in BOTH live composites (H5+H4 parsimony-first, H2b+H4 robustness-first). Ranking ≠ proof.

---

## Relative ranking (provisional, ≠ proof) — REVISED 2026-09-28 after Gate-D held-out + diagnostics (H1 KILLED, H2 WEAKENED; H5/H2b tabled)

1. **H5+H4 (parsimony-first test priority)** — minimal hybrid: H2-P2.2 cross-trigger (dates: 18/18 sweep, H2 ⊇ H1, D2 earliest-window hits, 19 in-window inside-band crosses per `heldout_results.md` §Results/§Verdicts (d)) + H1-V ATR-envelope width (widths: D3–D5 hw_err H1 +1.137/−2.112/−0.673 vs H2 +53.022/+6.175/+9.843; shared slow-EMA60 central-identical META +14.569 / MU +0.298 / MRNA +2.301) + H4 secondary-signal layer (core pixel-SUPPORTED, P4.2 E1/E2 revised). Smallest new grid (Exp-H5 minimal-first). Must survive joint date+width tolerances (18/18 + RMSE≥5/6 + P5.3 bands) or H5 dies.
2. **H2b+H4 (robustness-first test priority)** — guarded repair: same cross dates + rescaled/ATR-family envelope (V-basis three-way UNKNOWN: ATR-SMA / ATR-Wilder / rescaled-Stdev; `k,N` UNKNOWN) + whipsaw guard (HYPOTHESIZED eps-confirm/min-hold/reclaim; params UNKNOWN) predicting median ≤3× WITHOUT breaking 18/18 + MSFT 2024-11-14/15 zero-run resolved to 0 gap_viol (D1) + per-regime hw_err bands P2b.3. Larger grid (Exp-H2b). Test SECOND (after H5-minimal); subsumed by H5 if H5-minimal hits gap-zero + ≤3× with no guard (P5.4 parsimony rule).
3. **H1 (KILLED trigger, retained width-reference)** — P1.3 band-break rule KILLED (fit KILL 2 + held-out KILL 19 + D2 mechanism confirmation); display math (P1.1/P1.2/P1.4/P1.5/P1.6) pixel-SUPPORTED and V-rule reused by H5. No longer a live trigger candidate; do NOT revive band-break rule.
4. **H2-old (WEAKENED, superseded)** — P2.2 date-core survives (18/18) but Stdev10/k=2.5 envelope killed on widths (D3–D5 systematic over-width) + D1 zero-run + 4.0× whipsaw; superseded by H2b/H5. Do NOT implement old envelope.
5. **H3 (LAST, pixel-FALSIFIED)** — kill record kept; Gate-D adds nothing (never gridded); promotion requires NEW smoothed-extreme variant with fresh pixel-detectable predictions surviving digitized slope-histogram test.

Explicitly: this ordering is a work-priority hypothesis, not a finding. Ranking ≠ proof. New evidence must be able to kill H5 and H2b (killers below). In particular H5 dies on joint date+width failure; H2b dies on sweep/guard trade-off fatality; H1-P1.3 stays KILLED (P1.1 pixel-SUPPORTED with D5 sub-0.001 caveat applies to display math only, not the trigger).

## What kills each (summary for experimenter) — REVISED 2026-09-28 after Gate-D held-out + diagnostics (H1 KILLED, H2 WEAKENED; H5/H2b tabled)

- **H1 (P1.3 ALREADY KILLED — kill record above; do NOT re-test to revive):** killed by fit KILL=2 + held-out KILL=19 (≥2 fires 6/7 tickers, 5 tickers EACH ≥2; `heldout_results.md` §Verdicts (d)) + D2 earliest-window mechanism confirmation (H1 MISSES DELL W1 Sep2025 + MRNA W1 May-Jun2026 where H2 hits all). Display-math killers (for the surviving structural reference only): best-fit symmetric `mid ± W` cannot reproduce all three traces within pixel tolerance while an asymmetric edge-plotted model can (P1.1 — pixel census already SUPPORTS 21/21, D5 sub-0.001 caveat); gaps mid-trend without flip (P1.4 — pixel already SUPPORTS 8/8 gaps-at-flips); Donchian flats on digitized histogram (P1.5 — pixel cross-check already passes, D3 digitizer caveat).
- **H2-old core (WEAKENED, superseded — old envelope do NOT implement):** P2.2 date-core survives (18/18 sweep) but dies as FAMILY if: no `(wf,ws,type)` pair reproduces ≥80% of ledger flip dates within ±1 bar while band-break does (P2.2 dead — already contradicted by 18/18, kept as logical killer); OR Stdev-envelope width failure stands unrepaired (D3–D5 hw_err +53.022/+6.175/+9.843 + RMSE 3/6 + §Verdicts (a)–(c)). REVISED P2.5-secondary dies if: ≥3 triangle bars show no same-side band touch AND no local extreme within `k` post-flip AND no central-reclaim AND no E1/E2 exception signature; OR two-way coincidence ≈ 1.0 on full series (flip-marker revival). OLD P2.5-flip already pixel-FALSIFIED (`exp_h4_census.md` 21%/35% vs ~100%; D4 ±1 uncertainty) — do not re-test the flip variant.
- **H5 HYBRID (new — joint killer, HYPOTHESIZED):** **H5 dies if:** (joint fail) NO `(m,N)` in the pre-declared Exp-H5 minimal grid reproduces dates AND widths simultaneously within pre-declared tolerances — i.e. every `(m,N)` hitting 18/18 windows misses P5.3 hw_err bands (META ±5 / MU ±4 / MRNA ±3) or RMSE<5 falls <5/6, AND every `(m,N)` hitting P5.3 loses ≥2/18 windows (width/date trade-off fatal — fails dates AND widths simultaneously); OR (central fail) shared slow-leg central cannot hold the slow-leg-like central-miss pattern while any fast-leg central does (leg assumption wrong); OR (split fail) fit 3/3 + RMSE passes but held-out collapses (<13/18 or RMSE <4/6 — overfit). Gap/whipsaw does NOT kill H5-minimal (P5.4 boundary — residual routes to H2b). Locked BEST-H1/BEST-H2 triple-rescore does NOT test H5 (new `(m,N)` needs new grid justification — state grid scope as hypothesis, NOT instruction to fit silently; every combo logged, fit/held-out split, sensitivity/overfit per Gate D).
- **H2b VARIANT (new — envelope + guard + gap-zero + sweep-retention killer, HYPOTHESIZED):** **H2b dies if:** (envelope) NO `(V-basis,N,m/c)` in the pre-declared Exp-H2b grid reproduces P2b.3 hw_err bands + RMSE ≥5/6 while holding 18/18 dates (width/date joint fail); OR (guard) EVERY guard reaching median ≤3× loses ≥2/18 windows (sweep/guard trade-off fatal — P2b.2 vs P2b.5 mutually exclusive; guard-suppressed total floor <40 also fails via over-smoothing into H1-silence); OR (gap) D1 2024-11-14/15 zero-run persists under ALL guard variants (MSFT gap_viol ≥1) or NEW mid-state na runs appear on any held-out ticker (gap_viol ≠ 0 anywhere); OR (basis) rescaled-Stdev needs regime-varying `c` (>2× across META-extension vs MU-calm) AND both ATR branches miss P2b.3 (family exhausted). Subsumed (not killed) if H5-minimal hits gap-zero + ≤3× with NO guard (P5.4 parsimony — prefer H5). New params need new grid justification (same Gate-D discipline as H5).
- **H3 (already pixel-FALSIFIED — kill record above):** revival requires a NEW smoothed-extreme variant; that variant dies if digitized slope histogram stays unimodal-smooth with zero multi-bar flats AND full-series symmetry holds (D3/D5 caveats resolved against it).
- **H4-secondary (core pixel-SUPPORTED) dies if:** OHLCV full series shows arrow↔flip coincidence ≈ 1.0 both directions; OR ≥3 triangles lack any same-side touch / post-flip extreme / reclaim / E1-E2 signature; OR pre-flip/contrarian arrows exceed ~10% or lack opposite-side touch (revised-P4.2 exception budget blown). Pixel census already executed (21%/33–35%, `exp_h4_census.md` + D2/D4) — do not re-run pixel Exp-H4; run the OHLCV exception-rate test.

## OHLCV-gated follow-ups (for experimenter — HYPOTHESIZED grid scope, NOT silent-fit instruction)

- All `HYPOTHESIZED`; pre-declare + log every combo; fit/held-out split (fit MCD+NKE 3 windows per `fit_mcd_nke.md`, confirm scoring-only held-out 7 / 18 windows per `heldout_results.md` §Inputs); sensitivity/overfit required per Gate D. New params need NEW grid justification — a locked-triple rescore of H5/H2b candidates under BEST-H1 (`hl2/EMA60/SMA10/1.5 2-bar gap`) or BEST-H2 (`hl2/MAf5/MAs60/EMA/Stdev10/2.5 1-bar gap`) does NOT test H5/H2b (different `(V-basis,m,N,guard)`); state grid scope as hypothesis, NOT instruction to fit silently. NO code run here; no `src/`/`tmp/` writes by reconstructor.
- F1 Exp-H5-minimal (test FIRST): `S{hl2,close} × MAf{5,8} × MAs{60} × type{EMA} × V{ATR-SMA} × N{10,14} × m{1.0,1.5,2.0}` cross-trigger, gap `g∈{1,2}` pre-declared, guard OFF; tolerances P5.2 (18/18 ±5td) + P5.3 (hw_err META ±5 / MU ±4 / MRNA ±3, RMSE ≥5/6 scored; SNOW excluded D-H2); D4 ±1 bar-index uncertainty. Kills H5 per joint/central/split fail (gap/whipsaw excluded per P5.4).
- F2 Exp-H2b-guarded (test SECOND; subsumed if H5-minimal hits gap-zero + ≤3× guardless per P5.4): `S{hl2,close,hlc3} × MAf{3,5,8} × MAs{50,60} × type{EMA,SMA} × V-basis{ATR-SMA, ATR-Wilder, Stdev-rescaled} × N{10,14,21} × m{1.0,1.5,2.0,2.5}` (or `k{1.5,2.0,2.5}+c{0.4,0.6,0.8}` rescaled-Stdev branch) `× guard{eps-confirm, min-hold h∈{2,3,5}, reclaim}`; tolerances 18/18 + RMSE ≥5/6 + P2b.3 bands + gap_viol 0 all tickers (D1 MSFT 2024-11-14/15 idx 220/221 must resolve state −1 continuation, nearest flips 212/230) + median ≤3× / total ∈ [50,90] / floor ≥40 (P2b.5). Must re-score MAf≥8 held-out (open MAf-fragility item per `gate_d_full_log.md`). Kills H2b per envelope/guard/gap/basis fail.
- F3 H4-secondary exception-rate (DEFERRED at Gate D — no arrow dates invented; OHLCV full series only when arrow bars datable): two-way arrow↔flip coincidence ≈ 1.0 kills secondary; OR ≥3 triangles lacking touch/extreme/reclaim/E1-E2; OR pre-flip/contrarian >10% or lacking opposite-side touch (revised-P4.2 budget). Do NOT re-run pixel Exp-H4 census (DONE: 21%/33–35%).
- F4 H3-smoothing (only if NEW smoothed-extreme variant tabled with fresh pixel-detectable predictions): digitized slope-histogram unimodal-smooth + zero multi-bar flats + full-series symmetry kills variant (D3/D5 caveats). No variant tabled — F4 parked.
- Provenance/scope: record exchange/split-adjustment per window (obs §9 UNKNOWN); BE 2h stays Gate-G quarantined (never fit/score Daily grids); MCD/NKE fit vs CRM/MU/SNOW/DELL/MRNA/MSFT/META held-out split DECLARED both sides used; `sha256sum -c CHECKSUMS.sha256` before any scoring (D-S1 precedent).

## Data-constraint note (no data/ exists — §0 KNOWN, §9 UNKNOWN)

- Pixel-derivable now (no OHLCV): symmetry census (P1.1), gap-flip alignment (§4), arrow-flip coincidence (Exp-H4), flat-step test (Exp-H3-i), left-edge truncation check (G9).
- OHLCV-gated (source externally same tickers/windows §7–§8 or accept UNKNOWN): flip-rule discriminator H1-P1.3 vs H2-P2.2 vs H3-P3.3, param fit (`w,N,m,k`), warm-up length, 2h session rule, repaint check. Do not assume exchange/split-adjustment (§9); record provenance per window.
- Uniform 3-decimal legend snapshots at 21 crosshairs (§6 values) are fit targets; bar-index ground truth stays UNKNOWN until data provenance is fixed (§9).

## External research (HYPOTHESIZED only)

- Supertrend (Seban: basic bands `hl2 ± m·ATR`, final-band ratchet, direction state), Chandelier (LeBeau: extreme ± ATR ratchet), Donchian channels, MA envelopes / Bollinger-style `basis ± k·vol` — inform families above; none proves `mg-trend` equivalence. Every use above is labeled HYPOTHESIZED pending Exp-H1..H4.

## Gate C checklist

- [x] ≥2 falsifiable candidates (H1–H5 + H2b) with claim | evidence refs (§+filenames) | assumptions | unknowns | predictions | falsification experiment | status | ranking — H5 new Hn full fields; H2b variant full fields; H1 kill + H2 WEAKENED updated; H3 kill kept; H4 DEFERRED (no arrow dates invented).
- [x] Every candidate labeled HYPOTHESIZED; ranking explicitly ≠ proof (H5+H4 vs H2b+H4 test-priority; only validator can mark VALIDATED).
- [x] Symmetry explainer (H1, also H2/H2b/H5; H3-option-B dead) ✓; gaps-with-continuous-bands explainer (H1/H2/H2b/H5; D1 MSFT 2024-11-14/15 zero-run → H2b guard prediction) ✓; per-candidate triangle flip-vs-secondary prediction (P1.6/P2.5/P3.5/H4/P5.5) ✓.
- [x] No code, no experiments run, no `src/`/`tmp/`/`assets`/`validation` writes; Gate-D numbers absorbed LOCKED (do NOT refit, no new numbers invented).
