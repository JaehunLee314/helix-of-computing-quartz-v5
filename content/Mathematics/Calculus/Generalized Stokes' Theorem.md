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

$k$-form $\omega$에 exterior derivative를 취하면 $(k+1)$-form $d\omega$를 얻는다. $k$-form은 $k$차원 조각에 값을 매기는데, $(k+1)$차원 평행체의 경계는 $k$차원 면들로 이루어져 있으므로 $\omega$로 그 경계를 잴 수 있다. 이것이 $d\omega$의 정의이다.

> $d\omega$는 $(k+1)$차원 평행체에, 그 경계면들을 $\omega$로 잰 값의 합을 대응시킨다.

이때 각 경계면에는 유도된 방향(induced orientation)을 준다. 2차원에서는 경계를 반시계 방향으로 도는 것이고, 일반적으로는 바깥을 향하는 법선 벡터를 맨 앞에 붙였을 때 원래 평행체의 방향과 일치하도록 정한다. 이 방향 덕분에 서로 마주 보는 면은 반대 부호로 더해진다.

정확히 쓰면, 점 $p$에서 변 $\varepsilon v_1, \dots, \varepsilon v_{k+1}$로 만든 작은 평행체를 $P_\varepsilon$이라 할 때

$$
d\omega_p(v_1, \dots, v_{k+1}) = \lim_{\varepsilon \to 0} \frac{1}{\varepsilon^{k+1}} \int_{\partial P_\varepsilon} \omega
$$

이다.

$\varepsilon^{k+1}$로 나누는 이유는 다음과 같다. 각 면의 크기는 $\varepsilon^k$ 정도이지만, $\omega$가 위치에 따라 변하지 않는다면 마주 보는 두 면의 값은 정확히 상쇄된다. 살아남는 것은 두 면 사이에서 $\omega$가 변한 양뿐이고, 이는 (면의 크기 $\varepsilon^k$) × (면 사이의 거리 $\varepsilon$) × ($\omega$의 변화율) 정도의 크기이다. 따라서 $d\omega$는 "경계를 따라 $\omega$가 상쇄되지 않고 남는 양을 단위 부피당 잰 것"이며, 그런 의미에서 $\omega$의 미분이다.

### 예시 1: 상수 form

1-form $\omega(v) = v_1$, 즉 $\omega = dx$를 생각해 보자. $\omega$는 벡터의 첫 번째 성분을 취한다. 원점에서 시작하는 단위 정사각형의 경계를 반시계 방향으로 돌면 각 변의 벡터는 차례로 $e_1, e_2, -e_1, -e_2$이고, 각각의 첫 번째 성분을 더하면 다음과 같다.

$$
1 + 0 + (-1) + 0 = 0
$$

$\omega$가 위치에 따라 변하지 않으므로 마주 보는 변이 정확히 상쇄된 것이다. 일반적으로 계수가 상수인 form의 exterior derivative는 0이다. 특히 $d(dx) = 0$이다.

### 예시 2: $\omega = x dy$

이번에는 계수가 위치에 따라 변하는 경우이다. 원점에서 시작하는 한 변의 길이 $\varepsilon$인 정사각형의 경계를 반시계 방향으로 돈다.

|변|변 벡터의 $dy$ 값|그 변에서의 $x$ 값|기여|
|---|---|---|---|
|아래 (오른쪽으로)|$0$|–|$0$|
|오른쪽 (위로)|$\varepsilon$|$\varepsilon$|$\varepsilon^2$|
|위 (왼쪽으로)|$0$|–|$0$|
|왼쪽 (아래로)|$-\varepsilon$|$0$|$0$|

합은 $\varepsilon^2$이고, 이를 $\varepsilon^2$으로 나누면 $1$이다. 즉 $d(x dy)(e_1, e_2) = 1$이고 $d(x dy) = dx \wedge dy$이다. 오른쪽 변과 왼쪽 변에서 $x$ 값이 달라 상쇄가 깨진 만큼이 남은 것이다.

### 일반 공식

같은 계산을 일반화하면 다음을 얻는다.

- **함수(0-form) $f$.** 점 $a$에서 $b$로 가는 1차원 조각의 경계는 "끝점 $b$에 $+$, 시작점 $a$에 $-$"이므로 $df(\text{경로}) = f(b) - f(a)$이다. 일차근사로는 $df(v)$가 $v$ 방향의 방향도함수이고, 다음이 성립한다. 좌표 함수 $x^i$에 적용하면 앞에서 본 $dx^i$를 얻는다.

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

앞의 정의를 받아들이면 이 정리는 거의 자명하다.

1. $M$을 작은 평행체들로 분할한다.
2. 각 평행체에서 $d\omega$의 값은 정의에 의해 그 평행체의 경계를 $\omega$로 잰 값과 일차근사 수준에서 같다. 따라서 $\int_M d\omega \approx \sum_{c} \int_{\partial c} \omega$이다. ($c$는 분할의 각 조각)
3. 내부의 면은 이웃한 두 조각에 서로 반대 방향으로 한 번씩 속하므로 그 값이 상쇄된다. 남는 것은 어느 조각과도 공유되지 않는 면, 즉 $M$의 경계 $\partial M$을 이루는 면뿐이다.
4. 분할을 잘게 하는 극한에서 근사가 정확해진다.

즉 exterior derivative는 "아주 작은 조각에서 Stokes 정리가 성립하도록" 정의된 것이고, generalized Stokes' theorem은 그것을 적분의 가법성으로 이어 붙인 결과이다.

특히 경계가 없는 다양체($\partial M = \varnothing$, 예를 들어 구면)에서는 항상 $\int_M d\omega = 0$이다.

## Applications

앞선 정리는 벡터 미적분학의 중요한 정리 대부분을 일관되게 설명한다. $\mathbb{R}^3$에서 form과 벡터 미적분학의 대상은 다음과 같이 대응한다.

|form|대응하는 대상|적분의 의미|$d$의 의미|
|---|---|---|---|
|0-form $f$|함수|점에서의 값|gradient $\nabla f$|
|1-form $F_1 dx + F_2 dy + F_3 dz$|벡터장 $F$|일(work) $\int F \cdot d\mathbf{r}$|curl $\nabla \times F$|
|2-form $F_1 dy \wedge dz + F_2 dz \wedge dx + F_3 dx \wedge dy$|벡터장 $F$|유량(flux) $\iint F \cdot \mathbf{n} dA$|divergence $\nabla \cdot F$|
|3-form $g dx \wedge dy \wedge dz$|밀도 함수 $g$|총량 $\iiint g dV$|(항상 0)|

이 대응 아래에서 generalized Stokes' theorem 하나가 다음 정리들이 된다.

**미적분학의 기본정리.** $M = [a, b]$, $\omega = f$인 경우이다. $\partial M$은 "$b$에 $+$, $a$에 $-$"이므로

$$
\int_a^b f'(x) dx = f(b) - f(a).
$$

**선적분의 기본정리 (gradient theorem).** $M$이 $a$에서 $b$로 가는 곡선 $C$이고 $\omega = f$인 경우이다.

$$
\int_C \nabla f \cdot d\mathbf{r} = f(b) - f(a)
$$

**Green 정리.** $M$이 평면 영역 $D$이고 $\omega = P dx + Q dy$인 경우이다.

$$
\oint_{\partial D} P dx + Q dy = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA
$$

**(고전적) Stokes 정리.** $M$이 $\mathbb{R}^3$ 안의 곡면 $S$이고 $\omega$가 1-form인 경우이다.

$$
\oint_{\partial S} F \cdot d\mathbf{r} = \iint_S (\nabla \times F) \cdot \mathbf{n} dA
$$

**발산 정리 (Gauss 정리).** $M$이 $\mathbb{R}^3$ 안의 입체 $V$이고 $\omega$가 2-form인 경우이다.

$$
\iint_{\partial V} F \cdot \mathbf{n} dA = \iiint_V \nabla \cdot F dV
$$

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
