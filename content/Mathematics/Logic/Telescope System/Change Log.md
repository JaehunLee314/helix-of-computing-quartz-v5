Changes to the Telescope spec, newest first. Each entry lists the changes from the version before it.

## 0.2.0 (2026-11-25)

0.2.0 is a rewrite. The spec is now short (about six pages), builds up in complexity, and shows technical detail through examples rather than rules. Changes from 0.1.2:

**Structure and purpose**

- The spec states two purposes: stating existing mathematics clearly, and readable formalization, where Telescope is to Lean what Python is to C.
- New layout: 1 A first statement, 2 Order is meaning, 3 The pieces of a block, 4 Definitions, 5 Sums, sets and other aggregates, 6 Types and numbers, 7 Examples, 8 Under the hood, 9 Building a full system, 10 Cheat sheet. The terms tables and the separate pseudocode, zero-order and Lean sections of 0.1.2 are folded into these.
- The flow of a block is introduce, refine, assert. A line about an unfixed variable is a condition; a line starting with `exists`, `not exists` or `unique`, or whose variables are all fixed, is an assertion. Line order is quantifier order.

**Introducing and refining**

- `let x in S` is added as the readable form of `let x : T`; with `S : Set(A)` it means `let x : A`, then `x in S`.
- `where` attaches conditions to the line it ends, as in `let fix e in R where e > 0` or `exists d where …`.
- `let D = t` names a term without introducing a new variable.
- Every term must be defined where it is used (`1/x` needs `x != 0` above it).

**Asserting and formulas**

- Within one `exists`, variables fixed before the witness are given and those introduced after it are quantified inside, so one witness must serve all of them.
- A `fix x` after `exists x` keeps every condition written above it; to quantify afresh, open a new block.
- `<=>` chains pair by pair, so `A <=> B <=> C` makes all three equivalent. Chained comparisons such as `0 < e < 1` expand pair by pair, as in Python.
- A block in braces is itself a proposition and may be a condition, a hypothesis after `where`, or an operand of a connective.
- `exists consistency` asks whether some truth assignment of the unfixed `Prop` atoms meets every proposition so far. It replaces the bare `exists`, `not exists` and `unique` of 0.1.2 and seals nothing.

**Definitions**

- A definition without `return` is a proposition: it holds when the arguments meet the body's conditions and every assertion in the body holds, so `Prime(1)` is false.
- A definition with `return` gives a value and a proposition. `return y` of a variable requires `unique y` to be provable.
- Parameters are variables: a parameter receives the argument with all its values, and the caller's variable never changes. A condition on a parameter or a generic, or a `fix` followed by a condition in the body, is a precondition that each call proves. Without `fix`, the condition makes the function partial.
- Generics are declared in angle brackets, `def f<X : Type>(…)`, and are usually inferred; `f<X>(…)` writes them out. They replace 0.1.2's implicit parameters.
- Terms: `lambda x: t`, a lambda with conditions (`lambda h where h != 0: …`), which is partial, `lambda e, d: t` as shorthand for nested lambdas, and `if c then a else b`. Passing a partial function is allowed when every use stays inside its domain.
- A file's top-level lines are its theorem; several theorems in one file are each wrapped in braces.

**Aggregates**

- Square brackets open a fresh context for an aggregate: `B[x in S where C](t)` means introduce, refine, then apply B to every value t takes. The variable is bound and takes no part in the quantifier order.
- `Set[x in S where C](t)` is the one set-builder form. Aggregates include `range`, `Set`, `exists`, `unique`, `card`, `sum`, `prod`, `inf` and `sup`. `sum` and `prod` count once per point of the context.
- `a...b` is the integers from a to b, replacing `a..b`.

**Types and numbers**

- `Bool` is added, and a proposition becomes a `Bool` wherever one is expected. Pairs are written `(a, b)`, with components `z.1` and `z.2`.
- `A^n` is `Fin(n) -> A`, indexed from 0, so tuple entries are applications and tuples are built with `lambda`. A matrix is a tuple of rows. `R^n` carries the Euclidean norm.
- Numbers form the tower $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$ (written N, Z, Q, R, C), with reserved names and automatic upward casts. A `Finset` is cast to a `Set`, and an element of a set used as a type is cast to the larger type. Types are never guessed.
- Casting is as in Lean: arithmetic happens in the largest number type among its parts, and where nothing determines it the type is written, as in `(card(S) : Q) / card(W)`.
- Arithmetic: `mod`, `|x|` and `divides(a, b)` are added, with precedence `^`, then `*`, `/`, `mod`, then `+`, `-`. `/` is not defined on N or Z, and `a - b` on N needs `b <= a`. `ceil` and `floor` take R and give Z. `card(S)` needs `Finite(S)`.
- Names not defined in the file refer to Lean's mathlib and only need to look like mathlib's names.

**Examples**

- New examples include drafts turned into statements, Cantor, Bolzano–Weierstrass, uniqueness up to order, the fundamental theorem of algebra, Zorn's lemma, a derivative with the mean value theorem, a symmetric-matrix eigenvalue, graph connectedness, probability (two dice, Markov's inequality, the strong law of large numbers) and the VC dimension.
- Probability is written with events as sets, `Prob(P, S)` and `Integral(P, X)`. As an extension, `Prob[x ~ P](φ)`, `E[x ~ P](t)` and `P^m` are available.

**Theory and Lean**

- Under the hood: a block says $\Gamma \vdash \varphi$. Each variable is a map $\Omega \to A$ from the combinations of values that $\Gamma$ generates, $\Gamma$ is a telescope in de Bruijn's sense, and $\Omega$ is an iterated $\Sigma$-type. A table relates each construct to type theory and to Lean, and a background note gives references.
- Translation runs both ways, from Telescope to Lean and back, and an LLM may help in either direction without changing the meaning.

**Scope**

- Proofs are out of scope for 0.2.0; `P by { … }` remains a sketch.
- Building a full system lists what a full implementation must still decide: grammar, types, definedness, definitions, translation details, proofs, filters, binders with parameters, structures and a prelude.

## 0.1.2 (2026-11-24)

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

## 0.1.1 (2026-11-21)

- `final` is renamed `fix`.
- `exists` and `not exists` no longer close a variable: they are range propositions, and the variable stays open after them. `unique` is added.
- The `final exists` and `final not exists` forms are removed.
- The `where` clause is restricted: it only follows let, fix or a range proposition, never introduces a variable, and its conditions are ordinary predicates.
- Variables are introduced only by `let`; fixing or counting a name that was never introduced is an error. `let fix` is added for introducing and fixing in one statement.
- A type can only be written on `let`, and may be left out when it is clear from use. An undetermined or ambiguous type makes a block invalid.
- Lines are now called statements, and a sequence of statements a block. Judgement lines are split into propositions and range propositions; context lines that narrow a variable are now called predicates.
- A block now asserts all of its judgements together, instead of compiling to a single chain of quantifiers.
- `jug` is renamed `def`. Statements outside any definition are top-level code and form the file's top-level block, which is where theorems are written. Top-level variables live in the file scope.

## 0.1.0 (2026-11-06)

- Initial version.
