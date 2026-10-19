## Intuition for Variable

변수(variable)라는 단어는 수학에서 많은 의미로 사용된다. 여기서는 그 정의 중 비교적 편리한 것을 설명한다. 이때 변수의 정의는 다음과 같다.

- 변수는 그것을 나타내는 문자와, 그것이 만족해야 하는 성질로 정의된다.
- 변수를 나타내는 문자를 포함한 문장은, 그 문자를 해당 성질을 만족하는 임의의 대상으로 치환했을 때 항상 참이 되는 경우에만 참으로 규정한다.

예를 들어 변수 $p$는 소수여야 한다는 성질에 의해 정의된 수 있다. 그러면 $p$를 사용한 문장 "$p + 1$은 소수이다"와 같은 것을 생각할 수 있는데 이는 거짓이다. 왜냐하면 $p := 3$ 으로 치환하면 $p + 1 = 4$는 소수가 아니기 때문이다. 

여러 변수를 동시에 다루는 경우에 하나의 변수가 다른 변수에 의존적으로 정의되는 경우가 있다. 이런 때에는 위의 두 번째 조건을 조금 더 자세히, 다음과 같이 적을 필요가 있다.

- 변수를 나타내는 문자들을 포함한 문장은, 그 문자들을 해당 성질들을 모두 만족하는 임의의 대상들로 치환했을 때 항상 참이 되는 경우에만 참으로 규정한다.

예를 들어 변수 $x, y \in R$이고 $y = x^2$이라고 정의한다고 해 보자. 그러면 $x = 2 \to y = 1$ 이라는 문장은 거짓이다. 왜냐하면 가정에 의해 $x = 2$이면 $y = 4$로 반드시 치환되어야 하기 때문이다.

이러한 해석에서 상수란 등식을 성질로 가지는 변수이다.

## Category of Variables

서로 함수관계가 있는 변수들에 대한 해석은 카테고리를 통해 할 수 있다. 어떤 변수의 카테고리(category of variables) $V$는 다음과 같이 구성된다. 여기서 두 변수 간의 morphism은 유일하다고 가정한다.

### Objects

$V$의 object는  $x_1, x_2, x_3, ...$ 등의 변수이다. 각 변수는 어떤 집합에 의해 bound 되는데 이를 $x_i \in X_i$ 와 같이 대문자를 사용해 적는다.

### Morphisms

$V$의 morphism은 두 변수 사이에 유일하게 정의되는 함수이다. 즉 $f \in x_i \Rightarrow_V x_j$ 는 $f \in X_i \Rightarrow_{\text{Set}} X_j$ 인 함수이며, $x_j = f(x_i)$가 성립한다. 두 변수 간의 morphism이 유일함으로 $x_j$에서 $x_j$로의 morphism을 $f_{ij}$ 와 같이 적는다.

### Composition & Identity

$V$의 composition은 함수의 composition이다. 즉 다음과 같이 정의된다.

$$
t \in X_i \to (f_{ij} ; f_{jk})(t) = f_{jk}(f_{ij}(t))
$$

이때 두 변수 간의 morphism은 유일함으로 다음이 성립한다.

$$
f_{ij};f_{jk} = f_{ik}
$$

한편 $V$에서의 identity morphism은 identity function이다. 즉 다음과 같다.

$$
t \in X_i \to id_{x_i} (t) = f_{ii} (t) = t
$$

## Tangent Functor

이제 이러한 정의에서 어떻게 미분을 생각할 수 있는지 살펴보자. Category of variables $V$의 morphism이 어느 점 $x^* = (x_1^*, x_2^*, ...)$ 에서 미분가능하다고 하자. 이때 category of variables $V$에서 category of variables $W$로 가는 tangent functor $T_{x^*} \in V \Rightarrow_{\text{Cat}} W$ 를 정의할 수 있다.

### Object Mapping

Tangent functor는 $V$의 각 variable을 $W$의 variable에 대응시킨다.

$$
T_{x^*} (x_i) = dx_i
$$

### Morphism Mapping

Tangent functor는 $V$의 각 morphism을 $W$의 각 morphism으로 대응시킨다.

$$
T_{x^*} (f_{ij}) = g_{ij} \quad where \quad t \in X_i \to g_{ij}(t) = f_{ij}'(x_i^*) \cdot t
$$

### Tangent Functor의 성질

이제 tangent functor가 identity와 composition을 보존하는지 살펴보자. 

*(Identity)*
$$
T_{x^*}(id_{x_i})(t) = id_{x_i}'(x_i^*) \cdot t = 1 \cdot t = t
$$

따라서 identity를 identity function으로 mapping 함으로 identity를 보존한다.

*(Composition)*
$$
(T_{x^*}(f_{ij} ; f_{jk}))(t)=(T_{x^*}(f_{ik}))(t) = f_{ik}'(x_i^*) \cdot t
$$
$$
(T_{x^*}(f_{ij});T_{x^*}(f_{jk}))(t) = f_{jk}'(x_j^*) \cdot f_{ij}'(x_i^*) \cdot t = f_{jk}'(f_{ij}(x_i^*)) \ \cdot f_{ij}'(x_i^*) \cdot t= f_{ik}'(x_i^*) \cdot t \quad (\because \text{chain rule})
$$

두 식이 같음으로 tangent functor는 composition을 보존한다.

### 미분의 성질

이제 우리에게 잘 알려진 미분의 성질들을 $T_{x^*} V$ 에서 다음과 같이 적을 수 있다.

$$
\left . \frac{dy}{dx} \right |_{x := x^*} = f_{xy}'(x^*)
$$
$$
\frac{dy}{dx} = \frac{1}{\frac{dx}{dy}}
$$
$$
\frac{dz}{dx}=\frac{dz}{dy}\frac{dy}{dx}
$$

## 다차원 공간에서

보다 다차원 공간에서 우리는 $f_{ij}'(x_i^*)$ 대신 Jacobian matrix를 사용하는 것으로 위의 논의를 일반화할 수 있다.

## 결론

Category of variables에 tangent functor를 적용하면 미소 변수들에 대한 직관적인 이해를 얻는다.

## Footnote
- Category에 대한 논의는 [[Category]] 를 참고하라.
- 미분기하학에서 다루는 미분 형식(differential form)은 본 글에서 논의한 미소 변수 공간(tangent space)의 쌍대 공간(dual space)으로 정의된다.

## References
(1) David Bachman, A Geometric Approach to Differential Forms





