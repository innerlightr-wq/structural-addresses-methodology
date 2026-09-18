# Novelty and provenance audit

*Zotero-assisted literature, provenance and novelty audit, September 2026. Carried out after
the fact, with the explicit purpose of establishing whether Structural Addresses contributes
distinct mathematics or assembles classical material — and of **reducing** novelty wording
wherever prior work is closer than previously recognized.*

Companion: [`LITERATURE_CONTEXT.md`](LITERATURE_CONTEXT.md) (conceptual ancestry).
Bibliography: [`../references.bib`](../references.bib) — 27 entries, 25 with DOIs, every record
obtained from publisher or registry metadata by DOI content negotiation, none typed from memory.

**Headline answer.** The component mathematics is **entirely classical**, which the repository
already states. The *combination* — a discrete label paired with continuous coordinates, subject
to a descent condition — is **also not new**: it is the structure of a hybrid automaton and of a
stratified space. What survives as this project's own contribution is **not theorem-level**: it is
the crisp three-level separation of identifiability, stability and conditioning applied to
membership questions in analytic and arithmetic families, together with one genuinely useful
methodological warning. Classification: **METHODOLOGICAL SYNTHESIS**, with one claim needing
qualification.

**Method and its limits.** Claim-level comparison used verified bibliographic records and
published abstracts; the two finite-state claims and all four gamma identities were re-derived
here independently (see §5). This is a targeted prior-art search across seven fields, not a
systematic review of any of them. Absence of a prior result here means *not found in the sources
reviewed*.

---

## 1. Claim inventory

The repository is small: `README.md` (261 lines), five Python modules, two figures. Substantive
statements, classified before any literature search:

| # | statement | initial class |
|---|---|---|
| 1 | `Addr(x) = (Σ_c(x), δ(x))`, a continuous signature paired with a discrete invariant | methodological definition |
| 2 | "The two components carry independent information" | claimed new synthesis |
| 3 | "Continuous navigation and exact identification are different tasks"; signatures give local coordinates where they are local embeddings, after quotienting by automorphisms | classical ingredient |
| 4 | A marker closes iff `ker Σ_ℓ ⊆ ker(Σ_{ℓ+1} ∘ E_ℓ)` | proposition |
| 5 | Closure and separation are logically independent | proposition + witness |
| 6 | An injective continuous observable can permit exact recovery yet fail proximity-stable classification | proposition + witness |
| 7 | Three levels: exact recoverability / stable classification / numerical conditioning, with both implications strict | claimed new synthesis |
| 8 | `coarsest_stable_refinement` by iterated preimage refinement | algorithm |
| 9 | Control I: detuned Ramanujan `1/π` family, `L_396 = 1/π`, derivatives, digits-per-term | example / numerical |
| 10 | Control II: `J(s) = Γ(s+1)²/Γ(2s+2)`, `J(1/2) = π/8`, `J(1/4)·J(3/4) = π/20` | exact algebraic identity (classical) |
| 11 | Control III: the four-state system and its closure/separation table | example / witness |
| 12 | "Numerical closeness to a special value is not proof of arithmetic membership" | methodological warning |
| 13 | CM special values as discrete addresses | example |
| 14 | The term "structural address" | terminology |

## 2. Novelty matrix

Classifications: **CLASSICAL** · **KNOWN / REPARAMETERIZED** · **FORMALIZATION OF KNOWN RESULT** ·
**NEW DERIVATION OF KNOWN INGREDIENTS** · **NEW TERMINOLOGY / KNOWN STRUCTURE** ·
**METHODOLOGICAL SYNTHESIS** · **APPARENTLY DISTINCT RESULT** · **NEGATIVE RESULT** ·
**EXAMPLE ONLY** · **UNCERTAIN — MORE SEARCH NEEDED**

| # | Claim / concept | Location | Mathematical content | Closest prior work | Equivalent standard terminology | Relationship | Formal status | Novelty classification | Recommended wording | Keys |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `Addr(x) = (Σ_c(x), δ(x))` | README §2; `structural_address.py` | a pair: metric coordinate + class label | hybrid automata: state `(q, x) ∈ Q × ℝⁿ`; stratified spaces: stratum label + smooth chart | hybrid state; stratum + chart; labelled fibre | **equivalent under notation.** Both prior frameworks pair a discrete label with continuous coordinates *and* impose a compatibility condition | definition | **NEW TERMINOLOGY / KNOWN STRUCTURE** | "a two-part coordinate of the kind standard in hybrid-systems and stratification theory, applied here to analytic and arithmetic families" | `AlurEtAl1995`, `Henzinger1996`, `Thom1969`, `Whitney1936` |
| 2 | "The two components carry independent information" | README §2 | — | — | — | **overstated, and in tension with README §3.** Where `Σ_c` is injective — which is the case in *both* analytic controls, as §3 itself says — `ker Σ_c` is trivial, so `δ` factors through `Σ_c` and carries **no** additional set-theoretic information. The independence that the controls actually exhibit is of *stability*, not of information | — | **NEEDS QUALIFICATION** (see §4) | "the two components answer different questions; where `Σ_c` is injective, `δ` is determined by `Σ_c` set-theoretically, and the independence at issue is one of stability, not of information" | — |
| 3 | Local coordinates where `Σ_c` is a local embedding | README §2 | immersion / inverse function theorem | classical differential topology | immersion; local embedding | **identical**; the README already says so | classical import | **CLASSICAL** | keep, with a citation | `Whitney1936` |
| 4 | Closure condition `ker Σ_ℓ ⊆ ker(Σ_{ℓ+1} ∘ E_ℓ)` | README §2; `inheritance.py::is_congruence` | a partition induces well-defined reduced dynamics iff each block maps into a single block | Nerode congruence; f-invariant partition; deterministic bisimulation; **deterministic case of strong lumpability** | congruence; quotient/descent criterion | **identical.** This is the standard requirement that a map descend to a quotient. The module docstring already identifies it as a congruence | proposition (elementary) | **CLASSICAL** | "the classical congruence/descent criterion, in the deterministic case" — never "a new condition" or "a generalization of lumpability" | `Nerode1958`, `Moore1956`, `KemenySnell1960`, `KanellakisSmolka1990` |
| 5 | Closure and separation are independent | README §2, §4; Control III | a congruence need not refine a target partition, and a refinement need not be a congruence | elementary lattice-of-partitions fact | congruence vs. refinement | **classical fact**; the explicit 4-state witness realizing all four combinations is a clean pedagogical artefact | proposition + verified witness | **CLASSICAL** (fact) + **EXAMPLE ONLY** (witness) | "the two properties are logically independent, as the four-state witness shows" | `Nerode1958`, `PaigeTarjan1987` |
| 6 | Injective observable ⇒ exact recovery but not stable classification | README §2, §3 | an injective continuous map need not be a homeomorphism onto its image | classical point-set topology; ill-posedness | injective ≠ embedding; instability of inversion | **classical**, with new illustrative witnesses drawn from `1/π` series and gamma quotients | proposition + witnesses | **CLASSICAL** (fact), witnesses **EXAMPLE ONLY** | "a classical distinction, illustrated here by two analytic families" | `Rothenberg1971`, `Rice1966` |
| 7 | Three levels: recoverability / stability / conditioning, both implications strict | README §3 | uniqueness; local constancy; quantitative inverse bound | **Hadamard well-posedness** (existence/uniqueness/continuous dependence) refined by the condition number; identifiability (`Rothenberg1971`); `Turing1948`, `Rice1966` | identifiability; stability; conditioning | **the trichotomy is classical**, and is the standard decomposition in inverse problems. What is not found in one place in the reviewed literature is this trichotomy stated for *recovering a discrete label from a continuous observable*, with explicit strictness witnesses | definitions + witnesses | **METHODOLOGICAL SYNTHESIS** — the strongest surviving claim | "a restatement, for discrete-label recovery, of the classical separation between identifiability, stability and conditioning; no equivalent single treatment for this setting was identified in the literature reviewed" | `Rothenberg1971`, `Turing1948`, `Rice1966`, `HalmosSavage1949` |
| 8 | `coarsest_stable_refinement` | `inheritance.py` | coarsest refinement of a target that is stable under the map | **Moore's algorithm; Hopcroft; Paige–Tarjan relational coarsest partition** | partition refinement; coarsest bisimulation | **identical specification**, naive algorithm rather than `O(m log n)`. The docstring already says "bisimulation-style" | algorithm | **CLASSICAL** | "the classical coarsest-stable-refinement computation, restricted to deterministic maps; no algorithmic novelty" | `Moore1956`, `Hopcroft1971`, `PaigeTarjan1987`, `KanellakisSmolka1990` |
| 9 | Control I, Ramanujan `1/π` family | README §4; `ramanujan_control.py` | `L_396 = 1/π`; detuned `L_D`; analytic derivatives; digits/term `= 4log₁₀D − log₁₀256` | Ramanujan's `1/π` series (1914), surveyed in `BaruahBerndtChan2009` | Ramanujan-type series for `1/π` | the identity is **classical**; the detuning, the derivative values and the window width are the repository's own computation, and illustrate rather than establish | example + numerical | **EXAMPLE ONLY** (classical identity) | "an illustration built on a classical series; it establishes nothing about the framework" | `BaruahBerndtChan2009` |
| 10 | Control II, `J(s) = Γ(s+1)²/Γ(2s+2)` | README §4; `beta_gamma_control.py` | `J(1/2)=π/8`; `J(1/4)=Γ(1/4)²/(12√π)`; `J(3/4)=3Γ(3/4)²/(10√π)`; `J(1/4)J(3/4)=π/20` | gamma recursion + **reflection formula** | beta-function special values | **classical.** All four re-derived in this audit from `Γ(z+1)=zΓ(z)` and `Γ(1/4)Γ(3/4)=π√2` — see §5. `J = B(s+1,s+1)` is a beta value | exact identities, verified | **CLASSICAL** / **EXAMPLE ONLY** | "classical beta/gamma values, used as a stratified test family" | — |
| 11 | Control III, four-state table | README §4; `inheritance.py` | the 2×2 independence witness | — | — | **verified here** (§5), and the table's four rows are correct. The row labelled "composite" is `Σ ∧ κ`, not the meet of `Σ` and `M` | verified witness | **EXAMPLE ONLY** | see §4 for a labelling fix | — |
| 12 | "Numerical closeness is not proof of arithmetic membership" | README §8 | no finite tolerance certifies exact membership | folklore in experimental mathematics; the identifiability/stability gap | approximate vs. exact membership | **classical in substance**, but the clearest and most useful statement in the repository, and a real failure mode in special-function work | methodological warning | **METHODOLOGICAL SYNTHESIS** (best-value item) | keep verbatim; this is the framework's strongest practical contribution | `Waldschmidt2006` |
| 13 | CM special values as discrete addresses | README §8 | singular moduli, class-field rigidity | classical CM theory | complex multiplication; singular values | **classical**; used as an example of a discrete invariant, as the README says | example | **EXAMPLE ONLY** | "classical CM rigidity, used as an instance of a discrete invariant" | `Cox2013`, `ChowlaSelberg1967`, `Waldschmidt2006` |
| 14 | The term "structural address" | throughout | — | **"address" already denotes the symbolic itinerary** of a point under a Markov partition | symbolic address; itinerary; code | **terminology overlap.** In symbolic dynamics an address is precisely the *discrete* label; here "structural address" denotes the *pair*, so the term collides with established usage | terminology | **NEW TERMINOLOGY / KNOWN STRUCTURE** | define against the symbolic-dynamics meaning on first use, and note that `δ` is the analogue of a symbolic address | `LindMarcus1995`, `Adler1998`, `MilnorThurston1988` |
| 15 | Level hierarchy `Σ_0, Σ_1, Σ_2, …` | README §2 | a chain of markers with descent between consecutive levels | refinement lattice; abstraction/refinement hierarchies; nested partitions | filtration; abstraction hierarchy | **classical nested-partition machinery**; no composition theorem is proved, and none is claimed | definition | **CLASSICAL** | "a chain of nested markers, each descending to the next — standard refinement machinery" | `PaigeTarjan1987`, `Buchholz1994` |

## 3. Is the Structural Addresses synthesis itself distinct?

The decisive section. Each row answers the same six questions against one field.

| Field | Closest existing concept | Overlap | Difference | Adds theorem-level content? | Adds organizational language? | Enables nontrivial cross-domain transfer? |
|---|---|---|---|---|---|---|
| **Quotient / factorization theory** | universal property of the quotient; `ker f ⊆ ker g ⟹ g` factors | **complete** for claim 4 | none | **No** — claim 4 *is* the universal property | yes: "closes" is more vivid than "descends to the quotient" | no |
| **Symbolic dynamics & coding** | itinerary / symbolic address under a Markov partition | the discrete component `δ` | the continuous component is not part of a symbolic coding; no shift, no Markov partition | **No** | mixed — the word "address" collides with established usage | no |
| **Automata & bisimulation** | Nerode congruence; coarsest stable refinement; Moore/Hopcroft/Paige–Tarjan | **complete** for claims 4, 5, 8 and the algorithm | the repository's maps are total deterministic functions, the easiest case | **No** | yes: "inheritance marker" reads more naturally than "congruence-respecting partition" in a non-automata context | no |
| **Markov lumpability** | strong lumpability (`KemenySnell1960`), exact/ordinary lumpability (`Buchholz1994`) | claim 4 is the **deterministic special case** | the repository is deterministic, so strictly less general | **No** — and emphatically *not* a generalization | yes | no |
| **Inverse problems / identifiability** | identifiability; Hadamard well-posedness | claims 6, 7 level 1–2 | the "parameter" here is a discrete label rather than a continuous parameter | **No** | yes — level 1 vs. level 2 is often elided in practice | **partially yes** — importing identifiability language into special-function work is a real transfer |
| **Numerical conditioning** | condition number (`Turing1948`, `Rice1966`) | level 3 exactly | none | **No** | yes | no |
| **State abstraction / stratification** | abstract interpretation; Whitney/Thom stratification; hybrid automata | **the pairing itself, plus the descent condition** | purpose: hybrid automata analyse reachability of a dynamical system; the repository asks membership questions in families with no transition structure on the continuous part | **No** | yes | **partially yes** |

**Answers to the five separated questions.**

* **A. Are the component facts known?** **Yes, all of them** — and the repository says so in §8.
* **B. Is the combination known?** **Yes, in structure.** Hybrid automata pair a discrete mode with
  continuous coordinates and require a bisimulation-compatible partition; stratified spaces pair a
  stratum label with local charts. The repository's `Addr(x)` plus closure condition has the same
  shape as both. What was *not* located is this pairing deployed for membership questions in
  analytic/arithmetic families — but that is a change of subject matter, not of structure.
* **C. Is the residue substantive or organizational?** **Mainly organizational and expository.** No
  theorem in the repository fails to be a restatement or an instance of a classical one.
* **D. Does it prove anything beyond standard quotient language?** **No.** Every proposition is
  derivable in one or two lines from the universal property of quotients, the definition of a
  congruence, or elementary topology.
* **E. Does it identify a distinction obscured in existing terminology?** **Yes, one, and it is the
  project's best claim to value:** that numerical proximity to a special value carries no
  information about exact arithmetic membership, and that identifiability, stability and
  conditioning must be separated when the object recovered is a *discrete* label. In
  experimental-mathematics practice this is a live failure mode, and no single prior treatment of it
  in this setting was identified.

## 4. Claims requiring a wording change

Only two, both small.

**4.1 "The two components carry independent information" (README §2) — NEEDS QUALIFICATION.**
This is the one statement the audit judges too strong, and it conflicts with §3 of the same
README, which observes that `D ↦ L_D` and `s ↦ J(s)` are injective, so that "exact parameter and
class information *can* factor set-theoretically through the scalar observables". If `Σ_c` is
injective then `ker Σ_c` is trivial, hence `ker Σ_c ⊆ ker δ` holds automatically and `δ` is a
function of `Σ_c`: it adds **no** set-theoretic information. `structural_address.py`'s own
docstring makes the same point — "an injective signature makes this trivially true". The
independence the controls exhibit is between *what is determined* and *what is stably decidable*.
Recommended replacement: the two components **answer different questions**, and where `Σ_c` is
injective `δ` is set-theoretically redundant while remaining the only proximity-robust label.

**4.2 The "composite" row of the Control III table — labelling only.**
`{{1,3},{2},{4}}` does close and does separate `κ` (verified, §5), so the row is correct. But it is
the meet `Σ ∧ κ`, not `common_refinement(Σ, M)`, which is the discrete partition `{{1},{2},{3},{4}}`,
nor `coarsest_stable_refinement(X, f, κ)`, which returns `κ` itself. Name it `Σ ∧ κ`.

## 5. What this audit re-derived independently

* **All four gamma identities of Control II**, from `Γ(z+1) = zΓ(z)` and the reflection formula
  `Γ(1/4)Γ(3/4) = π√2`: `J(1/2) = (√π/2)²/2 = π/8`; `J(1/4) = (Γ(1/4)/4)²/((3/4)√π) =
  Γ(1/4)²/(12√π)`; `J(3/4) = (3Γ(3/4)/4)²/((15/8)√π) = 3Γ(3/4)²/(10√π)`; and
  `J(1/4)·J(3/4) = Γ(1/4)²Γ(3/4)²/(40π) = 2π²/(40π) = π/20`. **All four confirmed**, and all four
  are classical gamma manipulations.
* **The Control III table**, by running `inheritance.py`: `κ` closes and separates; `Σ` closes and
  does not separate; `M` does not close and does separate; `Σ ∧ κ` does both. **All four rows
  confirmed.**
* **`coarsest_stable_refinement(X, f, κ) = κ`** — correct, since `κ` already closes.

**Not executed:** Controls I and II as shipped. `mpmath`, `numpy` and `matplotlib` are absent from
this machine, and no `requirements.txt` exists in the repository (see §6). The gamma identities were
therefore verified symbolically by hand instead, which is stronger than a floating-point check.

## 6. Repository-hygiene findings (not novelty matters)

The README's §7 "Repository structure" describes a layout the repository does not have, and §5's
reproduction instructions cannot run as written:

| README says | actually |
|---|---|
| `src/…`, `examples/…`, `tests/…`, `paper/`, `data/`, `figures/` | all five Python modules sit at the repository root; none of these directories exist |
| `requirements.txt`, `pytest.ini`, `conftest.py`, `.gitignore` | absent |
| `pip install -r requirements.txt`; `python reproduce.py`; `pytest -q`; `python examples/01_…` | the first, third and fourth cannot run; figures are at the root, not in `figures/` |
| "Repository URL: `TODO`" | the repository is published at `innerlightr-wq/structural-addresses-methodology` |

These are documentation defects rather than provenance ones, and are listed so they are not lost.

## 7. Unresolved questions

1. **Hybrid automata and stratification as prior art for the *combination*** — flagged
   `uncertain-more-search`. The structural analogy is clear from the definitions; whether any prior
   author has explicitly drawn the "continuous proximity vs. discrete membership" distinction *for
   special-value membership questions* was not settled.
2. Whether the three-level separation (claim 7) appears as a unit anywhere in the inverse-problems
   literature specialized to discrete-label recovery. Not found; not proven absent.
3. The companion Pell-spine application was not audited here.
