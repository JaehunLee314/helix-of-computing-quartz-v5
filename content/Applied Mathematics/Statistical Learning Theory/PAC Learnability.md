## Introduction

어떤 sample $S$가 알려지지 않은 확률분포 $D : \mathcal{X} \times \mathcal{Y} \to [0, 1]$에 대하여 다음과 같이 주어진다고 하자.

$$
S = ( (X_1, Y_1), (X_2, Y_2), ..., (X_m, Y_m)) \sim_{i.i.d.} D
$$

이제 $S$의 관측치 $s$가 주어질 때 $(X, Y) \sim D$에 대해서 $Y \approx h(X)$가 성립하도록 하는 $h$를 찾는 방법에 대한 논의를 statistical supervised learning problem이라고 한다. 

## Learning Algorithm

Learning algorithm은 앞서 말한 $h$를 찾는 방법론을 말한다. 구체적으로 learning algorithm $A$는 각 sample size $m$에 대해 함수 $A_m : (\mathcal{X} \times \mathcal{Y})^m \to (\mathcal{X} \Rightarrow \mathcal{Y})$를 제공한다. 이때 $A_m$은 크기가 $m$인 sample $S$의 관측치 $s$가 주어질 때 $X, Y$의 관계를 예측하는 함수 $h$를 출력하는 함수이다. ($\mathcal{X} \Rightarrow \mathcal{Y}$는 $\mathcal{X}$에서 $\mathcal{Y}$로 가는 모든 함수의 집합이다.)  

만약 우리가 learning algorithm의 출력의 범위를 어떤 $\mathcal{H} \subseteq \mathcal{X} \Rightarrow \mathcal{Y}$로 제한한다면 (즉 모든 $A_m$에 대해 그 codomain이 $\mathcal{H}$라면) 이러한 $\mathcal{H}$를 hypothesis class라고 한다. Hypothesis class는 우리가 데이터에 대해 이미 알고 있는 지식(inductive bias)를 표현한다.

## Loss Function

앞서서 우리의 목표는 $Y \approx h(X)$인 $h$를 찾는 것이었다. 그런데 이는 질적인 목표이므로 실제 계산을 위해서는 $Y \approx h(X)$를 양적으로 정의할 필요가 있다. 따라서 loss function $l: \mathcal{H} \times (\mathcal{X} \times \mathcal{Y}) \to \mathbb{R}_{\geq 0}$는 가설 $h$를 임의의 관측치 $(x, y)$ 대해서 평가하여 성능이 우수할수록 낮은 값을 가지는 함수로 정의한다. 그런데 관측치는 $D$에서 sampling된 것에 지나지 않으므로 전체 확률분포에 대한 (true) risk function $L_D: \mathcal{H} \to \mathbb{R}_{\geq 0}$은 다음과 같이 정의된다.

$$
L_D(h) = \underset{(x, y) \sim D}{E} (l(h, (x, y)))
$$

한편 sampling을 통해 얻은 $L_D(h)$의 point-estimation은 empirical risk function $L_S: \mathcal{H} \to \mathbb{R}_{\geq 0}$이라고 하며 다음과 같이 정의한다.

$$
L_S (h) = \frac{1}{m}\sum_{i=1}^m l(h, (X_i, Y_i))
$$

## ERM Rule

Empirical risk minimization rule은 앞서서 정의한 empirical risk function을 주어진 가설 집합에 대해 최소화하는 learning algorithm이다. 즉 learning algorithm $ERM_{\mathcal{H}}: (\mathcal{X} \times \mathcal{Y})^m \to \mathcal{H}$은 다음과 같이 정의된다.

$$
ERM_{\mathcal{H}}(S) = \underset{h \in \mathcal{H}}{argmin} L_S(h)
$$

## Probably Approximately Correct

Learning algorithm은 sampling을 입력으로 받기 때문에 그 출력 역시 확률적이다. 따라서 learning algorithm의 성공에 대한 주장은 확률적인 주장이여야 한다. 따라서 다음과 같이 정의한다.

**Definition. Probably Approximately Correct (PAC)**
데이터가 어떤 분포 $D$를 따른다고 하고, sample size $m$과 loss function이 주어졌다고 하자. 이때 hypothesis class $\mathcal{H}$를 가지는 learning algorithm $A$가 어떤 $\epsilon, \delta \in (0, 1)$에 대해 probably approximately corret 하다는 것은 다음이 성립한다는 것을 의미한다.

$$
\underset{S \sim_{i.i.d.} D}{P}(L_D(A_m(S)) \leq \min_{h \in \mathcal{H}} L_{D}(h) + \epsilon) \geq 1-\delta
$$

이때 $\min_{h \in \mathcal{H}} L_{D}(h) = 0$이라면 $A$가 $D$에서 realizable 하다고 한다.

주어진 데이터셋의 크기가 $m$이고 우리가 loss function을 적당히 정의했다고 해 보자. 이로부터 우리가 learning algorithm을 설계하면, 우리는 이 algorithm이 달성가능한 최소의 risk보다 그렇게 크기 않은 risk를 제공하기를 기대한다.

## PAC Learnability

이제 우리는 어떤 learning algorithm이 학습가능한지의 여부를 정의하는 다음의 방식을 생각해 볼 수 있다. 

**Definition. PAC Learnability (of a Learning Algorithm)**
Loss function이 주어졌다고 하자. 이때 어떤 learning algorithm $A$가 PAC learnable하다는 것은 어떤 $m_A : (0, 1)^2 \to \mathbb{N}$이 존재하여 임의의 $\epsilon, \delta \in (0, 1)$에 대해 다음이 성립한다는 것이다.

- $A$가 realizable한 모든 분포 $D$에 대해 $m \geq m_A (\epsilon, \delta)$이면 $A$가 PAC하다.

따라서 $\mathcal{H}$에 정답이 존재하는 분포 $D$에 대해서 $A$는 항상 적은 오차범위 내에서 충분히 높은 확률로 그 정답을 찾을 수 있어야 한다.

한편 우리는 PAC learnability보다 완화된 조건으로 다음을 생각해 볼 수 있다. 

**Definition. Agnostic PAC (APAC) Learnability (of a Learning Algorithm)**
Loss function이 주어졌다고 하자. 이때 어떤 learning algorithm $A$가 Agnostic PAC learnable하다는 것은 어떤 $m_A : (0, 1)^2 \to \mathbb{N}$이 존재하여 임의의 $\epsilon, \delta \in (0, 1)$에 대해 다음이 성립한다는 것이다.

- 모든 분포에 대해 $m \geq m_A (\epsilon, \delta)$이면 $A$가 PAC하다.

이때 $A$는 분포에 상관없이 항상 $\mathcal{H}$에서 가능한 최선의 답을 찾을 수 있어야 한다.

우리는 가설 집합에 대해서도 learnability를 정의할 수 있다. Understanding machine learning에서는 이 정의를 사용한다.

**Definition. PAC Learnability (of a Hypothesis Class)**
Loss function이 주어졌다고 하자. 이때 가설 집합 $\mathcal{H}$가 PAC learnable하다는 것은 어떤 $\mathcal{H}$에 의해 제한되는 learning algorithm $A$가 존재하여 PAC learnable 하다는 것이다.

**Definition. APAC Learnability (of a Hypothesis Class)**
Loss function이 주어졌다고 하자. 이때 가설 집합 $\mathcal{H}$가 APAC learnable하다는 것은 어떤 $\mathcal{H}$에 의해 제한되는 learning algorithm $A$가 존재하여 APAC learnable 하다는 것이다.

## Notes on Inductive Bias

앞서서 우리는 $\mathcal{H}$가 inductive bias를 나타낸다고 했다. 이것에 대해 조금 더 구체적으로 살펴보자. 

No-free-lunch theorem (참고문헌 (1), section 5.1 참고)에 의하면 어떤 binary classification problem에 대한 learning algorithm $A$에 대해서도 만약 sample size가 domain size 보다 충분히 작으면 (여기서는,  $m < |\mathcal{X}|/2$ 이면) $A$가 물리적으로 $D$에 대해 충분한 정보를 얻지 못함으로 $A$가 충분히 작은 $\epsilon, \delta$에 대해 PAC 하지 않도록 하는 결정론적 정답 $f$가 존재하는 분포 $D$가 존재한다. 따라서 domain size가 무한하면 (즉, 가산무한 이상이면) 어떠한 경우에도 sample은 충분히 크지 못하다. 

이제 $A$의 가설 집합을 $\mathcal{H} = \mathcal{X} \Rightarrow \{ 0, 1\}\ (|\mathcal{X}| \geq |\mathbb{N}|)$이라고 정의해 보자. 그러면 $A$는 모든 결정론적 정답이 존재하는 분포에 대해 realizable하다. 따라서 만약 $A$가 PAC learnable 하다면 $A$는 모든 결정론적 정답이 존재하는 분포에 대해 PAC 해야 한다. 그런데 no-free-lunch theorem에 의하면 그렇지 않도록 하는 $D$가 항상 존재한다. 따라서 만약 가설 집합이 가능한 모든 함수라면, $A$는 PAC learnable하지 않다.

반대로 가설 집합을 적절하게 제한한다면 $A$는 PAC learnable할 수 있다. 직관적으로 만약 $D$의 일부 사례만을 관찰하는 것으로도 좋은 가설의 후보가 되는 $h$를 충분히 제한할 수 있다면 $A$는 학습 가능할 것이다. 이와 같은 개념은 [[VC Dimension]]에 의해 구체화된다.

## Footnote
- Understand Machine Learning에서는 learning algorithm이 아니라 hypothesis class의 learnability를 정의한다. 이곳에서 논의한 것과 논의의 결은 다르지 않다.
- 사실 loss function과 learning algorithm 간에는 밀접한 관련이 있으며 구체적인 task에 따라 적절한 loss function과 learning algorithm을 선택해야 한다.

## References
(1) Shalev-Shwartz, Ben-David, *Understanding Machine Learning*  

