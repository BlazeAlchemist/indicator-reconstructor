"""Tests for mg-trend H5-minimal core (IMPLEMENTED, Gate E).

Hypothesis H5-minimal (plans/mg-trend/hypotheses.md H5), status SUPPORTED
(Gate D pass: fit_h5_minimal.md 3/3 + rmse 0.3777; heldout_h5_results.md
18/18 windows, RMSE 5/6, hw 3/3; VALIDATED pending validator-only).
Locked BEST-H5: S=hl2, MAf=5, MAs=60, type=EMA, V=ATR-SMA, N=10, m=1.5, g=1.
Provenance: Yahoo Daily 2024-01-02->2026-09-25, read-only from
tmp/experiments/mg-trend/data/ (CSVs NEVER copied into src; regression tests
skip if files absent). Unknowns: 2h session, repaint beyond confirm,
LINE7-12 unused, triangles deferred (no arrow tests).
Stdlib unittest only. Run: uv run python -m pytest src/python/test_mg_trend.py
or: uv run python src/python/test_mg_trend.py
"""

import csv
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mg_trend import (LOCKED, ema, ma, render_lines, run_h5, sma,
                      source_series, true_range)

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "tmp" / "experiments" / "mg-trend" / "data"

# Fit legend anchors (fit_mcd_nke.md Inputs + observations.md S1/S6):
# (ticker, date, central, upper, lower), state green (-1) at both.
ANCHORS = [
    ("MCD", "2026-07-02", 285.806, 295.945, 275.667),
    ("NKE", "2026-07-08", 45.252, 47.908, 42.597),
]
# Fit hw_err preview (model_hw - legend_hw, fit_h5_minimal.md BEST-H5).
HW_PREVIEW = {"MCD": -0.2975, "NKE": -0.3425}
# Fit gap residual for BEST-H5 g=1 (P5.4 verdict-neutral residual, fit log).
FIT_GAP_RESIDUAL = 5


def load_daily(ticker):
    p = DATA / f"{ticker}_daily.csv"
    if not p.exists():
        raise FileNotFoundError(p)
    dates, O, H, L, C = [], [], [], [], []
    with p.open(newline="") as f:
        for row in csv.DictReader(f):
            dates.append(row["Date"])
            O.append(float(row["Open"]))
            H.append(float(row["High"]))
            L.append(float(row["Low"]))
            C.append(float(row["Close"]))
    return {"dates": dates, "O": O, "H": H, "L": L, "C": C}


def synth_ramp(n, start, slope):
    d = {"dates": [f"BAR-{i:04d}" for i in range(n)],
         "O": [], "H": [], "L": [], "C": []}
    for i in range(n):
        c = start + slope * i
        d["O"].append(c)
        d["H"].append(c + 1.0)
        d["L"].append(c - 1.0)
        d["C"].append(c)
    return d


def synth_vshape(n_up=75, n_dn=75, start=100.0, slope=0.5):
    peak = start + slope * (n_up - 1)
    d = {"dates": [], "O": [], "H": [], "L": [], "C": []}
    for i in range(n_up + n_dn):
        if i < n_up:
            c = start + slope * i
        else:
            c = peak - slope * (i - n_up + 1)
        d["dates"].append(f"BAR-{i:04d}")
        d["O"].append(c)
        d["H"].append(c + 1.0)
        d["L"].append(c - 1.0)
        d["C"].append(c)
    return d


def flips(state):
    """First-new-state-bar flip indices (experiment flips() observable)."""
    out = []
    last = 0
    for i, s in enumerate(state):
        if s == 0:
            continue
        if last != 0 and s != last:
            out.append(i)
        last = s
    return out


def gap_violations(state, first):
    """Gap bars (state 0, i >= first) farther than 2 bars from any flip."""
    fl = set(flips(state))
    viol = 0
    for i, s in enumerate(state):
        if s == 0 and i >= first:
            if not any(abs(i - j) <= 2 for j in fl):
                viol += 1
    return viol


def assert_series_equal(tc, a, b, msg):
    tc.assertEqual(len(a), len(b), msg)
    for x, y in zip(a, b):
        if isinstance(x, float) and isinstance(y, float):
            if math.isnan(x) and math.isnan(y):
                continue
        tc.assertEqual(x, y, msg)


class TestLockedParams(unittest.TestCase):
    def test_best_h5_defaults(self):
        self.assertEqual(LOCKED, {"S": "hl2", "MAf": 5, "MAs": 60,
                                 "type": "EMA", "V": "ATR-SMA",
                                 "N": 10, "m": 1.5, "g": 1})

    def test_run_h5_defaults_match_locked(self):
        d = synth_ramp(70, 100.0, 0.5)
        a = run_h5(d)
        b = run_h5(d, S=LOCKED["S"], maf_w=LOCKED["MAf"],
                   mas_w=LOCKED["MAs"], typ=LOCKED["type"],
                   N=LOCKED["N"], m=LOCKED["m"], g=LOCKED["g"])
        assert_series_equal(self, a["central"], b["central"], "defaults")


class TestUnits(unittest.TestCase):
    def test_source_series(self):
        d = {"H": [10.0, 12.0], "L": [8.0, 10.0], "C": [9.0, 11.0]}
        self.assertEqual(source_series(d, "close"), [9.0, 11.0])
        self.assertEqual(source_series(d, "hl2"), [9.0, 11.0])
        self.assertEqual(source_series(d, "hlc3"), [9.0, 11.0])
        with self.assertRaises(ValueError):
            source_series(d, "bogus")

    def test_sma(self):
        out = sma([1.0, 2.0, 3.0, 4.0], 2)
        self.assertTrue(math.isnan(out[0]))
        self.assertEqual(out[1:], [1.5, 2.5, 3.5])

    def test_ema_sma_seed(self):
        # seed=sum(first w)/w at w-1, then k=2/(w+1); hand-computed.
        out = ema([1.0, 2.0, 3.0, 4.0, 5.0], 3)
        self.assertTrue(math.isnan(out[0]) and math.isnan(out[1]))
        self.assertEqual(out[2:], [2.0, 3.0, 4.0])

    def test_ema_short_input_all_na(self):
        out = ema([1.0, 2.0], 5)
        self.assertTrue(all(math.isnan(v) for v in out))

    def test_ma_dispatch(self):
        xs = [1.0, 2.0, 3.0, 4.0, 5.0]
        assert_series_equal(self, ma(xs, 3, "SMA"), sma(xs, 3), "sma")
        assert_series_equal(self, ma(xs, 3, "EMA"), ema(xs, 3), "ema")

    def test_true_range(self):
        d = {"H": [10.0, 11.0], "L": [9.0, 8.0], "C": [9.5, 10.5]}
        tr = true_range(d)
        self.assertEqual(tr[0], 1.0)  # TR_0 = H0 - L0
        self.assertEqual(tr[1], 3.0)  # max(3, 1.5, 1.5)


class TestDeterminism(unittest.TestCase):
    def test_fixed_tiny_ohlc_fixed_output(self):
        d = synth_ramp(140, 100.0, 0.5)
        a = run_h5(d)
        b = run_h5(d)
        assert_series_equal(self, a["central"], b["central"], "central")
        assert_series_equal(self, a["upper"], b["upper"], "upper")
        assert_series_equal(self, a["lower"], b["lower"], "lower")
        self.assertEqual(a["state"], b["state"])
        self.assertEqual(a["first"], b["first"])
        ra, rb = render_lines(a), render_lines(b)
        for k in ra:
            assert_series_equal(self, ra[k], rb[k], k)


class TestOrderingSymmetry(unittest.TestCase):
    def test_ramp_warm_order_symmetry(self):
        d = synth_ramp(140, 100.0, 0.5)
        r = run_h5(d)
        self.assertEqual(r["first"], 60)  # warm = max(5, 60, 10)
        self.assertTrue(math.isnan(r["central"][59]))
        self.assertFalse(math.isnan(r["central"][60]))
        for i in range(60, len(d["C"])):
            c, u, l = r["central"][i], r["upper"][i], r["lower"][i]
            self.assertTrue(u > c > l, f"ordering at {i}")
            self.assertLess(abs((u - c) - (c - l)), 1e-9, f"symmetry {i}")
            self.assertFalse(math.isnan(u) or math.isnan(l), f"bands {i}")
        self.assertTrue(all(s == 1 for s in r["state"][60:]),
                        "ramp uptrend stays +1 red, no gaps")


class TestGaps(unittest.TestCase):
    def test_vshape_cross_gap_only_at_cross(self):
        d = synth_vshape()
        r = run_h5(d)
        self.assertEqual(r["state"][60], 1)
        self.assertEqual(r["state"][-1], -1)
        fl = flips(r["state"])
        self.assertGreaterEqual(len(fl), 1, "vshape forces >=1 flip")
        self.assertEqual(gap_violations(r["state"], r["first"]), 0,
                         "gaps only at flips +-2b")

    def test_bands_continuous_through_gaps(self):
        for g in (1, 2):
            d = synth_vshape()
            r = run_h5(d, g=g)
            for i in range(r["first"], len(d["C"])):
                self.assertFalse(math.isnan(r["upper"][i]), f"g{g} upper {i}")
                self.assertFalse(math.isnan(r["lower"][i]), f"g{g} lower {i}")


class TestRenderMapping(unittest.TestCase):
    def test_line_slots(self):
        d = synth_vshape()
        r = render_lines(run_h5(d))
        n = len(d["C"])
        for k in ("LINE7", "LINE8", "LINE9", "LINE10", "LINE11", "LINE12"):
            self.assertTrue(all(math.isnan(v) for v in r[k]), k)
        calc = run_h5(d)
        for i in range(n):
            s = calc["state"][i]
            if s == 1:
                self.assertEqual(r["LINE1"][i], calc["central"][i])
                self.assertEqual(r["LINE3"][i], calc["central"][i])
                self.assertTrue(math.isnan(r["LINE2"][i]))
                self.assertTrue(math.isnan(r["LINE4"][i]))
            elif s == -1:
                self.assertEqual(r["LINE2"][i], calc["central"][i])
                self.assertEqual(r["LINE4"][i], calc["central"][i])
                self.assertTrue(math.isnan(r["LINE1"][i]))
                self.assertTrue(math.isnan(r["LINE3"][i]))
            else:
                for k in ("LINE1", "LINE2", "LINE3", "LINE4"):
                    self.assertTrue(math.isnan(r[k][i]), f"{k} gap {i}")
            for k, src in (("LINE5", "upper"), ("LINE6", "lower")):
                x, y = r[k][i], calc[src][i]
                if isinstance(y, float) and math.isnan(y):
                    self.assertTrue(math.isnan(x))
                else:
                    self.assertEqual(x, y)


class TestFitAnchors(unittest.TestCase):
    def test_mcd_nke_regression(self):
        try:
            data = {t: load_daily(t) for t, _, _, _, _ in ANCHORS}
        except FileNotFoundError as e:
            self.skipTest(f"read-only CSV absent: {e}")
        for ticker, date, tc, tu, tl in ANCHORS:
            d = data[ticker]
            r = run_h5(d)  # locked defaults
            i = d["dates"].index(date)
            pc, pu, pl = r["central"][i], r["upper"][i], r["lower"][i]
            self.assertFalse(any(math.isnan(v) for v in (pc, pu, pl)),
                             f"{ticker} gap at anchor")
            self.assertEqual(r["state"][i], -1, f"{ticker} green at anchor")
            self.assertTrue(pu > pc > pl, f"{ticker} ordering")
            rmse = math.sqrt(((pc - tc) ** 2 + (pu - tu) ** 2
                              + (pl - tl) ** 2) / 3)
            self.assertLess(rmse, 1.0, f"{ticker} rmse {rmse}")
            model_hw = (pu - pl) / 2
            legend_hw = (tu - tl) / 2
            self.assertAlmostEqual(model_hw - legend_hw,
                                   HW_PREVIEW[ticker], delta=0.05,
                                   msg=f"{ticker} hw_err")

    def test_fit_gap_residual_locked(self):
        # P5.4 verdict-neutral residual (fit_h5_minimal.md BEST-H5 g=1 gap=5).
        try:
            data = {t: load_daily(t) for t in ("MCD", "NKE")}
        except FileNotFoundError as e:
            self.skipTest(f"read-only CSV absent: {e}")
        total = 0
        for t in ("MCD", "NKE"):
            r = run_h5(data[t])
            total += gap_violations(r["state"], r["first"])
        self.assertEqual(total, FIT_GAP_RESIDUAL, "P5.4 residual lock")


if __name__ == "__main__":
    unittest.main()
