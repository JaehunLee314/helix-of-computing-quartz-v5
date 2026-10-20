**Prerequisites:** [[Numerator Layout of Matrix Calculus]]

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
$$$$
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

## 일변수함수의 연쇄법칙

변수 $x, y, z \in R$와 미분가능한 함수 $f, g$에 대해 $y = f(x), z = g(y)$라면 다음이 성립한다.

$$
\frac{dz}{dx} = \frac{dz}{dy}\frac{dy}{dx}
$$

이것을 증명하기 위해 먼저 일차근사의 성질을 생각해 보자.

_(일차근사)_

$y = f(x)$이고 $f$가 미분가능하다고 하자. 이때 다음과 같은 식을 생각해 보자.

$$
\Delta y = f'(x) \Delta x + \epsilon
$$

여기서 $\Delta y = f(x + \Delta x) - f(x)$이다. 양변을 $\Delta x$로 나누면:

$$
\frac{\Delta y}{\Delta x} = f'(x) + \frac{\epsilon}{\Delta x}
$$

이고 이때 $\Delta x \to 0$ 라고 하면 $\Delta y / \Delta x \to f'(x)$ 가 되므로 위 식에 의해 다음이 성립해야 한다.

$$
\lim_{\Delta x \to 0} \frac{\epsilon}{\Delta x} = 0
$$

이는 $\Delta y$를 $f'(x) \Delta x$로 근사할 때, 즉 일차근사할 때, 그 오차항이 $0$ 주변에서 $\Delta x$보다 빠르게 감소한다는 것을 의미한다.

_(연쇄법칙의 증명)_

$\Delta z, \Delta y$의 일차근사를 다음과 같이 적을 수 있다.

$$
\Delta z = g'(y) \Delta y + \epsilon_y \quad \Delta y = f'(x)\Delta x + \epsilon_x
$$

이들을 연립하면 다음을 얻는다.

$$
\Delta z = g'(y) f'(x) \Delta x + g'(y) \epsilon_x + \epsilon_y
$$

양변을 $\Delta x$로 나누면 다음과 같다.

$$
\frac{\Delta z}{\Delta x} = g'(y) f'(x) + g'(y) \frac{\epsilon_x}{\Delta x} + \frac{\epsilon_y}{\Delta x}
$$

이때 $\Delta x \to 0$ 이라고 하자. 먼저 앞서서 논의한 일차근사의 성질에 의해 $\epsilon_x / \Delta x \to 0$이 성립한다.

다음으로 $\epsilon_y / \Delta x$를 살펴보자. 오차항 $\epsilon_y$는 다음과 같이 적을 수 있다.

$$
\epsilon_y = \eta \Delta y
$$

($\Delta y \neq 0$이면 $\eta = \epsilon_y / \Delta y$이고, $\Delta y = 0$이면 $\Delta z = 0$이므로 $\epsilon_y = 0$이 되어 $\eta = 0$으로 둘 수 있다.) 한편 $\Delta x \to 0$이면 $\Delta y = f'(x)\Delta x + \epsilon_x \to 0$이고, 따라서 일차근사의 성질에 의해 $\eta \to 0$이다. 그러므로 다음이 성립한다.

$$
\lim_{\Delta x \to 0} \frac{\epsilon_y}{\Delta x} = \lim_{\Delta x \to 0} \eta \frac{\Delta y}{\Delta x} = 0 \times f'(x) = 0
$$

결과적으로 $\Delta x \to 0$일 때 우변의 두 오차항이 모두 $0$으로 수렴하므로 $\Delta z / \Delta x \to g'(y) f'(x)$이다. 즉 다음이 성립한다.

$$
\frac{dz}{dx} = \frac{dz}{dy}\frac{dy}{dx}
$$

## 다변수함수의 연쇄법칙

이번에는 $x \in R^l, y \in R^n, z \in R^m$과 미분가능한 함수 $f, g$에 대해 $y = f(x), z = g(y)$인 경우를 생각해 보자. 이런 경우에도 앞서서와 동일한 형태의 연쇄법칙이 성립한다.

$$
\frac{\partial z}{\partial x} = \frac{\partial z}{\partial y} \frac{\partial y}{\partial x}
$$

다변수함수의 연쇄법칙을 증명하는 것은 일변수함수의 경우와 비슷하다. 먼저 다변수함수에서의 일차근사를 고려하자.

_(일차근사)_

$x \in R^l, y \in R$이고 $y = f(x)$이며 $f$가 미분가능하다고 하자. 이때 다음과 같은 식을 생각하자.

$$
\Delta y = \frac{\partial y}{\partial x} \Delta x + \epsilon = \sum_k \frac{\partial y}{\partial x_k} \Delta x_k + \epsilon \quad (\epsilon \in R)
$$

여기서 $\epsilon$은 일차근사의 오차항이다. 이때 다변수함수의 미분가능성의 정의에 의해 다음이 성립해야 한다. (참고문헌 (1) 887p 참고.)

$$
\lim_{\Delta x \to 0} \frac{|\epsilon|}{|\Delta x|} = 0
$$

이는 일변수의 경우와 마찬가지로, 일차근사의 오차항이 $0$ 주변에서 $|\Delta x|$보다 빠르게 감소한다는 것을 의미한다. 이때 $\Delta x \to 0$은 $R^l$에서의 극한이므로, $\Delta x$가 원점으로 다가가는 모든 방향에 대해 이 성질이 성립해야 한다.

_($l = 1, m = 1$ 인 경우의 연쇄법칙 증명)_

이제 $x, z \in R, y \in R^n$인 경우의 연쇄법칙을 증명해 보자. 앞선 일차근사에 따라 다음과 같이 적을 수 있다.

$$
\Delta z = \frac{\partial z}{\partial y} \Delta y + \epsilon_y \quad \Delta y = \frac{\partial y}{\partial x} \Delta x + \epsilon_x \quad (\epsilon_y \in R, \ \epsilon_x \in R^n)
$$

여기서 $\epsilon_y$는 $z = g(y)$의 일차근사 오차항이고, $\epsilon_x$는 $y$의 각 성분 $y_k = f_k(x)$의 일차근사 오차항을 모은 벡터이다. 이제 두 식을 연립하면 다음과 같이 된다.

$$
\Delta z = \frac{\partial z}{\partial y} \frac{\partial y}{\partial x} \Delta x + \frac{\partial z}{\partial y} \epsilon_x + \epsilon_y
$$

양변을 $\Delta x$로 나누면 다음과 같다.

$$
\frac{\Delta z}{\Delta x} = \frac{\partial z}{\partial y} \frac{\partial y}{\partial x} + \frac{\partial z}{\partial y} \frac{\epsilon_x}{\Delta x } + \frac{\epsilon_y}{\Delta x }
$$

이때 $\Delta x \to 0$ 이라고 하자. 먼저 $x$는 스칼라이므로 각 성분 $y_k$에 일변수의 일차근사 성질을 적용하면 $\epsilon_x / \Delta x \to 0$이다.

다음으로 $\epsilon_y / \Delta x$를 살펴보자. 오차항 $\epsilon_y$는 다음과 같이 적을 수 있다.

$$
\epsilon_y = \eta |\Delta y|
$$

($\Delta y \neq 0$이면 $\eta = \epsilon_y / |\Delta y|$이고, $\Delta y = 0$이면 $\Delta z = 0$이므로 $\epsilon_y = 0$이 되어 $\eta = 0$으로 둘 수 있다.) 한편 $\Delta x \to 0$이면 $\Delta y = \frac{\partial y}{\partial x} \Delta x + \epsilon_x \to 0$이고, 따라서 일차근사의 성질에 의해 $\eta \to 0$이다. 그러므로 다음이 성립한다.

$$ \lim_{\Delta x \to 0} \left| \frac{\epsilon_y}{\Delta x} \right| = \lim_{\Delta x \to 0} |\eta| \left| \frac{\Delta y}{\Delta x} \right| = 0 \times \left| \frac{\partial y}{\partial x} \right| = 0 $$

결과적으로 $\Delta x \to 0$일 때 우변의 두 오차항이 모두 $0$으로 수렴하므로 다음을 얻으며, 이로써 증명이 완료된다.

$$
\frac{\partial z}{\partial x} = \frac{\partial z}{\partial y} \frac{\partial y}{\partial x}
$$

나머지 경우에 대한 증명은 정의를 이용하면 된다.

## 참고문헌

(1) Stewart, 미분적분학