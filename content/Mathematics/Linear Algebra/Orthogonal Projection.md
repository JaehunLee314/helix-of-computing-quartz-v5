
**Prerequisites**: [[Basis and Coordinate]]

## Introduction

선형대수학에서 orthogonal projection은 어느 벡터에서 어느 벡터 공간으로 수선의 발을 내리는 것을 의미한다. 이를 그림으로 살펴보면 다음과 같다. 벡터 $v \in R^m$를 벡터 공간 $\text{span} \{ b_1, b_2 \}$ ($b_i \in R^m$) 으로 orthogonal projection 하면 그 결과로 벡터 $w \in R^m$을 얻는다.

![[OrthogonalProjection.png]]

이를 식으로 다음과 같이 적는다.

$$
w = \text{proj}_{\text{span} \{ b_1, b_2 \} }  v
$$

## Calculation of Projection

그렇다면 $w$를 어떻게 계산할 수 있을까? 이를 위해 우리는 다음의 두 조건을 이용한다.

- $w \in \text{span} \{ b_1, b_2 \}$ *(정사영의 결과는 사영되는 공간에 속한다.)*
- $(v - w) \cdot b_i = 0$ *(수선의 발은 사영되는 공간과 수직이다.)*

먼저 이들 조건을 행렬로 표현하여 보자. $B = (b_1 \ b_2) \in R^{m \times 2}$ 라고 두면 위의 식은 다음과 같이 적힌다.

$$
\exists k \in R^2, w = Bk \qquad B^T (v-w) = 0
$$

이제 두 식을 연립하면 다음을 얻는다.

$$
B^T(v-Bk) = 0 \to B^T v = B^T B k
$$

그런데 $B$의 열이 선형독립이므로 $B^TB$의 null space의 차원이 0이다. 따라서 rank-nullity theorem에 의해 $B^TB$는 full rank를 가지고 따라서 가역이다. 그러므로 다음이 성립한다.

$$
(B^TB)^{-1}B^Tv = k
$$

이를 원래 식에 대입하면 다음을 얻는다.

$$
w  =\text{proj}_{\text{span} \{ b_1, b_2 \} }  v = B(B^TB)^{-1}B^Tv 
$$

이처럼 실수 범위의 orthogonal projection은 행렬곱으로 표현할 수 있다. 

## Generalization

앞선 결과는 더 큰 차원에서도 적용할 수 있다. 어떤 벡터 공간 $V$와 그 기저 $\mathcal{B} = \{b_1, ..., b_n\}\ (b_i \in R^m)$이 주어지면 행렬 $B = (b_1 \ b_2 \ \cdots \ b_n) \in R^{m \times n}$ 에 대하여 다음이 성립한다.

$$
\text{proj}_{V} v = B(B^TB)^{-1}B^Tv \quad (v \in R^m)
$$

## Note on Pseudo Inverse

앞선 정사영 식에서 $(B^TB)^{-1}B^T$는 $B$의 Moore-Penrose pseudo inverse 라고 불리며 아래와 같이 적는다. (이는 각 열이 선형독립일 때 주어지는 left pseudo inverse이며 일반형은 SVD를 통해 정의된다.)

$$
B^+ = (B^TB)^{-1}B^T
$$

이때 $B = \underset{\mathcal{B} \to \mathcal{E}}{P}$ 와 같은 좌표변환으로 해석할 수 있다는 사실을 생각해 보자. 그러면 정사영은 다음과 같다.

$$
\underset{\mathcal{E} \to \mathcal{B}}{P} \text{proj}_{V} v = B^+v 
$$

즉 $B^+ v$는 $\mathcal{B}$의 관점에서 본 정사영의 결과다. 역행렬이 존재할 때 $B^{-1} = \underset{\mathcal{E} \to \mathcal{B}}{P}$가 된다는 사실을 고려하면 이것이 왜 역행렬의 일반화인지 이해할 수 있다.

## References
(1) David C. Lay, Linear Algebra and Its Applications (6th ed.), Pearson  