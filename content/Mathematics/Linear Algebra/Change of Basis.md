**Prerequisites**: [[Basis and Coordinate]]

벡터 공간의 기저를 정하면 벡터를 좌표 벡터 공간에서 표시할 수 있다. 그렇다면 서로 다른 기저를 통해 얻는 두 좌표 간에는 어떤 관계가 있을까? 

## Linearity of Coordinate Mapping

먼저 coordinate mapping이 linear 한지 살펴보자. 체 $F$위에 정의된 벡터 공간 $V$의 기저 $\mathcal{B} = \{ b_1, ..., b_n \}$를 생각하자. 이때 벡터 $v \in V$에 대해 정의에 의해 다음이 성립한다.

$$
\sum_i ([v]_\mathcal{B})_i b_i + \sum_i ([w]_\mathcal{B})_i b_i = v+ w
$$

이때 coordiante가 $F^n$에 속함으로 성분간의 덧셈을 가정하면,

$$
\sum_i ([v]_\mathcal{B} + [w]_\mathcal{B})_i b_i = v+ w
$$

그런데 coordinate는 유일함으로 이 식은 $[v + w]_\mathcal{B} = [v]_\mathcal{B} + [w]_\mathcal{B}$ 임을 의미한다. 스칼라 곱에 대해서도 비슷하게 증명할 수 있으므로 coordinate mapping은 linear 하다.

## Change of Basis

체 $F$위에 정의된 벡터 공간 $V$의 두 기저 $\mathcal{B} = \{ b_1, ..., b_n \}, \mathcal{C}  = \{ c_1, ..., c_n \}$를 생각하자. 그러면 벡터 $v \in V$에 대해 좌표 $[v]_\mathcal{B}, [v]_{\mathcal{C}}$를 생각할 수 있으며 이들이 다음을 만족한다.

$$
v = \sum_i ([v]_\mathcal{B})_i b_i = \sum_i ([v]_\mathcal{C})_i c_i
$$

이때 linearity에 의해 다음이 성립한다.

$$
[v]_\mathcal{C}= [\sum_i ([v]_\mathcal{B})_i b_i]_C = \sum_i ([v]_\mathcal{B})_i [b_i]_\mathcal{C}
$$

이를 행렬로 적으면 다음과 같이 된다.

$$
[v]_\mathcal{C}  = ([b_1]_\mathcal{C} \ [b_2]_\mathcal{C} \ \cdots \ [b_n]_\mathcal{C}) [v]_\mathcal{B}
$$

여기서 행렬 $([b_1]_\mathcal{C} \ [b_2]_\mathcal{C} \ \cdots \ [b_n]_\mathcal{C})$을 $\mathcal{B}$에서 $\mathcal{C}$로 가는 change-of-coordinate matrix 라고 하며 다음과 같이 적는다.

$$
\underset{\mathcal{B} \to \mathcal{C}}{P} = ([b_1]_\mathcal{C} \ [b_2]_\mathcal{C} \ \cdots \ [b_n]_\mathcal{C})
$$

## References
- David C. Lay, Linear Algebra and Its Applications (6th ed.), Pearson 