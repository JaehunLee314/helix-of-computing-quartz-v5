**Prerequisites:** [[Big-O Like Notations]]

이 글에서는 미분형식(differential form)을 작은 조각에 값을 매기는 측정 장치로 이해하고, 그 위에서 정의되는 exterior derivative와 wedge product를 살펴본다.

## Integral and Differential Form

Differential form은 우리가 아는 적분을 일반화한 것이다. 보통 적분은 다음 순서로 수행한다.

1. 적분할 도형을 작은 사각형으로 분할하고, 각 사각형에 넓이, 유량, 질량 등의 값을 부여한다.
2. 도형이 구부러져 있다면 부여한 값의 일차근사를 사용한다. 각 조각의 오차가 조각의 위치와 무관하게 조각의 크기보다 빠르게 작아지므로, 조각을 잘게 나눌수록 오차를 모두 더해도 그 합은 0으로 수렴하기 때문이다.
3. 각 사각형에 주어진 값을 모두 더하고, 분할을 한없이 잘게 할 때의 극한을 구한다. 이것이 적분이다.

이 과정은 다음과 같이 일반화할 수 있다.

1. 적분할 $n$차원 도형을 작은 $n$차원 평행체(parallelotope; 2차원에서는 평행사변형, 3차원에서는 평행육면체)로 분할한다. 평행체는 한 꼭짓점 $p$에서 뻗어 나가는 변 벡터 $n$개 $v_1, \dots, v_n$으로 결정된다. 각 평행체에 실수를 대응시키는 함수 $\omega_p(v_1, \dots, v_n)$를 differential $n$-form이라고 한다.
2. 도형이 구부러져 있다면 평행체의 변이 직선이 아니게 된다. 따라서 이때는 각 점 $p$의 접공간(tangent space) $T_pM$ 안의 평행체를 생각한다. 이것은 위의 일차근사와 같은 발상으로, 구부러진 조각을 그 점에서 가장 잘 근사하는 평평한 조각으로 바꾸는 것이다.
3. 각 평행체에 주어진 값을 모두 더하고 극한을 구한다. 이것이 적분이다.

$\omega_p$가 "조각에 값을 매기는 함수"로서 자연스러우려면 다음 두 성질을 만족해야 한다.

- **다중선형성(multilinearity).** 각 변 벡터에 대해 선형이다. 예를 들어 한 변을 두 배로 늘리면 값도 두 배가 되고, 평행체를 한 변을 따라 둘로 자르면 두 조각의 값의 합이 원래 값과 같다. 즉 적분의 가법성을 일차근사 수준에서 표현한 것이다.
- **교대성(alternating).** 두 변의 순서를 바꾸면 부호가 바뀐다. 변의 순서는 평행체의 방향(orientation)을 나타내므로, 방향이 반대인 조각에는 반대 부호의 값이 매겨진다. 특히 두 변이 같으면 평행체가 납작해지므로 값이 0이다.

정리하면, $n$차원 다양체 $M$ 위의 $n$-form $\omega$는 각 점 $p$마다 교대 다중선형 함수

$$
\omega_p : \underbrace{T_pM \times \cdots \times T_pM}_{n\text{ times}} \to \mathbb{R}
$$

를 하나씩 대응시킨 것이고, 그 적분은 다음과 같이 생각할 수 있다.

$$
\int_M \omega = \lim_{|P| \to 0} \sum_{p \in P} \omega_p(v^p_1, \dots, v^p_n)
$$

여기서 $P$는 $M$을 분할한 각 조각의 기준점들의 집합이고, $v^p_1, \dots, v^p_n$은 점 $p$에 놓인 조각을 근사하는 평행체의 변이며, $|P|$는 조각 크기의 최댓값이다. 변들은 $M$ 위가 아니라 접공간 $T_pM$ 안에 있다는 점, 그리고 변의 순서는 $M$의 방향과 일치하도록 정한다는 점에 주의하자. 복잡해 보이지만, 결국 도형 위의 작은 조각들에 숫자를 부여하고 그것들을 합치는 연산을 기술한 것에 지나지 않는다.

이처럼 $k$-form $\omega_p(v_1, \dots, v_k)$는 두 가지를 입력으로 받는다. 하나는 조각이 어디에 있는지를 나타내는 점 $p$(아래첨자)이고, 다른 하나는 조각의 모양을 나타내는 변 $v_1, \dots, v_k$(괄호 안)이다. 만약 $k=0$인 경우에 $\omega$는 오직 조각의 위치만을 입력받고 변을 입력받지 않는다. 물론 우리는 이것이 0차원 평행체인 점에 대해 값을 부여하는 함수인 것으로 생각할 수 있다. 이하에서 별다른 언급이 없으면 실숫값 함수 $f$는 0-form을 의미하는 것으로 생각하고 $f_p = f(p)$로 표기한다.

## Definition of Exterior Derivative

$k$-form $\omega$에 exterior derivative를 취하면 $(k+1)$-form $d\omega$를 얻는다. $d\omega$를 이해하기 위해, $(k+1)$차원 평행체의 각 경계면이 $k$차원 평행체라는 사실을 생각해 보자. 그러면 우리는 $(k+1)$차원 평행체의 각 면에 $\omega$를 통해 값을 대응시킬 수 있다. $d\omega$는 이러한 값을 유도된 방향(induced orientation)에 따라 더한 것의 일차근사로 정의된다. 유도된 방향은 2차원에서는 경계를 반시계 방향으로 도는 것이고, 일반적으로는 바깥을 향하는 법선 벡터를 맨 앞에 붙였을 때 원래 평행체의 방향과 일치하도록 정한 것이다. 이 방향 덕분에 서로 마주 보는 면은 반대 부호로 더해진다.

구체적으로, 점 $p$에서 변 $u_1, \dots, u_{k+1}$로 만든 평행체를 생각하자. $u_i$를 뺀 나머지 $k$개의 변이 만드는 면은 $p$와 $p + u_i$에 하나씩, 서로 마주 보며 놓여 있다. 각 면에서는 그 면이 놓인 위치에서 $\omega$를 계산해야 한다. 마주 보는 두 면은 유도된 방향이 반대이므로, 그 둘의 기여는 $\omega_{p+u_i}$와 $\omega_p$의 차이로 묶인다. $U = \max_i \lVert u_i \rVert$라 하면 정의는 다음과 같다.

$$
\begin{aligned} \sum_{i=1}^{k+1} &\sigma_i (\omega_{p+u_i}(u_1, \dots, u_{i-1}, u_{i+1}, \dots, u_{k+1}) - \omega_p(u_1, \dots, u_{i-1}, u_{i+1}, \dots, u_{k+1})) \\ &= d\omega_p(u_1, \dots, u_{k+1}) + \underset{U \to 0}o (U^{k+1}) \end{aligned}
$$

여기서 $\sigma_i$는 유도된 방향에서 오는 부호이다.

일차근사를 취하는 이유는 $d\omega$ 자체가 위치에 따라 변하는 효과를 제거하기 위해서다. 좌변은 평행체 전체에 걸친 양이므로, 평행체 안에서 $d\omega$가 변하는 만큼의 고차항을 포함한다. 일차근사, 즉 각 변 $u_i$에 대해 선형인 부분만 남기면 점 $p$ 하나에서의 값 $d\omega_p$를 얻는다. 이는 앞에서 $\omega_p(v_1, \dots, v_n)$을 $\int_P \omega$의 일차근사로 삼은 것과 같은 이유로 어차피 적분하면 $0$으로 수렴하기 때문이다.

앞선 식은 변을 $u_i = \varepsilon v_i$로 놓고 양변을 $\varepsilon^{k+1}$로 나누면 극한으로도 쓸 수 있다. 변 $\varepsilon v_1, \dots, \varepsilon v_{k+1}$로 만든 평행체를 $P_\varepsilon$이라 하면

$$
d\omega_p(v_1, \dots, v_{k+1}) = \lim_{\varepsilon \to 0} \frac{1}{\varepsilon^{k+1}} \int_{\partial P_\varepsilon} \omega
$$

이다. 이렇게 보면 $d\omega$의 정의는 곧 "아주 작은 평행체 $P$에서 $\int_P d\omega \approx \int_{\partial P} \omega$가 일차근사 수준에서 성립한다"는 말이다. [[Generalized Stokes' Theorem]]은 이것을 이어 붙인 것이다.

## Notation regarding Differential 0-Form

어느 1-form $\omega$가 0-form $f$와 1-form $\alpha$에 대해 다음과 같이 정의된다고 해 보자.

$$
\omega = f \alpha
$$

그러면 $\omega$를 점 $p$와 벡터 $v$에 대해 계산한 값은 다음과 같이 주어진다.

$$
\omega_p (v) = f_p \alpha_p(v) = f(p)\alpha_p(v)
$$

이와 같이 0-form이 식에 포함되어 있으면 점 $p$에 대해 계산해야 함에 유의하자.

## Coordinate Function and Its Differential

좌표 $x^i$는 각 점에 그 좌표값을 대응시키는 함수로 정의된다. 예를 들어 $\mathbb{R}^3$에서 $x(p)$는 점 $p$의 $x$좌표이다. 함수는 0-form으로 취급되므로, 앞의 정의에 따라 exterior derivative $dx^i$를 취할 수 있다.

$k = 0$이면 평행체는 점 $p$에서 변 $v$로 만든 선분 $[p, p+v]$이고, 그 경계는 끝점 $p + v$와 시작점 $p$이며 유도된 방향은 각각 $+$, $-$이다. 따라서 정의의 좌변은

$$
x^i(p+v) - x^i(p) = v^i
$$

이다. 좌변이 이미 $v$에 대해 선형이므로 오차항 없이 다음을 얻는다.

$$
dx^i_p(v) = v^i
$$

즉 $dx^i$는 벡터 $v$에 그 $i$번째 성분 $v^i$를 대응시키는 1-form이다. 예를 들어 $\mathbb{R}^3$에서 $dx(v) = v_x$이다. $dx^i_p$는 점 $p$에 의존하지 않는다.

### 예시: $df = f'$

실수선 위의 함수 $f$에 대해 정의의 좌변은

$$
f(p+v) - f(p) = f'(p) v + \underset{v \to 0}o (v)
$$

이다. 일차근사 부분을 읽으면 $df_p(v) = f'(p) v$이고, $dx(v) = v$이므로

$$
df = f' dx
$$

이다. 즉 $df$는 미분계수 $f'$ 그 자체이고, 위 식은 도함수의 정의를 그대로 옮긴 것이다. 여기서 걷어낸 $o_{v \to 0}(v)$는 선분 위에서 $f'$이 변하는 효과이다.

이를 $\mathbb{R}^n$으로 확장하면 $df_p(v)$는 $v$ 방향의 방향도함수이고, 다음이 성립한다. 좌표 함수 $x^i$에 적용하면 앞에서 본 $dx^i$를 얻는다.

$$
df = \sum_i \frac{\partial f}{\partial x^i} dx^i
$$

## Wedge Product

1-form 두 개 $\alpha, \beta$로 2-form을 만드는 연산이 쐐기곱(wedge product)이다. 쐐기곱은 각 점 $p$에서 따로 계산한다.

$$
(\alpha \wedge \beta)_p(u, v) = \alpha_p(u)\beta_p(v) - \alpha_p(v)\beta_p(u) = \det\begin{pmatrix} \alpha_p(u) & \alpha_p(v) \ \beta_p(u) & \beta_p(v) \end{pmatrix}
$$

기하학적으로 이는 $(\alpha(\cdot), \beta(\cdot))$를 좌표로 삼아 평행사변형을 평면에 투영했을 때 생기는 그림자의 부호 있는 넓이이다. 예를 들어 $(dx \wedge dy)(u, v)$는 $u, v$가 만드는 평행사변형을 $xy$평면에 투영한 넓이이다. 일반적으로 1-form $k$개의 쐐기곱은 $k \times k$ 행렬식으로 주어진다. 단순히 곱하지 않고 반대칭화하는 이유는 교대성을 만족시키기 위해서다.

$\mathbb{R}^n$에서 모든 $k$-form은 $dx^{i_1} \wedge \cdots \wedge dx^{i_k}$들에 함수 계수를 곱해 더한 꼴로 쓸 수 있다. 예를 들어 $\mathbb{R}^3$의 2-form은 다음 꼴이다.

$$
\omega = P dy \wedge dz + Q dz \wedge dx + R dx \wedge dy
$$

## Properties of Exterior Derivative

### 예시: $d(x dy) = dx \wedge dy$

$\mathbb{R}^2$에서 $\omega = x dy$, 즉 $\omega_q(v) = x(q) v_y$를 생각하자. ($v_y$는 $v$의 $y$ 성분이다.) 점 $p$에서 변 $u_1 = (a_1, b_1)$, $u_2 = (a_2, b_2)$로 만든 평행사변형을 잡으면

$$
(\omega_{p+u} - \omega_p)(v) = \big(x(p+u) - x(p)\big) v_y = u_x v_y
$$

이므로, $\sigma_1 = 1$, $\sigma_2 = -1$을 넣어 정의의 좌변을 계산하면

$$
(\omega_{p+u_1} - \omega_p)(u_2) - (\omega_{p+u_2} - \omega_p)(u_1) = a_1 b_2 - a_2 b_1 = (dx \wedge dy)(u_1, u_2)
$$

이다. 이 경우 좌변이 이미 각 변에 대해 선형이어서 오차항이 없고, 따라서 $d(x dy) = dx \wedge dy$이다. $u_1$ 방향으로 떨어진 두 변에서는 $x$ 값이 $a_1$만큼 달라 상쇄가 깨지고, $u_2$ 방향으로 떨어진 두 변에서는 $a_2$만큼 달라 상쇄가 깨진다. 그 차이가 평행사변형의 넓이로 남은 것이다.

### 일반 공식

같은 계산을 일반화하면 다음을 얻는다.

$$
d\left(f dx^{i_1} \wedge \cdots \wedge dx^{i_k}\right) = df \wedge dx^{i_1} \wedge \cdots \wedge dx^{i_k}
$$

예를 들어 $d(x dy) = dx \wedge dy$로, 위의 예시와 일치한다. 또 $\mathbb{R}^2$에서 $\omega = P dx + Q dy$이면 다음과 같다.

$$
d\omega = \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dx \wedge dy
$$

### $d^2 = 0$

$d$를 두 번 적용하면 항상 0이다. 정의에 따르면 $dd\omega$는 경계의 경계를 $\omega$로 잰 것인데, 경계의 경계는 비어 있기 때문이다. 예를 들어 정육면체 표면의 각 모서리는 인접한 두 면에서 서로 반대 방향으로 한 번씩 등장해 상쇄된다. 이 사실은 벡터 미적분학의 $\nabla \times (\nabla f) = 0$, $\nabla \cdot (\nabla \times F) = 0$에 해당한다.