**Prerequisites:** [[Numerator Layout of Matrix Calculus]], [[Differentiation]], [[Properties of Big-O Like Notations]]

## 편미분

편미분은 어느 문자가 다른 문자와 전혀 함수관계가 없는 독립적인 값이라고 가정하고 미분을 계산하는 것을 말한다. (반면에 전미분은 모든 함수관계를 고려하며 미분을 계산하는 것이다.) 예를 들어서 $z = f(x, y)$라고 해 보자. 이때 $\partial z / \partial x$는 $x, y$가 서로 어떤 관계도 없다고 가정하고 $x$가 변화할 때 $z$가 변화하는 정도를 계산하는 것이다.

예를 들어 $z = x + 2y$이고 $x = y^2$이라고 하면 어떨까? 이때 편미분은 다음과 같이 주어진다.

$$
\frac{\partial z}{\partial x} = 1 \quad \frac{\partial z}{\partial y} = 2
$$

둘 사이의 관계 $x = y^2$는 편미분을 계산할 때 없는 것으로 가정한다. 그런데 만약 $z = y^2 + 2y$ 라는 식 전개 후에 편미분을 수행하면 어떻게 될까?

$$
\frac{\partial z}{\partial x} = 0 \quad \frac{\partial z}{\partial y} = 2y + 2
$$

보는 바와 같이 결과가 달라진다. 이처럼 편미분은 대상이 되는 문자를 어떤 문자로 표현했느냐에 영향을 받기 때문에 주의해야 한다. 이러한 영향을 고려하고 싶지 않은 경우에는 $D_i$ 와 같은 위치 기반의 미분 연산자를 사용하는 것을 고려할 수 있다. 이는 다음과 같이 정의된다.

$$
D_i f(x_1, ..., x_n) = \lim_{\Delta x_i \to 0} \frac{f(x_1, ..., x_i + \Delta x_i, ..., x_n) - f(x_1, ..., x_i, ..., x_n)}{\Delta x_i}
$$

이는 함수의 정의에 의존하기 때문에 문자 표현에 영향을 받지 않는다. 참고로 같은 상황에서 전미분은 다음과 같이 주어진다. 전미분의 경우 $x = y^2$이라는 관계를 고려한다. (이때 $y > 0$, 즉 $y = \sqrt{x}$라고 하자.)

$$
\frac{dz}{dx} = \frac{d}{dx}(x + 2y) = 1 + 2\frac{dy}{dx} = 1 + 2 \cdot \frac{1}{2\sqrt x} = 1 + \frac{1}{\sqrt x}
$$

$$
\frac{dz}{dy} = \frac{d}{dy}(x + 2y) = \frac{dx}{dy} + 2 = 2y + 2
$$

한편 편미분 시에 '다른 문자'의 범위를 잘 생각해야 한다. 예를 들어서 다음과 같은 편미분을 생각해 보자.

$$
\frac{\partial}{\partial t} \phi(x(t), t) = \ ?
$$

이때 $x(t)$에도 $t$라는 문자가 포함되므로 이를 편미분의 범위에 속하는 것으로 생각하기 쉽다. 하지만 통상적으로 위의 편미분은 $t$와 $x(t)$의 관계를 고려하지 않고 다음과 같이 정의한다.

$$
\frac{\partial}{\partial t} \phi(x(t), t) = D_2 \phi(x(t), t)
$$

## 다변수함수의 미분가능성

다변수함수에서는 편미분계수가 모두 존재해도 함수가 연속이 아닐 수 있다. 그래서 미분가능성은 편미분이 아니라 일차근사로 정의한다. $\mathbb{R}^n$의 근방은 노름으로 정의한다([[Big-O Like Notations]]).

**정의. 다변수함수의 미분가능성** 
$f: \mathbb{R}^l \to \mathbb{R}^m$이 $a$에서 미분가능하다는 것은 어떤 $m \times l$ 행렬 $J$가 존재하여 다음이 성립한다는 것이다.

$$
f(x) = f(a) + J(x - a) + \underset{x \to a}o(\lVert x - a \rVert)
$$

**보조정리.** 위의 $J$는 $(i, j)$ 성분이 $D_j f_i(a)$인 행렬이다. 분자 표기법으로 $y = f(x)$라고 하면 $J = \frac{\partial y}{\partial x}$ 이다. 특히 $m = 1$이면 $J = \nabla f(a)^T$ 이다.

_증명._ $x = a + t e_j$를 대입하고 $t$로 나눈 뒤 $t \to 0$으로 보낸다. $\blacksquare$

**예시.** $f(x) = \lVert x \rVert^2$ 이면 $f(a + h) = f(a) + 2a^T h + \lVert h \rVert^2$ 이고 $\lVert h \rVert^2 \in o_{h \to 0}(\lVert h \rVert)$ 이므로 $\nabla f(a) = 2a$ 이다.

**예시.** $f(x, y) = \frac{xy}{x^2 + y^2}$, $f(0, 0) = 0$ 이면 두 좌표축 위에서 $f = 0$ 이므로 원점에서 편미분계수는 모두 $0$이다. 그러나 $f(t, t) = \frac{1}{2}$ 이므로 $f$는 원점에서 연속이 아니고, 따라서 미분가능하지 않다. 편도함수가 모두 존재하고 연속이면 미분가능하다(참고문헌 (1)).

## 다변수함수의 연쇄법칙

**정리. 연쇄법칙** 
$x \in \mathbb{R}^l, y \in \mathbb{R}^n, z \in \mathbb{R}^m$이고 $y = f(x), z = g(y)$라고 하자. $f$가 $x$에서, $g$가 $y$에서 미분가능하면 다음이 성립한다.

$$
\frac{\partial z}{\partial x} = \frac{\partial z}{\partial y}\frac{\partial y}{\partial x}
$$

_증명._ $A = \frac{\partial y}{\partial x}$, $B = \frac{\partial z}{\partial y}$ 라고 하고 다음과 같이 두자.

$$
k(h) = f(x + h) - f(x) = Ah + e_1(h)
$$

$$
e_2(k) = g(y + k) - g(y) - Bk
$$

$k \neq 0$ 이면 $\eta(k) = e_2(k) / \lVert k \rVert$, $\eta(0) = 0$ 으로 두자. 그러면 $e_2(k) = \eta(k)\lVert k \rVert$ 이고 $\eta$는 $0$에서 연속이다. 따라서 다음이 성립한다.

$$
g(f(x + h)) - g(f(x)) = BAh + Be_1(h) + \eta(k(h))\lVert k(h) \rVert
$$

$Be_1(h) \in o_{h \to 0}(\lVert h \rVert)$ 이다. 또 $h \to 0$ 이면 $k(h) \to 0$ 이므로 $\eta(k(h)) \in o_{h \to 0}(1)$ 이고, $\lVert k(h) \rVert \leq \lVert A \rVert\lVert h \rVert + \lVert e_1(h) \rVert$ 이므로 $\lVert k(h) \rVert \in O_{h \to 0}(\lVert h \rVert)$ 이다. 여기서 $\lVert A \rVert$는 행렬의 연산자 노름이다. [[Properties of Big-O Like Notations]]에 의해 마지막 항은 $o_{h \to 0}(\lVert h \rVert)$ 이다. $\blacksquare$

일변수의 경우와 같이 $k(h) = 0$인 $h$는 $\eta(0) = 0$으로 처리된다.

## 참고문헌
(1) Stewart, 미분적분학
