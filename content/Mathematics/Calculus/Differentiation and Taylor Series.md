**Prerequisites:** [[Big-O Like Notations]]

## 미분가능성

실수 함수 $f$가 $a$에서 미분가능하다는 것은 다음 극한이 존재한다는 것이다.

$$
f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}
$$

이 정의는 little-o notation으로 다음과 같이 적을 수 있다.

**보조정리.** 실수 함수 $f$가 $a$에서 미분가능하다는 것은 적당한 $u$가 존재하여 다음이 성립하는 것과 동치이다. 이때 $u = f'(a)$이다.

$$
f(x) = f(a) + u(x-a) + \underset{x \to a}o(x - a)
$$

$f(a) + u(x - a)$를 $f$의 $a$에서의 일차근사(linear approximation)라고 한다.

_증명._ $e(x) = f(x) - f(a) - u(x - a)$라고 두면 $x \neq a$일 때 다음이 성립한다.

$$
\frac{f(x) - f(a)}{x-a} = u + \frac{e(x)}{x-a}
$$

[[Big-O Like Notations]]의 보조정리에 의해 $e(x) \in o_{x \to a}(x - a)$라는 것은 $e(x)/(x-a) \to 0$가 성립한다는 것이고 이는 $x \to a$일 때 좌변이 $u$로 수렴하는 것과 동치이다. $\blacksquare$

**따름정리.** $f$가 $a$에서 미분가능하면 다음이 성립한다.

$$
f(x) = f(a) + \underset{x \to a}o(1)
$$

다시 말해 $f$는 $a$에서 연속이다.

_증명._ 미분가능성의 성질에 의해 $f(x) = f(a) + f'(a)(x - a) + e(x)$, $e(x) \in o_{x \to a}(x - a)$ 라고 적을 수 있다. $x \to a$ 이면 $x - a \to 0$ 이고 $e(x) = \frac{e(x)}{x - a}(x - a) \to 0$ 이므로 $\lim_{x \to a} \big(f'(a)(x - a) + e(x)\big) = 0$ 이다. 따라서 $f'(a)(x - a) + e(x) \in o_{x \to a}(1)$ 이다. $\blacksquare$

**예시.** $|x|$는 $0$에서 연속이므로 $|x| = 0 + o_{x \to 0}(1)$ 이지만, $|x| = ux + o_{x \to 0}(x)$를 만족하는 $u$는 없다.

## 미분 법칙

이 절에서 $o(h)$는 $o_{h \to 0}(h)$를 뜻한다. 보조정리에 의해 $f$가 $x$에서 미분가능하다는 것은 다음과 같다.

$$
f(x+h) = f(x) + f'(x)h + o(h)
$$

**정리. 곱의 미분법** $u, v$가 $x$에서 미분가능하면 $(uv)'(x) = u(x)v'(x) + u'(x)v(x)$ 이다.

_증명._ $u(x+h) = u(x) + u'(x)h + e_1(h)$, $v(x+h) = v(x) + v'(x)h + e_2(h)$ 라고 하자. 두 식을 곱하면 다음과 같다.

$$
u(x+h)v(x+h) = u(x)v(x) + \big(u(x)v'(x) + u'(x)v(x)\big)h + r(h)
$$

$$
r(h) = u'(x)v'(x)h^2 + \big(u(x) + u'(x)h\big)e_2(h) + \big(v(x) + v'(x)h\big)e_1(h) + e_1(h)e_2(h)
$$

$h \neq 0$ 이면 다음이 성립한다.

$$
\frac{r(h)}{h} = u'(x)v'(x)h + \big(u(x) + u'(x)h\big)\frac{e_2(h)}{h} + \big(v(x) + v'(x)h\big)\frac{e_1(h)}{h} + e_1(h)\frac{e_2(h)}{h}
$$

$h \to 0$ 이면 $e_1(h)/h \to 0$, $e_2(h)/h \to 0$, $e_1(h) \to 0$ 이므로 우변은 $0$으로 수렴한다. 따라서 $r \in o(h)$ 이다. $\blacksquare$

**정리. 연쇄법칙** $f$가 $x$에서 미분가능하고 $g$가 $y = f(x)$에서 미분가능하면 $(g \circ f)'(x) = g'(y)f'(x)$ 이다.

_증명._ $k(h) = f(x+h) - f(x)$, $e(k) = g(y + k) - g(y) - g'(y)k$ 라고 하면 다음이 성립한다.

$$
g(f(x+h)) - g(f(x)) = g'(y)k(h) + e(k(h))
$$

$k \neq 0$ 이면 $\eta(k) = e(k)/k$, $\eta(0) = 0$ 으로 두자. 그러면 $e(k) = \eta(k)k$ 이고, $e(k) \in o_{k \to 0}(k)$ 이므로 $\eta$는 $0$에서 연속이다. 따라서 $h \neq 0$ 이면 다음이 성립한다.

$$
\frac{g(f(x+h)) - g(f(x))}{h} = \big(g'(y) + \eta(k(h))\big)\frac{k(h)}{h}
$$

$h \to 0$ 이면 $f$의 연속성에 의해 $k(h) \to 0$ 이므로 $\eta(k(h)) \to 0$ 이고, $k(h)/h \to f'(x)$ 이다. $\blacksquare$

**예시.** $(x + h)^2 = x^2 + 2xh + h^2$ 이고 $h^2 \in o(h)$ 이므로 $(x^2)' = 2x$ 이다.

## 다변수함수의 미분가능성

$x, a \in \mathbb{R}^n$에 대해 [[Big-O Like Notations]]의 근방을 다음과 같이 바꾸어 같은 표기법을 사용한다.

$$
x \in N_\delta(a) \iff 0 < \lVert x - a \rVert < \delta
$$

**정의. 다변수함수의 미분가능성** $f: \mathbb{R}^n \to \mathbb{R}$이 $a$에서 미분가능하다는 것은 어떤 벡터 $v \in \mathbb{R}^n$가 존재하여 다음이 성립한다는 것이다.

$$
f(x) = f(a) + v^T (x-a) + \underset{x \to a}o(\lVert x-a \rVert)
$$

**보조정리.** 위의 $v$는 $f$의 $a$에서의 그래디언트 $\nabla f(a)$와 같다.

**예시.** $f(x) = \lVert x \rVert^2$ 이면 $f(a + h) = f(a) + 2a^T h + \lVert h \rVert^2$ 이고 $\lVert h \rVert^2 \in o_{h \to 0}(\lVert h \rVert)$ 이므로 $\nabla f(a) = 2a$ 이다.

## 테일러 정리

여러 번 미분가능한 함수는 더 높은 차수의 다항식으로 근사할 수 있고, 이때 오차항은 더 빨리 감소한다.

**정의. 테일러 다항식** 실수 함수 $f$가 $a$에서 $N$번 미분가능하다고 하자. $N$차 테일러 다항식은 다음과 같다.

$$
T_N(x) = \sum_{n = 0}^N \frac{f^{(n)}(a)}{n!} (x-a)^n
$$

나머지항을 $R_N = f - T_N$이라고 한다. $N \to \infty$로 보낸 급수를 테일러 급수라고 한다.

**정리. 테일러 정리** $f$가 $a$에서 $N$번 미분가능하면 다음이 성립한다.

$$
f(x) = \sum_{n = 0}^N \frac{f^{(n)}(a)}{n!} (x-a)^n + \underset{x \to a}o((x-a)^N)
$$

**예시.**

- $e^x = 1 + x + \frac{x^2}{2} + o_{x \to 0}(x^2)$
- $\sin x = x + o_{x \to 0}(x^2)$
- $\cos x = 1 - \frac{x^2}{2} + o_{x \to 0}(x^3)$

## 다변수함수의 테일러 정리

이차까지만 살펴보자. $f: \mathbb{R}^n \to \mathbb{R}$이 $a$의 근방에서 $C^2$라고 하고, $\nabla^2 f(a)$를 $f$의 헤세 행렬이라고 하자.

**정리.** 다음이 성립한다.

$$
f(x) = f(a) + \nabla f(a)^{T}(x-a) + \frac{1}{2!}(x-a)^{T}\nabla^2 f(a)(x-a) + \underset{x \to a}o(\lVert x - a \rVert^2)
$$

## 참고문헌
(1) Wikipedia, [Taylor series](https://en.wikipedia.org/wiki/Taylor_series)  
(2) Wikipedia, [Taylor's theorem](https://en.wikipedia.org/wiki/Taylor%27s_theorem)  
(3) Walter Rudin, Principles of Mathematical Analysis