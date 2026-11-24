*Telescope 0.1.2*

Telescope is a formal-enough, human-readable language for writing mathematical claims the way a textbook does, precise enough to translate into Lean.

## 1. Overview

A Telescope block says: in this context, these assertions hold. Logicians write this $\Gamma \vdash \varphi$. The **context** $\Gamma$ on the left is the background; the **assertions** on the right are where the work is done. "Context" is meant in its linguistic sense: the context decides what a statement means. The same statement `x > 0` is background or an assertion depending on what stands above it (1.1).

Telescope is **procedural**: a block is read top to bottom, and each statement acts on what the statements above it have set up. A **statement** ends at a line break or a semicolon, and a sequence of statements is a **block**. Every block follows the same flow:

1. **Let.** `let x : A` names a variable $x$ and its codomain $A$, the type its values come from.
2. **Refine.** Propositions about $x$ narrow down which of those values are meant.
3. **Conclude.** Either `fix x` and assert what holds for every value that remains, or count the values that remain with `exists`, `not exists` or `unique`.

Counting leaves $x$ open, so refining and counting can alternate; fixing ends the refinement. Short statements can share a line: `let x : R; x != 0; fix x`.

Sections 2 to 4 are the core: the context, the assertions and zero-order statements. Sections 5 to 8 add blocks, definitions, derived forms, functions and binders. Section 9 describes pseudocode for informal drafts, and sections 10 and 11 give examples and the translation to Lean.

### 1.1 Terms

| Term | Meaning |
| --- | --- |
| Statement | One unit of meaning, ended by a line break or `;` |
| Block | A sequence of statements; a layer of context stacked on the one around it (5.1) |
| Variable | A name introduced by `let`, with a codomain |
| Open variable | Introduced, not yet fixed; its range can still shrink |
| Closed variable | Fixed with `fix`; stands for an arbitrary value of its frozen range |
| Bound variable | Bound by a binder such as `sum` or `Set`; never open or closed (section 8) |
| Codomain | The type written on `let`; set once, never changes |
| Range | The values of the codomain that meet every context proposition so far |
| Proposition | A statement with a truth value, of type `Prop` |
| Open proposition | A proposition that mentions an open variable |
| Closed proposition | A proposition whose variables are all closed |
| Ground proposition | A proposition with no variables at all, such as `1 + 1 = 2`; a special case of closed |

Every statement falls on one side of $\Gamma \vdash \varphi$:

| Side | Statement | Form | Role |
| --- | --- | --- | --- |
| Context | Introduction | `let x : A` | Brings in a variable; asserts nothing |
| Context | Context proposition | An open proposition | Narrows the range of its open variables |
| Context | Fix | `fix x` | Closes $x$; its context propositions become background for later assertions |
| Assertion | Asserted proposition | A closed or ground proposition | Holds for every value of the closed variables in their ranges |
| Assertion | Range assertion | `exists x`, `not exists x`, `unique x`, or a bare `exists` | Counts the range of open variables, which stay open |

A statement's side is decided by its first word and its variables, never by a marker:

- a statement starting with `exists`, `not exists` or `unique` is a range assertion;
- a closed or ground proposition is an asserted proposition;
- an open proposition is a context proposition;
- `let` and `fix` are context statements, not propositions.

Derived forms (section 6) are sorted after they are expanded, and an executed block (5.3) is one statement, sorted by the outer variables it mentions.

## 2. Context

The context is built from three kinds of statement: introductions, context propositions and fixes. None of them asserts anything.

### 2.1 Variables

`let x : A` **introduces** $x$, a variable whose values lie in $A$, its **codomain** (its type). Every introduction starts with `let`, so the order of introductions can be read down the left margin. One statement may introduce several variables, and a later codomain may mention an earlier variable: `let N : Type, z : N`.

The codomain is written only on the `let` and never changes, so `d : R` on a line of its own is not allowed. It may be left out when use makes it clear: after `let d`, the proposition `|x - a| < d` with $x$ real makes $d$ real, and `x ∈ S` with `S : Set(A)` gives $x$ the codomain $A$.

**Typing.** Every variable has exactly one codomain by the time it is fixed or counted. A codomain that cannot be determined, or could be more than one, makes the block invalid: `let d; d > 0; exists d` is invalid, since $d$ could be natural, integer or real, while `let d : R; d > 0; exists d` is valid. Every expression must also be well typed: `x ∈ S` needs `S : Set(A)` with $A$ the codomain of $x$.

### 2.2 Context propositions and range

A newly introduced variable is **open**. A proposition that mentions an open variable is an **open proposition**, and in a block it is a **context proposition** on that variable: it narrows down which of its values are meant. The values that meet every context proposition so far form the **range** of $x$:

$$
\mathrm{range}(x) = \lbrace x \in A \mid P_1(x) \wedge \dots \wedge P_n(x) \rbrace \subseteq A
$$

The range starts as all of $A$ and shrinks with each context proposition. "Range" is meant in its mathematical sense, the image: the set of values that may fill the slot $x$. It has nothing to do with Python's `range()`. A proposition on several open variables narrows their joint range, the set of tuples that meet it.

### 2.3 fix

`fix x` **closes** $x$. From then on $x$ stands for an arbitrary but fixed value in its range, and every later statement about $x$ should hold for every such $x$. The context propositions written about $x$ so far become background for every later assertion about $x$ (3.3).

A fix asserts nothing itself; it changes how later statements are read. A variable is fixed at most once, and only after it is introduced. `fix x, y` fixes several variables at once, and `let fix x : A` introduces and fixes in one statement (section 6).

## 3. Assertions

An **assertion** states something in the context built so far. An asserted proposition says what holds for all values of closed variables; a range assertion counts the values of open ones.

### 3.1 Asserted propositions

A closed proposition, including a ground one, is an **asserted proposition**. It holds for every value of its variables that lies in their ranges.

```text
let x : R
x != 0
fix x
x^2 > 0          # for every real x with x != 0, x^2 > 0
```

Propositions combine with `not`, `and`, `or`, `=>` and `<=>`; precedence is in section 6.

### 3.2 Range assertions

A **range assertion** says how many values are left in an open variable's range. The variable stays open afterwards, so later context propositions can narrow it further and later range assertions can say more.

| Range assertion | Meaning | Logic |
| --- | --- | --- |
| `exists x` | The range of $x$ is not empty | $\exists$ |
| `not exists x` | The range of $x$ is empty | $\lnot\exists$ |
| `unique x` | The range of $x$ has exactly one element | $\exists!$ |

`exists p, q` counts the joint range of $p$ and $q$.

### 3.3 Building up

Range assertions and `fix` together let a block build up the way a textbook does:

```text
let x : A
P(x)
exists x        # there is an x with P(x)
Q(x)
exists x        # furthermore, there is an x with P(x) and Q(x)
fix x
R(x)            # for every x with P(x) and Q(x), R(x)
```

A block makes all its assertions together ($\land$), and each context proposition ends up in one of two roles. Written before `fix x`, it is background for every later assertion about $x$ ($\forall$ and $\to$). Written up to a range assertion, it is counted inside that assertion ($\exists$, $\lnot\exists$ or $\exists!$). $P(x)$ above plays both roles, so the block reads as:

$$
(\exists x. P(x)) \wedge (\exists x. P(x) \wedge Q(x)) \wedge \forall x. (P(x) \wedge Q(x) \to R(x))
$$

A variable that is never fixed or counted has no effect, which usually signals a mistake.

### 3.4 Quantifier order

Introduction order is quantifier order: read the `let` statements down the left margin and you have the quantifier prefix. In a range assertion about $x$, the variables closed before $x$ was introduced are given, and the witness may depend on them. Closed variables introduced after $x$ that appear in its context propositions are quantified inside the range assertion, so one witness must work for all of them.

```text
let fix b : B
let a : A where f(a) = b
exists a          # for all b there is an a: a may depend on b
```

Swap the two `let` statements and the block says that one $a$ works for every $b$.

## 4. Zero-order statements

A zero-order statement has no internal structure that Telescope looks into. There are two kinds, and both work on either side of $\Gamma \vdash \varphi$.

**Ground propositions** have no variables at all, such as `1 + 1 = 2`. Written on their own they are asserted propositions, since nothing in them is open.

**Atoms** are statements treated as opaque, such as "it rains". An atom is a `Prop` variable, introduced like any other, and it is an open proposition until it is fixed. While atoms are open, their joint range is the set of truth assignments that make every context proposition so far true.

A range assertion with no variable named counts the joint range of every open variable in the block. For atoms, that range is the combination of all their context propositions, so a bare `exists` says they are consistent and a bare `not exists` says they are inconsistent. Fixing the atoms instead turns later assertions into entailments:

```text
let P, Q, R : Prop
P => Q
Q => R
P
exists          # consistent: some assignment meets every context proposition
fix P, Q, R
R               # entailed: every such assignment makes R true
```

A bare `unique` says the context propositions force exactly one assignment. The bare form means exactly `exists P, Q, R`, with the open variables listed in introduction order.

## 5. Blocks: managing context

### 5.1 Blocks as a stack

Braces `{ … }` put a block inside a block. Picture the context as a stack of sheets of paper. An opening brace lays a fresh sheet on top, and every variable introduced inside the braces is written on that sheet. The closing brace removes the sheet, and those variables disappear with it. All that carries down to the sheet below is what the inner block asserted.

From the top sheet you can read everything on the sheets beneath, but you cannot write on them. Variables from outside can be used inside the braces, but not narrowed, fixed or counted there. So a name is visible from its introduction until its sheet is removed, and it cannot be introduced again while it is visible.

The inner block as a whole is one statement of the block around it: a context proposition if it mentions an open outer variable, and an asserted proposition otherwise. In Limit (section 10) the inner block mentions the open $d$, so it is a context proposition on $d$.

A short block fits on one line, with `;` between statements. A longer one spans several indented lines:

```text
{
  let d : N where d | p
  fix d
  d = 1 or d = p
}
```

For programmers: a block is a stack frame, and its variables are local variables.

### 5.2 Named definitions

`def Name(params) { … }` gives a block a name. The parameters are closed variables, and their types are required. A definition asserts nothing by itself; it names what its block asserts. `Name(args)` is then a statement like any other, sorted by its arguments (1.1).

```text
def Prime(p : N) {
  p > 1
  { let fix d : N where d | p; d = 1 or d = p }
}
```

A parameter may carry context propositions with `where`, so that callers need not restate them:

```text
def Close(eps : R where eps > 0, x : R, y : R) { |x - y| < eps }
```

Inside the definition, eps behaves as after `let fix eps : R where eps > 0`. At each use those propositions become proof obligations: `Close(e, a, b)` is well formed only where $e > 0$ follows from the context (section 11).

### 5.3 Executed blocks

`def() { … }()` defines a block with no name and runs it at once, like `(lambda: …)()` in Python. It lays a new sheet on the stack in the middle of a block (5.1). Unlike a named definition, it is a closure: it sees the variables around it. The bare form `{ … }` is shorthand for it (section 6). With parameters, `def(x : R) { x > 0 }` is a function of type `R -> Prop` (section 7).

### 5.4 File scope and theorems

Statements outside any `def` are the file's **top-level code**, as in Python, and form its **top-level block**. The file makes the assertions of its top-level block, so this is where theorems are written. Top-level variables live in the **file scope**, Python's module scope.

A named `def` sees only its parameters and the definitions above it, never file-scope variables. Its meaning is then the same wherever it is used, and introduction order stays quantifier order: a shared file-scope $X$ would otherwise sit outermost in every quantifier prefix, so a theorem whose constants must come before $X$ could not be stated. A definition gets what it needs as parameters, explicit or implicit (7.3).

A name can be introduced only once in the file scope, so several theorems in one file are each wrapped in an executed block:

```text
{ let fix n : N; let p : N where p > n, Prime(p); exists p }
{ let p, q : Z where q != 0, p^2 = 2 q^2; not exists p, q }
```

To name a theorem, define it and then state it: `def Euclid { … }`, then `Euclid` on a line of its own.

## 6. Derived forms

A derived form is pure shorthand: it means exactly what it expands to, in the order shown, and is sorted after expansion (1.1). $Q$ stands for `exists`, `not exists` or `unique`.

| Written | Means |
| --- | --- |
| `let fix x : A` | `let x : A`, then `fix x` |
| `let x : A where C` | `let x : A`, then `C` |
| `let fix x : A where C` | `let x : A`, then `C`, then `fix x` |
| `fix x where C` | `C`, then `fix x` |
| `Q x where C` | `C`, then `Q x` |
| `def F(x : A where C) { … }` | Parameter $x$ with context proposition $C$ (5.2) |
| `{ … }` | `def() { … }()` (5.3) |
| `def F { … }` and `F` | `def F() { … }` and `F()` |
| `A <=> B` | `(A => B) and (B => A)` |
| `a < b < c` | `a < b and b < c` |

**where.** `S where C1, …, Cn` attaches context propositions to $S$, which must be a `let`, a `fix`, a range assertion or a parameter. Each may mention only variables introduced above or by $S$, so `where` never introduces a variable; an executed block inside one may introduce local ones. Each must mention a variable of $S$. After `exists x where C`, $x$ stays open and $C$ keeps narrowing it. They are separated by commas and may continue on indented lines. `let fix e : R where e > 0` reads "for every $e > 0$", and `exists d where …` reads "there is a $d$ such that …".

**Equivalence.** "The following are equivalent" is written as `A <=> B` and `B <=> C`, not as a cycle of `=>`.

**Chained comparisons** expand pair by pair, as in Python: `0 < eps < 1`. A chain may not change direction, so `a < b > c` is not allowed.

**Precedence**, tightest first: atomic statements (comparisons, `∈`, uses of definitions), `not`, `and`, `or`, `=>`, `<=>`. `=>` groups to the right, and `<=>` does not chain. Parentheses group formulas; braces always delimit blocks.

## 7. Functions, types and sets

### 7.1 Every def is a function

A **value definition** names a term. It states its return type after `->` and gives its value with `return`:

```text
def sq(x : R) -> R { return x^2 }
def dist(x : R, y : R) -> R { return |x - y| }
```

A definition without a return type returns `Prop`, the truth value of what its block asserts. So `Prime` is a function of type `N -> Prop`, just as `sq` has type `R -> R`. In 0.1.2 the block of a value definition is a single `return t`. A definition with no parameters names a value: `def tau -> R { return 2 * pi }` is used as `tau`.

**Function terms.** `lambda x: t` is the function that sends $x$ to $t$, as in Python. The type of $x$ is inferred from use, or written `lambda (x : R): t`. For blocks, the counterpart is an anonymous definition `def(x : A) { … }` (5.3).

### 7.2 Prop and sets

`Prop` is the type of classical truth values. A property of elements of $A$ is a function `A -> Prop`, and a set is such a property:

$$
\mathrm{Set}(A) = A \to \mathrm{Prop}, \qquad x \in S \text{ means } S(x)
$$

Proofs are not values of the language; showing an assertion true is the job of a later proof layer (section 11). Sets are formed with the binder `Set[x : A](…)` (section 8), since braces always delimit blocks.

### 7.3 Types

**Function types.** `A -> B` groups to the right. A **dependent** function type names its argument so the result can mention it: `(m : N) -> (X × Bool)^m -> Hyp(X)` takes a size $m$ and a sample of that size.

**Products and tuples.** `A × B` has components `z.1` and `z.2`. `A^m` is the type of $m$-tuples, functions from `1..m` to $A$, so the $i$-th entry of $S$ is `S(i)`.

**Type abbreviations** are value definitions whose value is a type:

```text
def Hyp(X : Type) -> Type { return X -> Bool }
def Learner(X : Type) -> Type { return (m : N) -> (X × Bool)^m -> Hyp(X) }
```

**Sets as types.** A set can stand where a type is expected: with `S : Set(A)`, `let x : S` means `let x : A where x ∈ S`, and `S -> Bool` is the type of functions on the elements of $S$. `Finset(A)`, the type of finite subsets of $A$, works the same way.

**Implicit arguments.** Parameters in square brackets before the parentheses are inferred from the other arguments and left out at use:

```text
def L_S[X : Type, m : N](S : (X × Bool)^m, h : Hyp(X)) -> R { … }
L_S(S, h)          # X and m are read off the types of S and h
```

If an implicit argument cannot be inferred, or could be inferred in more than one way, the block is invalid (2.1); write it out as `L_S[X, m](S, h)`.

## 8. Binders

Sums, products, infima and set-builder notation bind a variable without quantifying over it. Telescope writes them in one form:

```text
B[x in S](body)    # x running through the set S
B[x : A](body)     # x running through the type A
```

$B$ is the binder, $x$ the **bound variable**, and the body a term or proposition in which $x$ is a given value. A body of several statements is written as a block: `B[x : A]{ … }`.

| Binder | Meaning | Body |
| --- | --- | --- |
| `sum[i in 1..m](t)`, `prod[i in 1..m](t)` | Sum and product of $t$ over $i = 1, \dots, m$ | Term |
| `inf[x in S](t)`, `sup[x in S](t)` | Infimum and supremum of $t$ over $S$ | Real term |
| `Set[x : A](φ)` | The set of $x$ in $A$ for which $\varphi$ holds | Proposition |

`1..m` is the set of integers from 1 to $m$.

**Bound variables are not introductions.** A bound variable is never open, fixed or counted: the binder adds or collects over it, and the result is a number or a set, not an assertion. So it takes no place in the quantifier order (3.4) and is visible only in its body.

**One form for all.** A binder is a function applied to a function: `B[x in S](t)` means `B(S, lambda x: t)`. Since a set is a property (7.2), `Set[x : A](φ)` is just `lambda (x : A): φ`. A new binder needs only a definition, not new syntax, so extensions can add their own.

## 9. Pseudocode

Telescope pseudocode is for rough drafts, the way C-style pseudocode is for algorithms: it borrows the shape of the language without being the language. A file or snippet that starts with the comment `# pseudo telescope` is pseudocode. It is never compiled, so nothing in it has to type-check.

```text
# pseudo telescope
let fix f where f is continuous on [a, b]
let M where |f(x)| <= M for all x in [a, b]
exists M
```

The point is to fix the order of quantifiers early: the `let`, `fix` and `exists` lines already say "for every such $f$ there is an $M$", while everything else can stay in plain words. Turning a draft into real Telescope means making each line precise, after which the comment is dropped:

```text
def Bounded(f : R -> R, a : R, b : R) {
  let M : R
  { let fix x : R where a <= x <= b; |f(x)| <= M }
  exists M
}
```

## 10. Examples

Concepts are named with `def`; theorems are written as top-level code (5.4). Each example is its own file, with the definitions it uses in scope.

**Limit.** The inner block mentions the open $d$, so it is a context proposition on $d$ (5.1). $x$ is local to it, so one $d$ must work for every $x$ (3.4).

```text
def Limit(f : R -> R, a : R, L : R) {
  let fix e : R where e > 0
  let d : R where d > 0
  { let fix x : R where 0 < |x - a| < d; |f(x) - L| < e }
  exists d
}
```

$$
\forall e > 0.\ \exists d > 0.\ \forall x.\ (0 < |x - a| < d \to |f(x) - L| < e)
$$

**Induction.** $P$ ranges over properties of $N$. The inner block is a context proposition on $P$, and becomes background when $P$ is fixed. Induction stays a definition: for arbitrary $N$, $z$ and $S$ it is a property they may or may not have, not a theorem.

```text
def Induction(N : Type, z : N, S : N -> N) {
  let fix P : N -> Prop where
    P(z),
    { let fix k : N where P(k); P(S(k)) }
  let fix n : N
  P(n)
}
```

$$
\forall P.\ P(z) \to (\forall k.\ P(k) \to P(S(k))) \to \forall n.\ P(n)
$$

**Cantor's theorem.** A theorem as top-level code, using a definition with implicit arguments (7.3). In Surjective, a is introduced after $b$, so it may depend on $b$.

```text
def Surjective[A : Type, B : Type](f : A -> B) {
  let fix b : B
  let a : A where f(a) = b
  exists a
}

let fix A : Type
let f : A -> Set(A) where Surjective(f)
not exists f
```

$$
\forall A.\ \neg\exists f : A \to \mathrm{Set}(A).\ \forall S.\ \exists a.\ f(a) = S
$$

**Continuity and uniform continuity.** The two definitions use the same statements; only the order of introductions differs (3.4). In Continuous, $x$ is fixed before $d$ is introduced, so $d$ may depend on $x$. In UniformlyContinuous, $d$ is introduced first and $x$ is local to the inner block, so one $d$ must work for every $x$.

```text
def Continuous(f : R -> R) {
  let fix x : R
  let fix e : R where e > 0
  let d : R where d > 0
  { let fix y : R where |x - y| < d; |f(x) - f(y)| < e }
  exists d
}

def UniformlyContinuous(f : R -> R) {
  let fix e : R where e > 0
  let d : R where d > 0
  { let fix x, y : R where |x - y| < d; |f(x) - f(y)| < e }
  exists d
}
```

$$
\forall x.\ \forall e > 0.\ \exists d > 0.\ \forall y.\ (|x - y| < d \to |f(x) - f(y)| < e)
$$

$$
\forall e > 0.\ \exists d > 0.\ \forall x, y.\ (|x - y| < d \to |f(x) - f(y)| < e)
$$

## 11. Connection with Lean and programming languages

Every definition, and the top-level block of every file, compiles deterministically to Lean: definitions to `def`, the top-level block to `theorem … : …`. Lean is based on type theory, and this is the only section where that background matters. Derived forms are expanded before translation. The Python column is an analogy, not a translation.

| Telescope | Lean | Python analogy |
| --- | --- | --- |
| `let x : A` | Binder `(x : A)` | Typed name `x: A` |
| Context proposition $P(x)$ | `P x`, with `P : A → Prop` | Boolean expression |
| Range of $x$ | Subtype `{x : A // P x}` | `[x for x in A if P(x)]` |
| `fix x` | `∀ x, P x → …` | Function parameter |
| Asserted proposition $\varphi$ | `φ`, proved in its context | `assert φ` |
| `exists x` | `∃ x, P x ∧ …` | `any(P(x) for x in A)` |
| `not exists x` | `¬ ∃ x, P x ∧ …` | `not any(…)` |
| `unique x` | `∃! x, …` | Exactly one match |
| Several assertions | `… ∧ …` | Several asserts |
| `A <=> B` | `A ↔ B` | `A == B` on booleans |
| Executed block `{ … }` | Parenthesised subformula | `(lambda: …)()` |
| `def Name(…) { … }` | `def Name … : Prop := …` | `def name(…) -> bool` |
| `def f(…) -> T { return t }` | `def f … : T := t` | `def f(…) -> T: return t` |
| `def F[X : Type](…)` | Implicit binder `{X : Type}` | Generic `def f[X](…)` |
| `where` on a parameter | Hypothesis argument `(h : C)` | Precondition |
| `lambda x: t` | `fun x => t` | `lambda x: t` |
| `(m : N) -> B(m)` | `(m : ℕ) → B m` | None |
| `Set(A)`, `x ∈ S` | `Set A`, `x ∈ S` | `set`, `in` |
| `Set[x : A](φ)` | `{x : A \| φ}` | `{x for x in A if φ}` |
| `sum[i in 1..m](t)` | `∑ i ∈ Finset.Icc 1 m, t` | `sum(t for i in range(1, m + 1))` |
| `inf[x in S](t)` | `⨅ x ∈ S, t` | `min(t for x in S)` |
| `# pseudo telescope` | Not compiled | Pseudocode |
| Top-level block | `theorem … : …` | Module-level code |

For example, the build-up in 3.3 becomes:

```text
(∃ x, P x) ∧ (∃ x, P x ∧ Q x) ∧ (∀ x, P x → Q x → R x)
```

**Contexts as dependent functions.** A context $\Gamma$ compiles to a sequence of Lean binders, one per variable and one per context proposition: `(x₁ : A₁) (h₁ : P₁ x₁) (x₂ : A₂) …`. Type theory calls such a sequence, where each type may mention the variables before it, a *telescope*, which gives the language its name. An assertion $\Gamma \vdash \varphi$ becomes `∀ (x₁ : A₁) (h₁ : P₁ x₁) …, φ`, and a proof of it is a dependent function from the whole context to a proof of $\varphi$.

**Design choices.** In type theory a variable's type is part of its declaration, which is why codomains stay on the `let` (2.1). Lean silently defaults numerals to $\mathbb{N}$ when a type is missing, which is why Telescope rejects undetermined types instead of guessing.

**Proof obligations.** Each assertion becomes a proof obligation, and so does each parameter proposition at each use (5.2). A later proof layer will discharge them, procedurally or with AI help, checked by Lean's kernel. Quantifier structure always comes from the structure of the block (sections 1.1 and 3), never from AI, so a translated block means exactly what was written.

## Appendix

### $A$. Keyword reference

| Keyword | Kind | Meaning |
| --- | --- | --- |
| `let x : A` | Introduction | $x$ takes values in $A$ (2.1) |
| `fix x` | Fix | $x$ is now arbitrary but fixed; its context propositions become background (2.3) |
| `exists x` | Range assertion | $\exists$: the range of $x$ is not empty (3.2) |
| `not exists x` | Range assertion | $\lnot\exists$: the range of $x$ is empty |
| `unique x` | Range assertion | $\exists!$: the range of $x$ has one element |
| `;` | Separator | Ends a statement, like a line break |
| `def Name(…) { … }` | Definition | Names what a block asserts (5.2) |
| `def f(…) -> T { return t }` | Value definition | Names a term of type $T$ (7.1) |
| `def() { … }()`, `{ … }` | Executed block | A new layer of context used as one statement (5.3) |
| `[X : Type]` after a name | Implicit parameters | Inferred at use (7.3) |
| `lambda x: t` | Function term | The function sending $x$ to $t$ (7.1) |
| `B[x in S](body)` | Binder | sum, prod, inf, sup, Set (section 8) |
| `S where C` | Derived form | Attaches context propositions $C$ to $S$ (section 6) |
| `let fix x : A` | Derived form | Introduces $x$ and fixes it at once |
| `not`, `and`, `or`, `=>`, `<=>` | Connectives | $\lnot$, $\land$, $\lor$, $\to$, $\leftrightarrow$, tightest first |
| `Prop`, `Type`, `Set(A)`, `Finset(A)` | Types | Truth values, types, sets, finite sets |

### $B$. Revisions

**0.1.2** (2026-11-24), changes from 0.1.1:

- The spec is split into a core (sections 1 to 4) and advanced features (sections 5 to 8), followed by pseudocode, examples and the Lean connection.
- A block is described as $\Gamma \vdash \varphi$. Statements are named by side: introductions, context propositions and fixes build the context, and asserted propositions and range assertions are the assertions. Propositions are open, closed or ground. A terms table is added (1.1).
- The scope of a variable's values is renamed its range, a subset of its codomain. "Scope" now means name visibility only.
- The rules are stated where they apply (1.1, 2.1, 3.3, 3.4, 5.1) instead of as a numbered list.
- Zero-order statements are added (section 4): ground propositions, atoms as `Prop` variables, and bare range assertions for consistency.
- Definitions use braces: `def Name(params) { … }` replaces `def Name(params) := …`.
- A nested block is now an executed anonymous definition, `def() { … }()`, with the bare `{ … }` as shorthand.
- A named `def` sees only its parameters and earlier definitions, never file-scope variables.
- Value definitions `def f(…) -> T { return t }` and function terms `lambda x: t` are added. A definition without parameters may drop its parentheses.
- `Prop` is a type of truth values, and `Set(A)` is `A -> Prop`.
- Binders `sum`, `prod`, `inf`, `sup` and `Set` are added in the form `B[x in S](body)`. Bound variables are not introductions.
- `<=>`, chained comparisons, precedence and parentheses are specified.
- Parameters may carry `where` propositions, which become proof obligations at each use.
- Dependent function types, products, type abbreviations, sets as types, `Finset` and implicit parameters are added.
- Pseudocode, marked `# pseudo telescope` and never compiled, is added for rough drafts (section 9).
- The Lean table gains a Python column and rows for the new constructs, and the top-level block compiles to `theorem`.
- The examples are rewritten and trimmed, and a continuity versus uniform continuity example is added.

**0.1.1** (2026-11-21), changes from 0.1.0:

- `final` is renamed `fix`.
- `exists` and `not exists` no longer close a variable: they are range propositions, and the variable stays open after them. `unique` is added.
- The `final exists` and `final not exists` forms are removed.
- The `where` clause is restricted: it only follows let, fix or a range proposition, never introduces a variable, and its conditions are ordinary predicates.
- Variables are introduced only by `let`; fixing or counting a name that was never introduced is an error. `let fix` is added for introducing and fixing in one statement.
- A type can only be written on `let`, and may be left out when it is clear from use. An undetermined or ambiguous type makes a block invalid.
- Lines are now called statements, and a sequence of statements a block. Judgement lines are split into propositions and range propositions; context lines that narrow a variable are now called predicates.
- A block now asserts all of its judgements together, instead of compiling to a single chain of quantifiers.
- `jug` is renamed `def`. Statements outside any definition are top-level code and form the file's top-level block, which is where theorems are written. Top-level variables live in the file scope.

**0.1.0** (2026-11-06): initial version.
