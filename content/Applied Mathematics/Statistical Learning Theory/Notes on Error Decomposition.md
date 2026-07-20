**Prerequisites:** [[Bias-Complexity Tradeoff]]

이곳에서는 model space에서 model은 decompose하는 것으로 approximation error, estimation error, bias, variance의 관계를 살펴본다.

## Basic Setup

확률적 데이터 $(x, y) \sim D$와 $y = f(x)$를 만족하는 deterministic한 함수 $f$를 가정하자. 이제 ERM rule의 loss function으로 L2-norm을 사용한다고 하고 sample $S \sim_{i.i.d.} D$에 대해 ERM rule을 통해 얻는 $h_S$를 다음과 같이 정의하자.

$$
h_S = \arg\min_{h \in \mathcal{H}} L_S(h)
$$

한편 $x \in D_x$와 $S \sim_{i.i.d} D$ 그리고 논의에 필요한 $g$에 대하여 다음이 성립한다고 가정하자.

$$
E_SE_x[g(S, x)] = E_xE_S[g(S, x)] = E_{S, x}[g(S, x)] \cdots (1)
$$

수학적으로 이는 Fubini 정리에 해당한다.

## Model Decomposition

Model space는 각 model $h$를 하나의 vector로 하는 subset of a vector space이다. 이때 우리는 true labeling function $f$, 달성 가능한 최적의 모델 $h^* = \arg\min_{h \in \mathcal{H}} L_D(h)$, 그리고 실제 학습에서 주어지는 모델 $h_S$ 간의 관계를 다음과 같이 벡터 간의 관계로 묘사할 수 있다. ($h^* = f + \Delta h^*, h_S = h^* + r_S$)

$$
\begin{array}{ccc}
f & & \\
\mathllap{\scriptstyle \Delta h^*}\bigg\downarrow & \searrow & \\
h^* & \stackrel{r_S}{\longrightarrow} & h_S
\end{array}
$$

이는 다음과 같은 bias-complexity tradeoff의 다른 표현이다.

$$
\begin{array}{ccc} L_D(f) = 0 & & \\ \llap{\scriptstyle}\bigg\downarrow & \stackrel{}{\searrow} & \\ L_D(h^*) = \epsilon_{app} & \stackrel{}{\longrightarrow} & L_D(h_S) = \epsilon_{app} + \epsilon_{est} \end{array}
$$

이를 사용하면 다음과 같이 $L_D(h_S)$를 분해할 수 있다.

$$
\begin{aligned}
L_D(h_S) &= E_x[(h_S(x) - f(x))^2] \\
&= E_x[(f(x) + \Delta h^*(x) + r_S(x) - f(x))^2] = E_x[(\Delta h^*(x) + r_S(x))^2] \\
&= E_x[\Delta h^*(x)^2] + E_x[2\Delta h^*(x) r_S(x)] + E_x[r_S(x)^2] \cdots (2)
\end{aligned}
$$

## Bias-Complexity Tradeoff

Approximation error의 정의를 고려하면 다음이 성립한다.

$$
\epsilon_{app} = \min_{h \in \mathcal{H}} L_D(h) = L_D(h^*) = E_x[(h^*(x) - f(x))^2] = E_x[\Delta h^*(x)^2] \cdots (3.1)
$$

이제 $L_D(h_S) = \epsilon_{app} + \epsilon_{est}$이므로 (2)과 (3.1)을 연립하면 다음을 얻을 수 있다.

$$
\epsilon_{est} = E_x[2\Delta h^*(x) r_S(x)] + E_x[r_S(x)^2] \cdots (3.2)
$$

이 식들의 의미를 고찰해 보자. (3.1)에 의하면 approximation error는 순전히 theoretical optimial model $h^*$이 각 입력값 $x$에 대해 가지는 MSE의 평균치다. 한편 (3.2)의 두 항은 각자 살펴보아야 한다. 전자의 항은 각 입력값에 대해 $h^*$가 $f$와 가지는 차이를 $h_S$가 $h^*$와 가지는 차이와 곱한 것이다. 만약 두 차이의 방향이 같다면 양수가 나오지만 만약 방향이 다르다면, 즉 $h_S$가 induction bias에 의한 loss를 줄이는 방향으로 작용한다면 음수가 나온다. 후자의 항은 $h_S$와 $h^*$간의 MSE로, 달성 가능한 최소 loss의 방향으로 감소한다.

## Bias-Variance Tradeoff

Bias와 variance의 표현은 정의의 반복에 지나지 않는다.

$$
\begin{aligned}
Bias(x) = E_{S} [h_S(x) - f(x)] &= E_{S}[\Delta h^*(x) + r_S(x)]
\end{aligned}
$$
$$
\begin{aligned}
Variance(x) = V_{S}[h_S(x) - f(x)] &= V_{S}[\Delta h^*(x) + r_S(x)]
\end{aligned}
$$
$$
E_S[l(h_S, x, f(x))] = Bias(x)^2 + Variance(x) = E_{S}[\Delta h^*(x) + r_S(x)]^2 + V_{S}[\Delta h^*(x) + r_S(x)]
$$

이때 가정 (1)을 적용하면 다음을 얻는다.

$$
\begin{aligned}
E_S[L_D(h_S)] &= E_SE_x[l(h_S, x, f(x))] = E_xE_S[l(h_S, x, f(x))] \\
&= E_x[Bias(x)^2 + Variance(x)] \\
&= E_x[Bias(x)^2] + E_x[Variance(x)] \\
\end{aligned}
$$

## Synthesis between two Decompositions

Approximation error와 bias squared 항을 비교하면 다음과 같다.

$$
\epsilon_{app} = E_x[\Delta h^*(x)^2] \qquad  E_x[Bias(x)^2] = E_x[E_S[\Delta h^*(x) + r_S(x)]^2]
$$

후자를 풀어 써보면 아래와 같이 된다.

$$
\begin{aligned}
E_x[Bias(x)^2] &= E_x[E_S[\Delta h^*(x) + r_S(x)]^2] \\
&= E_x[E_S[\Delta h^*(x)]^2] + 2E_x[E_S[\Delta h^*(x)]E_S[r_S(x)]] + E_x[E_S[r_S(x)]^2]
\end{aligned}
$$

따라서 만약 두 항이 같으려면 다음 조건이 성립해야 한다.

$$
2E_x[E_S[\Delta h^*(x)]E_S[r_S(x)]] + E_x[E_S[r_S(x)]^2] = 0 \cdots(4)
$$

이때 다음 조건이 성립하면 (4)가 성립한다.

$$
\forall x. E_{S}[r_S(x)] = 0 \cdots(4.1)
$$

(4.1)은 모든 입력값 $x$에 대해 ERM rule을 통해 주어진 $h_S(x)$가 $h^*(x)$의 unbiased estimation이라는 가정이다. 우리는 모델이 학습가능할 때 $h_S$가 충분히 큰 sample size에 대해 $h^*$로 수렴할 것이라고 생각할 수 있다. 따라서 이것이 성립한다고 가정해 보자. 그러면 approximation error와 bias의 관계는 다음과 같다.

$$
E_x[Bias(x)^2] = E_S[\epsilon_{app}] = \epsilon_{app} \cdots(5.1)
$$

이제 variance에 대해 살펴보자. 

$$
\begin{aligned}
E_x[Variance(x)] &= E_xV_{S}[\Delta h^*(x) + r_S(x)] = E_xV_S[r_S(x)] \\
&= E_x[E_S[r_S(x)^2] - E_S[r_S(x)]^2] \\
&= E_{S, x}[r_S(x)^2]
\end{aligned}
$$

따라서 estimation error의 식 (3.2)를 함께 고려하면 다음의 관계가 성립한다.

$$
\begin{aligned}
E_x[Variance(x)] &= E_S[\epsilon_{est}] \cdots (5.2)
\end{aligned}
$$

## Conclusion

이상의 논의를 통해 가정 (4.1)에서 (5.1)과 (5.2)를 유도했다. 우리는 이를 통해 충분히 강한 모델의 학습가능성 가정 하에서 bias-complexity tradeoff와 bias-variance tradeoff는 사실상 같은 것임을 알 수 있다.

Model space의 관점에서 좋은 learning method는 달성 가능한 최적의 모델 $h^*$와 모델이 제공하는 $h_S$의 잔차의 기댓값이 0이 되도록 하는 모델이다. 이때 loss의 선택에 따라 구체적인 learning path가 정해진다. L2-norm의 경우 $r_S^2$와 함께 $\langle \Delta h^*, r_S \rangle$이 estimation loss로 사용된다.