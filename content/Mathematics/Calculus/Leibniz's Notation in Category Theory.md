## Category of Variables

앞서서 우리는 라이프니츠 표기법에서 변수의 의미를 살펴보았다. 이는 카테고리를 통해 다시 정의할 수 있다. 어떤 변수의 카테고리(category of variables) $V$는 다음과 같이 구성된다.

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

Category of variables $V$의 morphism이 어느 점 $x^* = (x_1^*, x_2^*, ...)$ 에서 미분가능하다고 하자. 이때 category of variables $V$에서 category of variables $W$로 가는 tangent functor $T_{x^*} \in V \Rightarrow_{\text{Cat}} W$ 를 정의할 수 있다.

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





