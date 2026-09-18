# Literature context for Structural Addresses

Organized by **conceptual ancestry** rather than chronology: each section names the field a part of
the framework comes from, what that field already supplies, and what — if anything — is left over.

**This is not a novelty claim.** Per-claim provenance is in
[`NOVELTY_AND_PROVENANCE.md`](NOVELTY_AND_PROVENANCE.md); verified records are in
[`../references.bib`](../references.bib) (27 entries, 25 with DOIs, all obtained from publisher or
registry metadata).

**Scope rule.** Listed here is literature that is part of the framework's provenance — material a
claim uses, restates, or must be compared against as closest prior art — plus the classical sources
the worked examples rest on. Works merely consulted are not listed.

**How the references were checked (September 2026).** Bibliographic data came from DOI content
negotiation against publisher metadata, or from the Crossref transform endpoint where the publisher
returned no BibTeX. Two records ([Mi80], [CS67]) carry incomplete publisher metadata; the missing
author/title fields were supplied from the standard attribution and are flagged in the `.bib` note.
Two sources ([Mo56], [KS60]) are not deposited with Crossref and their metadata is from the standard
bibliographic record, unverified against the volumes.

---

## 1. Quotients, factorization and descent — the closure condition

The framework's central condition is that an inherited marker *closes*:

    ker Σ_ℓ ⊆ ker(Σ_{ℓ+1} ∘ E_ℓ)

**This is the universal property of the quotient.** A map factors through an equivalence relation
exactly when its kernel contains that of the quotient map; for a self-map of a finite set, a
partition induces well-defined reduced dynamics exactly when each block maps into a single block.
`inheritance.py`'s own docstring says so — it calls such a partition a *congruence*.

The same condition is the defining condition of a **Nerode congruence** [Ne58]: the minimal
automaton of a regular language is the quotient by the coarsest right-congruence, and the criterion
for a partition to descend is precisely the one above. Moore [Mo56] introduced the refinement
procedure for computing it.

**Nothing in the framework strengthens this criterion.** The contribution on this axis is
vocabulary: "a marker closes" in place of "the map descends to the quotient".

Adjacent, and worth knowing: **sufficient statistics** [HS49] are the probabilistic form of the
same factorization idea — a statistic is sufficient exactly when the likelihood factors through it.

## 2. Automata, bisimulation and partition refinement — the algorithm

`coarsest_stable_refinement` computes the coarsest refinement of a target partition that is stable
under the transition map, by iterated preimage splitting. This is a textbook computation with a
well-known lineage:

* **Moore** [Mo56] — refinement for state minimization;
* **Hopcroft** [Ho71] — the `O(n log n)` minimization algorithm;
* **Paige–Tarjan** [PT87] — the *relational coarsest partition* problem in `O(m log n)`, which is
  exactly the specification `coarsest_stable_refinement` implements;
* **Kanellakis–Smolka** [KS90], with **Milner** [Mi80] and **Park** [Pa81] for bisimulation itself —
  the same refinement, read as behavioural equivalence.

For a total deterministic map — the repository's case — bisimulation collapses to "f-invariant
partition", the easiest case of the general problem. The repository's implementation is the naive
iterative version, and claims no algorithmic novelty.

**On "inheritance markers."** A marker that closes is a congruence-respecting partition, i.e. a
deterministic bisimulation. The term is new; the object is not.

## 3. Markov lumpability — the stochastic form, and a direction-of-generality warning

**Strong lumpability** [KS60, Ch. VI]: a finite Markov chain is lumpable with respect to a partition
iff, for every pair of blocks, the transition probability into the second block is the same from
every state of the first; the lumped process is then Markov. Buchholz [Bu94] separates *exact* from
*ordinary* lumpability; weak lumpability is a genuinely different and harder condition
[AL82], and Larsen–Skou [LS91] give the process-algebraic counterpart, probabilistic bisimulation.

**Direction of generality.** A deterministic map is a Markov chain whose rows are 0/1 vectors, and
for such a chain the equal-row-sums criterion reduces to "each block maps into a single block". So
the repository's closure condition is the **deterministic special case** of strong lumpability — not
a generalization of it. The README's existing warning ("strong lumpability must not be conflated
with weak or stationary-distribution lumpability") is correct and should be kept; this section adds
the complementary warning, that the framework is *less* general, not more.

## 4. Symbolic dynamics and coding — where "address" already means something

In symbolic dynamics an **address** is the itinerary of a point: the sequence of partition elements
its orbit visits. Lind–Marcus [LM95] is the standard reference; Adler [Ad98] surveys Markov
partitions; Milnor–Thurston [MT88] develop the interval case as kneading theory.

So "address" is established terminology for what this framework calls the **discrete** component `δ`
alone. "Structural address" denotes the *pair* `(Σ_c, δ)`, which is not what the term means in
symbolic dynamics. The term should be defined against that usage on first appearance.

## 5. Immersions, embeddings and local coordinates — the continuous layer

"A signature map supplies local navigation coordinates exactly where it is a local embedding, and
only after quotienting by automorphisms" is classical differential topology: immersions, the inverse
function theorem, and local embedding [Wh36]. The repository states this as classical, and it is.

**Stratification** [Th69] is the geometric ancestor of the two-part address itself: a stratified
space is a disjoint union of strata, each a manifold with its own coordinates, so that "which
stratum" is a discrete invariant and "where in the stratum" is a continuous coordinate — exactly the
shape of `Addr(x)`.

## 6. Identifiability, stability and conditioning — the three levels

The framework's Appendix-D trichotomy maps onto three well-established notions:

| framework level | criterion | standard name |
|---|---|---|
| exact recoverability | `ker Σ_c ⊆ ker δ` | **identifiability** / injectivity of the parameter-to-observable map [Ro71]; sufficiency [HS49] |
| stable classification | each `Σ_c(S_τ)` relatively open | **stability** — Hadamard's third well-posedness condition, continuous dependence |
| numerical conditioning | smallest singular value of `dΣ_c` | **condition number** [Tu48, Ri66] |

Read together, these are Hadamard's well-posedness conditions (uniqueness, stability) refined by the
quantitative sensitivity measure that Turing introduced for matrix problems and Rice generalized to
arbitrary problems. The trichotomy is therefore **classical**.

What the reviewed literature did not supply in one place is this trichotomy stated for the problem
of recovering a **discrete label** from a continuous observable, with explicit witnesses showing
both implications strict. That is the framework's strongest surviving contribution, and it is
methodological rather than theorem-level.

## 7. Arithmetic and special-function examples — illustration, not evidence

These sources supply the *examples*. None of them is evidence for the framework.

* **Ramanujan-type series for `1/π`** [BBC09] — the survey covering the `9801/(2√2)` series with
  `1103 + 26390n` that Control I detunes. The identity is classical; the detuning and the derivative
  values are the repository's own computation.
* **Beta and gamma special values** — Control II's `J(s) = Γ(s+1)²/Γ(2s+2) = B(s+1, s+1)`. All four
  displayed identities follow from `Γ(z+1) = zΓ(z)` and the reflection formula, and were re-derived
  in the audit ([`NOVELTY_AND_PROVENANCE.md`](NOVELTY_AND_PROVENANCE.md) §5).
* **Complex multiplication and singular values** [Co13], with the **Chowla–Selberg formula** [CS67]
  for the gamma-period connection — classical arithmetic rigidity, used as an instance of a discrete
  invariant.
* **Transcendence of periods** [Wa06] — the standing context for why "numerically close to a
  special value" is not "equal to it", and for the open status of the Rohrlich–Lang classification
  problem the README correctly declines to address.

## 8. The combination — hybrid systems, and the one real comparison

The question that matters is not whether the ingredients are classical (they are) but whether their
**assembly** is new. The closest prior art is **hybrid automata** [ACH95, He96], where a state is a
pair `(q, x) ∈ Q × ℝⁿ` of a discrete mode and a continuous valuation, and the analysis proceeds by
partitioning the continuous part compatibly with the dynamics — i.e. by a bisimulation. That is a
discrete label, continuous coordinates, and a descent condition, in one framework, decades earlier.

The difference is **subject matter, not structure**: hybrid automata study reachability of a
dynamical system, whereas Structural Addresses asks membership questions in analytic and arithmetic
families where the continuous part carries no transition structure at all. Transferring the pairing
to that setting is a legitimate methodological act; it is not a new mathematical structure, and the
repository should not describe it as one.

## References

* **[Ad98]** R. L. Adler, "Symbolic dynamics and Markov partitions", *Bull. Amer. Math. Soc.* **35** (1998), 1–56. DOI: [10.1090/S0273-0979-98-00737-X](https://doi.org/10.1090/S0273-0979-98-00737-X).
* **[AL82]** A. M. Abdel-Moneim and F. W. Leysieffer, "Weak lumpability in finite Markov chains", *J. Appl. Probab.* **19** (1982), 685–691. DOI: [10.2307/3213528](https://doi.org/10.2307/3213528).
* **[ACH95]** R. Alur, C. Courcoubetis, N. Halbwachs, T. A. Henzinger et al., "The algorithmic analysis of hybrid systems", *Theoret. Comput. Sci.* **138** (1995), 3–34. DOI: [10.1016/0304-3975(94)00202-T](https://doi.org/10.1016/0304-3975(94)00202-T).
* **[BBC09]** N. D. Baruah, B. C. Berndt and H. H. Chan, "Ramanujan's series for 1/π: a survey", *Amer. Math. Monthly* **116** (2009), 567–587. DOI: [10.1080/00029890.2009.11920975](https://doi.org/10.1080/00029890.2009.11920975).
* **[Bu94]** P. Buchholz, "Exact and ordinary lumpability in finite Markov chains", *J. Appl. Probab.* **31** (1994), 59–75. DOI: [10.2307/3215235](https://doi.org/10.2307/3215235).
* **[Co13]** D. A. Cox, *Primes of the Form x² + ny²*, 2nd ed., Wiley, 2013. DOI: [10.1002/9781118400722](https://doi.org/10.1002/9781118400722).
* **[CS67]** S. Chowla and A. Selberg, "On Epstein's zeta-function", *J. reine angew. Math.* **227** (1967), 86–110. DOI: [10.1515/crll.1967.227.86](https://doi.org/10.1515/crll.1967.227.86). (The Crossref record carries no author field for this volume; the attribution is the standard one.)
* **[He96]** T. A. Henzinger, "The theory of hybrid automata", *Proc. 11th IEEE Symp. Logic in Computer Science* (1996), 278–292. DOI: [10.1109/LICS.1996.561342](https://doi.org/10.1109/LICS.1996.561342).
* **[Ho71]** J. E. Hopcroft, "An n log n algorithm for minimizing states in a finite automaton", in *Theory of Machines and Computations*, Academic Press, 1971, 189–196. DOI: [10.1016/B978-0-12-417750-5.50022-1](https://doi.org/10.1016/B978-0-12-417750-5.50022-1).
* **[HS49]** P. R. Halmos and L. J. Savage, "Application of the Radon–Nikodym theorem to the theory of sufficient statistics", *Ann. Math. Statist.* **20** (1949), 225–241. DOI: [10.1214/aoms/1177730032](https://doi.org/10.1214/aoms/1177730032).
* **[KS60]** J. G. Kemeny and J. L. Snell, *Finite Markov Chains*, Van Nostrand, 1960. (Not deposited; metadata from the standard record. Ch. VI: strong lumpability.)
* **[KS90]** P. C. Kanellakis and S. A. Smolka, "CCS expressions, finite state processes, and three problems of equivalence", *Inform. and Comput.* **86** (1990), 43–68. DOI: [10.1016/0890-5401(90)90025-D](https://doi.org/10.1016/0890-5401(90)90025-D).
* **[LM95]** D. Lind and B. Marcus, *An Introduction to Symbolic Dynamics and Coding*, Cambridge University Press, 1995. DOI: [10.1017/CBO9780511626302](https://doi.org/10.1017/CBO9780511626302).
* **[LS91]** K. G. Larsen and A. Skou, "Bisimulation through probabilistic testing", *Inform. and Comput.* **94** (1991), 1–28. DOI: [10.1016/0890-5401(91)90030-6](https://doi.org/10.1016/0890-5401(91)90030-6).
* **[Mi80]** R. Milner, *A Calculus of Communicating Systems*, Lecture Notes in Computer Science **92**, Springer, 1980. DOI: [10.1007/3-540-10235-3](https://doi.org/10.1007/3-540-10235-3). (The DOI record carries no author field.)
* **[Mo56]** E. F. Moore, "Gedanken-experiments on sequential machines", in *Automata Studies*, Princeton University Press, 1956, 129–153. (Not deposited; metadata from the standard record.)
* **[MT88]** J. Milnor and W. Thurston, "On iterated maps of the interval", *Lecture Notes in Mathematics* **1342** (1988), 465–563. DOI: [10.1007/BFb0082847](https://doi.org/10.1007/BFb0082847).
* **[Ne58]** A. Nerode, "Linear automaton transformations", *Proc. Amer. Math. Soc.* **9** (1958), 541–544. DOI: [10.1090/S0002-9939-1958-0135681-9](https://doi.org/10.1090/S0002-9939-1958-0135681-9).
* **[Pa81]** D. Park, "Concurrency and automata on infinite sequences", *Lecture Notes in Computer Science* **104** (1981), 167–183. DOI: [10.1007/BFb0017309](https://doi.org/10.1007/BFb0017309).
* **[PT87]** R. Paige and R. E. Tarjan, "Three partition refinement algorithms", *SIAM J. Comput.* **16** (1987), 973–989. DOI: [10.1137/0216062](https://doi.org/10.1137/0216062).
* **[Ri66]** J. R. Rice, "A theory of condition", *SIAM J. Numer. Anal.* **3** (1966), 287–310. DOI: [10.1137/0703023](https://doi.org/10.1137/0703023).
* **[Ro71]** T. J. Rothenberg, "Identification in parametric models", *Econometrica* **39** (1971), 577–591. DOI: [10.2307/1913267](https://doi.org/10.2307/1913267).
* **[Th69]** R. Thom, "Ensembles et morphismes stratifiés", *Bull. Amer. Math. Soc.* **75** (1969), 240–284. DOI: [10.1090/S0002-9904-1969-12138-5](https://doi.org/10.1090/S0002-9904-1969-12138-5).
* **[Tu48]** A. M. Turing, "Rounding-off errors in matrix processes", *Quart. J. Mech. Appl. Math.* **1** (1948), 287–308. DOI: [10.1093/qjmam/1.1.287](https://doi.org/10.1093/qjmam/1.1.287).
* **[Wa06]** M. Waldschmidt, "Transcendence of periods: the state of the art", *Pure Appl. Math. Q.* **2** (2006), 435–463. DOI: [10.4310/PAMQ.2006.v2.n2.a3](https://doi.org/10.4310/PAMQ.2006.v2.n2.a3).
* **[Wh36]** H. Whitney, "Differentiable manifolds", *Ann. of Math.* **37** (1936), 645–680. DOI: [10.2307/1968482](https://doi.org/10.2307/1968482).

Machine-readable records: [`../references.bib`](../references.bib).
