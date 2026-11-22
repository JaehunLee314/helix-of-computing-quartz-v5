*Telescope 0.1.1*

Telescope is a formal-enough, human-readable language for writing mathematical claims the way a textbook does, precise enough to translate into Lean.

## 1. Overview

Telescope is a **procedural** language for writing logical claims. Each **statement** ends at a line break or a semicolon, and a sequence of statements is a **block**. Procedural means that statement order matters: a block is read top to bottom, and each statement acts on what the statements above it have set up. A statement can only use variables introduced above it, a range proposition counts only the predicates written before it, and the order of introductions is the order of quantifiers.

Every block follows the same flow:

1. **Define a variable.** `let x : A` names x and says which domain A it ranges over.
2. **Refine its context.** Statements that mention x narrow down which values of x are meant.
3. **State a truth.** Either fix x with `fix x` and state what holds for every such value, or count the values that remain with `exists`, `not exists` or `unique`.

Counting leaves x open, so steps 2 and 3 can alternate; fixing ends the refinement. Statements are separated by line breaks or by `;`, so several short statements can share one line: `let x : R; x != 0; fix x`.

## 2. Core concepts

### 2.1 Variables

**Introduction.** `let x : A` introduces x as a variable that ranges over the domain A, its **type**. Nothing is asserted. A statement that starts with `let` always brings in a new name, so the order of introductions can be read down the left margin. One statement may introduce several variables, and a later type may mention an earlier one: `let N : Type, z : N`.

**Open and closed variables.** A newly introduced variable is **open**: it is still being described, and the statements that follow narrow down which of its values are meant. `fix x` makes it **closed**:

- x now stands for an arbitrary but fixed value among those still meant;
- the conditions written about x while it was open become its **assumptions**;
- every later statement about x should hold for every such x, under those assumptions.

The fix statement asserts nothing itself; it changes how later statements are read. A variable is fixed at most once, only after it is introduced, and can no longer be narrowed afterwards. `fix x, y` fixes several variables at once; section 3 shows how to introduce and fix in one statement.

**Scope.** While x is open, every statement that mentions it is a **predicate** on x. The values that satisfy every predicate so far form the **scope** of x:

$$
\mathrm{scope}(x) = {, x \in A \mid P_1(x) \wedge \dots \wedge P_n(x) ,}
$$

The scope narrows with each predicate and is frozen when x is fixed; its predicates are then the assumptions of x.

**Types.** The type says where x lives; predicates say which of those values are meant. So the type is written on the `let` statement, never as a statement of its own: `d : R` is not allowed. When the type is clear from how x is used, it can be left out:

- after `let d`, a predicate `|x - a| < d` with x real makes d real;
- `x ∈ S` makes x range over the elements of S.

A block is invalid if a variable's type cannot be determined, or could be more than one: `d > 0` alone fits $\mathbb{N}$, $\mathbb{Z}$ and $\mathbb{R}$. The type must be clear by the time x is fixed or used in a range proposition (2.2).

### 2.2 Statements

Every statement either builds the context or asserts something in it.

**Context statements** build the context and assert nothing:

- an introduction, `let x : A`;
- a **predicate**, a statement that mentions an open variable;
- a fix, `fix x`.

**Judgements** assert something:

- a **proposition** is a statement whose variables are all closed. It asserts that the statement holds for every value of the closed variables that meets their assumptions;
- a **range proposition** says how many values are left in an open variable's scope. The variable stays open afterwards: later predicates can narrow it further, and later range propositions can say more.

|Range proposition|Meaning|Logic|
|---|---|---|
|`exists x`|At least one value meets every predicate on x so far|$\exists$|
|`not exists x`|No value does|$\neg\exists$|
|`unique x`|Exactly one value does|$\exists!$|

When predicates tie two open variables together, count them jointly: `exists p, q`.

**Classification.** The variables in a statement decide its kind:

- a statement starting with `exists`, `not exists` or `unique` is a range proposition;
- a statement whose variables are all closed is a proposition;
- any other statement mentions an open variable and is a predicate on it.

Composite statements (section 3) are classified after they are expanded.

Statements are built with the connectives `A => B`, `and`, `or` and `not`.

**Building up a block.** Range propositions and `fix` together let a block build up the way a textbook does:

```text
let x
P(x)
exists x        # there is an x with P(x)
Q(x)
exists x        # furthermore, there is an x with P(x) and Q(x)
fix x
R(x)            # for every x with P(x) and Q(x), R(x)
```

The same predicate can be counted first and become an assumption later, as P(x) does here. A variable that is never fixed or counted has no effect, which usually signals a mistake.

### 2.3 Rules

**Polarity.** A block states all its judgements together ($\wedge$). Each judgement picks up the predicates it depends on:

- predicates written before `fix x` are assumptions of every later judgement about x ($\to$);
- predicates on x written up to a range proposition sit inside it ($\exists$, $\neg\exists$ or $\exists!$).

So the build-up example in 2.2 says: $(\exists x., P(x)) \wedge (\exists x., P(x) \wedge Q(x)) \wedge \forall x., (P(x) \wedge Q(x) \to R(x))$.

**Dependency.** Introduction order is quantifier order. In a range proposition about x, the variables closed before x was introduced are given, and the witness may depend on them. Closed variables introduced after x that appear in x's predicates are quantified inside the range proposition, so the witness must work for all of them. Writing such predicates as a nested block, as in Limit, makes this visible.

## 3. Composite statements

A composite statement combines several statements into one. It is pure shorthand: it means exactly the statements it expands to, in the order shown, so the order of introductions can still be read down the left margin.

### 3.1 let fix

`let fix x : A` introduces x and closes it in one statement: it means `let x : A`, then `fix x`. It suits a variable with no predicates, such as `let fix n : N`.

### 3.2 where

**Where Rule.** `S where C₁, …, Cₙ` attaches predicates to the statement S. The conditions are written out as separate predicates around S, where Q stands for `exists`, `not exists` or `unique`:

|Written|Means|
|---|---|
|`let x : A where C`|`let x : A`, then `C`|
|`let fix x : A where C`|`let x : A`, then `C`, then `fix x`|
|`fix x where C`|`C`, then `fix x`|
|`Q x where C`|`C`, then `Q x`|

- `where` only follows `let`, `fix` or a range proposition.
- A condition may only mention variables introduced above or by S itself, so `where` never introduces a variable. A nested block inside a condition may introduce variables of its own, since they are local to it.
- Each condition must mention at least one of S's variables, so it is always a predicate on them.
- The conditions are ordinary predicates. After `exists x where C`, x stays open and C keeps narrowing it.
- Conditions are separated by commas and may continue on indented lines.

`let fix e : R where e > 0` reads as "for every $e > 0$", and `exists d where …` as "there is a $d$ such that …". With composite statements, the Limit definition of section 5 shrinks to three statements after the header:

```text
def Limit(f : R -> R, a : R, L : R) :=
  let fix e : R where e > 0
  let d : R where d > 0
  exists d where { let fix x : R; 0 < |x - a| < d  =>  |f(x) - L| < e }
```

## 4. Definitions and nested blocks

`def Name(params) := …` names the proposition its block states: all of the block's judgements together (2.3). The parameters are closed variables. A definition asserts nothing by itself. `Name(args)` can then be used as a statement and is classified like any other: a proposition if all its arguments are closed, otherwise a predicate on the open ones.

**Nested blocks.** Braces `{ … }` group statements into one statement of the outer block. A short block can be written on one line, with `;` separating its statements.

- Variables introduced inside a block are local to it.
- Outer variables act as given values inside the block, whether open or closed: statements inside never narrow them.
- The block is classified by the outer variables it mentions. In Limit, the nested block mentions d, which is open, so it is a predicate on d.

In 0.1.1 every block lives inside a definition; top-level unnamed blocks are not part of this version.

## 5. Examples

Each example is a definition. In 0.1.1 a theorem is written as the definition of the proposition it states. Prime and Surjective are defined along the way, so the later examples can use them.

**Limit.** The nested block is a predicate on d, and x is local to it, so one d must work for every x.

```text
def Limit(f : R -> R, a : R, L : R) :=
  let e : R
  e > 0
  fix e
  let d : R
  d > 0
  { let fix x : R; 0 < |x - a| < d  =>  |f(x) - L| < e }
  exists d
```

Reads as: $\forall e > 0.\ \exists d > 0.\ \forall x.\ (0 < |x - a| < d \to |f(x) - L| < e)$.

**Induction.** P ranges over properties of N (Prop is the domain of propositions). The nested block is a predicate on P, and becomes an assumption when P is fixed.

```text
def Induction(N : Type, z : N, S : N -> N) :=
  let P : N -> Prop
  P(z)
  { let k : N; P(k); fix k; P(S(k)) }
  fix P
  let fix n : N
  P(n)
```

Reads as: $\forall P.\ P(z) \to (\forall k.\ P(k) \to P(S(k))) \to \forall n.\ P(n)$.

**Sum of limits.**

```text
def LimitAdd :=
  let fix f, g : R -> R
  let a, L, M : R
  Limit(f, a, L)
  Limit(g, a, M)
  fix a, L, M
  Limit(f + g, a, L + M)
```

Reads as: $\forall f, g.\ \forall a, L, M.\ \mathrm{Limit}(f, a, L) \wedge \mathrm{Limit}(g, a, M) \to \mathrm{Limit}(f + g, a, L + M)$.

**Prime numbers.** A definition may contain several judgements, and all of them must hold.

```text
def Prime(p : N) :=
  p > 1
  { let d : N; d | p; fix d; d = 1 or d = p }
```

Reads as: $p > 1 \wedge \forall d.\ (d \mid p \to d = 1 \vee d = p)$.

**Infinitely many primes.**

```text
def InfinitelyManyPrimes :=
  let fix n : N
  let p : N
  p > n
  Prime(p)
  exists p
```

Reads as: $\forall n.\ \exists p.\ p > n \wedge \mathrm{Prime}(p)$.

**$\sqrt{2}$ is irrational.**

```text
def Sqrt2Irrational :=
  let p, q : Z
  q != 0
  p^2 = 2 q^2
  not exists p, q
```

Reads as: $\neg\exists p, q \in \mathbb{Z}.\ q \neq 0 \wedge p^2 = 2q^2$.

**Surjectivity.** a is introduced after b, so it may depend on b.

```text
def Surjective(A : Type, B : Type, f : A -> B) :=
  let fix b : B
  let a : A
  f(a) = b
  exists a
```

Reads as: $\forall b.\ \exists a.\ f(a) = b$.

**Cantor's theorem.**

```text
def Cantor :=
  let fix A : Type
  let f : A -> Set(A)
  Surjective(A, Set(A), f)
  not exists f
```

Reads as: $\forall A.\ \neg\exists f : A \to \mathrm{Set}(A).\ \mathrm{Surjective}(f)$.

**Multiplicative inverses.**

```text
def Inverse :=
  let x : R
  x != 0
  fix x
  let y : R
  x * y = 1
  unique y
```

Reads as: $\forall x \neq 0.\ \exists! y.\ xy = 1$.

## 6. Connection with Lean

Every definition compiles deterministically to a Lean proposition. Lean is based on type theory, and this section is the only place where that background matters.

Composite statements (section 3) are expanded before translation, so they need no rows of their own.

|Telescope|Type theory|Lean|
|---|---|---|
|`let x : A`|Variable declaration $x : A$|Binder `(x : A)`|
|Predicate $P(x)$|$P : A \to \mathrm{Prop}$|`P x`|
|Scope of x|Subtype ${x : A \mid P,x}$|`{x : A // P x}`|
|`fix x`|Context extension $\Gamma, x : A, h : P,x$|`∀ x, P x → …`|
|Proposition $\varphi$|Judgement $\Gamma \vdash \varphi$|`φ`, proved in that context|
|`exists x`|The subtype is inhabited|`∃ x, P x ∧ …`|
|`not exists x`|The subtype is empty|`¬ ∃ x, P x ∧ …`|
|`unique x`|The subtype has one element|`∃! x, …`|
|Several judgements|Product|`… ∧ …`|
|`def Name(…) := …`|Definition of a proposition|`def Name … : Prop := …`|

For example, the build-up in 2.2 and the inverse example become:

```text
(∃ x, P x) ∧ (∃ x, P x ∧ Q x) ∧ (∀ x, P x → Q x → R x)

∀ x : ℝ, x ≠ 0 → ∃! y : ℝ, x * y = 1
```

Two design choices come from this background. In type theory a variable's type is part of its declaration, not a proposition, which is why Telescope keeps types on the `let` statement. And Lean silently defaults numerals to $\mathbb{N}$ when a type is missing, which is why Telescope rejects undetermined types instead of guessing.

Each judgement becomes a **proof obligation**. A later proof layer will discharge them, procedurally or with AI help, checked by Lean's kernel. Quantifier structure always comes from the rules in 2.3, never from AI, so a translated block means exactly what was written.

## 7. Revisions

**0.1.1** (2026-11-21), changes from 0.1.0:

- `final` is renamed `fix`.
- `exists` and `not exists` no longer close a variable: they are range propositions, and the variable stays open after them. `unique` is added.
- The `final exists` and `final not exists` forms are removed.
- The `where` clause is restricted: it only follows let, fix or a range proposition, never introduces a variable, and its conditions are ordinary predicates.
- Variables are introduced only by `let`; fixing or counting a name that was never introduced is an error. `let fix` is added for introducing and fixing in one statement.
- A type can only be written on `let`, and may be left out when it is clear from use. An undetermined or ambiguous type makes a block invalid.
- Lines are now called statements, and a sequence of statements a block. Judgement lines are split into propositions and range propositions; context lines that narrow a variable are now called predicates.
- A block now asserts all of its judgements together, instead of compiling to a single chain of quantifiers.
- `jug` is renamed `def`, and top-level unnamed blocks are removed.

**0.1.0** (2026-11-06): initial version.

## Appendix: Keyword reference

| Keyword                  | Kind                | Meaning                                                         |
| ------------------------ | ------------------- | --------------------------------------------------------------- |
| `let x : A`              | Introduction        | x ranges over A; nothing is asserted                            |
| `fix x`                  | Fix                 | x is now arbitrary but fixed; its predicates become assumptions |
| `let fix x : A`          | Composite statement | Introduces x and fixes it at once                               |
| `exists x`               | Range proposition   | $\exists$: some value meets every predicate on x so far         |
| `not exists x`           | Range proposition   | $\neg\exists$: no value does                                    |
| `unique x`               | Range proposition   | $\exists!$: exactly one value does                              |
| `;`                      | Separator           | Ends a statement, like a line break                             |
| `{ … }`                  | Nested block        | A group of statements used as one statement                     |
| `def Name(…) := …`       | Definition          | Names a proposition                                             |
| `not`, `=>`, `and`, `or` | Connectives         | $\neg$, $\to$, $\wedge$, $\vee$                                 |
| `S where C`              | Composite statement | Attaches predicates C to S (section 3.2)                        |