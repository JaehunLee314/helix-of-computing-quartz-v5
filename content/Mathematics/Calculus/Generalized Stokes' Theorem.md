이 글에서는 generalized Stokes' theorem의 개요를 살펴본다. 

## Differential Form and Integral

Differential form은 우리가 아는 적분을 일반화한 것이다. 보통 적분은 다음 순서로 수행한다.

1. 적분할 도형을 작은 사각형으로 분할하고, 각 사각형에 넓이, 유량, 질량 등의 값을 부여한다.
2. 도형이 구부러져 있다면 부여한 값의 일차근사를 사용한다. 각 조각의 오차가 조각의 크기보다 빠르게 작아지므로, 조각을 잘게 나눌수록 오차를 모두 더해도 그 합은 0으로 수렴하기 때문이다.
3. 각 사각형에 주어진 값을 모두 더하고, 분할을 한없이 잘게 할 때의 극한을 구한다. 이것이 적분이다.

이 과정은 다음과 같이 일반화할 수 있다.

1. 적분할 $n$차원 도형을 작은 $n$차원 평행체(parallelotope; 2차원에서는 평행사변형, 3차원에서는 평행육면체)로 분할한다. 평행체는 한 꼭짓점에서 뻗어 나가는 변 벡터 $n$개 $v_1, \dots, v_n$으로 결정된다. 각 평행체에 실수를 대응시키는 함수 $\omega(v_1, \dots, v_n)$을 differential $n$-form이라고 한다.
2. 도형이 구부러져 있다면 평행체의 변이 직선이 아니게 된다. 따라서 이때는 각 점 $p$의 접공간(tangent space) $T_pM$ 안의 평행체를 생각한다. 이것은 위의 일차근사와 같은 발상으로, 구부러진 조각을 그 점에서 가장 잘 근사하는 평평한 조각으로 바꾸는 것이다. 이때 form은 점마다 다를 수 있으므로 점 $p$에서의 form을 $\omega_p$라고 쓴다.
3. 각 평행체에 주어진 값을 모두 더하고 극한을 구한다. 이것이 적분이다.

$\omega_p$가 "조각에 값을 매기는 함수"로서 자연스러우려면 다음 두 성질을 만족해야 한다.

- **다중선형성(multilinearity).** 각 변 벡터에 대해 선형이다. 예를 들어 한 변을 두 배로 늘리면 값도 두 배가 되고, 평행체를 한 변을 따라 둘로 자르면 두 조각의 값의 합이 원래 값과 같다. 즉 적분의 가법성을 일차근사 수준에서 표현한 것이다.
- **교대성(alternating).** 두 변의 순서를 바꾸면 부호가 바뀐다. 변의 순서는 평행체의 방향(orientation)을 나타내므로, 방향이 반대인 조각에는 반대 부호의 값이 매겨진다. 특히 두 변이 같으면 평행체가 납작해지므로 값이 0이다.

정리하면, $n$차원 다양체 $M$ 위의 $n$-form $\omega$는 각 점 $p$마다 교대 다중선형 함수

$$
\omega_p : \underbrace{T_pM \times \cdots \times T_pM}_{n\text{개}} \to \mathbb{R}
$$

를 하나씩 대응시킨 것이고, 그 적분은 다음과 같이 생각할 수 있다.

$$
\int_M \omega = \lim_{|P| \to 0} \sum_{p \in P} \omega_p(v^p_1, \dots, v^p_n)
$$

여기서 $P$는 $M$을 분할한 각 조각의 기준점들의 집합이고, $v^p_1, \dots, v^p_n$은 점 $p$에 놓인 조각을 근사하는 평행체의 변이며, $|P|$는 조각 크기의 최댓값이다. 변들은 $M$ 위가 아니라 접공간 $T_pM$ 안에 있다는 점, 그리고 변의 순서는 $M$의 방향과 일치하도록 정한다는 점에 주의하자. 복잡해 보이지만, 결국 도형 위의 작은 조각들에 숫자를 부여하고 그것들을 합치는 연산을 기술한 것에 지나지 않는다.

### 기본 form $dx^i$와 쐐기곱

좌표 $x^i$는 각 점에 그 좌표값을 대응시키는 함수이다. $dx^i$는 벡터 $v$에 그 $i$번째 성분 $v^i$를 대응시키는 1-form이다. (뒤에서 보듯이, 정확히는 함수 $x^i$의 exterior derivative이다.) 예를 들어 $\mathbb{R}^3$에서 $dx(v) = v_x$이다.

1-form 두 개 $\alpha, \beta$로 2-form을 만드는 연산이 쐐기곱(wedge product)이다.

$$
(\alpha \wedge \beta)(u, v) = \alpha(u)\beta(v) - \alpha(v)\beta(u) = \det\begin{pmatrix} \alpha(u) & \alpha(v) \ \beta(u) & \beta(v) \end{pmatrix}
$$

기하학적으로 이는 $(\alpha(\cdot), \beta(\cdot))$를 좌표로 삼아 평행사변형을 평면에 투영했을 때 생기는 그림자의 부호 있는 넓이이다. 예를 들어 $(dx \wedge dy)(u, v)$는 $u, v$가 만드는 평행사변형을 $xy$평면에 투영한 넓이이다. 일반적으로 1-form $k$개의 쐐기곱은 $k \times k$ 행렬식으로 주어진다. 단순히 곱하지 않고 반대칭화하는 이유는 위의 교대성을 만족시키기 위해서다.

$\mathbb{R}^n$에서 모든 $k$-form은 $dx^{i_1} \wedge \cdots \wedge dx^{i_k}$들에 함수 계수를 곱해 더한 꼴로 쓸 수 있다. 예를 들어 $\mathbb{R}^3$의 2-form은 다음 꼴이다.

$$
\omega = P dy \wedge dz + Q dz \wedge dx + R dx \wedge dy
$$

## Exterior Derivative

$k$-form $\omega$에 exterior derivative를 취하면 $(k+1)$-form $d\omega$를 얻는다. $d\omega$를 이해하기 위해, $(k+1)$차원 평행체의 각 경계면이 $k$차원 평행체라는 사실을 생각해 보자. 그러면 우리는 $(k+1)$차원 평행체의 각 면에 $\omega$를 통해 값을 대응시킬 수 있다. $d\omega$는 이러한 값을 유도된 방향(induced orientation)에 따라 더한 것의 일차근사로 정의된다. 유도된 방향은 2차원에서는 경계를 반시계 방향으로 도는 것이고, 일반적으로는 바깥을 향하는 법선 벡터를 맨 앞에 붙였을 때 원래 평행체의 방향과 일치하도록 정한 것이다. 이 방향 덕분에 서로 마주 보는 면은 반대 부호로 더해진다.

구체적으로, 점 $p$에서 변 $u_1, \dots, u_{k+1}$로 만든 평행체를 생각하자. $u_i$를 뺀 나머지 $k$개의 변이 만드는 면은 $p$와 $p + u_i$에 하나씩, 서로 마주 보며 놓여 있다. 각 면에서는 그 면이 놓인 위치에서 $\omega$를 계산해야 한다. 마주 보는 두 면은 유도된 방향이 반대이므로, 그 둘의 기여는 $\omega_{p+u_i}$와 $\omega_p$의 차이로 묶인다. $U = \max_i |u_i|$라 하면 정의는 다음과 같다.

$$
\begin{aligned}
\sum_{i=1}^{k+1} &\sigma_i (\omega_{p+u_i}(u_1, \dots, u_{i-1}, u_{i+1}, \dots, u_{k+1}) - \omega_p(u_1, \dots, u_{i-1}, u_{i+1}, \dots, u_{k+1})) \\
&= d\omega_p(u_1, \dots, u_{k+1}) + \underset{U \to 0}{o}(U^{k+1})
\end{aligned}
$$

여기서 $\sigma_i$은 유도된 방향에서 오는 부호이다.

일차근사를 취하는 이유는 $d\omega$ 자체가 위치에 따라 변하는 효과를 걷어내기 위해서이다. 좌변은 평행체 전체에 걸친 양이므로, 평행체 안에서 $d\omega$가 변하는 만큼의 고차항을 포함한다. 일차근사, 즉 각 변 $u_i$에 대해 선형인 부분만 남기면 점 $p$ 하나에서의 값 $d\omega_p$를 얻는다. 이는 앞에서 $\omega_p(v_1, \dots, v_n)$을 $\int_P \omega$의 일차근사로 삼은 것과 같은 이유로 어차피 적분하면 $0$으로 수렴하기 때문이다.

앞선 식은 변을 $u_i = \varepsilon v_i$로 놓고 양변을 $\varepsilon^{k+1}$로 나누면 극한으로도 쓸 수 있다. 변 $\varepsilon v_1, \dots, \varepsilon v_{k+1}$로 만든 평행체를 $P_\varepsilon$이라 하면

$$
d\omega_p(v_1, \dots, v_{k+1}) = \lim_{\varepsilon \to 0} \frac{1}{\varepsilon^{k+1}} \int_{\partial P_\varepsilon} \omega
$$

이다. 이렇게 보면 $d\omega$의 정의는 곧 "아주 작은 평행체 $P$에서 $\int_P d\omega \approx \int_{\partial P} \omega$가 일차근사 수준에서 성립한다"는 말이다. 뒤의 Stokes 정리는 이것을 이어 붙인 것이다.

### 예시 1: $df = f'$

$k = 0$인 경우, 즉 실수선 위의 함수 $f$를 생각해 보자. 이를 위해 먼저 $0$-form에 대해 잠깐 논의할 필요가 있다.

앞서서 $k$-form $\omega_p(v_1, \dots, v_k)$은 점 $p$와 그 점에서의 평행체의 변 $v_1, ..., v_k$에 의존한다고 했다. 그런데 $k = 0$이면 평행체의 변이 하나도 없음으로 $w_p$는 입력값이 없는 함수가 된다. 그러면 우리는 $w_p$가 점 $p$에 의존하는 값이라고 생각해야 한다. 따라서 어떤 함수 $f$가 $0$-form이라는 것은 관례적으로 $w_p = f(p)$와 같이 정의된다는 것을 의미한다. 

이를 바탕으로 $df$에 대해 생각해 보자. 1차원 평행체는 점 $p$에서 변 $u$로 만든 선분 $[p, p+u]$이고, 그 경계면은 두 끝점이다. 유도된 방향은 끝점 $p + u$에 $+$, 시작점 $p$에 $-$이다. 정의의 좌변에서 $k = 0$이면 $i = 1$인 항 하나뿐이고, $u_1 = u$를 빼고 나면 괄호 안에 남는 벡터가 없다. 따라서 좌변은

$$\sigma_1 (f_{p+u} - f_p) = f(p+u) - f(p) = f'(p) u + \underset{U \to 0}{o}(U)$$

이다.  위 식의 일차근사 부분을 읽으면 $df_p(u) = f'(p) u$이다. $dx(u) = u$이므로

$$df = f' dx$$

이다. 즉 $df$는 미분계수 $f'$ 그 자체이고, 위 식은 도함수의 정의를 그대로 옮긴 것이다. 여기서 걷어낸 $o(U)$는 선분 위에서 $f'$이 변하는 효과이다.

### 예시 2: $\omega = x dy$

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

- **함수(0-form) $f$.** 예시 1을 $\mathbb{R}^n$으로 확장하면 $df_p(u)$는 $u$ 방향의 방향도함수이고, 다음이 성립한다. 좌표 함수 $x^i$에 적용하면 앞에서 본 $dx^i$를 얻는다.

$$
df = \sum_i \frac{\partial f}{\partial x^i} dx^i
$$

- **일반 $k$-form.**

$$
d\left(f dx^{i_1} \wedge \cdots \wedge dx^{i_k}\right) = df \wedge dx^{i_1} \wedge \cdots \wedge dx^{i_k}
$$

예를 들어 $d(x dy) = dx \wedge dy$로, 예시 2와 일치한다. 또 $\mathbb{R}^2$에서 $\omega = P dx + Q dy$이면 다음과 같다.

$$
d\omega = \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dx \wedge dy
$$

### $d^2 = 0$

$d$를 두 번 적용하면 항상 0이다. 정의에 따르면 $dd\omega$는 경계의 경계를 $\omega$로 잰 것인데, 경계의 경계는 비어 있기 때문이다. 예를 들어 정육면체 표면의 각 모서리는 인접한 두 면에서 서로 반대 방향으로 한 번씩 등장해 상쇄된다. 이 사실은 벡터 미적분학의 $\nabla \times (\nabla f) = 0$, $\nabla \cdot (\nabla \times F) = 0$에 해당한다.

## Stokes' Theorem

이제 generalized Stokes' theorem은 다음과 같은 정리이다.

**정리. Generalized Stokes' Theorem** $M$을 경계 $\partial M$을 가지는 방향 지어진(oriented) 콤팩트 $n$차원 다양체라 하고, $\partial M$에는 유도된 방향을 준다. $M$ 위의 매끄러운 $(n-1)$-form $\omega$에 대해 다음이 성립한다.

$$
\int_{\partial M} \omega = \int_M d\omega
$$

앞의 정의를 받아들이면 이 정리는 어느정도 직관적이다.

1. $M$을 작은 평행체들로 분할한다.
2. 각 평행체에서 $d\omega$의 값은 정의에 의해 그 평행체의 경계를 $\omega$로 잰 값과 일차근사 수준에서 같다. 따라서 $\int_M d\omega \approx \sum_{c} \int_{\partial c} \omega$이다. ($c$는 분할의 각 조각)
3. 내부의 면은 이웃한 두 조각에 서로 반대 방향으로 한 번씩 속하므로 그 값이 상쇄된다. 남는 것은 어느 조각과도 공유되지 않는 면, 즉 $M$의 경계 $\partial M$을 이루는 면뿐이다.
4. 분할을 잘게 하는 극한에서 근사가 정확해진다.

즉 exterior derivative는 "아주 작은 조각에서 Stokes 정리가 성립하도록" 정의된 것이고, generalized Stokes' theorem은 그것을 적분의 가법성으로 이어 붙인 결과이다.

특히 경계가 없는 다양체($\partial M = \varnothing$, 예를 들어 구면)에서는 항상 $\int_M d\omega = 0$이다.

## Applications

$\mathbb{R}^3$에서 form과 벡터 미적분학의 개념은 다음과 같이 대응된다.

| form $w$                                                        | $\int w$에 대응되는 개념                      | $dw$에 대응되는 개념               |
| --------------------------------------------------------------- | -------------------------------------- | --------------------------- |
| 0-form $f$                                                      | 점에서의 값                                 | gradient $\nabla f$         |
| 1-form $F_1 dx + F_2 dy + F_3 dz$                               | 일(work) $\int F \cdot d\mathbf{r}$     | curl $\nabla \times F$      |
| 2-form $F_1 dy \wedge dz + F_2 dz \wedge dx + F_3 dx \wedge dy$ | 유량(flux) $\iint F \cdot \mathbf{n} dA$ | divergence $\nabla \cdot F$ |
| 3-form $g dx \wedge dy \wedge dz$                               | 총량 $\iiint g dV$                       | 0                           |

이를 바탕으로 generalized Stokes' theorem은 벡터 미적분학의 정리들을 하나의 원리로 설명한다. 이하에서 벡터장 $F = (F_1, F_2, F_3)$에 대해 일과 유량으로 해석할 수 있는 다음의 미분형식들을 사용한다.

$$
\omega_F = F_1 dx + F_2 dy + F_3 dz, \qquad \eta_F = F_1 dy \wedge dz + F_2 dz \wedge dx + F_3 dx \wedge dy
$$

**미적분학의 기본정리.**

$$
\int_a^b f'(x) dx = \int_{[a,b]} df = \int_{\partial [a,b]} f = f(b) - f(a)
$$

$f'(x) dx$는 1-form $df$를 1차원에서 쓴 것이다. 구간 $[a, b]$의 경계는 두 점이고, 유도된 방향은 끝점 $b$에서 $+$, 시작점 $a$에서 $-$이다. 점 위의 적분은 그 점에서의 값을 부호와 함께 더하는 것이므로 식이 유도된다. 직관적으로는, 구간을 잘게 나눈 조각마다 $f$의 증가량을 더하면 내부의 점은 한 조각의 끝점이자 다음 조각의 시작점이어서 상쇄되고 양 끝만 남는다.

**선적분의 기본정리 (gradient theorem).** 곡선 $C$가 점 $a$에서 $b$까지 간다고 하자. 

$$
\int_C \nabla f \cdot d\mathbf{r} = \int_C \left( \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy + \frac{\partial f}{\partial z} dz \right) = \int_C df = \int_{\partial C} f = f(b) - f(a)
$$

결과가 양 끝점에만 의존하므로 gradient 장의 선적분은 경로에 무관하다.

**Green 정리.** 먼저 $d(P dx + Q dy)$를 계산한다. $dx \wedge dx = dy \wedge dy = 0$, $dy \wedge dx = -dx \wedge dy$를 쓰면

$$
d(P dx + Q dy) = dP \wedge dx + dQ \wedge dy = \frac{\partial P}{\partial y} dy \wedge dx + \frac{\partial Q}{\partial x} dx \wedge dy = \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx \wedge dy
$$

이다. 평면의 표준 방향에서 $dx \wedge dy$는 넓이 $dA$이므로

$$
\iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA = \int_D d(P dx + Q dy) = \int_{\partial D} P dx + Q dy = \oint_{\partial D} P dx + Q dy
$$

$\partial D$는 반시계 방향의 경계이다. 직관적으로, 영역을 작은 정사각형으로 나누어 각 정사각형의 둘레 순환을 모두 더하면 이웃한 정사각형이 공유하는 변은 반대 방향으로 두 번 지나므로 상쇄되고, 바깥 둘레만 남는다.

**(고전적) Stokes 정리.** 먼저 $d\omega_F$를 계산한다. $d(F_1 dx) = dF_1 \wedge dx$에서 $dx$를 포함한 항은 사라지므로

$$
d(F_1 dx) = \frac{\partial F_1}{\partial y} dy \wedge dx + \frac{\partial F_1}{\partial z} dz \wedge dx = -\frac{\partial F_1}{\partial y} dx \wedge dy + \frac{\partial F_1}{\partial z} dz \wedge dx
$$

이고, $F_2 dy$, $F_3 dz$도 같은 방법으로 계산해 모으면

$$
d\omega_F = \left( \frac{\partial F_3}{\partial y} - \frac{\partial F_2}{\partial z} \right) dy \wedge dz + \left( \frac{\partial F_1}{\partial z} - \frac{\partial F_3}{\partial x} \right) dz \wedge dx + \left( \frac{\partial F_2}{\partial x} - \frac{\partial F_1}{\partial y} \right) dx \wedge dy = \eta_{\nabla \times F}
$$

이다. 한편 곡면 위의 평행사변형 $(u, v)$에 대해 $\eta_G(u, v) = G \cdot (u \times v)$이고 $u \times v$는 법선 $\mathbf{n}$ 방향에 크기가 넓이이므로, 곡면 위에서 $\eta_G$를 적분하면 $\iint_S G \cdot \mathbf{n} dA$가 된다. 따라서

$$
\iint_S (\nabla \times F) \cdot \mathbf{n} dA = \int_S \eta_{\nabla \times F} = \int_S d\omega_F = \int_{\partial S} \omega_F = \oint_{\partial S} F \cdot d\mathbf{r}
$$

Green 정리는 곡면이 $xy$평면에 놓인 특수한 경우이다. 곡면이 휘어 있어도 작은 고리들의 순환을 더하면 내부의 변이 상쇄된다는 논리는 같다.

**발산 정리 (Gauss 정리).** 먼저 $d\eta_F$를 계산한다. $d(F_1 dy \wedge dz) = dF_1 \wedge dy \wedge dz$에서 $dy$나 $dz$가 두 번 나오는 항은 사라지므로 $\frac{\partial F_1}{\partial x} dx \wedge dy \wedge dz$만 남는다. 나머지 두 항도 마찬가지이며, $dy \wedge dz \wedge dx$와 $dz \wedge dx \wedge dy$는 $dx \wedge dy \wedge dz$의 순서를 순환시킨 것이라 부호가 바뀌지 않는다. 따라서

$$
d\eta_F = \left( \frac{\partial F_1}{\partial x} + \frac{\partial F_2}{\partial y} + \frac{\partial F_3}{\partial z} \right) dx \wedge dy \wedge dz = (\nabla \cdot F) dx \wedge dy \wedge dz
$$

이다. $dx \wedge dy \wedge dz$는 부피 $dV$이므로

$$
\iiint_V \nabla \cdot F dV = \int_V d\eta_F = \int_{\partial V} \eta_F = \iint_{\partial V} F \cdot \mathbf{n} dA
$$

$\partial V$에는 바깥을 향하는 법선을 준다. 직관적으로, 입체를 작은 상자로 나누어 각 상자에서 빠져나가는 유량을 모두 더하면 이웃한 상자가 공유하는 면에서는 한쪽에서 나간 양이 다른 쪽으로 들어온 양이므로 상쇄되고, 바깥 표면을 통과하는 유량만 남는다.

### 예: 원판의 넓이

Green 정리를 $\omega = x dy$에 적용하면 ($d\omega = dx \wedge dy$, 예시 2 참고) 영역의 넓이를 경계 위의 선적분으로 구할 수 있다.

$$
\text{넓이}(D) = \iint_D dx \wedge dy = \oint_{\partial D} x dy
$$

반지름 $R$인 원판이라면 경계를 $x = R\cos t$, $y = R\sin t$ ($0 \le t \le 2\pi$)로 매개화하여 $dy = R\cos t dt$이므로

$$
\oint_{\partial D} x dy = \int_0^{2\pi} R^2 \cos^2 t dt = \pi R^2.
$$

경계를 한 바퀴 따라가는 것만으로 넓이를 재는 면적계(planimeter)가 바로 이 원리로 작동한다.

### 예: 구의 겉넓이

2-form $\eta = x dy \wedge dz + y dz \wedge dx + z dx \wedge dy$를 생각하자. 이는 위치 벡터장 $\mathbf{r}$의 유량을 재는 form이다. $d\eta = 3 dx \wedge dy \wedge dz$이므로, 반지름 $R$인 공 $B$에 대해

$$
\int_{\partial B} \eta = \int_B 3 dV = 3 \cdot \frac{4}{3}\pi R^3 = 4\pi R^3.
$$

한편 구면 위에서는 $\mathbf{r} \cdot \mathbf{n} = R$이므로, $\eta$로 잰 값은 넓이의 $R$배이다. 따라서 구의 겉넓이는 $4\pi R^3 / R = 4\pi R^2$이다. 매개화 없이 부피만으로 겉넓이를 얻은 셈이다.
