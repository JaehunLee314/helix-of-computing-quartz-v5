## Overview

Every item in scope can be stated in Telescope 0.2.0, from PAC learnability through the Fundamental Theorem, and the definitions read close to the book's sentences. The statements use the spec's probability extension (`Prob[x ~ P](…)`, `E[x ~ P](…)`, `D^m`), chained `<=>`, `Bool`, pairs, `lambda e, d:` and preconditions on generics.

The text follows Shalev-Shwartz and Ben-David, *Understanding Machine Learning*, chapters 2 to 6, with the book's numbering. Everything is binary classification: labels are `Bool` (the book's {0, 1}) and the loss is the 0-1 loss, except for one general-loss definition in section 1. Proofs are out of scope for 0.2.0, so only statements are given. Nothing here has been compiled.

| Book | Telescope | Meaning |
| --- | --- | --- |
| $\mathcal{X}$, $h : \mathcal{X} \to \{0, 1\}$, $\mathcal{H}$ | `X : Type`, `h : X -> Bool`, `H : Set(X -> Bool)` | Domain, hypothesis, hypothesis class |
| $\mathcal{D}$ over $\mathcal{X} \times \{0, 1\}$ | `D : Measure(X × Bool) where IsProbabilityMeasure(D)` | Data distribution |
| $S = ((x_1, y_1), \dots, (x_m, y_m))$ | `S : (X × Bool)^m`, entries `S(i)` for $i$ in $0$ to $m - 1$ | Training sample |
| $\mathbb{P}_{S \sim \mathcal{D}^m}[\dots]$ | `Prob[S ~ D^m](…)` | Probability over i.i.d. samples |
| $L_{\mathcal{D}}(h)$, $L_{(\mathcal{D},f)}(h)$, $L_S(h)$ | `Error(D, h)`, `ErrorF(D, f, h)`, `EmpError(S, h)` | True, realizable, empirical error |
| $A : \bigcup_m (\mathcal{X} \times \{0, 1\})^m \to \{0, 1\}^{\mathcal{X}}$ | `A : (m : N) -> (X × Bool)^m -> (X -> Bool)`; with $m$ fixed, `let learn = A(m)` | Learning algorithm |
| $m_{\mathcal{H}}(\varepsilon, \delta)$ | `mH : R -> R -> N`, applied as `mH(e, d)` | Sample complexity |
| $\mathrm{VCdim}(\mathcal{H})$ | `VCdim(H) : ENat` | VC dimension, possibly $\infty$ |

Each code block is its own file with the earlier definitions in scope. $\varepsilon$ and $\delta$ are written `e` and `d`, except where `d` is the VC dimension; there $\delta$ is `delta`.

## 1. Setup: data, errors and learners

The book's formal model (sections 2.1 and 3.2) is a domain, binary labels, an unknown distribution over labelled points, and a sample of $m$ points drawn i.i.d. from it. Errors are probabilities of the event "$h$ gets it wrong", written with the probability binder `Prob[z ~ D](…)`.

**True error, realizable error and empirical error.** $L_{\mathcal{D}}(h) = \mathbb{P}_{z \sim \mathcal{D}}[h(x) \neq y]$. In the realizable chapters the distribution is over $\mathcal{X}$ alone and a labelling function $f$ supplies $y$, so $L_{(\mathcal{D},f)}(h) = \mathbb{P}_{x \sim \mathcal{D}}[h(x) \neq f(x)]$. The empirical error is the fraction of the sample $h$ gets wrong.

```text
def Error<X : Type>(D : Measure(X × Bool), h : X -> Bool) -> R {
  return Prob[z ~ D](h(z.1) != z.2)
}

def ErrorF<X : Type>(D : Measure(X), f : X -> Bool, h : X -> Bool) -> R {
  return Prob[x ~ D](h(x) != f(x))
}

def EmpError<X : Type, m : N where m >= 1>(S : (X × Bool)^m, h : X -> Bool) -> R {
  return card(Set[i : Fin(m) where h(S(i).1) != S(i).2](i)) / m
}
```

`card(…)` is a natural number and so is $m$, but `-> R` asks for a real, so the division happens in R by the spec's cast rule. `m >= 1` on the generic is a precondition: every call must show the sample is non-empty. `card` needs a finite set, and a subset of `Fin(m)` is one.

**Samples.** A sample is a tuple, and the book's $S \sim \mathcal{D}^m$ is the i.i.d. power `D^m`. In the realizable case the learner sees unlabelled points $x$ labelled by $f$.

```text
def Label<X : Type, m : N>(x : X^m, f : X -> Bool) -> (X × Bool)^m {
  return lambda i: (x(i), f(x(i)))
}
```

**Learners and ERM.** A learning algorithm takes a sample of any size and returns a hypothesis, so its type depends on the size. $\mathrm{ERM}_{\mathcal{H}}$ (section 2.2) returns some $h$ in $\mathcal{H}$ with the smallest empirical error. Ties are allowed, so ERM is a relation, and "an ERM rule" is any algorithm that always satisfies it.

```text
def ERM<X : Type, m : N where m >= 1>(H : Set(X -> Bool), S : (X × Bool)^m, h : X -> Bool) {
  h in H
  { let fix g in H; EmpError(S, h) <= EmpError(S, g) }
}

def ERMRule<X : Type>(H : Set(X -> Bool), A : (m : N) -> (X × Bool)^m -> (X -> Bool)) {
  let fix m in N where m >= 1
  let fix S : (X × Bool)^m
  ERM(H, S, A(m)(S))
}
```

**General loss (Definition 3.4).** With a domain $Z$ and a loss $\ell(h, z)$, the risk is an expectation and the empirical risk an average. The 0-1 loss gives back `Error`. Everything below uses the 0-1 forms, since the Fundamental Theorem is stated for them.

```text
def Risk<Z : Type, Hy : Type>(D : Measure(Z), l : Hy -> Z -> R, h : Hy) -> R {
  return E[z ~ D](l(h, z))
}

def EmpRisk<Z : Type, Hy : Type, m : N where m >= 1>(S : Z^m, l : Hy -> Z -> R, h : Hy) -> R {
  return sum[i : Fin(m)](l(h, S(i))) / m
}
```

## 2. PAC and agnostic PAC learnability

Both definitions are one Telescope pattern: introduce the sample complexity and the algorithm first, then a block that must hold for every $\varepsilon$, $\delta$ and distribution, then `exists`. Because `mH` and `A` come before `fix D`, they cannot depend on the distribution, which is exactly what "distribution-free" means in the book.

**Realizability (Definition 2.1).** Some hypothesis in $\mathcal{H}$ has zero true error.

```text
def Realizable<X : Type>(H : Set(X -> Bool), D : Measure(X), f : X -> Bool) {
  let h in H where ErrorF(D, f, h) = 0
  exists h
}
```

**PAC learnability (Definition 3.1).** $\mathcal{H}$ is PAC learnable if there are $m_{\mathcal{H}} : (0, 1)^2 \to \mathbb{N}$ and an algorithm such that, for every $\varepsilon, \delta \in (0, 1)$, every $\mathcal{D}$ over $\mathcal{X}$ and every $f$ realizable by $\mathcal{H}$, running the algorithm on $m \geq m_{\mathcal{H}}(\varepsilon, \delta)$ i.i.d. examples labelled by $f$ returns, with probability at least $1 - \delta$, an $h$ with $L_{(\mathcal{D},f)}(h) \leq \varepsilon$.

```text
def PACLearner<X : Type>(H : Set(X -> Bool), mH : R -> R -> N,
                         A : (m : N) -> (X × Bool)^m -> (X -> Bool)) {
  let fix e, d in R where 0 < e < 1, 0 < d < 1
  let fix D : Measure(X) where IsProbabilityMeasure(D)
  let fix f : X -> Bool where Realizable(H, D, f)
  let fix m in N where m >= mH(e, d), m >= 1
  let learn = A(m)
  Prob[x ~ D^m](ErrorF(D, f, learn(Label(x, f))) <= e) >= 1 - d
}

def PACLearnable<X : Type>(H : Set(X -> Bool)) {
  let mH : R -> R -> N
  let A : (m : N) -> (X × Bool)^m -> (X -> Bool)
  PACLearner(H, mH, A)
  exists mH, A
}
```

The last line of `PACLearner` is the book's "with probability at least $1 - \delta$ over $x \sim \mathcal{D}^m$", almost word for word. Splitting out `PACLearner` gives "$A$ learns $\mathcal{H}$ with sample complexity $m_{\mathcal{H}}$" its own name, which the Fundamental Theorem and the finite-class bounds reuse. The `m >= 1` is not in the book; it changes nothing, since any $m_{\mathcal{H}}$ can be raised to at least 1.

**Agnostic PAC learnability (Definition 3.3).** Drop realizability, let $\mathcal{D}$ be over $\mathcal{X} \times \{0, 1\}$, and compare with the best hypothesis in the class: $L_{\mathcal{D}}(h) \leq \min_{h' \in \mathcal{H}} L_{\mathcal{D}}(h') + \varepsilon$.

```text
def AgnosticPACLearner<X : Type>(H : Set(X -> Bool), mH : R -> R -> N,
                                 A : (m : N) -> (X × Bool)^m -> (X -> Bool)) {
  let fix e, d in R where 0 < e < 1, 0 < d < 1
  let fix D : Measure(X × Bool) where IsProbabilityMeasure(D)
  let fix m in N where m >= mH(e, d), m >= 1
  let learn = A(m)
  let best = inf[g in H](Error(D, g))
  Prob[S ~ D^m](Error(D, learn(S)) <= best + e) >= 1 - d
}

def AgnosticPACLearnable<X : Type>(H : Set(X -> Bool)) {
  let mH : R -> R -> N
  let A : (m : N) -> (X × Bool)^m -> (X -> Bool)
  AgnosticPACLearner(H, mH, A)
  exists mH, A
}
```

The book writes min, but the minimum need not be attained over an infinite class, so `inf` is the faithful reading. The algorithm may return a hypothesis outside $\mathcal{H}$, as the book allows.

**The same definition in Lean.** What the translator would emit for `PACLearnable`, to show the Python-to-C distance. The `MeasurableSpace` instance has no Telescope counterpart and must be added by the translator.

```text
def PACLearnable {X : Type*} [MeasurableSpace X] (H : Set (X → Bool)) : Prop :=
  ∃ (mH : ℝ → ℝ → ℕ) (A : (m : ℕ) → (Fin m → X × Bool) → X → Bool),
    ∀ e d : ℝ, 0 < e → e < 1 → 0 < d → d < 1 →
    ∀ (D : Measure X), IsProbabilityMeasure D →
    ∀ f : X → Bool, (∃ h ∈ H, (D {x | h x ≠ f x}).toReal = 0) →
    ∀ m : ℕ, mH e d ≤ m → 1 ≤ m →
      ((Measure.pi fun _ : Fin m => D)
        {x | (D {z | A m (fun i => (x i, f (x i))) z ≠ f z}).toReal ≤ e}).toReal ≥ 1 - d
```

## 3. Uniform convergence and finite classes

Uniform convergence says that, with high probability, the sample estimates every hypothesis's error at once. It implies agnostic PAC learnability by ERM, and every finite class has it.

**$\varepsilon$-representative samples (Definition 4.1) and uniform convergence (Definition 4.3).**

```text
def Representative<X : Type, m : N where m >= 1>(S : (X × Bool)^m, H : Set(X -> Bool),
                                                D : Measure(X × Bool), e : R) {
  let fix h in H
  |EmpError(S, h) - Error(D, h)| <= e
}

def UniformConvergenceWith<X : Type>(H : Set(X -> Bool), mUC : R -> R -> N) {
  let fix e, d in R where 0 < e < 1, 0 < d < 1
  let fix D : Measure(X × Bool) where IsProbabilityMeasure(D)
  let fix m in N where m >= mUC(e, d), m >= 1
  Prob[S ~ D^m](Representative(S, H, D, e)) >= 1 - d
}

def UniformConvergence<X : Type>(H : Set(X -> Bool)) {
  let mUC : R -> R -> N where UniformConvergenceWith(H, mUC)
  exists mUC
}
```

**Lemma 4.2.** If $S$ is $\varepsilon/2$-representative, every ERM output $h_S$ is within $\varepsilon$ of every hypothesis in the class. The book states it against $\min L_{\mathcal{D}}$; stating it against each $h$ avoids the inf.

```text
let fix X : Type
let fix H : Set(X -> Bool)
let fix D : Measure(X × Bool) where IsProbabilityMeasure(D)
let fix e in R where e > 0
let fix m in N where m >= 1
let fix S : (X × Bool)^m where Representative(S, H, D, e/2)
let fix hS : X -> Bool where ERM(H, S, hS)
let fix h in H
Error(D, hS) <= Error(D, h) + e
```

**Corollary 4.4.** If $\mathcal{H}$ has uniform convergence with $m^{UC}$, then any ERM rule agnostically PAC learns $\mathcal{H}$ with $m_{\mathcal{H}}(\varepsilon, \delta) = m^{UC}(\varepsilon/2, \delta)$.

```text
let fix X : Type
let fix H : Set(X -> Bool)
let fix mUC : R -> R -> N where UniformConvergenceWith(H, mUC)
let fix A : (m : N) -> (X × Bool)^m -> (X -> Bool) where ERMRule(H, A)
AgnosticPACLearner(H, lambda e, d: mUC(e/2, d), A)
```

**Finite classes, realizable case (Corollary 2.3).** If $\mathcal{H}$ is finite and $m \geq \log(\lvert\mathcal{H}\rvert/\delta)/\varepsilon$, then for every realizable $\mathcal{D}$ and $f$, with probability at least $1 - \delta$ every ERM hypothesis has error at most $\varepsilon$.

```text
let fix X : Type
let fix H : Set(X -> Bool) where Finite(H), card(H) >= 1
let fix e, d in R where 0 < e < 1, 0 < d < 1
let fix m in N where m >= log(card(H) / d) / e, m >= 1
let fix D : Measure(X) where IsProbabilityMeasure(D)
let fix f : X -> Bool where Realizable(H, D, f)
Prob[x ~ D^m]({ let fix h : X -> Bool where ERM(H, Label(x, f), h); ErrorF(D, f, h) <= e }) >= 1 - d
```

The line order is the book's: $\mathcal{H}$, then $\varepsilon$ and $\delta$, then $m$, then "for any $\mathcal{D}$ and $f$". `Finite(H)` is what lets `card(H)` be written at all. Writing it this way also surfaced a hidden assumption: `log(card(H) / d)` must be defined on the $m$ line, before realizability (which implies $\mathcal{H}$ is non-empty) appears, so `card(H) >= 1` has to be stated with $\mathcal{H}$.

As a learnability statement: finite classes are PAC learnable with $m_{\mathcal{H}}(\varepsilon, \delta) \leq \lceil \log(\lvert\mathcal{H}\rvert/\delta)/\varepsilon \rceil$. `ceil` gives an integer, and here it is used as an N, so its argument must be non-negative; it is, because $\lvert\mathcal{H}\rvert \geq 1$ and $\delta < 1$.

```text
let fix X : Type
let fix H : Set(X -> Bool) where Finite(H), card(H) >= 1
let A : (m : N) -> (X × Bool)^m -> (X -> Bool)
    where PACLearner(H, lambda e, d: ceil(log(card(H) / d) / e), A)
exists A
```

**Finite classes, agnostic case (Corollary 4.6).** Finite classes have uniform convergence with $m^{UC}(\varepsilon, \delta) \leq \lceil \log(2\lvert\mathcal{H}\rvert/\delta)/(2\varepsilon^2) \rceil$, so by Corollary 4.4 any ERM rule agnostically PAC learns them with $m_{\mathcal{H}}(\varepsilon, \delta) \leq \lceil 2 \log(2\lvert\mathcal{H}\rvert/\delta)/\varepsilon^2 \rceil$.

```text
let fix X : Type
let fix H : Set(X -> Bool) where Finite(H), card(H) >= 1
UniformConvergenceWith(H, lambda e, d: ceil(log(2 * card(H) / d) / (2 * e^2)))
```

```text
let fix X : Type
let fix H : Set(X -> Bool) where Finite(H), card(H) >= 1
let fix A : (m : N) -> (X × Bool)^m -> (X -> Bool) where ERMRule(H, A)
AgnosticPACLearner(H, lambda e, d: ceil(2 * log(2 * card(H) / d) / e^2), A)
```

## 4. No Free Lunch

**Theorem 5.1.** For any learning algorithm $A$ over a domain $\mathcal{X}$ and any sample size $m < \lvert\mathcal{X}\rvert/2$, there is a distribution $\mathcal{D}$ over $\mathcal{X} \times \{0, 1\}$ such that some $f$ has $L_{\mathcal{D}}(f) = 0$, yet with probability at least $1/7$ over $S \sim \mathcal{D}^m$, $L_{\mathcal{D}}(A(S)) \geq 1/8$.

```text
let fix X : Type
let fix A : (m : N) -> (X × Bool)^m -> (X -> Bool)
let fix m in N where { let C : Finset(X) where card(C) > 2 * m; exists C }
let learn = A(m)
let D : Measure(X × Bool) where IsProbabilityMeasure(D),
    { let f : X -> Bool where Error(D, f) = 0; exists f },
    Prob[S ~ D^m](Error(D, learn(S)) >= 1/8) >= 1/7
exists D
```

The order carries the theorem: $A$ and $m$ are fixed first, so the bad distribution may depend on both, and it is introduced after them, which is the "for every learner there is a task it fails" reading. The hypothesis $m < \lvert\mathcal{X}\rvert/2$ is written as "$\mathcal{X}$ has a finite subset with more than $2m$ points". `card(X)` would need `Finite(X)`, which would wrongly drop infinite domains from the theorem.

**Corollary 5.2.** Over an infinite domain, the class of all functions is not PAC learnable.

```text
let fix X : Type where Infinite(X)
not PACLearnable(Set[h : X -> Bool](h))
```

`Set[h : X -> Bool](h)` is the set of every $h$, the book's $\{0, 1\}^{\mathcal{X}}$.

## 5. VC dimension

**Restriction and shattering (Definitions 6.2 and 6.3).** The restriction of $\mathcal{H}$ to a finite $C \subseteq \mathcal{X}$ is the set of labellings of $C$ that $\mathcal{H}$ produces. $\mathcal{H}$ shatters $C$ when that is every labelling, so $\lvert\mathcal{H}_C\rvert = 2^{\lvert C\rvert}$. `Shatters` is the book's sentence and `ShattersByCount` is its "that is". In `Restriction`, each $c : C$ is used as a point of $\mathcal{X}$ by the spec's set-as-type cast.

```text
def Restriction<X : Type>(H : Set(X -> Bool), C : Finset(X)) -> Set(C -> Bool) {
  return Set[h in H](lambda c: h(c))
}

def Shatters<X : Type>(H : Set(X -> Bool), C : Finset(X)) {
  let fix g : C -> Bool
  let h in H where { let fix c in C; h(c) = g(c) }
  exists h
}

def ShattersByCount<X : Type>(H : Set(X -> Bool), C : Finset(X)) {
  card(Restriction(H, C)) = 2^card(C)
}
```

**VC dimension (Definition 6.5).** $\mathrm{VCdim}(\mathcal{H})$ is the largest size of a shattered set, and $\infty$ if there are arbitrarily large ones. That is a supremum in mathlib's `ENat`, $\mathbb{N}$ with $\infty$ added, so the definition is the book's in one line, as in the spec's own example.

```text
# ENat is mathlib's N with ∞ added; a natural number d is compared as an ENat
def VCdim<X : Type>(H : Set(X -> Bool)) -> ENat {
  return sup[C : Finset(X) where Shatters(H, C)](card(C))
}

def FiniteVCdim<X : Type>(H : Set(X -> Bool)) {
  let d in N where VCdim(H) <= d
  exists d
}
```

**Examples (section 6.3).** Thresholds $h_a(x) = \mathbb{1}[x < a]$ have VC dimension 1: any one point is shattered, but no threshold labels the smaller of two points 0 and the larger 1. Intervals $h_{(a,b)}(x) = \mathbb{1}[a < x < b]$ have VC dimension 2: no interval labels three points 1, 0, 1. A proposition becomes a `Bool` where one is expected, so each hypothesis is just its condition.

```text
let Thresholds = Set[a in R](lambda x: x < a)
VCdim(Thresholds) = 1
```

```text
let Intervals = Set[a, b in R where a < b](lambda x: a < x < b)
VCdim(Intervals) = 2
```

A finite class is the simplest case: shattering $C$ takes $2^{\lvert C\rvert}$ hypotheses, so $\mathrm{VCdim}(\mathcal{H}) \leq \log_2 \lvert\mathcal{H}\rvert$.

```text
let fix X : Type
let fix H : Set(X -> Bool) where Finite(H)
let fix d in N where VCdim(H) >= d
2^d <= card(H)
```

## 6. The Fundamental Theorem of Statistical Learning

**Theorem 6.7.** For a class $\mathcal{H}$ of functions $\mathcal{X} \to \{0, 1\}$ under the 0-1 loss, the following are equivalent: (1) uniform convergence; (2) any ERM rule is a successful agnostic PAC learner; (3) agnostic PAC learnability; (4) PAC learnability; (5) any ERM rule is a successful PAC learner; (6) finite VC dimension.

Items 2 and 5 need two more names, "any ERM rule learns $\mathcal{H}$":

```text
def ERMLearnsAgnostic<X : Type>(H : Set(X -> Bool)) {
  let fix A : (m : N) -> (X × Bool)^m -> (X -> Bool) where ERMRule(H, A)
  let mH : R -> R -> N where AgnosticPACLearner(H, mH, A)
  exists mH
}

def ERMLearnsPAC<X : Type>(H : Set(X -> Bool)) {
  let fix A : (m : N) -> (X × Bool)^m -> (X -> Bool) where ERMRule(H, A)
  let mH : R -> R -> N where PACLearner(H, mH, A)
  exists mH
}
```

With chained `<=>`, the six-way equivalence is one statement, in the book's order:

```text
let fix X : Type
let fix H : Set(X -> Bool)
UniformConvergence(H) <=> ERMLearnsAgnostic(H) <=> AgnosticPACLearnable(H)
  <=> PACLearnable(H) <=> ERMLearnsPAC(H) <=> FiniteVCdim(H)
```

The book's proof goes $1 \Rightarrow 2$ (Corollary 4.4), $2 \Rightarrow 3$ and $3 \Rightarrow 4$ and $2 \Rightarrow 5$ (immediate), $4 \Rightarrow 6$ and $5 \Rightarrow 6$ (No Free Lunch), and $6 \Rightarrow 1$ (Sauer's lemma, below).

**Sauer's lemma (Lemma 6.10).** If $\mathrm{VCdim}(\mathcal{H}) \leq d$, then $\mathcal{H}$ produces at most $\sum_{i=0}^{d} \binom{m}{i}$ labellings of any $m$ points. The book states it through the growth function $\tau_{\mathcal{H}}(m) = \max_{\lvert C\rvert = m} \lvert\mathcal{H}_C\rvert$; stating it for every $C$ says the same and needs no max.

```text
let fix X : Type
let fix H : Set(X -> Bool)
let fix d in N where VCdim(H) <= d
let fix C : Finset(X)
card(Restriction(H, C)) <= sum[i in 0...d](choose(card(C), i))
```

**Theorem 6.8, the quantitative form (agnostic part).** If $\mathrm{VCdim}(\mathcal{H}) = d < \infty$, there are absolute constants $C_1, C_2$ with $C_1 (d + \log(1/\delta))/\varepsilon^2 \leq m_{\mathcal{H}}(\varepsilon, \delta) \leq C_2 (d + \log(1/\delta))/\varepsilon^2$. "Absolute" is exactly line order: the constants come before $\mathcal{X}$ and $\mathcal{H}$, so they cannot depend on them. The upper bound is about some learner and the lower bound about every learner, so each half gets its own block.

```text
let C1, C2 in R where C1 > 0, C2 > 0, {
  let fix X : Type
  let fix H : Set(X -> Bool)
  let fix d in N where VCdim(H) = d, d >= 1
  {                                             # upper bound: some learner
    let mH : R -> R -> N
    let A : (m : N) -> (X × Bool)^m -> (X -> Bool)
    AgnosticPACLearner(H, mH, A)
    { let fix e, delta in R where 0 < e < 1, 0 < delta < 1
      mH(e, delta) <= C2 * (d + log(1/delta)) / e^2 }
    exists mH, A
  }
  {                                             # lower bound: every learner
    let fix mH : R -> R -> N
    let fix A : (m : N) -> (X × Bool)^m -> (X -> Bool) where AgnosticPACLearner(H, mH, A)
    let fix e, delta in R where 0 < e < 1, 0 < delta < 1
    mH(e, delta) >= C1 * (d + log(1/delta)) / e^2
  }
}
exists C1, C2
```

The two blocks follow the spec's rule from section 3.3: a `fix` after an `exists` keeps the conditions above it, so the lower bound needs a new block. The `d >= 1` is not in the book; with $d = 0$ the class has at most one hypothesis, a single sample suffices, and the lower bound cannot hold. The realizable part has the same shape with bounds $C_1 (d + \log(1/\delta))/\varepsilon$ and $C_2 (d \log(1/\varepsilon) + \log(1/\delta))/\varepsilon$, and uniform convergence repeats the agnostic bounds.
