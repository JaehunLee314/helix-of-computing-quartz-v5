**Prerequisites:** [[Orthogonally Diagonalizable]]
## Vector Valued RV

Random variable $X_1, X_2, ..., X_n$가 $X_i \in R^p$이고 독립항등분포를 따른다고 하자. 그러면 sample mean과 variance는 다음과 같이 주어진다.

$$
\bar{X} = \frac{1}{N} \sum_{i} X_i
$$
$$
S_X = \frac{1}{n-1} \tilde{X}\tilde{X}^T \quad where \quad \tilde{X}
 = (X_1 - \bar{X} \ X_2 - \bar{X}\ \cdots X_n - \bar{X})$$

만약 $\bar{X} = 0$이면 sample variance는 간단하게 다음과 같이 적을 수 있다.

$$
S_X = \frac{1}{n-1} XX^T
$$

## PCA

어떤 기저 $\mathcal{P}$에 대해 각 기저가 열을 구성하는 행렬 $P$를 생각하자. 그러면 벡터 $x$가 $\mathcal{P}$에서 가지는 좌표 $[x]_{\mathcal{P}}$는 $x = P[x]_{\mathcal{P}}$를 만족해야 하므로 다음과 같이 정의된다.

$$
P^{-1}x = [x]_{\mathcal{P}}
$$

이제 Principal Component Analysis (PCA) 각각의 기저가 $X_i$의 variance를 설명하는 정규직교기저를 찾는 문제이다.

**Question. PCA**
Random variable $X_1, X_2, ..., X_n$가 $X_i \in R^p$이고 평균이 $0$인 독립항등분포를 따른다고 하자. 이제 어떤 orthonormal basis $\mathcal{P}$에 대하여 $Y_i = [X_i]_{\mathcal{P}}$라고 정의하자. $S_Y = diag(k_1, ..., k_n)$이고 $k_1 \geq k_2 \geq \cdots \geq k_p$이 되도록 하는 $\mathcal{P}$를 구하라.

*Solution.*
행렬 $P$의 각 열이 $\mathcal{P}$의 각 기저라고 하자. 그러면 정의에 의해 $X = PY$이다. $\mathcal{P}$가 orthonormal basis이므로 $P^T = P^{-1}$이므로 $P^TX = Y$가 성립한다. 따라서 다음과 같다.

$$
S_Y = \frac{1}{n-1} YY^T = \frac{1}{n-1} (P^TX)(P^TX)^T = \frac{1}{n-1} P^TXX^TP = P^TS_XP
$$

이제 $S_Y$가 diagonal matrix여야 하므로 다음이 성립해야 한다.

$$
P^TS_XP = diag(k_1, ..., k_p) \to S_X = P diag(k_1, ..., k_p) P^T
$$

그런데 $S_X$는 real symmetric matrix이므로 항상 orthogonally diagonalizable하다. 따라서 $k_1, ..., k_n$은 $S_X$의 각 eigenvalue를 크기 순서대로 나열한 것이고 $P$는 대응되는 eigenvector이다.



