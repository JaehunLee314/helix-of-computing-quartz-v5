**Prerequisites:** [[Change of Basis]], [[Orthogonal Projection]]

이곳에서는 행렬곱을 이해하는 몇 가지 방법들을 살펴본다. 이하에서 $A \in F^{m \times n}, v \in F^n$이며 $[A]_i$는 $A$의 $i$번째 행을 $[A]^j$는 $A$의 $j$번째 열을 나타낸다. $F$는 실수나 복소수이다.

## As a Linear Combination

행렬곱은 행렬의 각 열을 $v$의 원소를 계수로 하여 선형결합하는 것으로 이해할 수 있다. 이를 식으로 적으면 다음과 같다.

$$
Av = \sum_j [A]^j v_j
$$

## As a Change of Basis

만약 행렬의 각 열이 선형독립이라면 행렬곱은 행렬의 각 열이 기저가 되는 벡터공간에서 표준기저 $\mathcal{E}$로 가는 change of coordinate 인 것으로 이해할 수 있다. 이를 식으로 적으면 다음과 같다.

$$
Av = \underset{\{[A]^1, ..., [A]^n\} \to \mathcal{E}}{P} v
$$

## As an Inner Product

행렬곱을 행렬의 각 행과 $v$의 내적의 결과로 이해할 수 있다. 이를 식으로 적으면 다음과 같다.

$$
Av = \begin{pmatrix}
[A]_1 \cdot v \\
[A]_2 \cdot v \\
\vdots \\
[A]_m \cdot v \\
\end{pmatrix}
$$

이때 $A$의 각 열이 정규직교인 경우를 가정해 보자. 그러면 $A$의 열이 구성하는 벡터 공간으로의 정사영은 다음과 같이 된다.

$$
\text{proj}_{\text{col} A} w = AA^Tw = A \begin{pmatrix}
[A]^1 \cdot w \\
[A]^2 \cdot w \\
\vdots \\
[A]^n \cdot w \\
\end{pmatrix} = \underset{\{[A]^1, ..., [A]^n\} \to \mathcal{E}}{P} \begin{pmatrix}
[A]^1 \cdot w \\
[A]^2 \cdot w \\
\vdots \\
[A]^n \cdot w \\
\end{pmatrix} \quad (w \in F^m)
$$

우리는 이것을 *$w$를 $A$의 열의 각 축으로 정사영한 후, 그것을 표준기저로 변환하여 표기한 것* 이라고 이해할 수 있다.





