"""Finite deterministic inheritance systems: closure and separation.

A partition of a finite state space is a *congruence* for a map f when f sends
each block into a single block; this is the deterministic case of the
inheritance-compatibility condition ker Sigma_l subset ker(Sigma_{l+1} o E_l).
A partition *separates* a target partition when it refines it.

Closure and separation are logically independent; the four-state control in
``examples/03_four_state_control.py`` exhibits all four combinations that the
manuscript needs.

Partitions are represented canonically as a tuple of sorted frozensets, sorted
by their minimum element, so equality and hashing are deterministic.

MIT License (see LICENSE-CODE).
"""

from __future__ import annotations

from typing import Callable, Dict, FrozenSet, Iterable, Mapping, Tuple

Partition = Tuple[FrozenSet, ...]


def canonical_partition(blocks: Iterable[Iterable]) -> Partition:
    """Return a canonical, hashable representation of a partition.

    Blocks are stored as frozensets and ordered by their minimum element.
    Empty blocks are dropped; overlapping blocks raise ValueError.
    """
    frozen = [frozenset(b) for b in blocks if len(frozenset(b)) > 0]
    seen: set = set()
    for block in frozen:
        if seen & block:
            raise ValueError("blocks of a partition must be pairwise disjoint")
        seen |= block
    return tuple(sorted(frozen, key=lambda b: (min(b), sorted(b))))


def block_of(partition: Partition, state) -> FrozenSet:
    """Return the block of ``partition`` containing ``state``."""
    for block in partition:
        if state in block:
            return block
    raise KeyError(f"state {state!r} is not covered by the partition")


def is_congruence(
    states: Iterable, transition: Mapping | Callable, partition: Partition
) -> bool:
    """True if ``partition`` closes: f maps each block into a single block."""
    f = _as_callable(transition)
    for block in partition:
        images = {block_of(partition, f(x)) for x in block if x in set(states)}
        if len(images) > 1:
            return False
    return True


def refines(partition_a: Partition, partition_b: Partition) -> bool:
    """True if ``partition_a`` refines ``partition_b``.

    Equivalently ker(partition_a) subset ker(partition_b): every A-block is
    contained in a single B-block, so A separates the classes of B.
    """
    for block in partition_a:
        if not any(block <= other for other in partition_b):
            return False
    return True


def common_refinement(partition_a: Partition, partition_b: Partition) -> Partition:
    """Coarsest common refinement (the meet): all nonempty pairwise intersections."""
    blocks = [a & b for a in partition_a for b in partition_b]
    return canonical_partition(blocks)


def induced_map(
    states: Iterable, transition: Mapping | Callable, partition: Partition
) -> Dict[FrozenSet, FrozenSet]:
    """Reduced dynamics T on the blocks, defined only when the partition closes.

    Raises ValueError if ``partition`` is not a congruence for ``transition``.
    """
    if not is_congruence(states, transition, partition):
        raise ValueError("partition is not a congruence; no reduced map exists")
    f = _as_callable(transition)
    return {block: block_of(partition, f(next(iter(block)))) for block in partition}


def coarsest_stable_refinement(
    states: Iterable, transition: Mapping | Callable, target: Partition
) -> Partition:
    """Coarsest inheritance-stable refinement of ``target``.

    Iterated preimage refinement (the deterministic, bisimulation-style
    algorithm): repeatedly split every block by the block into which its
    states are mapped, until the partition is a congruence.  The result is the
    coarsest partition that both closes and separates ``target``.
    """
    f = _as_callable(transition)
    state_list = list(states)
    partition = canonical_partition(
        [b & frozenset(state_list) for b in target]
    )
    while True:
        refined_blocks = []
        for block in partition:
            groups: Dict[FrozenSet, set] = {}
            for x in block:
                groups.setdefault(block_of(partition, f(x)), set()).add(x)
            refined_blocks.extend(groups.values())
        new_partition = canonical_partition(refined_blocks)
        if new_partition == partition:
            return partition
        partition = new_partition


def _as_callable(transition: Mapping | Callable) -> Callable:
    """Accept either a dict-like transition table or a function."""
    if callable(transition):
        return transition
    return lambda x: transition[x]
