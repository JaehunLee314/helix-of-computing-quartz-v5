신호 분석의 기초가 되는 LTI 시스템과 그 특성을 살펴보자.

## 신호와 시스템

신호는 보통 시간에 대한 어떤 값으로 이해된다. 따라서 실수 범위의 모든 신호의 집합은 단순히 $\mathbb{R}^\mathbb{R}$이다. (참고로, $Y^X = \{ f: X \rightarrow Y \}$) 이하에서 우리는 이러한 실수 범위의 신호를 주로 다룬다.

이제 신호에 대한 시스템이란 신호에서 다른 신호로 가는 함수이다. 따라서 우리는 어떤 시스템 $H$는 다음과 같다고 할 수 있다.

$$
H: \mathbb{R}^\mathbb{R} \rightarrow \mathbb{R}^\mathbb{R}
$$

그러므로 신호와 시스템을 정확하게 표기한다면 우리는 통상적으로 쓰이는

$$
H(x(t)) = y(t)
$$

와 같은 표기가 아니라

$$
H(x)(t) = y(t)
$$

와 같이 표기해야 한다. 이는 $H$가 함수 $x$를 받아 함수 $y$를 출력하는 함수라는 것을 명확히 하기 위함이다.

이 글에서는 이와 같은 명확한 표기를 채용하되, 괄호가 너무 많이 쓰이는 것을 방지하기 위해 다음과 같이 시스템이 신호에 적용되는 경우에 한하여 괄호를 때때로 생략할 것이다.

$$
H(x)(t) = Hx(t) = y(t)
$$

또한 우리는 다음과 같은 표현을 자연스럽게 사용한다.

$$
Hx = y
$$

이는 함수를 값으로 취급하는 선형대수학의 관점에서 자연스러운 표현이다.

## Delay

어떤 신호가 $k$초 만큼 delay된다는 것은 그 신호가 본래 신호에 비해 $k$초 뒤에 발생한다는 것을 의미한다. 이를 식으로 표기하면 다음과 같다.

$$
T_kx(t) = x(t-k)
$$

우리는 앞으로도 $T_k$를 delay operator로 사용한다.

## LTI 시스템의 정의

LTI(Linear Time-Invariant) 시스템은 다음과 같은 두 성질을 만족하는 시스템을 말한다.

**선형성(Linear)**
$$
\begin{aligned}
H(ax + by) &= aHx + bHy
\end{aligned}
$$

**시불변성(Time-Invariant)**
$$
HT_kx = T_kHx
$$

이때 LTI 시스템의 시불변성에는 적분에 대한 보다 확장된 정의가 주로 사용된다. 이는 다음과 같다.

**확장된 시불변성(Extended Time-Invariant)**
$$
H(\int_{[a, b]} g(\tau)T_\tau x d\tau) = \int_{[a, b]} g(\tau)T_\tau H x d\tau \quad ([a, b] \subseteq \mathbb{R})
$$

## 확장된 시불변성

확장된 시불변성을 이해하기 위해 적분의 정의를 생각해 보자. 우리는 좌변의 식으로부터 다음의 근사를 생각할 수 있다. 

$$
\begin{aligned}
H(\int_{[a, b]} g(\tau)T_\tau x d\tau) &= H(\lim_{n \rightarrow \infty} \sum_{i=1}^{n} g(\tau_i)T_{\tau_i}x\Delta \tau_i)\\
&\approx \lim_{n \rightarrow \infty} H(\sum_{i=1}^{n} g(\tau_i)T_{\tau_i}x\Delta \tau_i)\\
&= \lim_{n \rightarrow \infty} \sum_{i=1}^{n} g(\tau_i)T_{\tau_i}Hx\Delta \tau_i\\
&= \int_{[a, b]} g(\tau)T_\tau H x d\tau
\end{aligned}
$$

이것이 "확장된" 것이라는 의미는 위의 계산 과정에서 발생한 근사를 허용한다는 의미이다.

## References
(1) Oppenheim et al., Signals and Systems (Second Edition), Pearson