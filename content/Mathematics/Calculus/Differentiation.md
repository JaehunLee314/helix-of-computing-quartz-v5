**Prerequisites:** [[Big-O Like Notations]]

## 미분가능성

실수 함수 $f$가 $a$에서 미분가능하다는 것은 다음 극한이 존재한다는 것이다.

$$
f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}
$$

이 정의는 little-o notation으로 다음과 같이 적을 수 있다.

**보조정리.** 실수 함수 $f$가 $a$에서 미분가능하다는 것은 적당한 $u$가 존재하여 다음이 성립하는 것과 동치이다. 이때 $u = f'(a)$이다.

$$
f(x) = f(a) + u(x-a) + \underset{x \to a}o(x - a)
$$

$f(a) + u(x - a)$를 $f$의 $a$에서의 일차근사(linear approximation)라고 한다.

_증명._ $e(x) = f(x) - f(a) - u(x - a)$라고 두면 $x \neq a$일 때 다음이 성립한다.

$$
\frac{f(x) - f(a)}{x-a} = u + \frac{e(x)}{x-a}
$$

[[Big-O Like Notations]]의 보조정리에 의해 $e(x) \in o_{x \to a}(x - a)$라는 것은 $e(x)/(x-a) \to 0$가 성립한다는 것이고 이는 $x \to a$일 때 좌변이 $u$로 수렴하는 것과 동치이다. $\blacksquare$

**따름정리.** $f$가 $a$에서 미분가능하면 다음이 성립한다.

$$
f(x) = f(a) + \underset{x \to a}o(1)
$$

다시 말해 $f$는 $a$에서 연속이다.

_증명._ 미분가능성의 성질에 의해 $f(x) = f(a) + f'(a)(x - a) + e(x)$, $e(x) \in o_{x \to a}(x - a)$ 라고 적을 수 있다. $x \to a$ 이면 $x - a \to 0$ 이고 $e(x) = \frac{e(x)}{x - a}(x - a) \to 0$ 이므로 $\lim_{x \to a} \big(f'(a)(x - a) + e(x)\big) = 0$ 이다. 따라서 $f'(a)(x - a) + e(x) \in o_{x \to a}(1)$ 이다. $\blacksquare$

**예시.** $|x|$는 $0$에서 연속이므로 $|x| = 0 + o_{x \to 0}(1)$ 이지만, $|x| = ux + o_{x \to 0}(x)$를 만족하는 $u$는 없다.

## 미분 법칙

이 절에서 $o(h)$는 $o_{h \to 0}(h)$를 뜻한다. 보조정리에 의해 $f$가 $x$에서 미분가능하다는 것은 다음과 같다.

$$
f(x+h) = f(x) + f'(x)h + o(h)
$$

**정리. 곱의 미분법** 
$u, v$가 $x$에서 미분가능하면 $(uv)'(x) = u(x)v'(x) + u'(x)v(x)$ 이다.

_증명._ $u(x+h) = u(x) + u'(x)h + e_1(h)$, $v(x+h) = v(x) + v'(x)h + e_2(h)$ 라고 하자. 두 식을 곱하면 다음과 같다.

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

**정리. 연쇄법칙** 
$f$가 $x$에서 미분가능하고 $g$가 $y = f(x)$에서 미분가능하면 $(g \circ f)'(x) = g'(y)f'(x)$ 이다.

_증명._ $k(h) = f(x+h) - f(x)$, $e(k) = g(y + k) - g(y) - g'(y)k$ 라고 하면 다음이 성립한다.

$$
g(f(x+h)) - g(f(x)) = g'(y)k(h) + e(k(h))
$$

$k \neq 0$ 이면 $\eta(k) = e(k)/k$, $\eta(0) = 0$ 으로 두자. 그러면 $e(k) = \eta(k)k$ 이고, $e(k) \in o_{k \to 0}(k)$ 이므로 $\eta$는 $0$에서 연속이다. 따라서 $h \neq 0$ 이면 다음이 성립한다.

$$
\frac{g(f(x+h)) - g(f(x))}{h} = \big(g'(y) + \eta(k(h))\big)\frac{k(h)}{h}
$$

$h \to 0$ 이면 $f$의 연속성에 의해 $k(h) \to 0$ 이므로 $\eta(k(h)) \to 0$ 이고, $k(h)/h \to f'(x)$ 이다. $\blacksquare$

$k(h) = 0$인 $h$가 있어도 $\eta(0) = 0$으로 두었으므로 따로 처리할 필요가 없다.

**예시.** $(x + h)^2 = x^2 + 2xh + h^2$ 이고 $h^2 \in o(h)$ 이므로 $(x^2)' = 2x$ 이다.
