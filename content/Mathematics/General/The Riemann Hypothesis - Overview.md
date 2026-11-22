**Prerequisites:** [[Big-O Like Notations]], [[Impulse Response와 Convolution]]

The Riemann Hypothesis (RH) is a statement about how evenly the prime numbers are spread out. This guide explains what it says and why it is a statement about the zeros of one function, $\zeta$. Throughout, $\log$ means the natural logarithm.

## 1. Prime counter approximation

**Counting primes.** $\pi(x)$ is the number of primes up to $x$. For example, $\pi(10) = 4$, counting 2, 3, 5 and 7. Here $\pi$ names a function, not the constant $3.14\ldots$.

**The smooth model.** Near a large number $t$, roughly one integer in every $\log t$ is prime, so the density of primes near $t$ is about $1/\log t$. Adding up that density from 2 to $x$ gives the logarithmic integral $\operatorname{Li}(x)$, read "L-I of x":

$$
\operatorname{Li}(x) = \int_2^x \frac{dt}{\log t}
$$

The gap between the true count and the model is the error term:

$$
e(x) = \pi(x) - \operatorname{Li}(x)
$$

For example, $\pi(10^9) = 50{,}847{,}534$ while $\operatorname{Li}(10^9) \approx 50{,}849{,}235$, so $|e(10^9)| \approx 1{,}700$.

**Theorem (Prime Number Theorem, PNT; Hadamard and de la Vallée Poussin, 1896).** For large $x$, $\pi(x)$ behaves like $x/\log x$:

$$
\lim_{x\to\infty}\frac{\pi(x)}{x/\log x} = 1
$$

This is equivalent to saying the error is negligible compared to the count:

$$
e(x) = o\left(\frac{x}{\log x}\right)
$$

The two forms are equivalent because $\operatorname{Li}(x)/(x/\log x) \to 1$: by L'Hôpital. The PNT fixes only the leading order of $\pi(x)$. RH concerns the next order: the exact growth rate of $e(x)$.

## 2. The error term analysis

To understand $e(x)$, we pass from the primes to a function of a complex variable, $\zeta(s)$, and back. Sections 2.1 to 2.5 each explain one arrow of this route:

$$
\begin{aligned} \sum_{n\ge1} \frac{1}{n^{s}} &\xrightarrow{\ \text{Euler product}\ } \prod_{p\ \text{prime}} \frac{1}{1-p^{-s}} \xrightarrow{\ \text{log-derivative}\ } \sum_{n\ge1}\frac{\Lambda(n)}{n^{s}} \xrightarrow{\ \text{running sum}\ } \mathcal{L}{\psi(e^u)}(s) = -\frac{\zeta'(s)}{s,\zeta(s)} \\ &\xrightarrow{\ \text{analytic continuation of } \zeta,\ \text{inverse Laplace}\ } \psi(x) = x - \sum_{\rho\ \text{nontrivial zeros}} \frac{x^\rho}{\rho} - \cdots \xrightarrow{\ \text{undo the weights}\ } \pi(x) = \operatorname{Li}(x) + e(x) \end{aligned}
$$

### 2.1 The zeta function and the Euler product

The Riemann zeta function adds up $1/n^s$ over all positive integers $n$, where $s$ is a complex number. The sum converges when $\operatorname{Re} s$, the real part of $s$, is greater than 1:

$$
\zeta(s) = \sum_{n\ge1}\frac{1}{n^s} = 1 + \frac{1}{2^s} + \frac{1}{3^s} + \cdots
$$

**Theorem (Euler product).** For $\operatorname{Re} s > 1$, $\zeta$ is also a product over the primes alone:

$$
\zeta(s) = \prod_{p\ \text{prime}}\frac{1}{1-p^{-s}} \qquad (\operatorname{Re} s > 1)
$$

Proof sketch: expand each factor as $1 + p^{-s} + p^{-2s} + \cdots$ and multiply out; every integer appears exactly once, because it factors into primes in exactly one way. This is the bridge from all integers to the primes.

### 2.2 The von Mangoldt function

The von Mangoldt function $\Lambda$ marks the primes and their powers, giving each the weight $\log p$:

$$
\Lambda(n) = \begin{cases} \log p & \text{if } n = p^k \text{ for a prime } p \text{ and some } k \ge 1 \\ 0 & \text{otherwise} \end{cases}
$$

For example $\Lambda(7) = \log 7$, $\Lambda(8) = \Lambda(2^3) = \log 2$, and $\Lambda(6) = 0$, since $6 = 2\cdot 3$ is not a prime power.

**Theorem.** For $\operatorname{Re} s > 1$, the coefficients of $-\zeta'/\zeta$ are exactly the values $\Lambda(n)$:

$$
\log\zeta(s) = \sum_{p\ \text{prime}}\sum_{k\ge1}\frac{p^{-ks}}{k} \quad\Longrightarrow\quad -\frac{\zeta'(s)}{\zeta(s)} = \sum_{p\ \text{prime}}\sum_{k\ge1}\log p,(p^k)^{-s} = \sum_{n\ge1}\frac{\Lambda(n)}{n^s} \qquad (\operatorname{Re} s > 1)
$$

Proof sketch: take the log of the Euler product and expand each $-\log(1 - p^{-s})$ with $-\log(1 - y) = y + y^2/2 + \cdots$; this gives the first identity. Differentiating in $s$ (written $\zeta'$) brings down a factor $k\log p$ from each term, which cancels the $1/k$ and leaves the weights $\Lambda(n)$.

The left side is built from all integers, the right side only from primes. This identity carries whatever is known about $\zeta$ over to the primes.

### 2.3 The running total ψ and the Laplace view

**ψ is a weighted sum of primes.** The running total of $\Lambda$ is the Chebyshev function $\psi$. It counts each prime with weight $\log p$ instead of 1, once for each of its powers $p, p^2, p^3, \ldots$ that fit below $x$:

$$
\psi(x) = \sum_{n \le x}\Lambda(n) = \sum_{p \le x,\ p\ \text{prime}}\log p \cdot \left\lfloor \frac{\log x}{\log p} \right\rfloor
$$

The weight $\log p$ is not a choice: it is exactly what the log-derivative of $\zeta$ produces (section 2.2). In these terms the PNT reads as $\psi(x)/x \to 1$.

Now measure $x$ on a log scale, $u = \log x$. Then $n^{-s} = e^{-su}$, so sums such as $\sum \Lambda(n), n^{-s}$ become Laplace transforms. The Laplace transform turns a signal $f(u)$ into a function of $s$: $\mathcal{L}{f}(s) = \int f(u), e^{-su}, du$. The basic pair is $\mathcal{L}{e^{au}}(s) = 1/(s - a)$: an exponential term in the signal corresponds to a simple pole in the transform. Conversely, inverting a transform recovers one term $c, e^{au}$ for each pole $a$, where $c$ is the residue there, so $\operatorname{Re} a$ is that term's growth rate.

**Theorem.** For $\operatorname{Re} s > 1$, the transform of $\psi(e^u)$ is $\zeta$'s log-derivative divided by $s$; the factor $1/s$ appears because $\psi$ is a running sum:

$$
\mathcal{L}{\psi(e^u)}(s) = -\frac{1}{s},\frac{\zeta'(s)}{\zeta(s)}
$$

Near a zero $\rho$, $\zeta(s) \approx c,(s - \rho)$, so $-\zeta'/\zeta \approx -1/(s - \rho)$: a zero of $\zeta$ is a simple pole of $-\zeta'/\zeta$. Inverting the transform turns each pole into a term of $\psi$, so **every zero of ζ becomes a term in ψ**.

### 2.4 The zeros of ζ and the explicit formula

Inverting the transform needs $\zeta$ to the left of $\operatorname{Re} s = 1$, where its series diverges. $\zeta$ extends uniquely to all complex $s \neq 1$ (analytic continuation), with a simple pole at $s = 1$. It also satisfies a functional equation relating $\zeta(s)$ to $\zeta(1 - s)$. Its zeros come in two kinds:

- **Trivial zeros** at $-2, -4, -6, \ldots$, which are well understood.
- **Nontrivial zeros** $\rho$ (rho), all lying in the strip $0 < \operatorname{Re} s < 1$, placed symmetrically about the line $\operatorname{Re} s = \tfrac12$: by the functional equation, if $\rho$ is a zero, so are $1 - \rho$ and its conjugate $\bar\rho$.

**Theorem (explicit formula, von Mangoldt, 1895).** Inverting the transform and summing the residues gives $\psi$ exactly, for $x > 1$ not a prime power. The pole at $s = 1$ gives the main term $x$, the pole at $s = 0$ and the trivial zeros give the constant and the last term, and there is one wave per nontrivial zero $\rho$. Together, everything after the main term is the error $E(x)$:

$$
\psi(x) = x ;\underbrace{-\sum_{\rho\ \text{nontrivial zeros}} \frac{x^\rho}{\rho} - \log 2\pi - \tfrac12\log!\left(1 - x^{-2}\right)}_{E(x)}
$$

Each wave has size $|x^\rho| = x^{\operatorname{Re}\rho}$: **the real part of a zero decides how big its wave grows**, while the imaginary part only makes it oscillate.

### 2.5 Back to π

Let $\theta(x) = \sum_{p \le x,\ p\ \text{prime}} \log p$ count primes only. Then $\pi(x) = \int_2^x d\theta(t)/\log t$ exactly, since each jump of size $\log p$ at a prime $p$ is divided by $\log p$. Replacing $\theta$ by $\psi$ adds the prime powers $p^k$ with $k \ge 2$, which changes the result by only $O(\sqrt{x})$. With $\psi(x) = x + E(x)$ from above, the main term $x$ becomes $\operatorname{Li}(x)$ and $E$ becomes the error term exactly:

$$
\begin{aligned} \pi(x) &= \int_2^x \frac{d\psi(t)}{\log t} + O(\sqrt{x}) \\ e(x) &= \frac{E(x)}{\log x} + \int_2^x \frac{E(t)}{t,\log^2 t},dt + O(\sqrt{x}) \end{aligned}
$$

This formula is exact in principle but not closed-form, because the zeros are known only numerically. Its use is to turn the question "how big is $e(x)$?" into "where are the zeros?".

## 3. The Riemann Hypothesis

**Conjecture (Riemann Hypothesis, 1859).** Every nontrivial zero of $\zeta$ lies exactly on the middle line of the strip:

$$
\zeta(\rho) = 0 \ \text{ and } \ 0 < \operatorname{Re}\rho < 1 \quad\Longrightarrow\quad \operatorname{Re}\rho = \tfrac12
$$

**From the zeros to the error.** By the explicit formula, $E(x)$ is a sum of waves $x^\rho/\rho$, one per nontrivial zero, and each has amplitude $x^{\operatorname{Re}\rho}/|\rho|$. So the error is driven by the zeros furthest to the right: if $\Theta$ is the largest real part of a zero, $E(x)$ grows like $x^\Theta$, up to logarithmic factors. Under RH, $\Theta = \tfrac12$ and every wave has amplitude $\sqrt{x}/|\rho|$. There are about $(T/2\pi)\log T$ zeros up to height $T$, and summing the waves gives $E(x) = O(\sqrt{x},\log^2 x)$. Section 2.5 then gives:

$$
e(x) = O(\sqrt{x},\log x)
$$

$O(\cdot)$ means "at most a constant times": there is one constant $K$ with $|e(x)| \le K\sqrt{x},\log x$ for every $x \ge 2$.

**From the error back to the zeros.** The Laplace view also runs in reverse. A signal that grows no faster than $e^{\theta u}$ has a transform with no poles for $\operatorname{Re} s > \theta$, since a pole at $a$ would put a term growing like $e^{(\operatorname{Re} a)u}$ into the signal. Suppose $e(x) = O(x^{1/2+\varepsilon})$ for every $\varepsilon > 0$. Then $E(x) = O(x^{1/2+\varepsilon})$ as well, so its transform, $-\zeta'(s)/(s,\zeta(s)) - 1/(s - 1)$, has no poles with $\operatorname{Re} s > \tfrac12$. The zeros of $\zeta$ are exactly those poles, so $\zeta$ has no zeros with $\operatorname{Re} s > \tfrac12$, and by the symmetry $\rho \leftrightarrow 1 - \rho$ none with $\operatorname{Re} s < \tfrac12$. So the bound is **equivalent** to RH (von Koch, 1901). More generally, the growth exponent of the error and the largest real part of a zero are the same number:

$$
\sup_{\rho\ \text{nontrivial zeros}} \operatorname{Re}\rho \le \Theta \quad\iff\quad E(x) = O!\left(x^{\Theta+\varepsilon}\right) \text{ for every } \varepsilon > 0
$$

Since infinitely many zeros lie on the line, no bound of order $x^{1/2-\delta}$ with $\delta > 0$ is possible: under RH the error is as small as it can be.

|Statement|Size of the error $e(x)$|What it needs from the zeros|
|---|---|---|
|PNT (proved 1896)|$o(x/\log x)$|none on the line $\operatorname{Re} s = 1$|
|RH|$O(\sqrt{x},\log x)$|all on the line $\operatorname{Re} s = \tfrac12$|

Between the two rows lies every case with a zero off the line. A single zero with real part $\beta > \tfrac12$ would make $|e(x)|$ exceed $x^{\beta-\varepsilon}$ infinitely often, for every $\varepsilon > 0$, far above $\sqrt{x},\log x$.

## Footnote
- RH may have been proven as of 20 Nov, 2026. Impressive.