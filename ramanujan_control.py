"""Control I: the detuned Ramanujan 1/pi family.

The family is

    L_D = (2*sqrt(2)/9801) * sum_{n>=0} ((4n)!/(n!)^4) * (1103 + 26390 n) / D^(4n),

with the classical evaluation L_396 = 1/pi.

Everything here is evaluated with mpmath at high precision using a
deterministic fixed truncation.  First and second derivatives with respect to
D are computed analytically term by term; no finite differences are used.

MIT License (see LICENSE-CODE).
"""

from __future__ import annotations

from math import factorial
from typing import Iterable, List, Tuple

from mpmath import mp, mpf, sqrt, log10, pi

# High-precision working context.  All displayed digits in the manuscript are
# stable well within this precision.
mp.dps = 60

#: Deterministic truncation length (number of terms, n = 0 .. N_TERMS-1).
N_TERMS = 50

#: Prefactor 2*sqrt(2)/9801.
def prefactor() -> mpf:
    """Return the exact prefactor 2*sqrt(2)/9801 at current precision."""
    return 2 * sqrt(2) / 9801


def _integer_coefficient(n: int) -> int:
    """Exact integer coefficient (4n)!/(n!)^4."""
    return factorial(4 * n) // factorial(n) ** 4


def series_terms(d: float | mpf, n_terms: int = N_TERMS) -> List[mpf]:
    """Return the individual (prefactor-free) terms of the detuned series.

    Term n is ((4n)!/(n!)^4) * (1103 + 26390 n) / D^(4n).
    """
    dd = mpf(d)
    if dd <= 4:
        raise ValueError("the detuned series is used only for D > 4 (z = 256/D^4 < 1)")
    return [
        mpf(_integer_coefficient(n)) * (1103 + 26390 * n) / dd ** (4 * n)
        for n in range(n_terms)
    ]


def L(d: float | mpf, n_terms: int = N_TERMS) -> mpf:
    """Value L_D of the detuned family."""
    return prefactor() * sum(series_terms(d, n_terms))


def L_prime(d: float | mpf, n_terms: int = N_TERMS) -> mpf:
    """Analytic first derivative dL/dD, differentiated term by term.

    d/dD [ c_n (1103+26390n) D^{-4n} ] = -4n c_n (1103+26390n) D^{-4n-1}.
    """
    dd = mpf(d)
    total = mpf(0)
    for n in range(1, n_terms):
        coeff = mpf(_integer_coefficient(n)) * (1103 + 26390 * n)
        total -= 4 * n * coeff / dd ** (4 * n + 1)
    return prefactor() * total


def L_double_prime(d: float | mpf, n_terms: int = N_TERMS) -> mpf:
    """Analytic second derivative d^2L/dD^2, differentiated term by term.

    d^2/dD^2 [ c_n (1103+26390n) D^{-4n} ]
        = 4n(4n+1) c_n (1103+26390n) D^{-4n-2}.
    """
    dd = mpf(d)
    total = mpf(0)
    for n in range(1, n_terms):
        coeff = mpf(_integer_coefficient(n)) * (1103 + 26390 * n)
        total += 4 * n * (4 * n + 1) * coeff / dd ** (4 * n + 2)
    return prefactor() * total


def limiting_value() -> mpf:
    """lim_{D->inf} L_D = 2*sqrt(2)*1103/9801 (the n = 0 term alone)."""
    return prefactor() * 1103


def digits_per_term(d: float | mpf) -> mpf:
    """Asymptotic decimal digits gained per term: 4*log10(D) - log10(256)."""
    return 4 * log10(mpf(d)) - log10(mpf(256))


def value_window(d_min: float | mpf = 396) -> Tuple[mpf, mpf, mpf]:
    """Observable-value window occupied by the family for D >= d_min.

    Because L_D is strictly decreasing, the window is
    [lim_{D->inf} L_D, L_{d_min}].  Returns (lower, upper, width).
    """
    lower = limiting_value()
    upper = L(d_min)
    return lower, upper, upper - lower


def is_strictly_decreasing(values: Iterable[mpf]) -> bool:
    """True if the given sequence is strictly decreasing."""
    vals = list(values)
    return all(b < a for a, b in zip(vals, vals[1:]))


def is_strictly_increasing(values: Iterable[mpf]) -> bool:
    """True if the given sequence is strictly increasing."""
    vals = list(values)
    return all(b > a for a, b in zip(vals, vals[1:]))


def checks(tol: float = 1e-45) -> dict:
    """Principal numerical checks reported in the manuscript."""
    l396 = L(396)
    lp = L_prime(396)
    lpp = L_double_prime(396)
    grid = [10, 50, 100, 396, 1000, 5000]
    lower, upper, width = value_window(396)
    return {
        "L_396": l396,
        "L_396_agrees_with_1_over_pi": abs(l396 - 1 / pi) < mpf(tol),
        "L_prime_396": lp,
        "L_double_prime_396": lpp,
        "limiting_value": lower,
        "value_window_lower": lower,
        "value_window_upper": upper,
        "value_window_width": width,
        "digits_per_term_396": digits_per_term(396),
        "digits_per_term_increasing": is_strictly_increasing(
            [digits_per_term(d) for d in grid]
        ),
        "L_decreasing": is_strictly_decreasing([L(d) for d in grid]),
    }


def make_figure_1(path: str) -> str:
    """Figure 1.

    Left:  |L_D - 1/pi| on a logarithmic vertical scale, with D = 396 marked.
    Right: digits per term = 4 log10(D) - log10(256) versus D.
    """
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    inv_pi = 1 / pi

    # Left panel: a narrow window around D = 396 (D = 396 itself is the exact
    # zero of the difference and is excluded from the log-scale curve).
    d_left = [396 + mpf(k) / 10 for k in range(-60, 61) if k != 0]
    y_left = [float(abs(L(d) - inv_pi)) for d in d_left]
    x_left = [float(d) for d in d_left]

    # Right panel: digits per term over a broad range of D.
    x_right = np.linspace(10.0, 2000.0, 400)
    y_right = [float(digits_per_term(x)) for x in x_right]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))

    ax1.semilogy(x_left, y_left, color="#1f4e79", lw=1.6)
    ax1.axvline(396, color="#c0392b", ls="--", lw=1.2)
    ax1.annotate(
        "D = 396: $L_D = 1/\\pi$ exactly",
        xy=(396, min(y_left)),
        xytext=(396.7, min(y_left) * 6),
        color="#c0392b",
        fontsize=9,
        arrowprops=dict(arrowstyle="->", color="#c0392b", lw=1.0),
    )
    ax1.set_ylim(min(y_left) / 3, max(y_left) * 4)
    ax1.set_xlabel("D")
    ax1.set_ylabel(r"$|L_D - 1/\pi|$")
    ax1.set_title("Smooth, locally linear detuning near $D=396$")
    ax1.grid(alpha=0.3, which="both")

    ax2.plot(x_right, y_right, color="#1f4e79", lw=1.6)
    ax2.axvline(396, color="#c0392b", ls="--", lw=1.2)
    ax2.plot([396], [float(digits_per_term(396))], "o", color="#c0392b", ms=5)
    ax2.annotate(
        "D = 396 is not a\nconvergence-rate optimum",
        xy=(396, float(digits_per_term(396))),
        xytext=(520, float(digits_per_term(396)) - 3.2),
        color="#c0392b",
        fontsize=9,
        arrowprops=dict(arrowstyle="->", color="#c0392b", lw=1.0),
    )
    ax2.set_xlabel("D")
    ax2.set_ylabel(r"digits per term $= 4\log_{10}D - \log_{10}256$")
    ax2.set_title("Convergence rate is strictly increasing in $D$")
    ax2.grid(alpha=0.3)

    fig.suptitle(
        "Figure 1 — Ramanujan detuning: no continuous analytic datum "
        "distinguishes $D=396$",
        fontsize=11,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(path, dpi=160)
    plt.close(fig)
    return path
