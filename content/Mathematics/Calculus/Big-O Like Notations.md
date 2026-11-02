**Prerequisites**: [[Intuition for Variable]]

Big-O like notation은 두 함수 $f, g$의 점근적 크기를 비교하는 표기법이다.

## Neighborhood

$L$이 실수 $a$ 또는 $\pm\infty$일 때 $L$의 $\delta$-근방을 다음과 같이 정의한다.

$$
x \in N_\delta(a) \iff 0 < |x - a| < \delta
$$
$$
x \in N_\delta(\infty) \iff x > \frac{1}{\delta}, \quad x \in N_\delta(-\infty) \iff x < -\frac{1}{\delta}
$$

물론, $x, a \in \mathbb{R}^n$이면 근방을 norm으로 정의한다.

$$
x \in N_\delta(a) \iff 0 < \lVert x - a \rVert < \delta
$$

## Big-O Notation

$f \in O_L(g)$는 $L$ 근처에서 $|f|$가 $|g|$의 상수배보다 크지 않다는 뜻이다.

**정의. Big-O Notation** 
함수 $f, g$에 대해 다음과 같이 정의한다.

$$
f \in O_L(g) \iff \exists C > 0, \exists \delta > 0, (x \in N_\delta(L) \to |f(x)| \leq C|g(x)|)
$$

첨자를 생략하면 $L = \infty$이다. 즉 $O(g) = O_\infty(g)$ 이다.

**정의. 변수를 사용한 Big-O Notation** 
$x$에 대한 식 $f(x), g(x)$에 대해 다음과 같이 정의한다.

$$
f(x) \in \underset{x \to L}O (g(x)) \iff f \in O_L(g)
$$

여기서 우변의 $f, g$는 함수 $x \mapsto f(x)$, $x \mapsto g(x)$이다. 한 줄로 적을 때는 $O_{x \to L}(g(x))$와 같이 쓴다.

**예시.** $x > 1$이면 $3x^2 < 3x^3$ 이므로 $3x^2 \in O_{x \to \infty}(x^3)$ 이다.

## Big-Omega & Big-Theta Notation

**정의. Big-Omega Notation** 
함수 $f, g$에 대해 다음과 같이 정의한다.

$$
f \in \Omega_L(g) \iff \exists C > 0, \exists \delta > 0, (x \in N_\delta(L) \to |f(x)| \geq C|g(x)|)
$$

$f \in \Omega_L(g)$는 $g \in O_L(f)$와 동치이다.

**정의. Big-Theta Notation** 
$f \in O_L(g)$이고 $f \in \Omega_L(g)$이면 $f \in \Theta_L(g)$라고 적는다.

두 경우 모두 첨자를 생략하면 $L = \infty$이다.

**정의. 변수를 사용한 Big-Omega, Big-Theta Notation** 
$x$에 대한 식 $f(x), g(x)$에 대해 다음과 같이 정의한다.

$$
f(x) \in \underset{x \to L}\Omega (g(x)) \iff f \in \Omega_L(g)
$$

$$
f(x) \in \underset{x \to L}\Theta (g(x)) \iff f \in \Theta_L(g)
$$

**예시.** $x > 1$이면 $x^2 \leq 3x^2 + x \leq 4x^2$ 이므로 $3x^2 + x \in \Theta_{x \to \infty}(x^2)$ 이다.

## Little-o Notation

$f \in o_L(g)$는 $x$가 $L$에 가까워질 때 $f$가 $g$에 비해 무시할 수 있을 만큼 작아진다는 뜻이다.

**정의. Little-o Notation** 
함수 $f, g$에 대해 다음과 같이 정의한다.

$$
f \in o_L(g) \iff \epsilon > 0 \to \exists \delta > 0, (x \in N_\delta(L) \to |f(x)| \leq \epsilon|g(x)|)
$$

첨자를 생략하면 $L = 0$이다. 즉 $o(g) = o_0(g)$ 이다.

**정의. 변수를 사용한 Little-o Notation** 
$x$에 대한 식 $f(x), g(x)$에 대해 다음과 같이 정의한다.

$$
f(x) \in \underset{x \to L}o (g(x)) \iff f \in o_L(g)
$$

**보조정리.** $L$ 근처에서 $g(x) \neq 0$이면 다음이 성립한다.

$$
f \in o_L(g) \iff \lim_{x \to L} \frac{f(x)}{g(x)} = 0
$$

특히 $f \in o_L(1)$은 $\lim_{x \to L} f(x) = 0$과 같다.

**예시.**
- $x^2 \in o_{x \to 0}(x)$
- $\frac{1}{x} \in o_{x \to \infty}(1)$
- $x \in o_{x \to \infty}(x^2)$

## 수식에서의 Big-O Like 표기의 사용

$\mathcal{X}$가 $O, \Omega, \Theta, o$ 중 하나라고 하자. 식 안에서 쓰는 경우는 다음과 같이 정의한다.

$$
f = g + \mathcal{X}_L(h) \iff \exists e \in \mathcal{X}_L(h), f = g + e
$$
$$
f(x) = g(x) + \underset{x \to L}{\mathcal{X}} (h(x)) \iff \exists e(x) \in \underset{x \to L}{\mathcal{X}} (h(x)), f(x) = g(x) + e(x)
$$

이러한 표기가 여러 번 쓰이면 각각을 서로 다른 변수로 해석한다. 예를 들어

$$
f(x) + \underset{x \to L}o (h(x)) = g(x) + \underset{x \to L}O (k(x))
$$

는 다음을 뜻한다.

$$
\exists e_1(x) \in \underset{x \to L}o (h(x)), \exists e_2(x) \in \underset{x \to L}O (k(x)), f(x) + e_1(x) = g(x) + e_2(x)
$$

**예시.** $(x + 1)^2 = x^2 + O_{x \to \infty}(x)$ 이다.

## 참고문헌
(1) Kenneth Rosen, Discrete Mathematics and Its Applications 
(2) Wikipedia, Little-o notation, https://en.wikipedia.org/wiki/Big_O_notation#Little-o_notation