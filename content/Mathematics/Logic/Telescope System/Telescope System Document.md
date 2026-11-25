*Telescope 0.2.0*

Telescope is a small language for stating mathematics so that people can read it and Lean can check it. It has two purposes: **stating existing mathematics clearly**, as a readable alternative to quantifier-heavy notation, and **readable formalization**, where Telescope is to Lean what Python is to C, the same meaning in a form that is easier to write and read, compiled down for checking.

The document starts with what you need to read and write statements and adds detail as it goes. Sections 1 to 6 are the language, section 7 is examples, section 8 connects the language to its theory and to Lean, and section 9 lists what a full implementation must decide. Elementary logic and some programming are enough for sections 1 to 7; type theory helps for 8 and 9.

## 1. A first statement

```text
let x in N        # introduce: x stands for every natural number
x < 10            # refine: only 0, 1, …, 9 are kept
fix x             # from here on, x is any one of them
x^2 < 100         # assert: holds for each
```

Read it top to bottom. `let` introduces x as a stand-in for every natural number. The next line is a condition, so only the values below 10 are kept. `fix x` makes x "any one of them", and the last line must hold for each. In logic, the block says $\forall x \in \mathbb{N}.\ x < 10 \to x^2 < 100$.

Picture $x$ with an arrow to every value it may take: $x \to 0$, $x \to 1$, and so on. The lines above generate those arrows, the way a Python generator expression `(x for x in N if x < 10)` generates values, and an assertion is checked along all of them. The other way to assert is to ask whether anything is generated at all:

```text
let x in N
x^2 = 49
exists x          # some natural number has square 49
```

That is the whole language in miniature: **introduce** with `let`, **refine** with conditions, and **assert** with `fix` (for every) or `exists` (there is).

## 2. Order is meaning

A block is read like a program, so the order of the `let` lines is the order of the quantifiers. The limit of a function at a point, in Telescope, in logic and in Lean:

```text
def Limit(f : R -> R, a : R, L : R) {
  let fix e in R where e > 0
  let d in R where d > 0
  { let fix x in R where 0 < |x - a| < d; |f(x) - L| < e }
  exists d
}
```
$$
\forall e > 0.\ \exists d > 0.\ \forall x.\ (0 < |x - a| < d \to |f(x) - L| < e)
$$
```text
def Limit (f : ℝ → ℝ) (a L : ℝ) : Prop :=
  ∀ e > 0, ∃ d > 0, ∀ x, 0 < |x - a| ∧ |x - a| < d → |f x - L| < e
```

e is fixed first, so d may depend on e. The braces make one block. It mentions d, so it is a condition on d, and x lives only inside it, so one d must work for every x. Moving lines changes the statement, as moving words in the textbook would:

```text
def Continuous(f : R -> R) {
  let fix x in R
  let fix e in R where e > 0
  let d in R where d > 0
  { let fix y in R where |x - y| < d; |f(x) - f(y)| < e }
  exists d
}

def UniformlyContinuous(f : R -> R) {
  let fix e in R where e > 0
  let d in R where d > 0
  { let fix x, y in R where |x - y| < d; |f(x) - f(y)| < e }
  exists d
}
```

In Continuous, x is fixed before d appears, so d may depend on x. In UniformlyContinuous, x is inside the block, so one d serves every x.

**To write a statement:** introduce the objects in the textbook's order, attach hypotheses with `where` or write them on the next lines, decide for each variable between "for every" (`fix`) and "there is" (`exists`), and write the conclusion.

| Textbook | Telescope | Logic |
| --- | --- | --- |
| For every real $x \neq 0$, $x^2 > 0$ | `let fix x in R where x != 0; x^2 > 0` | $\forall x.\ x \neq 0 \to x^2 > 0$ |
| For every n there is a larger prime | `let fix n in N; let p in N where p > n, Prime(p); exists p` | $\forall n.\ \exists p.\ p > n \land \mathrm{Prime}(p)$ |
| $x^2 = 4$ has exactly one natural solution | `let x in N where x^2 = 4; unique x` | $\exists! x.\ x^2 = 4$ |

## 3. The pieces of a block

### 3.1 Introducing

`let x : T` introduces x with type T, and `let x in S` is the readable form, for a type or a set: with `S : Set(A)` it means `let x : A`, then `x in S`. Several variables may share a line, and a later type may mention an earlier variable: `let n in N, v : R^n`. `where` attaches conditions to the line it ends, so `let fix e in R where e > 0` reads "for every $e > 0$" and `exists d where …` reads "there is a d such that …". `def D := t` names a term; it introduces no variable. `=` stays a proposition that ties values together, and `:=` means "is defined as", as in Lean.

Every variable needs exactly one type by the time it is fixed or counted, and every term must be defined where it is used: `1/x` needs `x != 0` above it.

### 3.2 Refining

A proposition about a variable that is not yet fixed is a **condition**: it narrows the values generated, the variable's **range**. A condition on several variables ties their values together:

```text
let x, y in N
y = x + 2         # generates the pairs (0, 2), (1, 3), …
x < 10            # only the pairs with x < 10
fix x, y
y < 12            # holds for every pair kept
```

### 3.3 Asserting

`fix x` says that from here on x is any value generated. After it, a statement about x is no longer a condition but an **assertion** that must hold for each value. A statement with no unfixed variable, such as `1 + 1 = 2`, is an assertion too. `exists x`, `not exists x` and `unique x` ask about the range and leave x unfixed, so a block can build up the way a textbook does:

```text
let x : A
P(x)
exists x          # there is an x with P(x)
Q(x)
exists x          # furthermore, one with P(x) and Q(x)
fix x
R(x)              # every x with P(x) and Q(x) has R(x)
```

**How each line is read.** `let` and `fix` build the context. A line that mentions an unfixed variable is a condition. A line starting with `exists`, `not exists` or `unique`, and a line whose variables are all fixed, is an assertion. A block's assertions all hold together, each under the conditions written above it. Within one `exists`, variables fixed before the witness was introduced are given, and those introduced after it are quantified inside, so the witness must serve all of them; this is the e, d and x of Limit. A `fix x` after `exists x` keeps every condition written above it; to quantify afresh, open a new block.

### 3.4 Formulas and nested blocks

Propositions combine with `not`, `and`, `or`, `=>` and `<=>`, tightest first, and `=>` groups to the right. A chain such as `0 < e < 1` expands pair by pair, as in Python. `A <=> B <=> C` chains the same way, so all three are equivalent. Braces make a block, and a block is itself a proposition, so it can be a condition, a hypothesis after `where`, or an operand. Fermat's theorem on sums of two squares uses one as half of an iff:

```text
let fix p in N where Prime(p), p != 2
{ let a, b in N where p = a^2 + b^2; exists a, b } <=> p mod 4 = 1
```

Variables introduced inside a block disappear when it closes. Outer variables can be used inside it but not fixed or narrowed there.

## 4. Definitions

`def` names a block for reuse. A definition without `return` is a proposition:

```text
def Prime(p : N) {
  p > 1
  { let fix d in N where divides(d, p); d = 1 or d = p }
}
```

`Prime(q)` holds when q meets the body's conditions and every assertion in the body holds, so `Prime(1)` is false. A definition with `return` gives a value, and a proposition with it:

```text
def sqrt(x : R) -> R {
  fix x
  x >= 0
  let y in R where y >= 0, y^2 = x
  return y
}
```

`sqrt(t)` is the non-negative square root of t. Because x is fixed, `x >= 0` is something the body asserts, so every call carries the precondition $t \geq 0$, proved from the caller's context. Without `fix x` it would be a condition, and sqrt would be partial: defined on non-negative t, undefined elsewhere. `return y` of a variable requires `unique y` to be provable, as it is here.

**Parameters are variables.** `x : R` in a parameter list means what it means on `let`: the parameter receives the argument with all its values, and whatever the body does stays in the body; the caller's variable never changes. A condition on a parameter or a generic is a precondition that each call proves from its own context, the same as `fix` followed by the condition. `where` works on parameters: `def Close(e : R where e > 0, x : R, y : R) { |x - y| < e }`.

**Generics.** Angle brackets declare parameters that the others depend on. They are usually inferred: `Surjective(f)` reads A and B off the type of f, and `Surjective<A, B>(f)` writes them out.

```text
def Surjective<A : Type, B : Type>(f : A -> B) {
  let fix b : B
  let a : A where f(a) = b
  exists a
}
```

**Named terms.** `def D := t` is a definition with no parameters and no body to run: it names the term t. It introduces no variable, and like every `def` it captures its context, so t may mention variables fixed above it. Section 3.1 introduces it; `def W := Fin(6) × Fin(6)` in section 7 is one use. `def D : T := t` gives the named term a type. t is read with T expected, so the casts apply: `def h : X -> Bool := lambda x: x in S`. `:=` is kept for definitions, and `=` for propositions.

**Terms and files.** `lambda n: s(phi(n))` is a function term, and `if c then a else b` is a term. A lambda may carry conditions, which make it partial: `lambda h where h != 0: (f(x + h) - f(x))/h` is the difference quotient, defined for every h except 0. `lambda e, d: t` is short for `lambda e: lambda d: t`. Passing a partial function is allowed when every place that applies it stays inside its domain, which is an obligation. A file's top-level lines are its theorem; several theorems in one file are each wrapped in braces.

## 5. Sums, sets and other aggregates

Some functions use all of a variable's values at once. Square brackets open a fresh context for them, and the function runs over it:

```text
sum[i in 1...n](i^2)                  # 1² + 2² + … + n²
Set[x in R where x^2 < 2](x)          # the set of x with x² < 2
Set[a in A](f(a))                     # the image of A under f
card(Set[s : Perm(Fin(n)) where Derangement(s)](s))
```

`B[x in S where C](t)` means `{ let x in S; C; return B(t) }`: introduce, refine, then apply B to everything t takes. The variable is **bound**: it is invisible outside, and it takes no part in the quantifier order, like the loop variable of a comprehension `[t for x in S if C]`. So with n fixed, `sum[i in 1...n](i) = n(n + 1)/2` is an assertion about n alone. Without brackets an aggregate runs over its argument's own values: `range(x)`, `sum(1...100)`.

| Aggregate | Gives |
| --- | --- |
| `range`, `Set` | The set of values taken |
| `exists`, `unique` | Whether some, or exactly one, value is taken |
| `card` | The number of values taken; `card(S)` needs `Finite(S)` |
| `sum`, `prod` | Sum or product, once per point of the context, which must be finite |
| `inf`, `sup` | Infimum and supremum |

"Once per point" matters when values repeat: `sum[x in -1...1](x^2)` is 2, because three points give 1, 0 and 1. `a...b` is the integers from a to b, so `sum(1...100)` is 5050.

## 6. Types and numbers

- **Basic types.** `Prop` is the type of propositions and `Type` the type of types. A set is a function to `Prop`, so `Set(A)` is `A -> Prop` and `x in S` means S(x); `Finset(A)` is the finite subsets. `Bool` has `true` and `false`, and a proposition becomes a Bool wherever a Bool is expected. The cast passes through function results: an `A -> Prop` (a `Set(A)`) becomes an `A -> Bool` wherever an `A -> Bool` is expected, so `Set[a in R](lambda x: x < a)` is a `Set(R -> Bool)`.
- **Building types.** `A -> B` groups to the right, and a dependent function type names its argument: `(m : N) -> R^m`. `A × B` has components `z.1` and `z.2`. Pairs are written `(a, b)`. A set may stand for a type, as in `f : D -> D`.
- **Tuples.** `A^n` is `Fin(n) -> A`, where `Fin(n)` is $0$ to $n - 1$. So an entry is an application, `v(i)`; two tuples are equal when every entry is; `lambda i: t` builds one; and a matrix is a tuple of rows, `M : (R^n)^m` with entries `M(i)(j)`. `R^n` carries the Euclidean norm.
- **Numbers.** $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$, written N, Z, Q, R, C, and these names are reserved. A number is cast upward automatically where a larger type is expected, and a `Finset` where a `Set` is. A value of a set used as a type is an element of the larger type: for `C : Finset(X)` and `c : C`, c is an X wherever an X is expected. Types are never guessed: a numeral whose type nothing determines is an error. Casting is as in Lean: arithmetic happens in the largest number type among its parts, and where nothing says which, you write the type: `(card(S) : Q) / card(W)`.
- **Arithmetic.** `+ - * / ^`, `mod`, `|x|` for absolute value and `divides(a, b)`. `^` binds tightest, then `*`, `/` and `mod`, then `+` and `-`, each grouping left. `/` is not defined on N or Z, and `a - b` on N needs `b <= a`; write them in Q or R instead. `ceil` and `floor` take R and give Z; where an N is expected, their argument must be shown non-negative.
- **Library names.** A name not defined in the file refers to Lean's mathlib and is written to look like mathlib's name. This is a matter of style: translation may involve an LLM, so a recognizable name is enough. Common ones: `Fin(n)`, `Perm(A)`, `card(S)`, `Finite(A)`, `exp`, `log`, `sin`, `pi`, `Continuous`, `Measure(X)`.
- **Propositional atoms.** `let A, B : Prop` introduces atoms like any variable, and `exists consistency` asks whether some truth assignment of the unfixed atoms meets every proposition so far.

## 7. Examples

Each example is its own file, with the definitions above in scope.

**From draft to statement.** A snippet marked `# pseudo telescope` is a draft: never compiled, it settles the quantifier order before the details. Making each line precise turns it into a definition and a theorem.

```text
# pseudo telescope
let fix f where f is continuous on [a, b]
let M where |f(x)| <= M for all x in [a, b]
exists M
```

```text
def Bounded(f : R -> R, a : R, b : R) {
  let M in R
  { let fix x in R where a <= x <= b; |f(x)| <= M }
  exists M
}

let fix a, b in R where a <= b
let fix f : R -> R where Continuous(f)
Bounded(f, a, b)
```

**Cantor.** No map from A onto its power set, and R is uncountable, read as "every sequence of reals misses a real":

```text
let fix A : Type
let f : A -> Set(A) where Surjective(f)
not exists f
```

```text
let fix s : N -> R
let x in R where { let fix n in N; s(n) != x }
exists x
```

**Bolzano–Weierstrass.** A function-valued witness: `exists phi, L` asks for a subsequence and its limit together.

```text
def SeqLimit(s : N -> R, L : R) {
  let fix e in R where e > 0
  let K in N
  { let fix n in N where n >= K; |s(n) - L| < e }
  exists K
}

def StrictMono(phi : N -> N) {
  let fix m, n in N where m < n
  phi(m) < phi(n)
}

let fix s : N -> R where { let M in R; { let fix n in N; |s(n)| <= M }; exists M }
let phi : N -> N where StrictMono(phi)
let L in R where SeqLimit(lambda n: s(phi(n)), L)
exists phi, L
```

**Unique up to order.** A prime $p \equiv 1 \pmod 4$ is a sum of two squares in exactly one way; `a <= b` removes the swap.

```text
let fix p in N where Prime(p), p mod 4 = 1
let a, b in N where a <= b, p = a^2 + b^2
unique a, b
```

**Fundamental theorem of algebra.** A sum binder writes the polynomial out:

```text
let fix n in N where n >= 1
let fix c : C^(n + 1) where c(n) != 0
let z in C where sum[k in 0...n](c(k) * z^k) = 0
exists z
```

**Zorn's lemma.** A hypothesis that is itself a $\forall\exists$ statement is a block after `where`:

`PartialOrder` and `Chain` are ordinary definitions, not shown.

```text
let fix X : Type
let fix le : X -> X -> Prop where PartialOrder(le), {
  let fix C : Set(X) where Chain(le, C)
  let u : X where { let fix c in C; le(c, u) }
  exists u
}
let m : X where { let fix y : X where le(m, y); y = m }
exists m
```

**Writing your field.** Four patterns that come up first in a new area.

*A derivative*, through a partial lambda, and the mean value theorem with it:

```text
def HasDeriv(f : R -> R, x : R, L : R) {
  Limit(lambda h where h != 0: (f(x + h) - f(x))/h, 0, L)
}

let fix a, b in R where a < b
let fix f : R -> R where Continuous(f),
    { let fix x in R where a < x < b; let L in R where HasDeriv(f, x, L); exists L }
let c in R where a < c < b, HasDeriv(f, c, (f(b) - f(a))/(b - a))
exists c
```

Limit applies its function only where $0 < \lvert x - a \rvert$, so the quotient is never used at $h = 0$, and the obligation is met.

*A matrix*, as a tuple of rows. A symmetric real matrix has a real eigenvalue:

```text
def MatVec<n : N>(M : (R^n)^n, v : R^n) -> R^n {
  return lambda i: sum[j : Fin(n)](M(i)(j) * v(j))
}

let fix n in N where n >= 1
let fix M : (R^n)^n where { let fix i, j : Fin(n); M(i)(j) = M(j)(i) }
let l in R
let v : R^n where v != (lambda i: 0), MatVec(M, v) = (lambda i: l * v(i))
exists l, v
```

*A path*, as a tuple of vertices. A graph is connected when any two vertices are joined by a path:

```text
def Connected<V : Type>(E : V -> V -> Prop) {
  let fix u, w : V
  let k in N
  let p : V^(k + 1) where p(0) = u, p(k) = w, { let fix i in 0...k-1; E(p(i), p(i + 1)) }
  exists k, p
}
```

k and p are introduced after u and w, so the path may depend on its endpoints.

*Probability*, as measure theory. An event is a set, `Prob(P, S)` is its probability as a real number, and an expectation is `Integral(P, X)`. Two dice sum to 7 with probability 1/6:

```text
def W := Fin(6) × Fin(6)
(card(Set[w : W where w.1 + w.2 + 2 = 7](w)) : Q) / card(W) = 1/6
```

Markov's inequality, and the strong law of large numbers, where "almost surely" is "with probability 1":

```text
let fix W : Type
let fix P : Measure(W) where IsProbabilityMeasure(P)
let fix X : W -> R where Measurable(X), { let fix w : W; X(w) >= 0 }
let fix t in R where t > 0
Prob(P, Set[w : W where X(w) >= t](w)) <= Integral(P, X) / t
```

```text
let fix W : Type
let fix P : Measure(W) where IsProbabilityMeasure(P)
let fix X : N -> W -> R where IID(X, P), Integrable(X(0), P)
def A := Set[w : W where SeqLimit(lambda n: sum[i in 0...n](X(i)(w)) / (n + 1), Integral(P, X(0)))](w)
Prob(P, A) = 1
```

As an extension, not core syntax, probability may use its own binders. `Prob[x ~ P](φ)` means `Prob(P, Set[x : T where φ](x))`, `E[x ~ P](t)` means `Integral(P, lambda x: t)`, and `P^m` is the product of m independent copies of P (mathlib's `Measure.pi`). Markov's inequality then reads:

```text
Prob[w ~ P](X(w) >= t) <= E[w ~ P](X(w)) / t
```

mathlib's own types can be used where the core numbers fall short. The VC dimension of a class of classifiers may be infinite:

```text
# ENat is mathlib's N with ∞ added; Shatters is an ordinary definition, not shown
def VCdim<X : Type>(H : Set(X -> Bool)) -> ENat {
  return sup[C : Finset(X) where Shatters(H, C)](card(C))
}
```

**Propositional logic.** Inconsistent premises, and an entailment:

```text
let A, B : Prop
A => B
A
not B
not exists consistency   # the three premises cannot all hold
```

```text
let P, Q, R : Prop
P => Q
Q => R
P
exists consistency       # the premises can all hold
fix P, Q, R
R                        # and they entail R
```

## 8. Under the hood

This section connects the picture of sections 1 to 6 to type theory and to Lean, so that a reader who knows them can fill in the details.

**Arrows and contexts.** The lines written so far form the context $\Gamma$, and a block says $\Gamma \vdash \varphi$: under $\Gamma$, its assertions hold. $\Gamma$ is finite and constructive; the values it generates are not listed and may be infinitely many. Label each combination of values that $\Gamma$ generates together; the labels form a set $\Omega$, and each variable becomes a map $\Omega \to A$, a generalised element in category theory or a random variable on a sample space. An arrow $x \to a$ is the substitution $[x := a]$.

**Why "telescope".** Each type may mention the variables before it, so $\Gamma$ is a telescope in de Bruijn's sense and $\Omega$ is an iterated $\Sigma$-type. Introduction order is the order of the $\Sigma$s, which is why line order is quantifier order.

**Arrows explain; types and proofs decide.** Nothing enumerates the arrows. The type checker checks judgements such as `x : A` mechanically, and each assertion becomes a proof obligation discharged symbolically from $\Gamma$ by Lean, the way algebra proves $(a + b)^2 = a^2 + 2ab + b^2$ without trying numbers.

| Telescope | Theory | Lean |
| --- | --- | --- |
| A block's context $\Gamma$ | Telescope, iterated $\Sigma$ | Binders `(x : A) (h : P x) …` |
| `let x : T` | Judgement $\Gamma \vdash x : T$ | `(x : T)` |
| Condition on x | Refinement type $\{x : A \mid P\,x\}$ | Hypothesis `(h : P x)` |
| `fix x`, then $\varphi$ | $\Pi$, right adjoint of weakening | `∀ x, P x → φ` |
| `exists x`, `unique x` | Truncated $\Sigma$, left adjoint; $\exists!$ | `∃ x, P x ∧ …`, `∃! x, …` |
| `def` without `return` | Predicate, $\lambda$-abstraction | `def Name … : Prop := …` |
| `def` with `return y` | Definite description, from `unique y` | `def f … : T := …` |
| `fix` on a parameter | Proof argument | `(h : C)` |
| Generics `<X : Type>` | Implicit $\Pi$ | `{X : Type}` |
| `Set[x : A where C](x)` | Comprehension | `{x : A ∣ C}` |
| `sum[i in 1...n](t)` | Finite sum over the context | `∑ i ∈ Finset.Icc 1 n, t` |
| Top-level block | Theorem | `theorem … : … := by …` |

Translation runs both ways and is deterministic once the block is written: the order of statements fixes the quantifiers, derived forms are expanded first, and Lean's kernel checks the result. An LLM may help with either direction without changing the meaning.

**Background.** Telescopes come from de Bruijn (1991) and Martin-Löf type theory (1984); quantifiers as adjoints from Lawvere (1969); refinement types from work such as Liquid Haskell (2014). The target is Lean 4 with mathlib. Mizar, Isabelle/Isar and Naproche are earlier readable formal languages; Telescope stays closer to a small programming language than to prose, so its order of statements is never ambiguous.

## 9. Building a full system

0.2.0 fixes what statements mean. A full system must also decide the following. Where a likely answer is known, it is given.

1. **Grammar and reading rules.** A formal grammar, with the rule of section 3.3 made exact for nested and executed blocks and bound variables.
2. **Types.** Inference, the upward casts of section 6, sets as domains (compiled to subtypes), and the rejection of undetermined types.
3. **Definedness.** Each partial operation, such as `/`, `-` on N, `sqrt`, integrals and limits, emits an obligation. So do `card(S)`, which needs `Finite(S)`, and `ceil` or `floor` used as an N, which needs a non-negative argument. The translator must not rely on Lean's total versions, in which 1/0 = 0, or a statement can become silently false.
4. **Definitions.** The `unique` obligation for `return`, partial functions, closures, and recursion, which 0.2.0 omits; constructions such as inductive types are imported from Lean by name.
5. **Translation details.** Index shifts between `a...b` and `Fin n`, casts between types that look alike but differ in Lean (`Vec(A, m + n)` and `Vec(A, n + m)`), and the round trip from Lean back to Telescope.
6. **Proofs.** `P by { … }` with elementary steps exists only as a sketch; proofs are out of scope for 0.2.0. A full layer needs to prove any assertion, including `not exists f` for Cantor. A proof must be able to take a generated value under its own name, obtain witnesses from hypotheses, and derive a contradiction, in the style of Isar's fix, obtain and show, with `calc` chains.
7. **Filters.** `fix n eventually`, `fix w almost(P)` and `exists n frequently`, compiled to mathlib's $\forall^{\mathsf{f}}$ and $\exists^{\mathsf{f}}$, would shorten every limit and give probability its "almost surely".
8. **Binders with parameters.** `Integral(mu)[x : X](t)` and user-defined aggregates, so that measure theory can be written without workarounds.
9. **Structures.** Predicates such as `Group(mul, one, inv)` work but give theorems that are not mathlib's. A full system needs bundled structures (`let fix G : Group`), bridges to type classes, and user infix relations such as `x <= y` for an order.
10. **Prelude.** $\emptyset$, $\subseteq$, $\cup$, $\cap$, image and preimage, and one-line quantifier binders `All[x : A](φ)` and `Some[x : A](φ)`.

## 10. Cheat sheet

| Written | Means |
| --- | --- |
| `let x : T`, `let x in S` | Introduce x with type T, or in S |
| `S where C` | Attach condition C to the line S |
| `def D := t`, `def D : T := t` | Name a term |
| `fix x`, `let fix x in S` | From here on, x is any value generated ($\forall$) |
| A line about an unfixed x | A condition: narrows what x takes |
| `exists x`, `not exists x`, `unique x` | $\exists$, $\lnot\exists$, $\exists!$ over what is generated |
| `exists consistency` | Some truth assignment of the unfixed atoms works |
| `{ … }` | A block, itself a proposition |
| `def P(…) { … }` | A named proposition |
| `def f(…) -> T { … return t }` | A function giving a value |
| `def f<X : Type>(…)` | Generics, usually inferred |
| `lambda x: t`, `if c then a else b` | Terms |
| `B[x in S where C](t)` | Aggregate B over a fresh x |
| `a...b` | The integers from a to b |
| `not`, `and`, `or`, `=>`, `<=>` | Connectives, tightest first; `=>` groups right |
| `P by { … }` | A proof of P |
| `;`, `#`, `# pseudo telescope` | End of statement, comment, draft marker |
| `Prop`, `Type`, `Set(A)`, `Finset(A)`, `A^n` | Propositions, types, sets, finite sets, tuples from 0 |
| N, Z, Q, R, C | Number types, cast upward automatically |
