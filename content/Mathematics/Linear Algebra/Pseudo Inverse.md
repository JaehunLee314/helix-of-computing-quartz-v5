**Prerequisites:** [[SVD]]

어떤 matrix $A \in R^{m \times n}$에 대해 SVD를 사용하면 다음과 같은 orthonormal matrix $U, V$를 얻을 수 있다.

$$
A = U \Sigma V^T
$$

이때 만약 $\Sigma$가 어떤 diagonal matrix $D \in R^{r \times r}$에 대해 다음과 같다고 하면,

$$
\Sigma = \begin{pmatrix}
D \ 0 \\
0 \ 0
\end{pmatrix}
$$
다음과 같이 계산할 수 있다.

$$
A = ( U_r \ U_{m-r}) \begin{pmatrix}
D\ 0 \\
0\ 0
\end{pmatrix} \begin{pmatrix}
V_r^T \\
V_{n-r}^T
\end{pmatrix} = U_r D V_r^T
$$

이때 $r = rank\ A$이다. 그러면 $A$의 pseudo inverse $A^+$는 다음과 같이 정의된다.

$$
A^+ = V_r D^{-1}U_r^T
$$

이때 $A^+b$는 $Ax = b$의 least square solution $x$ 중 최소의 길이를 가지는 solution이다.