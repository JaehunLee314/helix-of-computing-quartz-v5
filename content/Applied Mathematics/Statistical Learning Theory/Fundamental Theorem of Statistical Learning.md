**Prerequisites:** [[Telescope System Document]]

Every step answers one question: given accuracy e and sample size m, how likely is a bad sample?
The answer is the right-hand side of the `Prob` line. Watch which variables it mentions as the conditions loosen.

## Step 1. One h

```
let fix X : Type
let fix D : Measure(X × Bool) where IsProbabilityMeasure(D)
let fix h : X -> Bool # fixed before the sample is drawn
let fix e in R where e > 0
let fix m in N where m >= 1
# Hoeffding
Prob[S ~ D^m](|EmpError(S, h) - Error(D, h)| > e) <= 2 * exp(-2 * e^2 * m)
```

The bound mentions only e and m, not D or h.

## Step 2. Bad h chosen after seeing S

```
let fix X : Type
let fix P : Measure(X) where IsProbabilityMeasure(P), NoAtoms(P)
def D := Measure.map(lambda x: (x, true), P) # every label is 1
let fix m in N where m >= 1
Prob[S ~ D^m]({
  # 1 only on sample points; labels are ignored, which is fine because every label is 1
  def hS : X -> Bool := lambda x: { let i : Fin(m) where S(i).1 = x; exists i }
  # perfect on S, wrong almost everywhere
  EmpError(S, hS) = 0 and Error(D, hS) = 1
}) = 1
```

For hS the bad-sample probability is 1, for every m. Step 1's bound only covers an h fixed before S is drawn, so we need a bound that covers every h in H at once.

From now on we use the following definition.

```
def Representative<X : Type, m : N where m >= 1>(
  S : (X × Bool)^m,
  H : Set(X -> Bool),
  D : Measure(X × Bool),
  e : R
) {
  let fix h in H
  |EmpError(S, h) - Error(D, h)| <= e
}
```

## Step 3. Finite H

```
let fix X : Type
let fix D : Measure(X × Bool) where IsProbabilityMeasure(D)
let fix H : Set(X -> Bool) where Finite(H), card(H) >= 1
let fix e in R where e > 0
let fix m in N where m >= 1
# Step 1 for each h, added up
Prob[S ~ D^m](not Representative(S, H, D, e)) <= 2 * card(H) * exp(-2 * e^2 * m)
```

Loosening h to H multiplies the bound by card(H). The bound still doesn't mention D, so one formula serves every distribution. This is what later lets a single sample size work without knowing D.

## Step 4. Infinite H: count behaviours

A finite set of points C only sees what H does on C. Restricting H to C gives at most 2^card(C) functions, however large H is. Growth counts them for the worst C of size m.

```
# H seen only on C
def Restriction<X : Type>(H : Set(X -> Bool), C : Finset(X)) -> Set(C -> Bool) {
  return Set[h in H](lambda c: h(c))
}

# the most behaviours H shows on any m points
def Growth<X : Type>(H : Set(X -> Bool), m : N) -> N {
  return sup[C : Finset(X) where card(C) = m](card(Restriction(H, C)))
}
```

Growth(H, m) <= 2^m always holds, and for finite H, Growth(H, m) <= card(H).

```
let fix X : Type
let fix D : Measure(X × Bool) where IsProbabilityMeasure(D)
let fix H : Set(X -> Bool)
let fix e in R where e > 0
let fix m in N where m >= 1
# ghost sample: on 2m points, H acts like only Growth(H, 2m) functions
Prob[S ~ D^m](not Representative(S, H, D, e)) <= 4 * Growth(H, 2 * m) * exp(-e^2 * m / 8)
```

card(H) becomes Growth(H, 2m). The count can now grow with m, so the bound goes to 0 only if the decay outruns it.

## Step 4. Infinite H: count behaviours

```
let fix X : Type
let fix D : Measure(X × Bool) where IsProbabilityMeasure(D)
let fix H : Set(X -> Bool)
let fix e in R where e > 0
let fix m in N where m >= 1
# ghost sample: on 2m points, H acts like only Growth(H, 2m) functions
Prob[S ~ D^m](not Representative(S, H, D, e)) <= 4 * Growth(H, 2 * m) * exp(-e^2 * m / 8)
```

card(H) becomes Growth(H, 2m). The count can now grow with m, so the bound goes to 0 only if the decay outruns it.

## Step 5. Finite VC dimension

```
let fix X : Type
let fix D : Measure(X × Bool) where IsProbabilityMeasure(D)
let fix d in N
let fix H : Set(X -> Bool) where VCdim(H) = d
let fix e in R where e > 0
let fix m in N where m >= 1
# Sauer: Growth(H, 2m) <= (2m + 1)^d
Prob[S ~ D^m](not Representative(S, H, D, e)) <= 4 * (2 * m + 1)^d * exp(-e^2 * m / 8)
```

A polynomial count against exponential decay, so the bound goes to 0. d sets how long that takes.

## Step 6. All functions

```
let fix X : Type where Infinite(X)
def H := Set[h : X -> Bool](h)
# Growth(H, 2m) = 4^m, so Step 4 gives 4 * 4^m * exp(-e^2 * m / 8)
#   = 4 * exp(m * (log(4) - e^2 / 8)), which grows with m: no information

# No Free Lunch: no better bound exists
let fix m in N where m >= 1
let fix A : (X × Bool)^m -> (X -> Bool)
let D : Measure(X × Bool) where IsProbabilityMeasure(D),
    Prob[S ~ D^m](Error(D, A(S)) >= 1/8) >= 1/7
exists D
```

At e = 1/8, the failure probability stays at least 1/7, for every m and every algorithm. Here D is a witness chosen after m and A, so it may depend on both.

## Step 7. Realizable D

```
let fix X : Type
let fix H : Set(X -> Bool) where Finite(H), card(H) >= 1
# D moved below H: Realizable(H, D) mentions H, so H must come first
# both lines are fixed, so the move changes nothing else
let fix D : Measure(X × Bool) where IsProbabilityMeasure(D), Realizable(H, D)
let fix e in R where 0 < e < 1
let fix m in N where m >= 1
# one bad h survives m draws with probability (1 - e)^m <= exp(-e m)
Prob[S ~ D^m]({ let h in VersionSpace(H, S) where Error(D, h) > e; exists h }) <= card(H) * exp(-e * m)
```

Tightening D to realizable ones changes the exponent from e^2 to e.

## The Theorem

```
let fix X : Type
let fix H : Set(X -> Bool)
UniformConvergence(H) <=> ERMLearnsAgnostic(H) <=> AgnosticPACLearnable(H)
  <=> PACLearnable(H) <=> ERMLearnsPAC(H) <=> FiniteVCdim(H)
```

| Step | condition | bound | → 0 as m grows? |
|---|---|---|---|
| 1 | one h | 2 exp(-2e²m) | yes |
| 3 | finite H | 2 card(H) exp(-2e²m) | yes |
| 4 | any H | 4 Growth(H, 2m) exp(-e²m/8) | depends on Growth |
| 5 | VCdim d | 4 (2m + 1)^d exp(-e²m/8) | yes |
| 6 | all functions | at least 1/7 at e = 1/8 | no |
| 7 | realizable D, finite H | card(H) exp(-em) | yes, faster |