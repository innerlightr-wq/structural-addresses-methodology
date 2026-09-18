# structural-addresses

Reference implementation and reproducibility companion for:

**Structural Addresses: Continuous Proximity, Discrete Membership, and Compatible Markers in Inheritance Systems — A Methodological Note with Hypergeometric, Gamma–Period, and Finite-State Controls**

Elias De Jesús · Independent Researcher · ORCID [0009-0007-0190-9143](https://orcid.org/0009-0007-0190-9143) · <dejesuselias10@gmail.com> · July 2026

**Archival record**

- Current version DOI: [10.5281/zenodo.21297926](https://doi.org/10.5281/zenodo.21297926)
- Concept DOI, all versions: [10.5281/zenodo.21263921](https://doi.org/10.5281/zenodo.21263921)

The concept DOI always resolves to the latest available version. The current-version DOI identifies one specific archived version and does not represent all versions.

---

## 1. Purpose

This repository is a lightweight reproducibility companion, not a software product. The manuscript is the scholarly record; the code here exists only to reproduce the paper's computational claims and to demonstrate its central framework in executable form.

It reproduces two analytic controls (the detuned Ramanujan 1/π family and the beta/gamma family), one minimal finite-state inheritance control, and both figures.

## 2. Structural-address framework

Each object `x` in an analytic, arithmetic, or inherited family is assigned a two-part address

```
Addr(x) = ( Σ_c(x), δ(x) )
```

where

- `Σ_c : X → C` is a **continuous signature** into a metric space, answering *which objects are nearby*;
- `δ : X → Δ` is a **discrete invariant** into a set with no assumed metric, answering *which exact structural class x belongs to*.

> **Terminology.** In symbolic dynamics an *address* is the itinerary of a point under a Markov
> partition — that is, the **discrete** label alone. Here "structural address" names the *pair*
> `(Σ_c, δ)`, and `δ` is the analogue of a symbolic address. See
> [`docs/LITERATURE_CONTEXT.md`](docs/LITERATURE_CONTEXT.md) §4.

The two components **answer different questions**. They are not in general independent as
*information*: wherever `Σ_c` is injective — which is the case in both analytic controls below, as
§3 notes — `ker Σ_c` is trivial, so `δ` factors through `Σ_c` and is set-theoretically redundant.
What the controls exhibit is independence of *stability*: `δ` remains the only proximity-robust
label even when it is determined. The central methodological statements are:

- **Continuous navigation and exact identification are different tasks.** A signature map supplies local navigation coordinates exactly where it is a local embedding, and only after quotienting by automorphisms.
- **An inherited marker closes exactly when its fibers satisfy the congruence condition** `ker Σ_ℓ ⊆ ker(Σ_{ℓ+1} ∘ E_ℓ)`, i.e. when the marker map sends each fiber consistently forward under inheritance. This is the **classical descent criterion** — the universal property of the quotient, equivalently the condition defining a Nerode congruence, equivalently the deterministic case of strong Markov lumpability. No strengthening of it is claimed.
- **Closure and separation are independent.** A marker may induce well-defined reduced dynamics without distinguishing the target classes, or distinguish them without closing.
- **An injective continuous observable can allow exact recovery while still failing to provide proximity-stable classification.**

## 3. Three levels of recovery

Following Appendix D of the manuscript, three properties must be kept apart:

| Level | Question | Criterion |
|---|---|---|
| **Exact recoverability** | Does `δ` factor set-theoretically through `Σ_c`? | `ker Σ_c ⊆ ker δ` |
| **Stable classification** | Is the induced classifier locally constant? | each `Σ_c(S_τ)` open in the relative topology |
| **Numerical conditioning** | Can the classification be performed from finite-precision data? | quantitative inverse estimates (smallest singular value of `dΣ_c`) |

Because `D ↦ L_D` and `s ↦ J(s)` are injective on the stated domains, exact parameter and class information *can* factor set-theoretically through the scalar observables. The controls demonstrate the failure of **proximity-stable exact classification**, not the failure of exact recoverability. Both implications above are strict: exact recoverability does not imply stable classification, and stable classification does not imply well-conditioned recovery.

## 4. What this repository reproduces

**Control I — the detuned Ramanujan family**

```
L_D = (2√2 / 9801) · Σ_{n≥0} ((4n)! / (n!)^4) · (1103 + 26390 n) / D^(4n)
```

- `L_396 = 1/π` to high precision;
- `L'(396) ≈ −7.821535972847 × 10⁻¹¹` and `L''(396) ≈ 9.88 × 10⁻¹³`, computed as analytic term-by-term derivatives (no finite differences);
- the limiting value `2√2 · 1103 / 9801`, which lies ≈ 7.8 × 10⁻⁹ below `1/π`;
- the narrow observable-value window occupied by the family for `D ≥ 396` (width < 10⁻⁸);
- digits per term `= 4 log₁₀ D − log₁₀ 256`, strictly increasing in `D`, so `D = 396` is not a convergence-rate optimum.

**Control II — the beta/gamma family**

```
J(s) = Γ(s+1)² / Γ(2s+2)
```

- `J(1/2) = π/8`;
- `J(1/4) = Γ(1/4)² / (12√π)` and `J(3/4) = 3 Γ(3/4)² / (10√π)`;
- `J(1/4) · J(3/4) = π/20`;
- monotone decrease of `J` over the displayed interval.

**Control III — the four-state deterministic inheritance system**

The last row is the meet `Σ ∧ κ`. (It is *not* `Σ ∧ M`, which is the discrete partition
`{{1},{2},{3},{4}}`, nor `coarsest_stable_refinement(X, f, κ)`, which returns `κ` itself.)

`X = {1,2,3,4}` with `f(1)=1, f(2)=2, f(3)=1, f(4)=4` and target `κ = {{1,2,3},{4}}`:

| Marker | Closes | Separates κ |
|---|---|---|
| `κ = {{1,2,3},{4}}` | yes | yes |
| `Σ = {{1,3},{2,4}}` | yes | no |
| `M = {{1},{2,3},{4}}` | no | yes |
| `Σ ∧ κ = {{1,3},{2},{4}}` | yes | yes |

**Figures**

- `figures/figure_1_ramanujan_detuning.png` — left: `|L_D − 1/π|` on a logarithmic vertical scale with `D = 396` marked; right: digits per term versus `D`.
- `figures/figure_2_beta_family.png` — `J(s)` with the exact strata `s = 1/2, 1/4, 3/4, 1/3, 2/3` marked, together with the nearby comparison points `s = 0.24` and `s = 0.26`.

## 5. Installation and reproduction

Python 3.10 or newer, with `mpmath` and `matplotlib`:

```bash
pip install mpmath matplotlib
python reproduce.py
```

`reproduce.py` creates `data/` and `figures/` if needed, regenerates both figures, prints all numerical checks, and exits with a nonzero status if any required check fails.

Individual controls can be run directly:

```bash
python ramanujan_control.py
python beta_gamma_control.py
python inheritance.py
```

The finite-state control needs no dependencies beyond the standard library, so
`inheritance.py` and `structural_address.py` can be exercised on their own.

All high-precision computation uses `mpmath` at 60 decimal digits, with a deterministic fixed truncation of the Ramanujan series at 50 terms (the manuscript requires ≥ 45). Displayed digits are stable under increased precision and truncation length.

## 6. Expected results

```
Ramanujan control
L_396 agrees with 1/pi: True
L_prime_396: approximately -7.821535972847e-11
L_double_prime_396: approximately 9.88e-13
Digits per term increase with D: True

Beta/gamma control
J(1/2) = pi/8: True
J(1/4) * J(3/4) = pi/20: True
J is decreasing on the tested grid: True

Four-state control
kappa closes: True
kappa separates target: True
Sigma closes: True
Sigma separates target: False
M closes: False
M separates target: True
Composite closes: True
Composite separates target: True
```

## 7. Repository structure

```
structural-addresses-methodology/
├── README.md
├── LICENSE                    CC BY 4.0 (prose, figures, generated data)
├── LICENSE-CODE               MIT (source and reproduce.py)
├── CITATION.cff
├── references.bib             verified bibliography for the provenance audit
├── docs/
│   ├── NOVELTY_AND_PROVENANCE.md   claim-by-claim novelty matrix
│   └── LITERATURE_CONTEXT.md       conceptual ancestry of the framework
├── ramanujan_control.py       Control I: series, analytic derivatives, Figure 1
├── beta_gamma_control.py      Control II: J(s), exact identities, Figure 2
├── inheritance.py             partitions, congruence, refinement, induced map
├── structural_address.py      factorization, local stability, Addr(x)
├── reproduce.py               regenerates both figures and prints every check
├── figure_1_ramanujan_detuning.png
└── figure_2_beta_family.png
```

`reproduce.py` writes generated CSVs to `data/` and re-renders the figures into `figures/`,
creating both directories on first run.

### Core utilities

`inheritance.py`

- `canonical_partition(blocks)` — canonical, hashable partition representation
- `is_congruence(states, transition, partition)` — does the marker close?
- `refines(partition_a, partition_b)` — does A separate the classes of B?
- `common_refinement(partition_a, partition_b)` — the meet
- `induced_map(states, transition, partition)` — reduced dynamics `T`, defined only under closure
- `coarsest_stable_refinement(states, transition, target)` — coarsest inheritance-stable refinement that still separates the target, by iterated preimage refinement

`structural_address.py`

- `exact_factorization_possible(signature_values, invariant_values)`
- `local_stability_flags(signature_values, invariant_values, tolerance)`
- `structural_address(continuous_signature, discrete_invariant, provenance=None)`

## 8. Scope and non-claims

- The component theorems are **classical**: the immersion/local-embedding theorem, the universal property of quotient maps, the gamma reflection and multiplication formulas, the generalized hypergeometric differential equation, complex-multiplication special values, and Markov lumpability. Novelty is claimed only for their **methodological assembly** — and a September 2026 provenance audit found that **the assembly is not new in structure either**: see §9 and [`docs/NOVELTY_AND_PROVENANCE.md`](docs/NOVELTY_AND_PROVENANCE.md).
- The framework **proves nothing beyond standard quotient language**. Every proposition here follows in a line or two from the universal property of the quotient, the definition of a congruence, or elementary topology.
- The closure condition is the **deterministic special case** of strong lumpability, i.e. strictly *less* general — not a generalization of it.
- `coarsest_stable_refinement` is the classical coarsest-stable-refinement computation (Moore / Hopcroft / Paige–Tarjan lineage) restricted to deterministic maps. No algorithmic novelty is claimed.
- **Numerical closeness to a special value is not proof of arithmetic membership.** No finite tolerance certifies exact class membership.
- The code **does not classify all gamma-value relations**. Only the specific reductions proved in the manuscript are asserted.
- The **Rohrlich–Lang classification problem remains open**; no contribution to it is claimed.
- **No universal structural-address theory is claimed.** The discrete invariant `δ` is an input supplied by the domain; the framework does not discover it.
- The framework asserts neither density nor topological isolation of the arithmetically special locus on the real Ramanujan slice.
- Failure of an integer-relation search is not a proof of algebraic independence.
- Strong lumpability must not be conflated with weak or stationary-distribution lumpability.

## 9. Relation to prior work

A Zotero-assisted provenance audit (September 2026) compared the framework against seven fields.
Full claim-by-claim matrix: [`docs/NOVELTY_AND_PROVENANCE.md`](docs/NOVELTY_AND_PROVENANCE.md);
conceptual ancestry: [`docs/LITERATURE_CONTEXT.md`](docs/LITERATURE_CONTEXT.md); verified records:
[`references.bib`](references.bib).

**The components are classical, and so is the combination.**

| part of the framework | standard name | closest prior work |
|---|---|---|
| closure condition `ker Σ_ℓ ⊆ ker(Σ_{ℓ+1} ∘ E_ℓ)` | congruence / quotient descent | universal property of quotients; Nerode congruence; strong lumpability (deterministic case) |
| `coarsest_stable_refinement` | relational coarsest partition | Moore; Hopcroft; Paige–Tarjan; Kanellakis–Smolka |
| "inheritance marker" that closes | congruence-respecting partition; deterministic bisimulation | Milner; Park; Kanellakis–Smolka |
| continuous layer | immersion / local embedding | Whitney |
| `Addr(x) = (Σ_c(x), δ(x))` | hybrid state `(mode, continuous valuation)`; stratum label + chart | **Alur et al.; Henzinger; Thom** |
| exact recoverability | identifiability; sufficiency | Rothenberg; Halmos–Savage |
| stable classification | stability (Hadamard's third condition) | inverse-problem literature |
| numerical conditioning | condition number | Turing; Rice |
| "address" | symbolic itinerary | Lind–Marcus; Adler; Milnor–Thurston |

The **closest prior art for the pairing itself is hybrid automata**, where a state is a pair of a
discrete mode and continuous coordinates and the analysis requires a bisimulation-compatible
partition of the continuous part. That is a discrete label, continuous coordinates, and a descent
condition, in one framework, decades earlier. The difference here is subject matter, not structure:
hybrid automata analyse reachability of a dynamical system, whereas this framework asks membership
questions in analytic and arithmetic families whose continuous part carries no transition structure.

**What the audit concluded survives as this project's contribution**, stated at its safe strength:

- the **three-level separation** of exact recoverability, stable classification and numerical
  conditioning, applied to recovering a *discrete* label from a continuous observable, with explicit
  witnesses showing both implications strict. The trichotomy is classical; no equivalent single
  treatment for this setting was identified in the literature reviewed;
- the methodological warning that **numerical closeness to a special value is not evidence of exact
  arithmetic membership** — classical in substance, but a live failure mode in special-function
  practice and the clearest statement in the repository;
- the executable controls, as illustrations.

The worked examples are **classical identities used illustratively** and are not evidence for the
methodology: the Ramanujan `1/π` series, the gamma/beta special values (all four re-derived in the
audit from the reflection formula), and CM singular values.

Overall classification: **methodological synthesis**, not new mathematics.

## 10. Related work

This repository accompanies the general methodological note. A separate application of the same framework appears in:

**The Pell Spine as an Optimal Rational Separator: Extremal Resolution and Smooth Transport in Primitive Pythagorean Triples** — companion repository: <https://github.com/innerlightr-wq/pell-spine-optimal-separator>

That work distinguishes the continuous separation coordinate `Δ_k = (b − a)/c` from the exact arithmetic condition `b − a = 1`, which defines the Pell spine, and shows that the Pell spine forms the record frontier of the continuous proximity measure when primitive triples are ordered by increasing hypotenuse.

The two repositories are complementary: **Structural Addresses** develops the general framework; **Pell Spine** provides one concrete arithmetic application. Both are reproducibility companions; the authoritative scholarly records, including the most recent conceptual revisions, are maintained on Zenodo.

## 11. Citation

Cite the manuscript rather than the repository.

> De Jesús, E. (2026). *Structural Addresses: Continuous Proximity, Discrete Membership, and Compatible Markers in Inheritance Systems: A Methodological Note with Hypergeometric, Gamma–Period, and Finite-State Controls.* Zenodo.

- Current version: <https://doi.org/10.5281/zenodo.21297926>
- All versions / latest version: <https://doi.org/10.5281/zenodo.21263921>

```bibtex
@article{dejesus2026structuraladdresses,
  author  = {De Jes{\'u}s, Elias},
  title   = {Structural Addresses: Continuous Proximity, Discrete Membership,
             and Compatible Markers in Inheritance Systems: A Methodological
             Note with Hypergeometric, Gamma--Period, and Finite-State Controls},
  year    = {2026},
  publisher = {Zenodo},
  doi     = {10.5281/zenodo.21297926},
  url     = {https://doi.org/10.5281/zenodo.21297926}
}
```

Repository: <https://github.com/innerlightr-wq/structural-addresses-methodology>

## 12. Licensing

- **Source code, tests, examples, and `reproduce.py`**: MIT License — see [`LICENSE-CODE`](LICENSE-CODE).
- **README prose, generated figures, generated data, and manuscript-related material**: Creative Commons Attribution 4.0 International (CC BY 4.0) — see [`LICENSE`](LICENSE).

## 13. AI-assistance disclosure

AI assistance (Anthropic's Claude) was used for algebraic and computational verification, adversarial auditing, repository construction, testing, and manuscript preparation. Conceptual development, research direction, interpretation, and final responsibility for all content remain with the author. AI systems are not authors.

## 14. Author

**Elias De Jesús**
Independent Researcher
ORCID: [0009-0007-0190-9143](https://orcid.org/0009-0007-0190-9143)
Email: <dejesuselias10@gmail.com>
