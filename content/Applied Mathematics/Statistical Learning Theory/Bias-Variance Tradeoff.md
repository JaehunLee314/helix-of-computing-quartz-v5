이곳에서는 기계 학습에서 자주 등장하는 Bias-Variance Tradeoff 에 대해 살펴본다.

## 정의

우리의 자료 $(x, y)$가 결합확률분포 $D$를 따른다고 하자 (즉, $(x, y) \sim D$). 그런데 학습하는 우리는 $D$에 대해 완전하게 파악할 수 없다. 따라서 우리는,

$$
S = \{(x_1, y_1), (x_2, y_2), \dots, (x_m, y_m)\} \sim_{i.i.d.} D
$$

와 같이 독립항등분포를 따르는 $m$개의 샘플을 추출하여 이를 통해 학습을 진행하고자 한다.

만약 우리가 L2 loss를 사용하기로 한다면, 모델 $h$에 대해 다음 두 가지 loss 값을 생각할 수 있다. 먼저 $L_D$는 모델이 실제로 가지는 loss이다.

$$
L_D(h) = E_{(x, y) \sim D}[(h(x) - y)^2]
$$

한편, $L_S$는 우리가 추출한 샘플을 통해 추정한 loss이다.

$$
L_S(h) = \frac{1}{m} \sum_{i = 1}^{m} (h(x_i) - y_i)^2
$$

## Approximation Error와 Estimation Error

이상적으로 우리는 다음과 같은 최적화를 원한다.

$$
h_D = \arg\min_{h \in H} L_D(h)
$$

하지만 우리가 아는 것은 $L_S$뿐이므로, 실제로는 다음 식을 통해 모델 학습을 수행한다.

$$
h_S = \arg\min_{h \in H} L_S(h)
$$

이제 이 모델의 실제 loss에 대해 다음과 같은 식을 적을 수 있다.

$$
L_D(h_S) = L_D(h_D) + \epsilon_{est}
$$

즉, 우리는 이 모델 집합 $H$에서 가능한 최적의 loss인 $L_D(h_D)$에, loss의 추정에 의해 발생하는 오차 $\epsilon_{est}$를 더한 모델의 loss $L_D(h_S)$를 얻는다. 이때 $L_D(h_D)$를 approximation error ($\epsilon_{app}$)라 부르고, $\epsilon_{est}$를 estimation error라고 한다.

Approximation error는 우리가 가진 모델 집합 $H$의 한계로 인해 발생하는 오차이다. 한편, estimation error는 전체 분포 $D$가 아니라 샘플 $S$를 통해 계산을 수행하기 때문에 발생하는 오차이다. Underfitting과 overfitting은 다음과 같이 해석된다.

- **Underfitting:** 주로 $H$의 한계로 인해 approximation error가 높아져 발생한다.
- **Overfitting:** 주로 $S$의 한계로 인해 $L_S$가 정확히 $L_D$를 근사하지 못하고 estimation error가 높아져 발생한다.

## Bias와 Variance

이제 $(x, y) \sim D$에 대해 $y = f(x)$가 성립한다고 하자. 또한 아래 식에서 $S \sim_{i.i.d.} D,\ x \sim D_x$라고 가정하자. 이때 다음이 성립한다.

$$
\begin{aligned}
E_{S}[L_D(h_S)] &= E_{S,x}[(h_S(x) - f(x))^2] \\
&= \left(E_{S,x}[h_S(x) - f(x)]\right)^2 + E_{S,x}\left[\left((h_S(x) - f(x)) - E_{S,x}[h_S(x) - f(x)]\right)^2\right]
\end{aligned}
$$

여기서 첫 번째 항 $E_{S,x}[h_S(x) - f(x)]$가 bias를 나타내고, 두 번째 항 $E_{S,x}\left[\left((h_S(x) - f(x)) - E_{S,x}[h_S(x) - f(x)]\right)^2\right]$ 가 variance를 나타낸다. 즉, 샘플 $S$의 선택에 따라 모델 출력의 오차가 어떻게 변화하는지를 표현하는 것이 이 두 값이라 할 수 있다.

이 식은 이전의 approximation error, estimation error와 유사하긴 하지만 의미가 조금 다르다. 보통 이 값들은 모델의 복잡도(혹은 표현능력)과 연관된다. (비록 이러한 분석이 보다 복잡한 모델 – MLP, Regularized Model 등 – 에서도 항상 성립하는 것은 아니다.)

- **Simple Model:** 모델이 데이터의 정확한 예측에 실패함으로 Bias가 높지만, 전반적으로 $S$에 대해 안정적임으로 Variance가 낮다.
- **Complex Model:** 모델이 대부분 데이터를 정확히 예측해 Bias가 낮지만, 전반적으로 $S$에 대해 불안정적임으로 Variance가 높다.

## Model Complexity, Bias, Variance, Est. Error, App. Error

앞선 관계들을 정리해 보면 다음과 같다.

| **Model Complexity** | **Low** | **Mid (Optimal)** | **High** |
| -------------------- | ------- | ----------------- | -------- |
| **Bias**             | High    | Low               | Low      |
| **Variance**         | Low     | Low               | High     |
| **App. Error**       | High    | Low               | Low      |
| **Est. Error**       | Low     | Low               | High     |

## References
(1) Shalev-Shwartz, Ben-David, *Understanding Machine Learning*  
(2) Bias-Variance Tradeoff, [https://en.wikipedia.org/wiki/Bias-variance_tradeoff](https://en.wikipedia.org/wiki/Bias-variance_tradeoff)