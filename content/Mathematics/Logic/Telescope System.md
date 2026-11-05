*Version 0.1.0*

## 1. Lines

A document is a sequence of lines, and every line is one of two kinds:

- a **context line**, which introduces a variable or narrows what it can be;
- a **judgment line**, which asserts that something holds in the current context, written Γ ⊢ φ.

## 2. Variables and States

Every variable has a type and is either **open** or **closed**. `let x : A` makes x open: it is still being specified. Its scope starts as the whole type A, and every later context line that mentions x narrows it:

$$
\text{scope}(x) = \{\, u : A \mid \text{every constraint on } x \,\}
$$

`final` closes a variable: all information about it is now set. An optional claim word says what is asserted about its scope:

| Closing | Claim about scope(x) | Logic |
| --- | --- | --- |
| `final x` | The judgments hold on all of it | ∀ |
| `final exists x` | It is non-empty | ∃ |
| `final not exists x` | It is empty | ¬∃ |

Header parameters of a `jug` are closed.

**Shorthand.**

- `let x : A where C` declares x together with a constraint C.
- `final [exists | not exists] x : A where C` declares and closes in one line. x counts as declared at that line, and C holds its constraints.
- A `where` clause may continue over indented lines.
- One line may declare several variables in order, and a later type may mention an earlier variable: `final N : Type, z : N`.

## 3. Core Rules

Three rules turn a block of lines into one exact statement.

**Classification.** If every free variable in a line is closed, the line is a judgment line. If the line mentions any open variable, it is a context line that constrains those open variables. The state of the variables decides a line's role, not its position or wording.

**Polarity.** To read a block as one statement, place each line right after the latest-declared variable it mentions. Then:

- a constraint on a variable later closed by `final` is a **hypothesis** (→);
- a constraint on a variable later closed by `final exists` or `final not exists` is a **requirement**, the body of the ∃ or ¬∃;
- a judgment line is a **conclusion**.

**Dependency.** Declaration order is quantifier order. A variable closed by `final exists` or `final not exists` treats `final` variables declared *before* it as parameters it may depend on. `final` variables declared *after* it are quantified inside its claim.

## 4. Blocks and Naming

**Anonymous blocks.** Braces `{ … }` form a block that stands as a single line in its outer block. A short block can be written inline, with `;` separating its lines.

- Variables declared inside the block are local to it.
- The block must be closed internally.
- Outer variables act as parameters inside the block. The outer variables it mentions are its free variables, and the classification rule applies to the block through them.
- A block at top level is an unnamed theorem.

**Naming.** A closed block is a judgment. `jug Name(params) := …` gives it a name, and `Name(args)` can then be used as a single line anywhere. The classification rule applies through its arguments: if all are closed it is a judgment line, otherwise it constrains its open arguments. `not` may be applied to any judgment. A block that ends with open variables is ill-formed.

## 5. Examples

**Limit.** d is declared after e and before x, so it may depend on e but not on x.

```text
jug Limit(f : R -> R, a : R, L : R) :=
  final e : R where e > 0
  let d : R where d > 0
  final x : R
  0 < |x - a| < d  =>  |f(x) - L| < e    # d is open: constrains d
  final exists d
```

Reads as: ∀e > 0. ∃d > 0. ∀x. (0 < |x−a| < d → |f(x)−L| < e).

**Induction.** A nested block serves as a hypothesis on P.

```text
jug Induction(N : Type, z : N, S : N -> N) :=
  final P : N -> Prop where
    P(z)
    { final k : N where P(k); P(S(k)) }   # P is open: a hypothesis
  final n : N
  P(n)
```

Reads as: ∀P. P(z) → (∀k. P(k) → P(S(k))) → ∀n. P(n).

**Sum of limits.** An unnamed top-level theorem.

```text
{ final f, g : R -> R
  final a, L, M : R where Limit(f, a, L), Limit(g, a, M)
  Limit(f + g, a, L + M) }
```

**Infinitely many primes.**

```text
{ final n : N
  final exists p : N where p > n, Prime(p) }
```

**√2 is irrational.**

```text
{ final not exists p, q : Z where q != 0, p^2 = 2 q^2 }
```

**Cantor's theorem.**

```text
{ final A : Type
  final not exists f : A -> Set(A) where Surjective(A, Set(A), f) }
```

Reads as: ∀A. ¬∃f. Surjective(f).

## 6. Meaning

Every closed block compiles deterministically to an ordered list of binders, which gives it an exact type-theoretic meaning and a direct Lean translation.

| Construct | Type theory | Lean |
| --- | --- | --- |
| `final x` | Π | `∀ x, …` |
| `final exists x` | Σ (as a proposition) | `∃ x, …` |
| `final not exists x` | ¬Σ | `¬ ∃ x, …` |
| Hypothesis | Function domain | `h → …` |
| Requirement | Pair component | `… ∧ …` |
| `jug Name(…) := …` | Named proposition | `def Name … : Prop` |
| Top-level block | Judgment | `example : …` |

For example, the sum-of-limits block becomes:

```text
example (f g : ℝ → ℝ) (a L M : ℝ)
    (h₁ : Limit f a L) (h₂ : Limit g a M) :
    Limit (f + g) a (L + M) := by sorry
```

Each judgment line is a **proof obligation**. A later justification layer (`by …`) will attach proofs, which can be filled procedurally or with AI help and then checked by Lean's kernel. Quantifier structure always comes from the rules above, never from AI, so a translated statement means exactly what was written.
