"""Control II: the beta/gamma family J(s) = Gamma(s+1)^2 / Gamma(2s+2).

J(s) is the integral of [a(1-a)]^s over a in (0,1), i.e. B(s+1, s+1).  It is
real-analytic and strictly decreasing on s > -1, while its exact gamma-period
relations occur only at special rational arguments.

Exact identities verified numerically here:

    J(1/2)          = pi/8
    J(1/4)          = Gamma(1/4)^2 / (12 sqrt(pi))
    J(3/4)          = 3 Gamma(3/4)^2 / (10 sqrt(pi))
    J(1/4) J(3/4)   = pi/20

MIT License (see LICENSE-CODE).
"""

from __future__ import annotations

from typing import Dict, Iterable, List

from mpmath import mp, mpf, gamma, pi, sqrt, psi

mp.dps = 60

#: Tolerance used for "exact identity holds numerically" checks.
EXACT_TOL = mpf("1e-45")


def J(s: float | mpf) -> mpf:
    """J(s) = Gamma(s+1)^2 / Gamma(2s+2), defined for s > -1."""
    ss = mpf(s)
    if ss <= -1:
        raise ValueError("J(s) requires s > -1")
    return gamma(ss + 1) ** 2 / gamma(2 * ss + 2)


def J_half_closed_form() -> mpf:
    """Closed form pi/8 for J(1/2)."""
    return pi / 8


def J_quarter_closed_form() -> mpf:
    """Closed form Gamma(1/4)^2 / (12 sqrt(pi)) for J(1/4)."""
    return gamma(mpf(1) / 4) ** 2 / (12 * sqrt(pi))


def J_three_quarter_closed_form() -> mpf:
    """Closed form 3 Gamma(3/4)^2 / (10 sqrt(pi)) for J(3/4)."""
    return 3 * gamma(mpf(3) / 4) ** 2 / (10 * sqrt(pi))


def reflection_product_closed_form() -> mpf:
    """Closed form pi/20 for J(1/4) J(3/4)."""
    return pi / 20


def log_derivative(s: float | mpf) -> mpf:
    """d/ds log J(s) = 2 psi(s+1) - 2 psi(2s+2); negative for s > -1."""
    ss = mpf(s)
    return 2 * psi(0, ss + 1) - 2 * psi(0, 2 * ss + 2)


def is_strictly_decreasing(values: Iterable[mpf]) -> bool:
    vals = list(values)
    return all(b < a for a, b in zip(vals, vals[1:]))


def monotone_grid(start: float = 0.0, stop: float = 2.0, steps: int = 200) -> List[mpf]:
    """A deterministic grid of s-values on the displayed interval."""
    a, b = mpf(start), mpf(stop)
    return [a + (b - a) * mpf(k) / steps for k in range(steps + 1)]


def checks(tol: mpf = EXACT_TOL) -> Dict[str, object]:
    """Exact numerical verification of the identities used in the manuscript."""
    grid = monotone_grid()
    j_quarter = J(mpf(1) / 4)
    j_three_quarter = J(mpf(3) / 4)
    return {
        "J_half": J(mpf(1) / 2),
        "J_half_equals_pi_over_8": abs(J(mpf(1) / 2) - J_half_closed_form()) < tol,
        "J_quarter": j_quarter,
        "J_quarter_closed_form_holds": abs(j_quarter - J_quarter_closed_form()) < tol,
        "J_three_quarter": j_three_quarter,
        "J_three_quarter_closed_form_holds": abs(
            j_three_quarter - J_three_quarter_closed_form()
        )
        < tol,
        "product_quarter_three_quarter": j_quarter * j_three_quarter,
        "product_equals_pi_over_20": abs(
            j_quarter * j_three_quarter - reflection_product_closed_form()
        )
        < tol,
        "J_decreasing_on_grid": is_strictly_decreasing([J(s) for s in grid]),
        "log_derivative_negative_on_grid": all(log_derivative(s) < 0 for s in grid),
    }


#: Points marked in Figure 2.  Labels record the exact structural stratum; the
#: comparison points are labelled only by their reduced denominator.  No
#: arithmetic classification is asserted by the figure itself.
MARKED_POINTS = [
    (mpf(1) / 2, "s = 1/2  (pure power of pi)", "exact"),
    (mpf(1) / 4, "s = 1/4  (discriminant -4)", "exact"),
    (mpf(3) / 4, "s = 3/4  (discriminant -4)", "exact"),
    (mpf(1) / 3, "s = 1/3  (discriminant -3)", "exact"),
    (mpf(2) / 3, "s = 2/3  (discriminant -3)", "exact"),
    (mpf("0.24"), "s = 0.24  (q = 25)", "comparison"),
    (mpf("0.26"), "s = 0.26  (q = 50)", "comparison"),
]


def make_figure_2(path: str) -> str:
    """Figure 2: J(s) with exact strata and nearby comparison points marked."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    xs = np.linspace(0.0, 1.5, 400)
    ys = [float(J(x)) for x in xs]

    fig, ax = plt.subplots(figsize=(9.5, 5.4))
    ax.plot(xs, ys, color="#1f4e79", lw=1.8, label=r"$J(s)=\Gamma(s+1)^2/\Gamma(2s+2)$")

    offsets = {
        "s = 1/2  (pure power of pi)": (0.10, 0.030),
        "s = 1/4  (discriminant -4)": (-0.02, 0.045),
        "s = 3/4  (discriminant -4)": (0.09, 0.022),
        "s = 1/3  (discriminant -3)": (0.13, 0.048),
        "s = 2/3  (discriminant -3)": (0.14, 0.036),
        "s = 0.24  (q = 25)": (-0.30, -0.055),
        "s = 0.26  (q = 50)": (0.02, -0.070),
    }

    for s, label, kind in MARKED_POINTS:
        x, y = float(s), float(J(s))
        if kind == "exact":
            ax.plot([x], [y], "o", color="#c0392b", ms=7, zorder=5)
            colour = "#c0392b"
        else:
            ax.plot([x], [y], "s", color="#2471a3", ms=7, zorder=5)
            colour = "#2471a3"
        dx, dy = offsets[label]
        ax.annotate(
            label,
            xy=(x, y),
            xytext=(x + dx, y + dy),
            fontsize=8.5,
            color=colour,
            arrowprops=dict(arrowstyle="-", color=colour, lw=0.7, alpha=0.7),
        )

    ax.plot([], [], "o", color="#c0392b", label="exact gamma-period strata")
    ax.plot([], [], "s", color="#2471a3", label="nearby comparison points")

    ax.set_xlabel("s")
    ax.set_ylabel("J(s)")
    ax.set_title(
        "Figure 2 — the beta family $J(s)$: smooth and strictly decreasing\n"
        "continuous proximity and exact gamma-relation membership are "
        "different relations",
        fontsize=11,
    )
    ax.grid(alpha=0.3)
    ax.legend(loc="upper right", fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)
    return path
