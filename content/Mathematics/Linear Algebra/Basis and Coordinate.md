**Prerequisites**: [[Array over Field]]
## Basis

벡터공간 $A$의 부분공간 $V$를 생각해 보자. ($V$는 벡터공간이며 $A$의 벡터들 중 일부로 이루어진다.) 이때 $\mathcal{B} \subseteq A$가 $V$의 기저이기 위한 조건은 다음과 같다.

- $\mathcal{B}$에 속한 벡터들이 선형독립이다.
- $V = span\ \mathcal{B}$

$\mathcal{B}$에 속한 벡터를 기저벡터라고 한다. 어느 벡터공간의 기저벡터의 수는 기저에 관계없이 항상 동일하며 그 개수가 $V$의 차원을 나타낸다. 

## Coordinate Vector Space

어느 체 $F$에 대해 $F^n$을 다음과 같이 정의한다.

$$
F^n = \text{Arr}_{n}(F)
$$

이때 $F^n$은 벡터 공간의 성질을 만족한다. 이와 같이 배열을 통해 정의되는 벡터 공간을 coordinate space라고 한다.

## Coordinate

체 $F$ 위에 정의되는 벡터 공간 $A$와 그 부분공간 $V$를 생각하고 $V$의 기저 $\mathcal{B} = \{ b_1, ..., b_n \} \subseteq A$를 가정하자. 그러면 기저의 성질에 의해 어느 벡터 $v \in V$는 기저벡터의 선형조합으로 유일하게 표현된다. 즉 다음이 성립하도록 하는 $k = (k_1, ..., k_n) \in F^n$이 유일하게 존재한다.

$$
v = \sum_i k_i b_i
$$

이를 바탕으로 coordinate mapping $[\cdot]_\mathcal{B} : V \to F^n$ 은 다음을 만족하도록 정의되며 이때 $k$를 $v$의 $\mathcal{B}$에서의 coordinate(좌표)라고 한다.

$$
k = [v]_\mathcal{B}
$$

기저의 성질에 의해 coordinate mapping이 전단사함수이므로 이는 $V$와 $F^n$간의 isomorphism이다.

## Coordinate Space vs Coordinate Mapping

앞서서 논의한 바에 의하면 체 $F$ 에서 정의되는 $n$ 차원 벡터 공간 $V$는 coordinate vector space $F^n$과 동형이다. 하지만 우리가 $V$의 기저를 선택하는 것으로 그 벡터들의 표기법을 바꿀 수 있기 때문에 표기의 문제는 사용자의 것이다.

반면 우리가 coordinate vector space $F^n$에서 논의를 전개한다면 우리는 그것이 제공하는 하나의 정해진 표기법을 사용하기로 결정하는 것이다. 물론 coordinate vector space에서 standard basis를 사용하면 이 대수적 공간이 가지고 있는 표기법과 coordinate mapping이 제공하는 표기법이 동일하게 된다. 하지만 그렇다고 해서 우리가 coordinate vector space는 standard basis를 통한 coordinate mapping을 통해 표기된다고 말할 수는 없다. Coordinate vector space는 이미 표기법이 결정된 벡터 공간이다.

## Coordinate Mapping to a Higher Dimension

앞서서 살펴본 coordinate mapping은 체 $F$ 위에 정의되는 $n$ 차원 벡터 공간을 $F^n$에 대응시킨다. 만약 우리가 그것을 $F^{n+k} \ (k \geq 1)$ 에 대응시킨다면 우리에게는 남은 차원들에게 부여할 값이 필요해진다. 이와 같은 경우에 우리는 더 높은 차원의 공간에 더 낮은 차원의 공간을 매장(embedding) 하는 것이 된다.

## Footnote
- 체(field)는 *상식적인* 덧셈과 곱셈이 정의되는 대수적 대상으로 유리수, 실수, 복소수 등이 이에 해당한다. 이곳의 논의에서 추상적인 체의 성질은 별로 중요하지 않으므로 $F$를 $\mathbb{R}$인 것으로 생각해도 상관없다.

## References
- Wikipedia, Vector space - Coordinate space (https://en.wikipedia.org/wiki/Vector_space#Coordinate_space)
- David C. Lay, Linear Algebra and Its Applications (6th ed.), Pearson 