"""The structural address Addr(x) = (Sigma_c(x), delta(x)).

Three distinct properties are kept apart, following Appendix D of the
manuscript:

1. *Exact set-theoretic recoverability* — delta factors through Sigma_c,
   i.e. ker Sigma_c is contained in ker delta.  This is a purely set-theoretic
   condition and holds automatically whenever Sigma_c is injective.
2. *Stable classification* — the induced classifier is locally constant: some
   positive tolerance around each signature value contains only states of the
   same discrete class.
3. *Numerical conditioning* — a separate quantitative question, not decided by
   either of the above.

The utilities below are demonstrations of these distinctions, not a
general-purpose mathematical framework.

MIT License (see LICENSE-CODE).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence


def exact_factorization_possible(
    signature_values: Sequence, invariant_values: Sequence
) -> bool:
    """True if the discrete invariant factors set-theoretically through Sigma_c.

    Equivalent to ker Sigma_c subset ker delta: whenever two states share a
    signature value they must share a discrete class.  Note that an injective
    signature makes this trivially true — which is exactly why exact
    recoverability must not be confused with stable classification.
    """
    if len(signature_values) != len(invariant_values):
        raise ValueError("signature and invariant sequences must have equal length")
    fibers: Dict[Any, set] = {}
    for sig, inv in zip(signature_values, invariant_values):
        fibers.setdefault(sig, set()).add(inv)
        if len(fibers[sig]) > 1:
            return False
    return True


def local_stability_flags(
    signature_values: Sequence[float],
    invariant_values: Sequence,
    tolerance: float,
) -> List[bool]:
    """Per-state flags for proximity-stable classification at a given tolerance.

    Flag i is True when every other state whose scalar signature lies within
    ``tolerance`` of state i carries the same discrete class.  A False flag
    exhibits a *false neighbour* at that scale: proximity in the observable
    does not certify membership.
    """
    if len(signature_values) != len(invariant_values):
        raise ValueError("signature and invariant sequences must have equal length")
    if tolerance <= 0:
        raise ValueError("tolerance must be positive")
    flags: List[bool] = []
    for i, (sig_i, inv_i) in enumerate(zip(signature_values, invariant_values)):
        stable = True
        for j, (sig_j, inv_j) in enumerate(zip(signature_values, invariant_values)):
            if i == j:
                continue
            if abs(float(sig_i) - float(sig_j)) < tolerance and inv_j != inv_i:
                stable = False
                break
        flags.append(stable)
    return flags


@dataclass(frozen=True)
class Address:
    """A structural address (Sigma_c(x), delta(x)) with optional provenance."""

    continuous_signature: Any
    discrete_invariant: Any
    provenance: Optional[Any] = None

    def as_tuple(self) -> tuple:
        if self.provenance is None:
            return (self.continuous_signature, self.discrete_invariant)
        return (self.continuous_signature, self.discrete_invariant, self.provenance)

    def __str__(self) -> str:
        return f"Addr = {self.as_tuple()}"


def structural_address(
    continuous_signature: Any, discrete_invariant: Any, provenance: Any = None
) -> Address:
    """Construct Addr(x) = (Sigma_c(x), delta(x)), optionally typed by provenance.

    The provenance slot records the normalization context of the continuous
    coordinate when several conventions coexist; it is omitted when the
    normalization is globally fixed.
    """
    return Address(continuous_signature, discrete_invariant, provenance)
