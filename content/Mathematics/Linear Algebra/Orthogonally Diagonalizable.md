이곳에서는 직교 대각화와 대칭행렬의 관계를 알아본다. 이하에서 특별한 언급이 없는 한 벡터, 행렬은 실수 범위의 것으로 가정한다.

## Orthogonally Diagonalizable

정사각행렬 $A \in \mathbb{M}_{n \times n}(\mathbb{R})$가 대각화 가능하다는 것은 다음을 만족하는 행렬 $P$와 대각행렬 $D$가 존재한다는 것이다.

$$
A = PDP^{-1}
$$

이제 특수한 경우를 생각한다. $\mathcal{P}$가 정규직교기저(orthonormal basis)라면 어떨까? 그렇다면 $P^T P = I$이고 $P^T = P^{-1}$이다. 따라서 다음과 같이 쓸 수 있다.

$$
A = PDP^T
$$

이러한 경우에 우리는 $A$가 직교 대각화 가능(orthogonally diagonalizable)하다고 말한다.

## Symmetric Matrix와 Orthogonally Diagonalizable의 관계

이 상황에서 $A$가 대칭행렬이라는 사실은 다음과 같이 보일 수 있다.

$$
A^T = (PDP^T)^T = PD^TP^T = PDP^T = A
$$

따라서 $A$가 직교대각화 가능하다는 것은 $A$가 대칭행렬이라는 것을 의미한다. 반대로 $A$가 대칭행렬이라면 직교대각화 가능할까? 실제로 이때 $A$는 직교 대각화 가능하다. 이것은 선형대수학의 중요한 정리 중 하나이다.

앞선 사실을 증명하기 위해 $A$가 대칭행렬이라고 가정해 보자. $A$가 직교 대각화 가능함을 보이기 위해 우리는 다음 두 사실을 보여야 한다.

(1) $A$의 eigenspace의 차원의 합이 $n$이다.
(2) $A$의 서로 다른 eigenspace의 eigenvector들은 서로 직교한다.

이 두 사실 중 (2)를 보이는 것이 더 간단하다. 

### Proof of (2)
$v_1, v_2$가 서로 다른 eigenspace의 eigenvector라고 하고 각각 eigenvalue $\lambda_1, \lambda_2$를 가진다고 하자. 그렇다면,

$$
v_1 \cdot v_2 = v_1^T v_2 = v_1^T A v_2 = \lambda_1 v_1^T v_2 = \lambda_2 v_1^T v_2
$$

이므로

$$
(\lambda_1 - \lambda_2) v_1^T v_2 = 0
$$

이때 $\lambda_1 \neq \lambda_2$이므로 $v_1^T v_2 = 0$이다. 따라서 서로 다른 eigenspace의 eigenvector들은 서로 직교한다.

### Proof of (1)
이 증명은 두 단계를 밟는다. 먼저 대칭행렬은 중복을 포함해 $n$개의 실수 eigenvalue를 가진다는 것을 보인다. 그 다음 어떤 행렬이 실수 eigenvalue를 가지면 Schur factorization이 가능하다는 Schur's theorem을 사용한다. 마지막으로 대칭행렬이 Schur factorization 가능하다면 직교대각화가 가능함을 보인다.

**(a) 대칭행렬은 중복을 포함해 $n$개의 실수 eigenvalue를 가진다.**
 
우리는 특성방정식이 $n$차 다항식임으로 대수학의 기본정리에 따라 $n$개의 복소근을 가짐을 안다. 그 중 하나의 복소근을 $\lambda$, 그에 대응하는 eigenvector를 $v = p + qi$라고 하자. 그러면

$$
Ax = \lambda v
$$

이고 이때

$$
\overline{\bar{v}^TAv} = v^TA\bar{v} = (v^T A \bar{v})^T = \bar{v}^T A^T v = \bar{v}^T A v
$$

이므로 

$$
\begin{aligned}
&\overline{\bar{v}^TAv} = \overline{\bar{v}^T \lambda v} = \bar{\lambda} v^T\bar{v} \\
&\overline{\bar{v}^TAv} = \bar{v}^T A v = \lambda \bar{v}^T v\\
&\therefore \bar{\lambda} = \lambda,\ \lambda \in \mathbb{R}
\end{aligned}
$$

와 같이 $\lambda$가 실수임을 알 수 있다. 여기서 내적의 성질, $\bar{v}^T v = v^T \bar{v}$ 임을 이용했다. 이제

$$
\begin{aligned}
&Av = A(p + qi) = \lambda (p + qi) = \lambda p + \lambda qi \\
&Ap = \text{Re}(Av) = \text{Re}(\lambda p + \lambda qi) = \lambda p
\end{aligned}
$$

이므로 $p$는 실수 eigenvalue $\lambda$에 대응하는 실수 eigenvector이다.

**(b) Schur Factorization을 이용한 직교대각화 가능성 증명**

이제 다음의 정리가 성립함이 알려져 있다.

**Theorem (Schur's Theorem)** 
실수 eigenvalue만을 가지는 행렬은 Schur factorization이 가능하다. 즉 직교행렬 $Q$와 상삼각행렬 $T$가 존재하여 $A = Q T Q^T$가 성립한다.

이것에 대한 증명은 참고문헌 (4)를 참고하라. 이제 $A$가 대칭행렬이라는 사실을 이용하면 $T$가 대각행렬임을 알 수 있는데 그 과정은 다음과 같다.

$$
\begin{aligned}
&A^T = (Q T Q^T)^T = Q T^T Q^T = Q T Q^T = A \\
&Q T^T Q^T = Q T Q^T \rightarrow Q^T(QT^TQ^T)Q = Q^T(QTQ^T)Q \\
&\therefore T = T^T
\end{aligned}
$$

따라서 원하는 사실이 증명된다. $\square$

## References
(1) David C. Lay, Linear Algebra and Its Applications (6th ed.), Pearson  
(2) 이인석, 선형대수와 군 (개정판), 서울대학교출판부  
(3) Gilbert Strang, Introduction to Linear Algebra (6th ed.), Wellesley-Cambridge Press  
(4) David H. Wagner, Proof of Schur's Theorem, https://math.mit.edu/~gs/linearalgebra/ila6/lafe_schur03.pdf