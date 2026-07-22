**Prerequisites:** [[PAC Learnability]]

이곳에서는 기계 학습에서 자주 등장하는 Bias-Complexity Tradeoff에 대해 살펴본다.

## Basic Setup

확률적 데이터 $(x, y) \sim D : \mathcal{X} \times \mathcal{Y} \to [0, 1]$를 가정하고 sample $S \sim_{i.i.d.} D$에 대해 ERM rule을 통해 얻는 $h_S$를 다음과 같이 정의하자.

$$
h_S = \arg\min_{h \in H} L_S(h)
$$

이하에서는 $h_S$의 true risk $L_D(h_S)$를 이해하는 두 가지 방법을 살펴본다.

## Approximation Error와 Estimation Error

가설 집합 $H$에 대해서 이론적으로 가능한 최소의 loss는 $\min_{h \in H} L_D(h)$로 주어진다. 따라서 우리는 다음과 같은 분해를 생각할 수 있다.

$$
L_D(h_S) =\min_{h \in H}  L_D (h) + \epsilon_{est} = \epsilon_{app} + \epsilon_{est} \qquad(\epsilon_{app}=\min_{h \in H}  L_D (h) )
$$

여기서 $\epsilon_{app}$를 approximation error라고 하고 $\epsilon_{est}$를 estimation error라고 한다. 전자는 $H$에 의해 주어지는 가능한 최소의 loss이고 후자는 sampling, learning algorithm, loss estimation등에 의해 발생하는 loss이다. 특히 ERM rule이 $L_D(h_S)$가 아니라 $L_S(h_S)$를 사용하기 때문에 발생하는 loss를 포함한다.

## Bias와 Variance

앞선 가정에 더하여 $y = f(x)$를 만족하는 deterministic한 함수 $f$를 가정하고 ERM rule의 loss function으로 L2-norm을 사용한다고 하자. 그러면 sample $S$와 어떤 결정론적 입력값 $x \in \mathcal{X}$에 대해 다음이 성립한다.

$$
\begin{aligned}
E_S[l(h_S, x, f(x))] &= E_{S}[(h_S(x) - f(x))^2] \\
&= \left(E_{S}[h_S(x) - f(x)]\right)^2 + E_{S}\left[\left((h_S(x) - f(x)) - E_{S}[h_S(x) - f(x)]\right)^2\right] \\
&= (E_{S} [h_S(x) - f(x)])^2 + V_{S}[h_S(x) - f(x)]
\end{aligned}
$$

여기서 첫 번째 항의 부분 $E_{S}[h_S(x) - f(x)]$가 model의 입력 $x$에 대한 bias를 나타내고, 두 번째 항 $E_{S}\left[\left((h_S(x) - f(x)) - E_{S}[h_S(x) - f(x)]\right)^2\right]$가 model의 입력 $x$에 대한 variance를 나타낸다. Bias는 모델이 평균적으로 가지는 loss이고 variance는 모델이 가지는 loss가 흩어진 정도이다.

## Model Complexity, Bias, Variance, Est. Error, App. Error

Approximation error와 bias, estimation error와 variance는 거의 같은 의미를 가지고 있다. 전자는 induction bias에 의해 발생하는 오차를 의미하고 후자는 sampling에 의해 발생하는 학습 과정에서의 오차를 의미한다. 

경험적으로 model complexity (간단히는 가설 집합의 크기)가 크면 approximation error는 작아지지만 estimation error는 커진다. 왜냐하면 표현 가능한 데이터의 범위가 넓어지면서 induction bias에 의한 오차는 줄어들지만 loss estimation은 더 어려워지기 때문이다. 물론 그 반대도 성립한다. Approximation error와 estimation error간의 tradeoff를 bias-complexity tradeoff라고 하고, bias와 variance의 tradeoff는 bias-variance tradeoff라고 한다. 이 관계들을 정리해 보면 다음과 같다.

| **Model Complexity** | **Low** | **Mid (Optimal)** | **High** |
| -------------------- | ------- | ----------------- | -------- |
| **Bias**             | High    | Low               | Low      |
| **Variance**         | Low     | Low               | High     |
| **App. Error**       | High    | Low               | Low      |
| **Est. Error**       | Low     | Low               | High     |

## Footnote
- $V(X) = E(X^2)-E(X)^2 \leftrightarrow E(X^2) = E(X)^2 + V(X)$
- 이것에 대한 더 세부적인 논의는 [[Notes on Error Decomposition]]을 볼 것.

## References
(1) Shalev-Shwartz, Ben-David, *Understanding Machine Learning*  
(2) Bias-Variance Tradeoff, [https://en.wikipedia.org/wiki/Bias-variance_tradeoff](https://en.wikipedia.org/wiki/Bias-variance_tradeoff)