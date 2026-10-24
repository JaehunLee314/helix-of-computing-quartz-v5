**Prerequisites:** [[Intuition for Variable]], [[Big-O Like Notations]], [[Differentiation and Taylor Series]]

## Uniform Big-O Like Notation

구간 $I$의 두 점 $x, y$가 가까워질 때, $x, y$의 위치와 무관하게 작아지는 양을 나타내는 표기법을 정의한다.

**정의. Uniform Little-o Notation** 구간 $I$와 함수 $f, g: I \times I \to \mathbb{R}$에 대해 다음과 같이 정의한다.

$$
f \in o_I(g) \iff \epsilon > 0 \to \exists \delta > 0, (x, y \in I, 0 < |x - y| < \delta \to |f(x, y)| \leq \epsilon|g(x, y)|)
$$

**정의. 변수를 사용한 Uniform Little-o Notation** $x, y$에 대한 식 $f(x, y), g(x, y)$에 대해 다음과 같이 정의한다.

$$
f(x, y) \in \underset{x, y \in I, x - y \to 0}o (g(x, y)) \iff f \in o_I(g)
$$

맥락상 명확하면 $o_{x, y \in I}$로 줄여 적는다. $O, \Omega, \Theta$도 같은 방식으로 정의하고, 식 안에서 쓰는 경우도 [[Big-O Like Notations]]와 같이 해석한다.

정의에서 $x, y$는 대칭이다. 따라서 $f(x, y) \in o_{x, y \in I}(g(x, y))$ 이면 $f(y, x) \in o_{x, y \in I}(g(y, x))$ 이다.

**예시. 균등연속** 함수 $f$가 구간 $I$에서 균등연속이라는 것은 다음과 같다.

$$
f(y) = f(x) + \underset{x, y \in I}o (1)
$$

예를 들어 $y^2 - x^2 = (x + y)(y - x)$ 이므로 $x^2$은 $[0, 1]$에서 균등연속이지만 $\mathbb{R}$에서는 균등연속이 아니다.

**정리. 하이네-칸토어 정리** 닫힌 구간 $[a, b]$에서 연속인 함수는 $[a, b]$에서 균등연속이다. (참고문헌 (1))

## 리만 적분의 정의

함수 $f$의 그래프 아래, 구간 $[x, y]$ 위의 (부호 있는) 넓이 $A(x, y)$를 구하고자 한다. 넓이는 다음을 만족해야 한다.

- _(가법성)_ $a \leq x \leq y \leq z \leq b$ 이면 $A(x, z) = A(x, y) + A(y, z)$

그래프는 곡선이므로 분할을 점차 세밀하게 하며 넓이를 직사각형으로 근사하는 방법을 생각해 보자. $[a, b]$의 분할(partition) $P: a = x_0 < x_1 < \cdots < x_n = b$에 대해 $h_i = x_{i+1} - x_i$, $\lVert P \rVert = \max_i h_i$ 라고 하자. 각 소구간 $[x_i, x_{i+1}]$에서 점 $t_i$를 골라 높이가 $f(t_i)$인 직사각형을 생각하자. 그러면 직사각형의 넓이와 실제 넓이간의 오차는 다음과 같다.

$$
e_i = A(x_i, x_{i+1}) - f(t_i)h_i
$$

가법성에 의해 다음이 성립한다.

$$
A(a, b) = \sum_{i=0}^{n-1} f(t_i)h_i + \sum_{i=0}^{n-1} e_i
$$

첫 번째 합을 리만 합 $S(P, t)$, 두 번째 합을 오차합이라고 하자. $\lVert P \rVert \to 0$ 일 때 오차합이 $0$으로 수렴하면 넓이는 리만 합의 극한이 된다. 넓이 $A$는 아직 정의되지 않았으므로, 거꾸로 리만 합의 극한이 존재하는 것을 적분가능성의 정의로, 그 극한을 넓이의 정의로 삼는다.

**정의. 리만 적분** 어떤 $L$에 대해 다음이 성립하면 $f$가 $[a, b]$에서 리만 적분가능하다고 하고 $L = \int_a^b f$ 라고 적는다.

$$
\lim_{\lVert P \rVert \to 0} S(P, t) = L
$$

여기서 극한은 분할과 대표점을 어떻게 고르든 $\lVert P \rVert$가 충분히 작으면 $S(P, t)$가 $L$에 가까워진다는 뜻이다.

**정리.** $[a, b]$에서 연속인 함수는 리만 적분가능하다. (참고문헌 (1))

### 오차합과 균등성

각 오차 $e_i$가 $h_i$보다 빨리 작아지는 것만으로는 오차합이 $0$으로 가지 않는다. 오차가 작아지는 속도가 위치와 무관해야, 즉 균등해야 한다.

**정리. 균등오차의 합** $e(x, y) \in o_{x, y \in [a, b]}(y - x)$ 이면 다음이 성립한다.

$$
\lim_{\lVert P \rVert \to 0} \sum_{i=0}^{n-1} e(x_i, x_{i+1}) = 0
$$

_증명._ $\epsilon > 0$에 대해 다음을 만족하는 $\delta > 0$가 존재한다.

$$
x, y \in [a, b], 0 < |x - y| < \delta \to |e(x, y)| \leq \epsilon|y - x|
$$

따라서 $\lVert P \rVert < \delta$ 이면 다음과 같다.

$$
\Big|\sum_{i=0}^{n-1} e(x_i, x_{i+1})\Big| \leq \epsilon \sum_{i=0}^{n-1} h_i = \epsilon(b - a)
$$

$\blacksquare$

넓이의 경우 오차를 다음과 같이 두면 $|e_i| \leq e(x_i, x_{i+1})$ 이다.

$$
e(x, y) = \sup_{x \leq t \leq y} |A(x, y) - f(t)(y - x)|
$$

따라서 $e(x, y) \in o_{x, y \in [a, b]}(y - x)$ 이면 오차합은 $0$으로 수렴한다. 즉 직사각형 근사의 오차가 균등하게 작으면 $f$는 리만 적분가능하다. 연속함수의 경우 $A(x, y) = \int_x^y f$ 로 두면 $A(x, y) - f(t)(y - x) = \int_x^y \big(f(s) - f(t)\big)ds$ 이고 $|s - t| \leq |y - x|$ 이므로, 균등연속성에 의해 이 조건을 만족한다.

**예시.** 균등하지 않으면 정리가 성립하지 않는다. $[0, 1]$에서 $0 < x < y - x$ 이면 $e(x, y) = 1$, 그렇지 않으면 $e(x, y) = 0$ 이라고 하자. 각 $x$에 대해 $e(x, y) \in o_{y \to x}(y - x)$ 이다. 그러나 분할 $x_0 = 0, x_1 = \frac{1}{2n}, x_i = \frac{i}{n}$ ($2 \leq i \leq n$)에 대해 $\lVert P \rVert \to 0$ 이지만 합은 항상 $1$ 이다.

**예시.** 균등성은 충분조건이지 필요조건은 아니다. $[0, 1]$에서 $x \geq \frac{1}{2}$ 이면 $f(x) = 1$, 그렇지 않으면 $f(x) = 0$ 이라고 하자. $x < \frac{1}{2} < y$ 이고 $t = x$ 이면 오차는 $y - \frac{1}{2}$ 이므로 $e(x, y) \notin o_{x, y \in [0, 1]}(y - x)$ 이다. 그러나 오차가 $0$이 아닌 소구간은 많아야 두 개이고 각 오차는 $h_i$ 이하이므로 오차합은 $0$으로 수렴한다.

## 적분의 기본 성질

$f, g$가 $[a, b]$에서 연속이라고 하자.

1. _(선형성)_ $\int_a^b (\alpha f + \beta g) = \alpha \int_a^b f + \beta \int_a^b g$
2. _(상수함수)_ $\int_a^b c = c(b - a)$
3. _(크기의 비교)_ $|f| \leq M$ 이면 $\left|\int_a^b f\right| \leq M|b - a|$
4. _(구간 가법성)_ $\int_a^b f = \int_a^c f + \int_c^b f$

단 $\int_b^a f = -\int_a^b f$ 로 약속한다.

## 미적분학의 기본정리

**정의. 균등미분가능성** 구간 $I$에서 다음이 성립할 때 $F$가 $I$에서 균등미분가능하다고 한다.

$$
F(y) = F(x) + f(x)(y - x) + \underset{x, y \in I}o (y - x)
$$

**보조정리 1.** $F$가 $I$에서 균등미분가능하면 $f$는 $I$에서 균등연속이다.

_증명._ 오차항을 $e(x, y)$라고 하자. $|x - y| = |y - x|$ 이므로 $e(y, x) \in o_{x, y \in I}(y - x)$ 이다. 정의의 식과 $x, y$를 바꾼 식을 더하면 다음을 얻는다.

$$
\big(f(y) - f(x)\big)(y - x) = e(x, y) + e(y, x) \in \underset{x, y \in I}o (y - x)
$$

양변을 $y - x$로 나누면 $f(y) - f(x) \in o_{x, y \in I}(1)$ 이다. $\blacksquare$

**보조정리 2.** $F$가 $[a, b]$에서 $C^1$이면 $F$는 $[a, b]$에서 균등미분가능하다.

_증명._ 평균값 정리에 의해 $x$와 $y$ 사이의 $\xi$가 존재하여 다음이 성립한다.

$$
F(y) - F(x) - F'(x)(y - x) = \big(F'(\xi) - F'(x)\big)(y - x)
$$

$|\xi - x| \leq |y - x|$ 이므로 하이네-칸토어 정리에 의해 $F'(\xi) - F'(x) \in o_{x, y \in [a, b]}(1)$ 이다. $\blacksquare$

따라서 닫힌 구간에서 균등미분가능한 것은 $C^1$인 것과 같다.

**예시.** $F(x) = x^2$ 이면 $F(y) = F(x) + 2x(y - x) + (y - x)^2$ 이고 $(y - x)^2 \in o_{x, y \in I}(y - x)$ 이므로 $F$는 임의의 구간 $I$에서 균등미분가능하다. 반면 $F(x) = x^2 \sin \frac{1}{x}$, $F(0) = 0$은 $[-1, 1]$에서 미분가능하지만 $F'$이 $0$에서 연속이 아니므로, 보조정리 1에 의해 $[-1, 1]$에서 균등미분가능하지 않다.

**정리. 미적분학의 기본정리 1** $F$가 $[a, b]$에서 $C^1$이면 다음이 성립한다.

$$
\int_a^b F' = F(b) - F(a)
$$

_증명._ 보조정리 2에 의해 $F$는 균등미분가능하다. 그 오차항을 $e(x, y)$라고 하면 다음이 성립한다.

$$
F(b) - F(a) = \sum_{i=0}^{n-1} \big(F(x_{i+1}) - F(x_i)\big) = \sum_{i=0}^{n-1} F'(x_i)h_i + \sum_{i=0}^{n-1} e(x_i, x_{i+1})
$$

$\lVert P \rVert \to 0$ 이면 첫 번째 합은 $\int_a^b F'$로, 두 번째 합은 균등오차의 합 정리에 의해 $0$으로 수렴한다. $\blacksquare$

**정리. 미적분학의 기본정리 2** $f$가 $[a, b]$에서 연속이고 $F(x) = \int_a^x f$ 이면 다음이 성립한다.

$$
F(y) = F(x) + f(x)(y - x) + \underset{x, y \in [a, b]}o (y - x)
$$

_증명._ 다음이 성립한다.

$$
F(y) - F(x) - f(x)(y - x) = \int_x^y \big(f(t) - f(x)\big)dt
$$

$t$가 $x$와 $y$ 사이에 있으면 $|t - x| \leq |y - x|$ 이므로, 하이네-칸토어 정리에 의해 $f(t) - f(x)$는 $o_{x, y \in [a, b]}(1)$로 균등하게 작다. 따라서 위 적분은 $o_{x, y \in [a, b]}(y - x)$ 이다. $\blacksquare$

## 라이프니츠 표기법에 대해서

적분 $\int_a^b f(x)dx$는 리만 합 $\sum_i f(x_i)\Delta x_i$를 옮긴 것이다. $\int$는 합(summa)의 S를 늘인 기호이고, $dx$는 $\Delta x_i = x_{i+1} - x_i$에 해당한다.

$y = F(x)$에 대해 $dx = \Delta x$로 두고 미분소를 다음과 같이 정의한다.

$$
dy = F'(x)dx
$$

그러면 $dy$는 $\Delta y$에서 오차항을 버린 일차 부분이다.

$$
\Delta y = dy + \underset{\Delta x \to 0}o (\Delta x)
$$

$dy$를 $dx$에 대한 선형함수로 보는 관점은 미분형식(differential form)으로 이어진다(참고문헌 (2)).

### 미적분학의 기본정리

기본정리 1은 다음과 같이 적힌다.

$$
\int_a^b dy = F(b) - F(a)
$$

$\Delta y$의 합은 $F(b) - F(a)$이고, $F$가 $C^1$이면 $dy$와 $\Delta y$의 차이는 균등한 오차항 $o_{x, y \in [a, b]}(y - x)$ 이므로 그 합은 $0$으로 수렴한다. 즉 $\Delta y$ 대신 $dy$를 더해도 극한은 같다.

### 치환적분

$u = g(x)$이면 연쇄법칙에 의해 $du = g'(x)dx$ 이다.

**정리. 치환적분** $g$가 $[a, b]$에서 $C^1$이고 $f$가 $g([a, b])$를 포함하는 닫힌 구간에서 연속이면 다음이 성립한다.

$$
\int_a^b f(g(x))g'(x)dx = \int_{g(a)}^{g(b)} f(u)du
$$

### 부분적분

곱의 미분법에 의해 $d(uv) = udv + vdu$ 이다.

**정리. 부분적분** $u, v$가 $[a, b]$에서 $C^1$이면 다음이 성립한다.

$$
\int_a^b udv = \big[uv\big]_a^b - \int_a^b vdu
$$

## 참고문헌
(1) Walter Rudin, Principles of Mathematical Analysis 
(2) David Bachman, A Geometric Approach to Differential Forms