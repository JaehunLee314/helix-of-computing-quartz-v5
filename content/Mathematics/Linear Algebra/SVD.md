SVD(Singular Value Decomposition)은 매우 강력한 행렬 분해 기법이며 행렬이 가지는 주요 성질을 잘 요약하여 보여준다. 이곳에서는 SVD의 증명과 그 의의를 살핀다.

## SVD

모든 실수 행렬은 직교행렬 $U, V$와 대각행렬 $\Sigma$를 이용하여 다음과 같이 분해할 수 있다.

$$
A = U \Sigma V^T
$$

이러한 분해를 SVD라고 부른다. 

## SVD의 이해

먼저 우리는 다음의 정리를 확인한다.

**Theorem** $A^T A$는 대칭행렬이므로 직교대각화된다. 이때 $A^T A$의 0보다 큰 고유값에 대응되는 고유벡터들을 $\{v_1, ..., v_r\}$이라 하자. 그러면 $\{Av_1, ..., Av_r\}$은 $\text{Col} A$의 기저이다.

**Proof** 
참고문헌 (1)의 465쪽을 참고하라.

위 정리를 고려할 때 당연히 $AA^T$의 0보다 큰 고유값에 대응되는 고유벡터들 $\{A^Tu_1, ..., A^Tu_r\}$은 $\text{Row} A = \text{Col} A^T$의 기저이다.

이제 $A^TA$의 0보다 큰 고유값에 대응되는 고유벡터들을 $\{v_1, ..., v_r\}$라 하고 이를 Gram-Schmidt process를 통해 $\{v_1, ..., v_n\}$으로 확장하자. 이제 $V$를 다음과 같이 정의하자.

$$
V = [v_1, ..., v_n]
$$

또한 $U = [u_1, ..., u_n]$을 다음과 같이 정의하자.

$$
u_i = \begin{cases}
\frac{1}{|| A v_i ||} A v_i = \frac{1}{\sigma_i} A v_i \quad (i = 1, ..., r) \\
(\text{Extended by Gram-Schmidt Process}) \quad (i = r+1, ..., n)
\end{cases}
$$

이때 보통 $\sigma_1 \geq \sigma_2 \geq ... \geq \sigma_r > 0$ 라고 둔다. 이러한 정의에서 $U$는 orthonormal이다. 이제 $\Sigma$를 다음과 같이 정의하자.

$$
\Sigma = \text{diag}(\sigma_1, ..., \sigma_r, 0, ..., 0)
$$

그러면 $AV = U \Sigma$ 임을 다음과 같이 보일 수 있다.

$$
\begin{aligned}
AV &= A[v_1, ..., v_n] \\
&= [Av_1, ..., Av_n] \\
&= [A v_1, ..., A v_r, 0, ..., 0] \\
&= [u_1 \sigma_1, ..., u_r \sigma_r, 0, ..., 0] \\
&= [u_1, ..., u_n] \text{diag}(\sigma_1, ..., \sigma_r, 0, ..., 0) \\
&= U \Sigma
\end{aligned}
$$

따라서 $A = U \Sigma V^T$이다. $\square$

## SVD의 의의

우리는 이제 다음의 $U, V$의 의의를 파악할 것이다. 먼저 다음과 같이 적자.

$$
\begin{aligned}
U = [U_r | U_{n-r}] = [u_1, ..., u_n]\\
V = [V_r | V_{n-r}] = [v_1, ..., v_n]
\end{aligned}
$$

이제 앞선 정리에 따라 $U_r$의 행은 $\text{Col}A$의 기저이다. 또한 $V_{n-r}$의 열은 $\text{Nul}A$의 기저이다. 우리는 $(\text{Nul} A)^\bot = \text{Row} A$라는 사실을 안다. 즉, $V_r$의 열은 $\text{Row} A$의 기저이다. 마지막으로 같은 방식으로 $U_{n-r}$의 행은 $\text{Nul}A^T$의 기저이다.

이제 우리는 4개의 fundamental subspaces가 각각 다음과 같음을 알게 되었다.

| Fundamental Subspace | Basis |
|:---:|:---:|
| $\text{Col} A$ | $U_r$ |
| $\text{Row} A$ | $V_r$ |
| $\text{Nul} A$ | $V_{n-r}$ |
| $\text{Nul} A^T$ | $U_{n-r}$ |

## References
(1) David C. Lay, Linear Algebra and Its Applications (6th ed.), Pearson  
(2) 이인석, 선형대수와 군 (개정판), 서울대학교출판부  
(3) Gilbert Strang, Introduction to Linear Algebra (6th ed.), Wellesley-Cambridge Press  