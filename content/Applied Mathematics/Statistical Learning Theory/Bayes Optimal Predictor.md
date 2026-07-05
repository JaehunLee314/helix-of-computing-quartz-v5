이곳에서는 Bayes optimal predictor에 대해 살펴본다.

## Bayes Optimal Predictor

자료 $(X, Y) \in \mathcal{X} \times \{0, 1\}$가 확률분포 $D$를 따르고 $X$가 이산확률변수라 하자. 이때 $X, Y$의 함수 관계를 예측하는 문제를 고려하자. 이는 이진 분류 문제로 이때 최적해는 다음과 같은 함수임이 알려져 있다.

$$
f_D(x) = \begin{cases}
1 \quad (P(Y = 1 | X = x)) > 1/2 \\
0 \quad otherwise
\end{cases}
$$
 $f_D$가 최적해라는 것은 다른 함수 $g: \mathcal{X} \rightarrow \{0, 1\}$에 대해 다음이 항상 성립한다는 것을 의미한다. (a.k.a. $L_D(f_D) \leq L_D(g)$)

$$
P(f_D(X) \neq Y) \leq P(g(X) \neq Y)
$$

이와 같은 $f_D$를 Bayes optimal predictor 라고 한다.  $f_D$의 정의는 다음과도 동치이다.

$$
f_D(x) = \text{argmax}_{y} P(Y=y | X = x)
$$

## Proof of Bayes Optimal Predictor's Optimality

이곳에서는 $X$가 이산 확률 변수인 경우만을 증명한다. 

일반성을 잃지 않고 $f_D$와 $g$가 단 하나의 지점 $x'$에서만 다르다고 가정하고, 이때 $f_D(x') = 1, g(x') = 0$ 이라고 하자. 이제 다음이 성립한다. ($g$에 대해서도 동일하게 성립한다.)

$$
P(f_D(X) \neq Y) = E_{X, Y} (I(f_D(X) \neq Y)) = \sum_{x, y \in \mathcal{X}, \mathcal{Y}} I(f_D(x) \neq y) P(X = x, Y = y)
$$
따라서 $f_D$와 $g$의 loss의 차이는 $x'$ 의 지점에서 결정된다는 사실을 알 수 있다. 가정에 의해 그 값은 각각,

$$
(For\ f_D) \quad P(X = x', Y = 0) \quad v.s. \quad P(X = x', Y = 0) \quad (For\ g)
$$
과 같이 주어진다. 이제,

$$
(For\ f_D) \quad P(Y = 0|X = x')\cancel{P(X = x')} \quad v.s. \quad P(Y = 1|X = x')\cancel{P(X = x')} \quad (For\ g)
$$

이고 $f_D$는 항상 더 확률이 높은 쪽을 선택함으로 부등호는 아래와 같다.

$$
(For\ f_D) \quad P(Y = 0|X = x')\quad \leq \quad P(Y = 1|X = x') \quad (For\ g)
$$

따라서 우리는 $f_D$의 loss가 항상 $g$ 보다 작거나 같음을 알 수 있다. $\square$

*위의 기댓값  $E_{X, Y} (I(f_D(X) \neq Y))$을 조건부 기댓값을 사용해 전개해도 같은 결과를 얻을 수 있다.*

## References
(1) Shai Shalev-Shwartz, Shai Ben-David, Understanding Machine Learning, 22-30pp.