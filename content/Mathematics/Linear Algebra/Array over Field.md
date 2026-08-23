Array는 덧셈과 스칼라 곱셈이 정의되는 인덱스된 수의 나열이다.

**Definition. Array**
어느 체 $F$ 위에 정의되는 $m$ order $(n_1, ..., n_m)$ dimensional array $\text{Arr}_{n_1, ..., n_m}(F)$는 다음과 같이 정의된다. 

$$
\text{Arr}_{n_1, ..., n_m} (F) = \{ a | a : [n_1] \times [n_2] \times \cdots \times [n_m] \to F \}
$$

이때 $n_i \in N \cup \{ \infty \}$ 이며 $[n] = \{ 1, 2, ..., n\}$ 이다. 또한 array 간의 덧셈과 스칼라 곱셈이 이하로 정의된다.

*(덧셈)* $a, b \in \text{Arr}_{n_1, ..., n_m} (F)$ 라고 할 때 각 $i_1, ..., i_m$에 대해 다음과 같이 정의한다. 

$$
(a + b)_{i_1, ..., i_m} = a_{i_1, ..., i_m} + b_{i_1, ..., i_m}
$$

*(스칼라 곱셈)* $k \in F, a \in \text{Arr}_{n_1, ..., n_m} (F)$라고 할 때 각 $i_1, ..., i_m$에 대해 다음과 같이 정의한다.

$$
(ka)_{i_1, ..., i_m} = ka_{i_1, ..., i_m}
$$
