이곳에서는 벡터의 Change of Basis 개념을 통해 대각화에 대해 살펴본다.

## 1. Change of Basis

체 $F$위에 정의된 벡터공간 $V$가 기저 $\mathcal{B} = \{ \mathbf{b_1}, \mathbf{b_2}, ..., \mathbf{b_r}\}$를 가진다고 해 보자. 그렇다면 우리는 다음과 같이 $v \in V$를 $\mathcal{B}$의 선형조합으로 표현할 수 있다.

$$
v = \sum_{i=1}^{r} k^\mathcal{B}_i \mathbf{b_i} \quad (a_i \in F)
$$

이때 $[k^\mathcal{B}_1, ..., k^\mathcal{B}_r]^T$를 $v$의 $\mathcal{B}$에 대한 좌표라고 부르고 아래와 같이 표기한다.

$$
[v]_{\mathcal{B}} = \begin{bmatrix} k^\mathcal{B}_1 \\ \vdots \\ k^\mathcal{B}_r \end{bmatrix}
$$

이제 다른 기저 $\mathcal{C} = \{ \mathbf{c_1}, \mathbf{c_2}, ..., \mathbf{c_r}\}$가 주어졌다고 해 보자. 그렇다면 $v$는 $\mathcal{C}$의 선형조합으로도 다음과 같이 표현할 수 있다.

$$
v = \sum_{i=1}^{r} k^\mathcal{C}_i \mathbf{c_i} \quad (b_i \in F)
$$

다음과 같이 두 표현을 번역해 주는 함수 $T$를 생각해 보자. (흔히 이 함수는 $P$로 표기하는데, 여기서는 이후 대각화에서의 논의와 기호가 겹치기 때문에 $T$로 표기한다. 이 기호의 겹침은 다분히 의도적이라는 것을 곧 보게 될 것이다.)

$$
\begin{aligned}
T: F^r &\rightarrow F^r \\
T([v]_{\mathcal{B}}) &= [v]_{\mathcal{C}}
\end{aligned}
$$

앞선 식을 행렬로 표현하기 위해 먼저 $B$, $C$를 다음과 같이 정의하자.

$$
\begin{aligned}
B &= \begin{bmatrix} \mathbf{b_1} & \cdots & \mathbf{b_r} \end{bmatrix}\\
C &= \begin{bmatrix} \mathbf{c_1} & \cdots & \mathbf{c_r} \end{bmatrix}
\end{aligned}
$$

이제 앞서서 본 좌표계의 정의는 다시 다음과 같이 적힌다.

$$
\begin{aligned}
[v]_{\mathcal{B}} &= B^{-1}v\\
[v]_{\mathcal{C}} &= C^{-1}v
\end{aligned}
$$

여기서 기저벡터들은 선형독립임으로 $B$, $C$의 가역성은 보장된다. 따라서 $P$는 다음과 같이 표현할 수 있다.

$$
T([v]_{\mathcal{B}}) = C^{-1}B[v]_{\mathcal{B}}
$$

이제 일반적으로 좌표의 기저를 바꾸는 $T_{\mathcal{B} \rightarrow \mathcal{C}}$는 다음과 같이 쓸 수 있다.

$$
T_{\mathcal{B} \rightarrow \mathcal{C}}(A) = C^{-1}BA
$$

선형변환이 행렬로 적힌다는 사실을 알고 있기 때문에 다음과 같은 약간의 기호적 편의성을 추구하기로 한다.

$$
T_{\mathcal{B} \rightarrow \mathcal{C}} = C^{-1}B
$$

## 2. Diagonalization

대각화는 정사각행렬에 대해 정의된다. 어떤 정사각행렬 $A \in \mathbb{M}_{n \times n}(F)$가 대각화 가능하다는 것은 다음과 같은 가역행렬 $P$와 대각행렬 $D$가 존재한다는 것을 의미한다.

$$
A = PDP^{-1}
$$

이 식의 의미를 해석해 보자. 먼저 $P$는 선형독립인 행으로 이루어져 있음으로 그 행들은 기저라고 생각할 수 있다. 즉 이 식은 다음과 같이 적힌다. 이때 $\mathcal{E}$는 표준기저이다.

$$
A = PDT_{\mathcal{E} \rightarrow \mathcal{P}}
$$

사실 이 방식으로 우리는 다음도 쓸 수 있다.

$$
A = T_{\mathcal{P} \rightarrow \mathcal{E}}DT_{\mathcal{E} \rightarrow \mathcal{P}}
$$

이때 $D$가 대각행렬이라는 의미는 이것이 스케일링 연산이라는 것이다. 결과적으로 우리는 $A = PDP^{-1}$로 적힌다는 것이 다음을 의미함을 알 수 있다.

어떤 벡터 $v$에 선형변환(혹은 행렬) $A$를 곱하는 것은 다음의 과정을 수행하는 것과 같다.

  (1) $v$를 $\mathcal{P}$에 대한 좌표로 변환한다.  
  (2) $v$에 $D$만큼의 스케일링 연산을 한다.  
  (3) $v$를 $\mathcal{E}$에 대한 좌표로 되돌린다.  

그렇다면 이러한 사실이 성립할 수 있는 경우는 언제일까? 그 조건을 우리는 다음과 같이 쓸 수 있다.

$$
\text{dim}\ \text{span} \{ x | Ax = \lambda x , \lambda \in F \} = n
$$

이 조건이 특성다항식의 근의 갯수와 같은 의미라는 것을 어렵지 않게 이해할 수 있다.

## References
(1) David C. Lay, Linear Algebra and Its Applications (6th ed.), Pearson  
(2) 이인석, 선형대수와 군 (개정판), 서울대학교출판부  