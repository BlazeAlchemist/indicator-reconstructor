"""mg-trend H5-minimal core — production truth (IMPLEMENTED).

Hypothesis: H5-minimal (plans/mg-trend/hypotheses.md H5).
  Claim: cross-trigger flip rule (H2-P2.2, MAf x MAs) + ATR-envelope width
  (H1-V rule, SMA_N/m) on shared slow-leg central (MAs).
Status: SUPPORTED (Gate D pass: fit_h5_minimal.md 3/3 + rmse 0.3777;
  heldout_h5_results.md 18/18 windows, RMSE 5/6, hw 3/3).
  VALIDATED pending validator-only (never claimed here).
Locked params (BEST-H5, do NOT retune):
  S=hl2, MAf=5, MAs=60, type=EMA, V=ATR-SMA, N=10, m=1.5, g=1.
  Guard OFF. Slow-leg central.
Provenance:
  Yahoo Daily 2024-01-02 -> 2026-09-25 (tmp/experiments/mg-trend/data/
  PROVENANCE.md + CHECKSUMS.sha256). Fit anchors MCD 2026-07-02 /
  NKE 2026-07-08 (observations.md S1/S6).
Math provenance (byte-equiv, copied not re-derived):
  tmp/experiments/mg-trend/grid_h5_minimal.py run_h5 (lines 118-243).
  source hl2=(H+L)/2; EMA with SMA-seed (seed=sum(xs[:w])/w at w-1,
  then k=2/(w+1)); TR_t=max(H-L,|H-C_prev|,|L-C_prev|) with TR_0=H0-L0;
  ATR-SMA=SMA_N(TR); central=MAs (EMA60 hl2); V=m*ATR;
  upper=central+V (=LINE5); lower=central-V (=LINE6); mid=central.
  State: warm=max(5,60,10) bars na, prev_diff frozen across warm-up;
  diff=MAf-MAs; diff==0 -> state 0 na; cross (prev_diff!=0 and sign
  flip) -> state 0 na 1 bar (g=1); else +1 red if diff>0 else -1 green.
  pending/re-trigger kept for g param (default 1); g=2 = cross bar + 1
  pending bar (upper/lower stay defined through gap).
Display (render mapping, separate from calc):
  LINE1=LINE3=mid iff +1 else na; LINE2=LINE4=mid iff -1 else na;
  LINE5=upper, LINE6=lower always defined post-warm; LINE7-12 na.
Unknowns (stay UNKNOWN, never assumed):
  2h session definition; repaint beyond confirmed-close; LINE7-12 unused;
  triangles (H4) DEFERRED — do NOT implement arrows; H1-P1.3 band-break
  KILLED — do NOT implement; H2-old Stdev envelope superseded.
Deterministic: stdlib only, no I/O, no randomness, no time.
Calc/render separation: run_h5 (calc) returns central/upper/lower/state;
  render_lines (render) maps calc -> LINE1..LINE12 display slots.
"""

import math

__all__ = [
    "source_series",
    "sma",
    "ema",
    "ma",
    "true_range",
    "run_h5",
    "render_lines",
    "LOCKED",
]

# Locked BEST-H5 defaults (single source of truth for defaults).
LOCKED = {
    "S": "hl2",
    "MAf": 5,
    "MAs": 60,
    "type": "EMA",
    "V": "ATR-SMA",
    "N": 10,
    "m": 1.5,
    "g": 1,
}


def source_series(d, which="hl2"):
    """Price source series. Byte-equiv to grid_h5_minimal.py."""
    if which == "close":
        return list(d["C"])
    if which == "hl2":
        return [(h + l) / 2 for h, l in zip(d["H"], d["L"])]
    if which == "hlc3":
        return [(h + l + c) / 3 for h, l, c in zip(d["H"], d["L"], d["C"])]
    raise ValueError(which)


def sma(xs, w):
    """Simple moving average. Byte-equiv to grid_h5_minimal.py."""
    out = [math.nan] * len(xs)
    s = 0.0
    for i, v in enumerate(xs):
        s += v
        if i >= w:
            s -= xs[i - w]
        if i >= w - 1:
            out[i] = s / w
    return out


def ema(xs, w):
    """EMA with SMA seed. Byte-equiv to grid_h5_minimal.py.

    seed=sum(xs[:w])/w at index w-1, then k=2/(w+1).
    NOTE: Pine mirror must NOT use ta.ema (seeds differently);
    it implements this SMA-seed recursion manually.
    """
    out = [math.nan] * len(xs)
    k = 2.0 / (w + 1)
    if len(xs) >= w:
        seed = sum(xs[:w]) / w
        out[w - 1] = seed
        for i in range(w, len(xs)):
            out[i] = xs[i] * k + out[i - 1] * (1 - k)
    return out


def ma(xs, w, typ="EMA"):
    """MA dispatcher. Byte-equiv to grid_h5_minimal.py."""
    return sma(xs, w) if typ == "SMA" else ema(xs, w)


def true_range(d):
    """True range. Byte-equiv to grid_h5_minimal.py."""
    tr = []
    for i in range(len(d["C"])):
        if i == 0:
            tr.append(d["H"][0] - d["L"][0])
        else:
            tr.append(max(d["H"][i] - d["L"][i],
                          abs(d["H"][i] - d["C"][i - 1]),
                          abs(d["L"][i] - d["C"][i - 1])))
    return tr


def run_h5(d, S="hl2", maf_w=5, mas_w=60, typ="EMA", N=10, m=1.5, g=1):
    """H5 calc core (no rendering). Byte-equiv to grid_h5_minimal.run_h5.

    H2 cross-trigger (MAf x MAs, eps=0, prev_diff frozen across warm-up,
    diff==0 -> na) + H1 ATR-SMA width (V=m*SMA_N(TR)) on slow-leg central.
    Guard OFF: pending-bar raw cross re-triggers, no suppression.
    Central = slow leg MAs. g=1 -> 1-bar na at cross bar (H2 verbatim);
    g=2 -> cross bar + 1 following pending bar (H1 D-F2 verbatim,
    trigger=cross bar, upper/lower stay defined).
    Returns dict with central/upper/lower/state (+maf/mas/vol/first/cross
    diagnostics). state: +1 red, -1 green, 0 gap/na.
    """
    s = source_series(d, S)
    maf = ma(s, maf_w, typ)
    mas = ma(s, mas_w, typ)
    tr = true_range(d)
    vol = sma(tr, N)  # ATR-SMA only; Wilder excluded per H5-minimal scope
    n = len(d["C"])
    central = [math.nan] * n
    upper = [math.nan] * n
    lower = [math.nan] * n
    state = [0] * n
    warm = max(maf_w, mas_w, N)
    prev_diff = None
    cross = []
    pending = 0
    for i in range(n):
        if i < warm or math.isnan(maf[i]) or math.isnan(mas[i]) or math.isnan(vol[i]):
            continue  # gap/na; prev_diff frozen (no spurious cross across warm-up)
        diff = maf[i] - mas[i]
        V = m * vol[i]
        central[i] = mas[i]
        upper[i] = mas[i] + V
        lower[i] = mas[i] - V
        if pending > 0:
            # extra gap bar after a g=2 cross (upper/lower stay defined, central na)
            if prev_diff is not None and prev_diff != 0 and diff != 0 and (prev_diff <= 0) != (diff <= 0):
                cross.append(i)
                pending = 1  # re-trigger (guard OFF)
                state[i] = 0
                central[i] = math.nan
                prev_diff = diff
                continue
            state[i] = 0
            central[i] = math.nan
            pending -= 1
            prev_diff = diff
            continue
        if diff == 0:
            state[i] = 0
            central[i] = math.nan
            # no extra pending for touch-without-cross
        elif prev_diff is not None and prev_diff != 0 and (prev_diff <= 0) != (diff <= 0):
            # cross bar -> na (eps=0 variant)
            cross.append(i)
            state[i] = 0
            central[i] = math.nan
            if g == 2:
                pending = 1
        else:
            state[i] = 1 if diff > 0 else -1
        prev_diff = diff
    return {"central": central, "upper": upper, "lower": lower, "state": state,
            "maf": maf, "mas": mas, "vol": vol, "first": warm, "cross": cross}


def render_lines(calc):
    """Render mapping (display only, no math). Separate from calc.

    LINE1=LINE3=mid iff +1 else na; LINE2=LINE4=mid iff -1 else na;
    LINE5=upper, LINE6=lower always defined post-warm; LINE7-12 na.
    Input: calc dict from run_h5. Output: dict LINE1..LINE12 lists.
    NaN used for na (Pine na equivalent).
    """
    central = calc["central"]
    upper = calc["upper"]
    lower = calc["lower"]
    state = calc["state"]
    n = len(state)
    line1 = [math.nan] * n
    line3 = [math.nan] * n
    line2 = [math.nan] * n
    line4 = [math.nan] * n
    for i in range(n):
        if state[i] == 1:
            line1[i] = central[i]
            line3[i] = central[i]
        elif state[i] == -1:
            line2[i] = central[i]
            line4[i] = central[i]
    nan12 = [math.nan] * n
    return {
        "LINE1": line1, "LINE2": line2, "LINE3": line3, "LINE4": line4,
        "LINE5": list(upper), "LINE6": list(lower),
        "LINE7": list(nan12), "LINE8": list(nan12), "LINE9": list(nan12),
        "LINE10": list(nan12), "LINE11": list(nan12), "LINE12": list(nan12),
    }
