**Prerequisites**: [[Change of Basis]]

## Diagonalization and Change of Basis

대각화는 정사각행렬에 대해 정의된다. 어떤 정사각행렬 $A \in \mathbb{M}_{n \times n}(F)$가 대각화 가능하다는 것은 다음과 같은 가역행렬 $P$와 대각행렬 $D$가 존재한다는 것을 의미한다.

$$
A = PDP^{-1}
$$

이 식의 의미를 해석해 보자. 먼저 $P$는 선형독립인 열로 이루어져 있으며 각각은 $F^n$에 속한 벡터이다. 이때 표준기저 $\mathcal{E}$를 사용하면 $v = [v]_\mathcal{E}$라는 사실로부터 다음이 성립함을 알 수 있다. 문자의 중복을 막기 위해 change-of-coordinate matrix를 $T$로 표기한다.

$$
P = T_{\mathcal{P} \to \mathcal{E}}
$$

직관적으로 $P^{-1} = T_{\mathcal{E} \to \mathcal{P}}$가 된다. 그러므로 앞선 식은 다음과 같이 적을 수 있다.

$$
A = T_{\mathcal{P} \rightarrow \mathcal{E}}DT_{\mathcal{E} \rightarrow \mathcal{P}}
$$

이때 $D$가 대각행렬이라는 의미는 이것이 scaling 연산이라는 것이다. 결과적으로 우리는 $A = PDP^{-1}$로 적힌다는 것이 다음을 의미함을 알 수 있다. ($D$의 성분은 $F$에 속해야 한다.)

어떤 벡터 $v$에 선형변환(혹은 행렬) $A$를 곱하는 것은 다음의 과정을 수행하는 것과 같다.

  (1) $v$를 $\mathcal{P}$에 대한 좌표로 변환한다.  
  (2) $v$에 $D$만큼의 scaling 연산을 한다.  
  (3) $v$를 $\mathcal{E}$에 대한 좌표로 되돌린다.  

## Diagonalizable Matrix

앞선 논의를 고려할 때 대각화가 가능하다는 것은 $A$가 좌표의 변환과 scaling이라는 형식을 만족하며 동작한다는 것이다. 만약 $A$의 동작이 어떤 기저에서도 scaling으로 표현될 수 없다면 $A$는 대각화 가능하지 않다. 예를 들어 회전은 실수 범위에서는 scaling으로 표현되지 않으므로 회전행렬은 실수 범위에서 대각화할 수 없다.

$A$의 동작이 어떤 좌표에서 scaling 이라는 것은 *$A$가 공간을 늘어나거나 줄어들게 만드는 전체 차원의 갯수만큼의 서로 선형독립인 방향이 존재한다는* 것이다. 만약 우리가 그 방향들을 기저로 사용하면, 그때는 $A$를 단순히 대각행렬로 표현할 수 있다. 이를 구체적으로 살펴보자.

먼저 $\exists x \neq 0, Ax = \lambda x$가 성립하도록 하는 $\lambda \in F$를 eigenvalue라고 하고 이때의 $x$의 집합 $E_\lambda = \{x | Ax = \lambda x\}$를 $\lambda$에 대한 eigenspace라고 하며 eigenspace의 원소를 eigenvector라고 한다. (물론, eigenspace는 vector space이다.) 이때 $\lambda_1 \neq \lambda_2$ 이면 $E_{\lambda_1}, E_{\lambda_2}$에 속한 eigenvector들은 서로 선형독립임이 알려져 있다. 이제 위에서 살핀 $A$의 대각화 조건을 고려하면, 다음이 성립하는 것과 $A$가 대각화 가능한 것이 동치임을 알 수 있다.

$$
\dim \text{span} \bigcup_\lambda E_\lambda = n
$$

또한 각 eigenspace가 독립적이므로 위의 식은 아래와도 동치이다.

$$
\sum_\lambda \dim E_\lambda = n
$$

## Footnote
- 회전행렬은 복소수 범위에서 대각화 가능한데, 왜냐하면 복소수의 scaling은 회전을 표현할 수 있기 때문이다.

## References
(1) David C. Lay, Linear Algebra and Its Applications (6th ed.), Pearson  
(2) 이인석, 선형대수와 군 (개정판), 서울대학교출판부  