**Prerequisites:** [[Telescope System Document]]

## Step 1. Simple Estimation of Loss

```
let fix X : Type
let fix D : Measure(X × Bool) where IsProbabilityMeasure(D)
let fix h : X -> Bool # fixed before the sample is drawn
let fix e in R where e > 0
let fix m in N where m >= 1
# Hoeffding
Prob[S ~ D^m](|EmpError(S, h) - Error(D, h)| > e) <= 2 * exp(-2 * e^2 * m)
```

## Step 2. Build h using S

```
let fix X : Type
let fix P : Measure(X) where IsProbabilityMeasure(P), NoAtoms(P)
def D := Measure.map(lambda x: (x, true), P)      # every label is 1
let fix m in N where m >= 1
Prob[S ~ D^m]({
  # 1 only on sample points
  def hS := lambda x: { let i : Fin(m) where S(i).1 = x; exists i }
  # perfect on S, wrong almost everywhere
  EmpError(S, hS) = 0 and Error(D, hS) = 1
}) = 1
```

## Step 3. Uniform Convergence

```
# fragment: X, D, H, e, delta, m as in Step 4

# before: for each h, most samples are good
let fix h : X -> Bool
Prob[S ~ D^m](|EmpError(S, h) - Error(D, h)| <= e) >= 1 - delta

# after: most samples are good for every h at once (uniform convergence)
Prob[S ~ D^m]({ let fix h in H; |EmpError(S, h) - Error(D, h)| <= e }) >= 1 - delta
```

## Step 4. Finite H

```
let fix X : Type
# D fixed first
let fix D : Measure(X × Bool) where IsProbabilityMeasure(D)
# card(H) = 1 is Step 1
let fix H : Set(X -> Bool) where Finite(H), card(H) >= 1
let fix e, delta in R where 0 < e < 1, 0 < delta < 1
let m in N where m >= 1, Prob[S ~ D^m](Representative(S, H, D, e)) >= 1 - delta
# m may depend on D
exists m
# union bound: m ≈ log(2 card(H) / delta) / (2 e^2)
```

## Step 5. For any D

```
let fix X : Type
let fix H : Set(X -> Bool) where Finite(H), card(H) >= 1
let fix e, delta in R where 0 < e < 1, 0 < delta < 1
let m in N where m >= 1, {
  # moved below m
  let fix D : Measure(X × Bool) where IsProbabilityMeasure(D)
  Prob[S ~ D^m](Representative(S, H, D, e)) >= 1 - delta
}
# one m works for every D
exists m
```

## Step 6. Infinite H

```
# replaces BOTH the X and H lines in Step 5; X is now R; still true
def H := Thresholds
# only m + 1 behaviours on m points
{ let fix m in N; Growth(H, m) = m + 1 }
```

## Step 7. Finite VC Dimension

```
# replaces the H line in Step 5; still true
let fix d in N
let fix H : Set(X -> Bool) where VCdim(H) = d
# Sauer: about m^d behaviours
{ let fix m in N; Growth(H, m) <= sum[i in 0...d](choose(m, i)) }
```

## Step 8. All Functions

```
let fix X : Type where Infinite(X)
def H := Set[h : X -> Bool](h)
# exponential behaviours
{ let fix m in N; Growth(H, m) = 2^m }

# Step 5 fails: some e, delta admit no m
let e, delta in R where 0 < e < 1, 0 < delta < 1, {
  let m in N where m >= 1, {
    let fix D : Measure(X × Bool) where IsProbabilityMeasure(D)
    Prob[S ~ D^m](Representative(S, H, D, e)) >= 1 - delta
  }
  not exists m
}
exists e, delta
```

## Step 9. Realizable Case

```
# fragment: X, H, e, delta, m as in Step 5
# extra condition on D
let fix D : Measure(X × Bool) where IsProbabilityMeasure(D), Realizable(H, D)
# m now grows like 1/e instead of 1/e^2
Prob[S ~ D^m]({ let fix h in VersionSpace(H, S); Error(D, h) <= e }) >= 1 - delta
```

## The Theorem

```
let fix X : Type
let fix H : Set(X -> Bool)
UniformConvergence(H) <=> ERMLearnsAgnostic(H) <=> AgnosticPACLearnable(H)
  <=> PACLearnable(H) <=> ERMLearnsPAC(H) <=> FiniteVCdim(H)
```