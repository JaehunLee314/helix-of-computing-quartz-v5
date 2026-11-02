**Prerequisites:** [[Uniform Big-O Like Notations]], [[Partial Derivative and Multivariate Chain Rule]], [[Riemann Integration]]

$F(t) = \int_a^b f(x, t)dx$ 라고 하자. 언제 미분과 적분의 순서를 바꿀 수 있을까?

$$
\frac{d}{dt}\int_a^b f(x, t)dx = \int_a^b \frac{\partial f}{\partial t}(x, t)dx
$$

적분은 오차를 $x$에 대해 더하는 것이므로, 오차가 $x$와 무관하게 작아야 적분 후에도 작다. 즉 $t$에 대한 일차근사의 오차가 $x$에 대해 균등하면 된다.

## 적분 기호 아래에서의 미분

**정리.** 
$t$를 고정하자. $\frac{\partial f}{\partial t}(x, t)$가 $x$에 대해 $[a, b]$에서 적분가능하고 다음이 성립하면, $F$는 $t$에서 미분가능하고 $F'(t) = \int_a^b \frac{\partial f}{\partial t}(x, t)dx$ 이다.

$$
f(x, t + s) = f(x, t) + \frac{\partial f}{\partial t}(x, t)s + \underset{x \in [a, b], s \to 0}o (s)
$$

_증명._ 오차항을 $e(x, s)$라고 하면 다음이 성립한다.

$$
F(t + s) - F(t) - s\int_a^b \frac{\partial f}{\partial t}(x, t)dx = \int_a^b e(x, s)dx
$$

균등성에 의해 $0 < |s| < \delta$ 이면 $x$와 무관하게 $|e(x, s)| \leq \epsilon|s|$ 이므로, 우변의 절댓값은 $\epsilon|s|(b - a)$ 이하이다. 따라서 우변은 $o_{s \to 0}(s)$ 이다. $\blacksquare$

이는 [[Riemann Integration]]의 균등오차의 소거와 같은 논리이다.

**따름정리.** 
$f$와 $\frac{\partial f}{\partial t}$가 $[a, b] \times [c, d]$에서 연속이면 $t \in [c, d]$에서 다음이 성립한다.

$$
\frac{d}{dt}\int_a^b f(x, t)dx = \int_a^b \frac{\partial f}{\partial t}(x, t)dx
$$

_증명._ 평균값 정리에 의해 $t$와 $t + s$ 사이의 $\xi$가 존재하여 다음이 성립한다.

$$
f(x, t + s) - f(x, t) - \frac{\partial f}{\partial t}(x, t)s = \left(\frac{\partial f}{\partial t}(x, \xi) - \frac{\partial f}{\partial t}(x, t)\right)s
$$

[[Uniform Big-O Like Notations]]의 따름정리에 의해 괄호 안은 $o_{x \in [a, b], s \to 0}(1)$ 이다. $\blacksquare$

이 증명은 [[Riemann Integration]]에서 $C^1$이면 균등미분가능하다는 보조정리와 같다. 연속성이 닫힌 직사각형에서 균등성을 보장한다.

**예시.** $t \geq c > 0$ 에서 $f(x, t) = x^t$ 와 $\frac{\partial f}{\partial t}(x, t) = x^t \ln x$ 는 $[0, 1] \times [c, d]$에서 연속이다($x = 0$에서 $0$으로 둔다). 따라서 $\int_0^1 x^t dx = \frac{1}{t + 1}$ 을 미분하여 다음을 얻는다.

$$
\int_0^1 x^t \ln x dx = -\frac{1}{(t + 1)^2}
$$

**예시.** 균등하지 않으면 성립하지 않는다. $[0, 1]$에서 $t > 0$이면 $t < x < 2t$일 때 $f(x, t) = 1$, $t < 0$이면 $|t| < x < 2|t|$일 때 $f(x, t) = -1$, 나머지에서는 $0$이라고 하자. 각 $x$에서 $|t| < \frac{x}{2}$이면 $f(x, t) = 0$ 이므로 $\frac{\partial f}{\partial t}(x, 0) = 0$ 이고, 따라서 $\int_0^1 \frac{\partial f}{\partial t}(x, 0)dx = 0$ 이다. 그러나 $|t|$가 작으면 $F(t) = t$ 이므로 $F'(0) = 1$ 이다. 각 $x$에서 오차는 $o(s)$ 이지만, 폭이 $|t|$인 띠가 $0$ 쪽으로 움직이므로 균등하지 않다.

## 적분 구간이 변하는 경우

**정리. 라이프니츠 적분 법칙** 
$f$와 $\frac{\partial f}{\partial t}$가 연속이고 $a(t), b(t)$가 미분가능하면 다음이 성립한다.

$$
\frac{d}{dt}\int_{a(t)}^{b(t)} f(x, t)dx = f(b(t), t)b'(t) - f(a(t), t)a'(t) + \int_{a(t)}^{b(t)} \frac{\partial f}{\partial t}(x, t)dx
$$

_증명._ $G(u, v, t) = \int_u^v f(x, t)dx$ 라고 하면 미적분학의 기본정리 2에 의해 $D_1 G = -f(u, t)$, $D_2 G = f(v, t)$ 이고, 위의 따름정리에 의해 $D_3 G = \int_u^v \frac{\partial f}{\partial t}dx$ 이다. 세 편도함수가 연속이므로 $G$는 미분가능하고, 다변수 연쇄법칙을 적용한다. $\blacksquare$

## 더 일반적인 경우
- 적분 구간이 무한하거나 이상적분인 경우, 위의 조건에 더해 $\int \frac{\partial f}{\partial t}(x, t)dx$가 $t$에 대해 균등하게 수렴해야 한다.

## 참고문헌
(1) Walter Rudin, Principles of Mathematical Analysis
