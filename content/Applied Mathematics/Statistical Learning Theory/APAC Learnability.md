## Introduction

어떤 sample $S$가 알려지지 않은 확률분포 $D : \mathcal{X} \times \mathcal{Y} \to [0, 1]$에 대하여 다음과 같이 주어진다고 하자.

$$
S = ( (X_1, Y_1), (X_2, Y_2), ..., (X_m, Y_m)) \sim_{i.i.d.} D
$$

이제 $S$의 관측치 $s$가 주어질 때 $(X, Y) \sim D$에 대해서 $Y \approx h(X)$가 성립하도록 하는 최선의 $h$를 찾는 방법 중 최선의 방법을 찾는 문제를 statistical supervised learning problem이라고 한다. 

## Learning Algorithm

세부적인 내용을 다루기에 앞서 먼저 learning algorithm을 정의하자. Learning algorithm $A_m : (\mathcal{X} \times \mathcal{Y})^m \to (\mathcal{X} \Rightarrow \mathcal{Y})$는 크기가 $m$인 sample $S$의 관측치 $s$가 주어질 때 $X, Y$의 관계를 예측하는 함수 $h$를 출력하는 함수이다. ($\mathcal{X} \Rightarrow \mathcal{Y}$는 $\mathcal{X}$에서 $\mathcal{Y}$로 가는 모든 함수의 집합이다.) 

만약 우리가 learning algorithm의 출력의 범위를 어떤 $\mathcal{H} \subseteq \mathcal{X} \Rightarrow \mathcal{Y}$로 제한한다면 이러한 $\mathcal{H}$를 hypothesis class라고 한다. hypothesis class는 우리가 데이터에 대해 이미 알고 있는 지식(inductive bias)를 표현한다.

## Loss Function

이제 어떤 $h$가 최선인지는 어떻게 정의할 수 있을까? 만약 어떤 관측치 $(x, y)$에 대해서 $h$의 성능을 정량적으로 평가할 수 있다면 우리는 그와 같은 성능을 최대화하는 것으로 최선의 $h$를 찾을 수 있을 것이다.

따라서 loss function $l: \mathcal{H} \times (\mathcal{X} \times \mathcal{Y}) \to \mathbb{R}_{\geq 0}$는 가설 $h$를 임의의 관측치 $(x, y)$ 대해서 평가하여 성능이 우수할 수록 낮은 값을 가지는 함수로 정의한다. 그런데 관측치는 $D$에서 sampling된 것에 지나지 않으므로 전체 확률분포에 대한 (true) risk function $L_D: \mathcal{H} \to \mathbb{R}_{\geq 0}$은 다음과 같이 정의된다.

$$
L_D(h) = \underset{(x, y) \sim D}{E} (l(h, (x, y)))
$$

한편 sampling을 통해 얻은 $L_D(h)$의 point-estimation은 empirical risk function $L_S: \mathcal{H} \to \mathbb{R}_{\geq 0}$이라고 하며 다음과 같이 정의한다.

$$
L_S (h) = \frac{1}{m}\sum_{i=1}^m l(h, (X_i, Y_i))
$$

## ERM Method

Empirical risk minimization method는 앞서서 정의한 empirical risk function을 최소화하는 learning algorithm이다. 즉 learning algorithm $ERM_{\mathcal{H}}: (\mathcal{X} \times \mathcal{Y})^m \to \mathcal{H}$은 다음과 같이 정의된다.

$$
ERM_{\mathcal{H}}(S) = \underset{h \in \mathcal{H}}{argmin} L_S(h)
$$

## APAC Learnability

이제 우리는 어떤 learning algorithm $A$가 언제 최선이 되는지를 정의해야 한다. 직관적으로 만약 이 알고리즘이 가능한 모든 분포에 대하여 충분히 많은 데이터가 있을 때 일정 확률 이상으로 일정 loss 이하를 가지는 가설을 제공한다면 $A$가 성공적이라고 생각할 수 있다. 이와 같은 조건을 Agnostic Probably Approximately Correct Learnability라고 하고 짧게 APAC Learnability라고 부른다. 구체적으로 다음과 같이 정의한다.

**Definition. APAC Learnability (of a Learning Algorithm)**
어떤 loss function $l: \mathcal{H} \times (\mathcal{X} \times \mathcal{Y}) \to \mathbb{R}_{\geq 0}$에 대하여 learning algorithm $A_m : (\mathcal{X} \times \mathcal{Y})^m \to \mathcal{H}$가 APAC learnable 하다는 것은 어떤 $m_A : (0, 1)^2 \to \mathbb{N}$이 존재하여 임의의 $\epsilon, \delta \in (0, 1)$, 확률분포 $D : \mathcal{X} \times \mathcal{Y} \to [0, 1]$에 대해 다음이 성립한다는 것이다.

$$
m \geq m_A (\epsilon, \delta) \to \underset{S \sim_{i.i.d.} D}{P}((L_D(A_m(S))) \leq \min_{h \in \mathcal{H}} L_D(h) + \epsilon) \geq 1 - \delta
$$

Understand Machine Learing에서는 이것과 유사하지만 약간 다른 정의를 제공한다. 이때 우리는 learning algorithm이 아니라 hypothesis class의 learnability를 생각한다.

**Definition. APAC Learnability (of a hypothesis Class)**
어떤 loss function $l: \mathcal{H} \times (\mathcal{X} \times \mathcal{Y}) \to \mathbb{R}_{\geq 0}$에 대하여 hypothesis class $\mathcal{H} \subseteq \mathcal{X} \Rightarrow \mathcal{Y}$가 learnable 하다는 것은 어떤 $m_A : (0, 1)^2 \to \mathbb{N}$과 learning algorithm $A_m : (\mathcal{X} \times \mathcal{Y})^m \to \mathcal{H}$가 존재하여 임의의 $\epsilon, \delta \in (0, 1)$, 확률분포 $D : \mathcal{X} \times \mathcal{Y} \to [0, 1]$에 대해 다음이 성립한다는 것이다.

$$
m \geq m_A (\epsilon, \delta) \to \underset{S \sim_{i.i.d.} D}{P}((L_D(A_m(S))) \leq \min_{h \in \mathcal{H}} L_D(h) + \epsilon) \geq 1 - \delta
$$

많은 경우에 이 정의를 만족시키는 learning algorithm은 ERM method이다.

## References
(1) Shalev-Shwartz, Ben-David, *Understanding Machine Learning*  

