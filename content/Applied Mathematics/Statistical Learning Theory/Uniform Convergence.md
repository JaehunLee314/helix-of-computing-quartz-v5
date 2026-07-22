**Prerequisites:** [[PAC Learnability]], [[Bias-Complexity Tradeoff]]

## Introduction

모델의 APAC Learnability는 approximation error와 estimation error에 의해 정해진다. 이때 estimation error는 우리가 실제 분포 $D$ 대신 sampling $S$를 사용하기 때문에 발생하는 에러를 포함한다. 따라서 만약 empirical risk와 true risk간의 차이가 bounded 되어 있다면 학습이 가능하리라고 추론해 볼 수 있다. 따라서 다음과 같이 정의된다.

## Uniform Convergence

**Definition. Uniform Convergence**
가설 집합 $H$가 uniform convergence property를 가진다는 것은 어떤 $m_{H}^{UC} : (0, 1)^2 \to \mathbb{N}$가 존재하여 임의의 $\epsilon, \delta \in (0, 1)$, 확률분포 $D : \mathcal{X} \times \mathcal{Y} \to [0, 1]$에 대해 다음이 성립한다는 것이다. 

$$
m \geq m_{H}^{UC}(\epsilon, \delta), h \in H \to \underset{S \sim_{i.i.d.} D}{P}(\left | L_S(h) - L_D(h) \right | \leq \epsilon) \geq 1-\delta
$$
