**Prerequisites:** [[LTI System]]

Impulse response는 시스템의 특성을 파악하는 데 있어 중요한 도구로서 작용한다. 여기서는 impulse response 및 그것과 convolution의 관계를 알아본다.

## Impulse Response

Impulse는 짧은 시간동안 높은 값이 발생하는 신호로 디렉-델타 함수 $\delta$를 통해 모델링할 수 있다. 이때 $\delta$는 다음을 만족하는 임의의 함수이다.

$$
\int_{-\infty}^{\infty} x(t)\delta(t)dt = x(0)
$$

Impulse response는 시스템에 impulse를 입력했을 때의 출력을 의미한다. 즉, 시스템의 impulse response $h(t)$는 다음과 같이 적을 수 있다.

$$
h = H\delta
$$

## Impulse의 합을 통한 신호의 표현

임의의 신호 $x(t)$는 다음과 같이 지연된 impulse의 합으로 표현할 수 있다.

$$
x(t) = \int_{-\infty}^{\infty} x(\tau)T_t\delta(\tau) d\tau
$$

왜냐하면

$$
\begin{aligned}
\int_{-\infty}^{\infty} x(\tau)T_\tau\delta(t) d\tau &= \int_{-\infty}^{\infty} x(\tau)\delta(\tau-t) d\tau \\
&= \int_{-\infty}^{\infty} x(u+t)\delta(u) du \quad (u = \tau - t) \\
&= \int_{-\infty}^{\infty} T_{-t}x(u)\delta(u) du \\
&= T_{-t}x(0) = x(0 + t) = x(t)
\end{aligned}
$$

과 같기 때문이다. 한편 

$$
T_t\delta(\tau) = \delta(\tau - t) = \delta(t - \tau) = T_\tau\delta(t)
$$

이므로 위 식은

$$
x(t) = \int_{-\infty}^{\infty} x(\tau)T_t\delta(\tau) d\tau = \int_{-\infty}^{\infty} x(\tau)T_\tau\delta(t) d\tau
$$

와 같이 적을 수 있다. 이때 두 번째 식의 의미를 조금 더 자세히 살펴보자.
우리는 이 식을 다음과 같이 근사할 수 있다.

$$
\int_{-\infty}^{\infty} x(\tau)T_\tau\delta(t) d\tau \approx \sum_{n=-\infty}^{\infty} x(n\Delta)T_{n\Delta}\delta(t) \Delta 
$$

이때 $t = k\Delta$라고 하자. 또한 $\delta(t)$를 다음과 같이 근사하자.

$$
\delta(t) = \begin{cases} 1/\Delta & \text{if } t = 0 \\ 0 & \text{otherwise} \end{cases}
$$

그러면 우리는 다음과 같이 쓸 수 있다.

$$
\begin{aligned}
&\sum_{n=-\infty}^{\infty} x(n\Delta)T_{n\Delta}\delta(t) \Delta \\
&= \cdots + x((k-1)\Delta)T_{(k-1)\Delta}\delta(t) \Delta + x(k\Delta)T_{k\Delta}\delta(t) \Delta + x((k+1)\Delta)T_{(k+1)\Delta}\delta(t) \Delta + \cdots \\
&= \cdots + x((k-1)\Delta)T_{(k-1)\Delta}\delta(k\Delta) \Delta + x(k\Delta)T_{k\Delta}\delta(k\Delta) \Delta + x((k+1)\Delta)T_{(k+1)\Delta}\delta(k\Delta) \Delta + \cdots \\
&= \cdots + 0 + x(k\Delta) \cdot 1 + 0 + \cdots \\
&= x(k\Delta) = x(t)
\end{aligned}
$$

이처럼 이 식을 $t$에서 evaluation 하면 나머지 부분의 값이 모두 0이 되어 $x(t)$가 남게 된다. 이는 $x(t)$가 impulse의 합으로 표현될 수 있음을 의미한다.

이 식을 아래와 같은 형태로 자주 적게 될 것이다.

$$
x = \int_{-\infty}^{\infty} x(\tau)T_\tau\delta d\tau
$$


## LTI Systems의 Impulse Response

LTI 시스템의 확장된 시불변성을 이용하면 출력되는 신호를 impulse response의 합으로 표현할 수 있다.
$y = Hx$ 이고 $h = H\delta$ 라고 하자. 이제,

$$
\begin{aligned}
y = Hx &= H\int_{-\infty}^{\infty} x(\tau)T_\tau\delta d\tau \\ &= \int_{-\infty}^{\infty} x(\tau)HT_\tau\delta d\tau \\ &= \int_{-\infty}^{\infty} x(\tau)T_\tau H \delta d\tau \\
&= \int_{-\infty}^{\infty} x(\tau)T_\tau h d\tau
\end{aligned}
$$

와 같음으로 정리하면 다음이 성립한다.

$$
y = \int_{-\infty}^{\infty} x(\tau)T_\tau h d\tau
$$

## Convolution

두 신호 $x, h$의 convolution은 다음과 같이 정의된다.

$$
(x * h) = \int_{-\infty}^{\infty} x(\tau)T_\tau h d\tau
$$

따라서 신호의 표현은 다음과 같이 쓸 수 있다.

$$
x = x * \delta
$$

또한 LTI 시스템 $H$의 출력은 다음과 같이 쓸 수 있다.

$$
y = Hx = H(x * \delta) = x * H(\delta) = x * h
$$

## References
(1) Oppenheim et al, Signals and Systems (Second Edition), Pearson

