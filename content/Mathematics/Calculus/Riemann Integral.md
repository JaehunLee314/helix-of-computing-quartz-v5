**Prerequisites:** [[Intuition for Variable]], [[Big-O Like Notations]], [[Differentiation and Taylor Series]]

## Uniform Big-O Like Notation

Uniform little-o notation은 little-o notation의 응용으로 이해할 수 있다.

**정의. Uniform Little-o Notation** 
구간 $I$와 함수 $f, g: I \times I \to \mathbb{R}$에 대해 다음과 같이 정의한다.

$$
f \in o_I(g) \iff \epsilon > 0 \to \exists \delta > 0, (x, y \in I, 0 < |x - y| < \delta \to |f(x, y)| \leq \epsilon|g(x, y)|)
$$

**정의. 변수를 사용한 Uniform Little-o Notation** 
$x, y$에 대한 식 $f(x, y), g(x, y)$에 대해 다음과 같이 정의한다.

$$
f(x, y) \in \underset{x, y \in I, x - y \to 0}o (g(x, y)) \iff f \in o_I(g)
$$

맥락상 명확하면 $o_{x, y \in I}$로 줄여 적는다. $O, \Omega, \Theta$도 같은 방식으로 정의하고, 식 안에서 쓰는 경우도 [[Big-O Like Notations]]에서 설명한 바와 같이 해석한다. Little-o가 가지는 성질은 uniform little-o에 대해서도 성립하며 증명 방식도 동일하다.

정의에서 $x, y$는 대칭이다. 따라서 $f(x, y) \in o_{x, y \in I}(g(x, y))$ 이면 $f(y, x) \in o_{x, y \in I}(g(y, x))$ 이다.

## 균등연속

**정의. 균등연속(Uniform Continuity)** 
함수 $f$가 구간 $I$에서 다음을 만족하면 $I$에서 균등연속이라고 한다.

$$
f(y) = f(x) + \underset{x, y \in I}o (1)
$$

$f(y) = f(x) + o_{y \to x}(1)$이 각 $x$에서 성립하는 것이 연속이다. 균등연속은 $f(y)$가 $f(x)$에 가까워지는 속도가 $x$와 무관하게 모든 지점에서 동등하다는 의미를 가진다.

**예시.** $y^2 - x^2 = (x + y)(y - x)$ 이므로 $x^2$은 $[0, 1]$에서 균등연속이지만 $\mathbb{R}$에서는 균등연속이 아니다. $\mathbb{R}$에서는 $|x + y|$가 유계가 아니기 때문이다.

**정리. 하이네-칸토어 정리** 
닫힌 구간 $[a, b]$에서 연속인 함수는 $[a, b]$에서 균등연속이다. 
*증명.* 참고문헌 (1)을 보라.

즉 닫힌 구간에서는 연속성이 균등성을 보장한다. 아래에서 오차항의 균등성은 대부분 이 정리에 의존한다.

## 리만 적분의 개요

함수 $f$의 그래프 아래, 구간 $[x, y]$ 위의 (부호 있는) 넓이 $A(x, y)$를 구하고자 한다고 해 보자. 직관적으로 넓이는 다음을 만족해야 한다.

- $a \leq x \leq y \leq z \leq b$ 이면 $A(x, z) = A(x, y) + A(y, z)$ _(가법성)_ 

그래프는 곡선이므로 구간을 세밀하게 분할하여 넓이를 직사각형으로 근사하는 방법을 생각해 보자. $[a, b]$의 분할 $P: a = x_0 < x_1 < \cdots < x_n = b$에 대해 $h_i = x_{i+1} - x_i$, $\lVert P \rVert = \max_i h_i$ 라고 하자. 각 소구간 $[x_i, x_{i+1}]$에서 대표점 $t_i$를 골라 높이가 $f(t_i)$인 직사각형을 생각하자. 이러한 직사각형의 넓이는 각각 $f(x_i)h_i$이다. 그런데 직사각형의 넓이와 실제 넓이 사이에는 오차가 존재할 것이다. 이를 다음과 같이 정의하자.

$$
e_i = A(x_i, x_{i+1}) - f(t_i)h_i
$$

가법성에 의해 실제 넓이는 직사각형 넓이의 합과 오차의 합으로 정확히 나뉜다.

$$
A(a, b) = \sum_{i=0}^{n-1} f(t_i)h_i + \sum_{i=0}^{n-1} e_i
$$

첫 번째 합을 리만 합 $S(P, t)$, 두 번째 합을 오차합이라고 하자. 넓이를 직사각형으로 근사하는 것이 가능하려면 $\lVert P \rVert \to 0$ 일 때 오차합이 $0$으로 수렴해야 하고, 이는 리만 합이 $A(a, b)$로 수렴하는 것과 같다. 따라서 리만 합의 극한이 존재하는 것을 적분가능성의 정의로, 그 극한을 넓이의 정의로 삼는다.

**정의. 리만 적분** 
어떤 $L$에 대해 다음이 성립하면 $f$가 $[a, b]$에서 리만 적분가능하다고 한다.

$$
\lim_{\lVert P \rVert \to 0} S(P, t) = L
$$

여기서 극한은 분할과 대표점을 어떻게 고르든 $\lVert P \rVert$가 충분히 작으면 $S(P, t)$가 $L$에 가까워진다는 뜻이다. 이때 $L$을 다음과 같이 적는다.

$$
\int_a^b f = \int_a^b f(x)dx
$$

$\int$는 합(summa)의 S를 늘인 기호이고, $f(x)dx$는 직사각형의 넓이 $f(t_i)h_i$에 해당한다. $x$는 식 안에서만 의미를 갖는 변수이므로 $\int_a^b f(x)dx = \int_a^b f(t)dt$ 이다. 또 $\int_b^a f = -\int_a^b f$ 로 약속한다.

**정리.** $[a, b]$에서 연속인 함수는 리만 적분가능하다.
*증명.* 참고문헌 (1)을 보라.

## 균등오차의 합

앞선 논의에서 오차의 합 $\sum_i e_i$가 $0$으로 수렴할 때 적분이 가능하다고 했다. 이것이 가능한 한 가지 경우는 각 오차가 균등하게 $0$으로 수렴하는 경우이다.

**정리. 균등오차의 합** 
적당한 분할 $P$를 가정하자. $e(x, y) \in o_{x, y \in [a, b]}(y - x)$ 이면 다음이 성립한다.

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

**예시.** 만약 오차가 균등하게 수렴하지 않는다면 오차의 합도 수렴하지 않는다. $[0, 1]$에서 $0 < x < y - x$ 이면 $e(x, y) = 1$, 그렇지 않으면 $e(x, y) = 0$ 이라고 하자. 각 $x$에 대해 $e(x, y) \in o_{y \to x}(y - x)$ 이다. 그러나 분할 $x_0 = 0, x_1 = \frac{1}{2n}, x_i = \frac{i}{n}$ ($2 \leq i \leq n$)에 대해 $\lVert P \rVert \to 0$ 이지만 합은 항상 $1$ 이다.

**예시.** 균등성은 충분조건이지 필요조건은 아니다. $[0, 1]$에서 $x \geq \frac{1}{2}$ 이면 $f(x) = 1$, 그렇지 않으면 $f(x) = 0$ 이라고 하자. $\frac{1}{2}$을 포함하는 소구간에서는 직사각형 근사의 오차가 $h_i$와 같은 크기이므로 균등하게 $o(h_i)$가 아니다. 그러나 그런 소구간은 많아야 두 개이므로 오차합은 $0$으로 수렴한다.

**따름정리. 적분에서의 균등오차의 소거** 
적당한 분할 $P$를 가정하자. 함수 $q(x, y)$와 $[a, b]$에서 연속인 함수 $g$에 대해 다음이 성립한다고 하자.

$$
q(x, y) = g(x)(y - x) + \underset{x, y \in [a, b]}o (y - x)
$$

그러면 다음이 성립한다.

$$
\lim_{\lVert P \rVert \to 0} \sum_{i=0}^{n-1} q(x_i, x_{i+1}) = \int_a^b g
$$

특히 $Q$가 가법성을 만족하고 $Q(x, y) = g(x)(y - x) + o_{x, y \in [a, b]}(y - x)$ 이면 $Q(a, b) = \int_a^b g$ 이다.

_증명._ $\sum q(x_i, x_{i+1})$는 왼쪽 끝점을 대표점으로 한 리만 합과 균등한 오차항의 합으로 나뉜다. 앞의 것은 $\int_a^b g$로, 뒤의 것은 $0$으로 수렴한다. $Q$가 가법성을 만족하면 $\sum Q(x_i, x_{i+1}) = Q(a, b)$ 이다. $\blacksquare$

즉 작은 조각의 양을 $g(x)(y - x)$로 근사했을 때 그 오차가 균등하게 $o(y - x)$이면, 오차를 버리고 적분할 수 있다. 오차가 $O(y - x)$에 그치면 버릴 수 없다. 아래의 미적분학의 기본정리, 길이, 부피, 겉넓이는 모두 이 따름정리의 응용이다.

## 미적분학의 기본정리

[[Differentiation and Taylor Series]]의 일차근사에 의해 $F(y) - F(x) = F'(x)(y - x) + o_{y \to x}(y - x)$ 이다. 즉 $F$의 증분은 높이가 $F'(x)$인 직사각형의 넓이로 근사된다. 또 $Q(x, y) = F(y) - F(x)$는 가법성을 만족한다. 따라서 이 근사의 오차가 균등하면, $F$의 증분은 $F'$의 그래프 아래 넓이처럼 행동한다.

**정의. 균등미분가능성** 
구간 $I$에서 다음이 성립할 때 $F$가 $I$에서 균등미분가능하다고 한다.

$$
F(y) = F(x) + f(x)(y - x) + \underset{x, y \in I}o (y - x)
$$

**보조정리.** 닫힌 구간에서 $F$가 균등미분가능한 것은 $F$가 $C^1$인 것과 같다.

_증명._ $F$가 $C^1$이면 평균값 정리에 의해 $x$와 $y$ 사이의 $\xi$가 존재하여 다음이 성립하고, 하이네-칸토어 정리에 의해 $F'(\xi) - F'(x) \in o_{x, y \in [a, b]}(1)$ 이다.

$$
F(y) - F(x) - F'(x)(y - x) = \big(F'(\xi) - F'(x)\big)(y - x)
$$

역으로 $F$가 균등미분가능하면, 정의의 식과 $x, y$를 바꾼 식을 더하여 다음을 얻는다.

$$
\big(f(y) - f(x)\big)(y - x) \in \underset{x, y \in I}o (y - x)
$$

따라서 $f(y) - f(x) \in o_{x, y \in I}(1)$ 이다. $\blacksquare$

**예시.** $F(x) = x^2 \sin \frac{1}{x}$, $F(0) = 0$은 $[-1, 1]$에서 미분가능하지만 $F'$이 $0$에서 연속이 아니므로 균등미분가능하지 않다.

**정리. 미적분학의 기본정리 1** 
$F$가 $[a, b]$에서 $C^1$이면 다음이 성립한다.

$$
\int_a^b F' = F(b) - F(a)
$$

_증명._ 보조정리에 의해 $F(y) - F(x) = F'(x)(y - x) + o_{x, y \in [a, b]}(y - x)$ 이고, $F(y) - F(x)$는 가법성을 만족한다. 적분에서의 균등오차의 소거에 의해 결론이 성립한다. $\blacksquare$

**정리. 미적분학의 기본정리 2** 
$f$가 $[a, b]$에서 연속이고 $F(x) = \int_a^x f$ 이면 다음이 성립한다.

$$
F(y) = F(x) + f(x)(y - x) + \underset{x, y \in [a, b]}o (y - x)
$$

_증명._ $F(y) - F(x) - f(x)(y - x) = \int_x^y \big(f(t) - f(x)\big)dt$ 이고, $|t - x| \leq |y - x|$ 이므로 하이네-칸토어 정리에 의해 피적분함수는 $o_{x, y \in [a, b]}(1)$ 이다. $\blacksquare$

기본정리 2는 리만 적분의 개요에서 넓이에 기대했던 성질, 즉 $A(x, y) = f(x)(y - x) + o(y - x)$가 연속함수의 적분에 대해 실제로 균등하게 성립한다는 것을 말해준다.

**참고. 라이프니츠 표기법** 
$y = F(x)$에 대해 $dx = \Delta x$로 두고 미분소를 $dy = F'(x)dx$로 정의하면 $dy$는 $\Delta y$에서 오차항을 버린 일차 부분으로 이해할 수 있다.

$$
\Delta y = dy + \underset{\Delta x \to 0}o (\Delta x)
$$

$\Delta y$의 합은 정확히 $F(b) - F(a)$이고, $F$가 $C^1$이면 $dy$와의 차이는 균등한 오차이므로 적분에서 소거된다. 이것이 다음 식의 의미이다.

$$
\int_a^b dy = F(b) - F(a)
$$

$dy$를 $dx$에 대한 선형함수로 보는 관점은 미분형식(differential form)으로 이어진다(참고문헌 (2)).

## 길이와 부피의 계산

이하의 계산에서 다음 사실을 사용한다. 

(1) $f$가 $[a, b]$에서 $C^1$이면 균등미분가능하므로 다음이 성립한다.

$$
\frac{f(y) - f(x)}{y - x} = f'(x) + \underset{x, y \in [a, b]}o (1)
$$

(2) $\left|\frac{d}{du}\sqrt{1 + u^2}\right| \leq 1$ 이므로 $\left|\sqrt{1 + u^2} - \sqrt{1 + v^2}\right| \leq |u - v|$ 이다.

### 곡선의 길이

$f$가 $[a, b]$에서 $C^1$이라고 하자. 곡선 $y = f(x)$의 길이는 분할점을 이은 선분 길이의 합의 극한으로 정의한다. 소구간 $[x, y]$ 위의 선분의 길이는 다음과 같다.

$$
q(x, y) = \sqrt{(y - x)^2 + \big(f(y) - f(x)\big)^2} = \sqrt{1 + \left(\frac{f(y) - f(x)}{y - x}\right)^2}(y - x)
$$

위의 두 사실에 의해 $q(x, y) = \sqrt{1 + f'(x)^2}(y - x) + o_{x, y \in [a, b]}(y - x)$ 이므로, 적분에서의 균등오차의 소거에 의해 길이는 다음과 같다.

$$
L = \int_a^b \sqrt{1 + f'(x)^2}dx
$$

**예시. 계단 역설** 
$[0, 1]$에서 $f(x) = x$의 그래프를 가로 $y - x$, 세로 $y - x$인 계단으로 근사하면 한 계단의 길이는 다음과 같다.

$$
q(x, y) = 2(y - x) = \sqrt{2}(y - x) + (2 - \sqrt{2})(y - x)
$$

오차 $(2 - \sqrt{2})(y - x)$는 $O_{x, y \in [0, 1]}(y - x)$ 이지만 $o_{x, y \in [0, 1]}(y - x)$가 아니므로 소거되지 않는다. 따라서 계단의 길이는 분할이 아무리 세밀해져도 $\sqrt{2}$가 아니라 $2$이다.

### 입체의 부피

축 위의 구간 $[x, y]$ 사이에 있는 입체의 부피를 $V(x, y)$, 점 $x$에서 축에 수직인 단면의 넓이를 $S(x)$라고 하자. 부피는 가법성과 다음 성질을 만족해야 한다.

- $\min_{[x, y]} S \cdot (y - x) \leq V(x, y) \leq \max_{[x, y]} S \cdot (y - x)$  

$S$가 연속이면 하이네-칸토어 정리에 의해 $\max_{[x, y]} S - \min_{[x, y]} S \in o_{x, y \in [a, b]}(1)$ 이므로 $V(x, y) = S(x)(y - x) + o_{x, y \in [a, b]}(y - x)$ 이다. 적분에서의 균등오차의 소거에 의해 부피는 다음과 같다.

$$
V(a, b) = \int_a^b S(x)dx
$$

**예시. 회전체의 부피** 
$f \geq 0$이 연속이고 곡선 $y = f(x)$를 $x$축 둘레로 회전시킨 입체의 단면은 반지름 $f(x)$인 원판이다. 구간 $[x, y]$ 부분은 반지름 $\min_{[x, y]} f$인 원기둥과 반지름 $\max_{[x, y]} f$인 원기둥 사이에 있으므로 위의 성질을 만족한다. 따라서 $V = \int_a^b \pi f(x)^2 dx$ 이다. 예를 들어 반지름 $r$인 구의 부피는 다음과 같다.

$$
V = \int_{-r}^r \pi(r^2 - x^2)dx = \frac{4}{3}\pi r^3
$$

부피에는 연속성만 필요하고, 길이와 겉넓이에는 $C^1$이 필요하다.

## 회전체의 겉넓이

$f \geq 0$이 $[a, b]$에서 $C^1$이라고 하자. 곡선 $y = f(x)$를 $x$축 둘레로 회전시킨 곡면의 겉넓이는, 선분을 회전시켜 얻은 원뿔대들의 겉넓이 합의 극한으로 정의한다. 소구간 $[x, y]$ 위의 원뿔대의 겉넓이는 다음과 같다.

$$
q(x, y) = 2\pi\frac{f(x) + f(y)}{2}\sqrt{(y - x)^2 + \big(f(y) - f(x)\big)^2}
$$

**정리.** 회전체의 겉넓이는 다음과 같다.

$$
A = \int_a^b 2\pi f(x)\sqrt{1 + f'(x)^2}dx
$$

_증명._ 다음과 같이 두자.

$$
dA = 2\pi f(x)\sqrt{1 + f'(x)^2}(y - x)
$$

$$
e_1 = \frac{f(x) + f(y)}{2} - f(x), \quad e_2 = \sqrt{1 + \left(\frac{f(y) - f(x)}{y - x}\right)^2} - \sqrt{1 + f'(x)^2}
$$

그러면 $q(x, y) = 2\pi\big(f(x) + e_1\big)\big(\sqrt{1 + f'(x)^2} + e_2\big)(y - x)$ 이므로 다음이 성립한다.

$$
q(x, y) - dA = 2\pi\Big(f(x)e_2 + \sqrt{1 + f'(x)^2}e_1 + e_1 e_2\Big)(y - x)
$$

$e_1 = \frac{f(y) - f(x)}{2}$ 이므로 균등연속성에 의해 $e_1 \in o_{x, y \in [a, b]}(1)$ 이고, 균등미분가능성과 $\sqrt{1 + u^2}$의 성질에 의해 $e_2 \in o_{x, y \in [a, b]}(1)$ 이다. $f$와 $f'$은 유계이므로 괄호 안은 $o_{x, y \in [a, b]}(1)$ 이고, 적분에서의 균등오차의 소거에 의해 결론이 성립한다. $\blacksquare$

**예시.** $[0, H]$에서 $f(x) = kx$ 이면 원뿔의 옆넓이는 다음과 같다.

$$
A = \int_0^H 2\pi kx\sqrt{1 + k^2}dx = \pi k\sqrt{1 + k^2}H^2
$$

밑면의 반지름 $R = kH$와 모선의 길이 $\ell = H\sqrt{1 + k^2}$를 쓰면 $A = \pi R\ell$ 이다.

**예시. 원기둥 근사** 
원뿔대 대신 원기둥 $2\pi f(x)(y - x)$로 근사하면 합은 $\int_a^b 2\pi f$로 수렴한다. 실제 겉넓이와의 차이 $2\pi f(x)\left(\sqrt{1 + f'(x)^2} - 1\right)(y - x)$는 $O(y - x)$ 이지만 $f' \neq 0$인 곳에서 $o(y - x)$가 아니므로 소거되지 않는다. 반지름은 어떻게 근사해도 오차가 $o(1)$이라 무해하지만, 빗변의 길이는 $y - x$에 대해 일차까지 정확해야 한다.

**참고.** 곡면을 삼각형들로 근사하면 삼각형이 작아져도 넓이의 합이 수렴하지 않을 수 있다(슈바르츠 랜턴, 참고문헌 (3)). 그래서 회전체의 겉넓이는 원뿔대로 정의한다.

## 참고문헌
(1) Walter Rudin, Principles of Mathematical Analysis 
(2) David Bachman, A Geometric Approach to Differential Forms 
(3) Wikipedia, [Schwarz lantern](https://en.wikipedia.org/wiki/Schwarz_lantern)