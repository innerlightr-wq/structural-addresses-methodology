"""One-command reproduction of every computational claim in the manuscript.

Usage:
    python reproduce.py

Creates data/ and figures/ if needed, regenerates Figures 1 and 2, prints the
principal numerical checks for both analytic controls and the four-state
finite control, and exits with a nonzero status if any required check fails.
"""

from __future__ import annotations

import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "src"))

from mpmath import mp, mpf, nstr, pi  # noqa: E402

import beta_gamma_control as bg  # noqa: E402
import ramanujan_control as rc  # noqa: E402
from inheritance import (  # noqa: E402
    canonical_partition,
    coarsest_stable_refinement,
    common_refinement,
    is_congruence,
    refines,
)
from structural_address import (  # noqa: E402
    exact_factorization_possible,
    local_stability_flags,
    structural_address,
)

mp.dps = 60

DATA_DIR = os.path.join(HERE, "data")
FIGURES_DIR = os.path.join(HERE, "figures")

FAILURES: list[str] = []


def require(name: str, condition: bool) -> bool:
    """Record a required check; returns the boolean for printing."""
    ok = bool(condition)
    if not ok:
        FAILURES.append(name)
    return ok


def ensure_directories() -> None:
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(FIGURES_DIR, exist_ok=True)


def ramanujan_section() -> None:
    r = rc.checks()
    lower, upper, width = r["value_window_lower"], r["value_window_upper"], r["value_window_width"]

    print("Ramanujan control")
    print(
        "L_396 agrees with 1/pi:",
        require("L_396 = 1/pi", r["L_396_agrees_with_1_over_pi"]),
    )
    print("L_prime_396: approximately", nstr(r["L_prime_396"], 13))
    print("L_double_prime_396: approximately", nstr(r["L_double_prime_396"], 3))
    print("limiting value 2*sqrt(2)*1103/9801:", nstr(r["limiting_value"], 15))
    print(
        "observable-value window for D >= 396: [%s, %s], width %s"
        % (nstr(lower, 12), nstr(upper, 12), nstr(width, 4))
    )
    print("digits per term at D = 396:", nstr(r["digits_per_term_396"], 6))
    print(
        "Digits per term increase with D:",
        require("digits per term increasing", r["digits_per_term_increasing"]),
    )

    require(
        "L'(396) matches reported value",
        abs(r["L_prime_396"] - mpf("-7.821535972847e-11")) < mpf("1e-22"),
    )
    require(
        "L''(396) matches reported value",
        abs(r["L_double_prime_396"] - mpf("9.88e-13")) < mpf("1e-15"),
    )
    require(
        "limiting value below 1/pi by about 7.8e-9",
        mpf("7.5e-9") < 1 / pi - r["limiting_value"] < mpf("8.1e-9"),
    )
    require("value window narrower than 1e-8", width < mpf("1e-8"))

    path = os.path.join(DATA_DIR, "ramanujan_control.csv")
    with open(path, "w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["D", "L_D", "abs_L_D_minus_inv_pi", "digits_per_term"])
        for k in range(-60, 61):
            d = 396 + mpf(k) / 10
            writer.writerow(
                [
                    nstr(d, 8),
                    nstr(rc.L(d), 25),
                    nstr(abs(rc.L(d) - 1 / pi), 12),
                    nstr(rc.digits_per_term(d), 12),
                ]
            )
    print("wrote", os.path.relpath(path, HERE))


def beta_gamma_section() -> None:
    b = bg.checks()
    print()
    print("Beta/gamma control")
    print("J(1/2) = pi/8:", require("J(1/2) = pi/8", b["J_half_equals_pi_over_8"]))
    print(
        "J(1/4) * J(3/4) = pi/20:",
        require("J(1/4)J(3/4) = pi/20", b["product_equals_pi_over_20"]),
    )
    print(
        "J(1/4) = Gamma(1/4)^2/(12 sqrt(pi)):",
        require("J(1/4) closed form", b["J_quarter_closed_form_holds"]),
    )
    print(
        "J(3/4) = 3 Gamma(3/4)^2/(10 sqrt(pi)):",
        require("J(3/4) closed form", b["J_three_quarter_closed_form_holds"]),
    )
    print(
        "J is decreasing on the tested grid:",
        require("J decreasing", b["J_decreasing_on_grid"]),
    )
    require("log J' negative", b["log_derivative_negative_on_grid"])

    path = os.path.join(DATA_DIR, "beta_family.csv")
    with open(path, "w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["s", "J_s"])
        for s in bg.monotone_grid(0.0, 1.5, 150):
            writer.writerow([nstr(s, 8), nstr(bg.J(s), 25)])
        for s, label, kind in bg.MARKED_POINTS:
            writer.writerow([nstr(s, 8), nstr(bg.J(s), 25)])
    print("wrote", os.path.relpath(path, HERE))


def four_state_section() -> None:
    states = (1, 2, 3, 4)
    f = {1: 1, 2: 2, 3: 1, 4: 4}
    kappa = canonical_partition([[1, 2, 3], [4]])
    sigma = canonical_partition([[1, 3], [2, 4]])
    m = canonical_partition([[1], [2, 3], [4]])
    composite = common_refinement(sigma, kappa)

    print()
    print("Four-state control")
    print("kappa closes:", require("kappa closes", is_congruence(states, f, kappa)))
    print(
        "kappa separates target:",
        require("kappa separates", refines(kappa, kappa)),
    )
    print("Sigma closes:", require("Sigma closes", is_congruence(states, f, sigma)))
    sigma_separates = refines(sigma, kappa)
    require("Sigma does not separate", not sigma_separates)
    print("Sigma separates target:", sigma_separates)
    m_closes = is_congruence(states, f, m)
    require("M does not close", not m_closes)
    print("M closes:", m_closes)
    print("M separates target:", require("M separates", refines(m, kappa)))
    print(
        "Composite closes:",
        require("composite closes", is_congruence(states, f, composite)),
    )
    print(
        "Composite separates target:",
        require("composite separates", refines(composite, kappa)),
    )
    print("composite partition:", _fmt(composite))
    print(
        "coarsest inheritance-stable refinement separating kappa:",
        _fmt(coarsest_stable_refinement(states, f, kappa)),
    )


def address_section() -> None:
    """Essential internal validations of the structural-address utilities."""
    print()
    print("Structural-address validations")

    # Injective signature: exact factorization holds, stability can still fail.
    sig = [float(bg.J(mpf(1) / 4)), float(bg.J(mpf("0.24"))), float(bg.J(mpf("0.26")))]
    inv = ["disc -4", "q = 25", "q = 50"]
    exact = exact_factorization_possible(sig, inv)
    flags = local_stability_flags(sig, inv, tolerance=0.02)
    print("exact factorization through an injective signature:", require("exact factorization", exact))
    print("proximity-stable at tolerance 0.02:", flags)
    require("stability fails at coarse tolerance", not all(flags))

    # A genuine fiber collision: exact factorization must fail.
    collide = exact_factorization_possible([1.0, 1.0], ["A", "B"])
    require("fiber collision detected", not collide)
    print("fiber collision correctly detected:", not collide)

    addr = structural_address(float(bg.J(mpf(1) / 4)), "disc -4", provenance="J-value")
    print("example address:", addr)


def _fmt(partition) -> str:
    return "{" + ", ".join(
        "{" + ",".join(str(s) for s in sorted(b)) + "}" for b in partition
    ) + "}"


def figures_section() -> None:
    print()
    print("Figures")
    fig1 = rc.make_figure_1(os.path.join(FIGURES_DIR, "figure_1_ramanujan_detuning.png"))
    fig2 = bg.make_figure_2(os.path.join(FIGURES_DIR, "figure_2_beta_family.png"))
    for path in (fig1, fig2):
        exists = os.path.exists(path)
        require(f"figure exists: {os.path.basename(path)}", exists)
        print("wrote", os.path.relpath(path, HERE), "-", exists)


def main() -> int:
    ensure_directories()
    ramanujan_section()
    beta_gamma_section()
    four_state_section()
    address_section()
    figures_section()

    print()
    if FAILURES:
        print("FAILED checks:")
        for name in FAILURES:
            print("  -", name)
        return 1
    print("All required checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
