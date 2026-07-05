- **Prerequisites:** [[Information Content and Entropy]]
## KL Divergence의 정의

KL divergence 혹은 Kullback-Leibler distance는 다음과 같이 정의된다.

$$
D(p||q) = E_{X \sim p}(i_{X \sim q}(X) - i_{X \sim p}(X))
$$

이때 이산확률변수를 가정하고 우변을 풀어 보면 다음과 같이 된다.

$$
E_{X \sim p}(i_{X \sim q}(X) - i_{X \sim p}(X)) = \sum_{x \in \mathcal{X}} (i_{X \sim q} (X=x) - i_{X \sim p}(X=x)) \cdot p(x)
$$
$$
= \sum_{x \in \mathcal{X}} (-log_2 q(x) - (-log_2 p(x))) \cdot p(x) = \sum_{x \in \mathcal{X}} log_2 \frac{p(x)}{q(x)} \cdot p(x)
$$

## Cross Entropy의 정의

Cross Entropy는 다음과 같이 정의된다.

$$
CE(p||q) = E_{X \sim p}(i_{X \sim q}(X))
$$

따라서 KL divergence는 다음과 같다.

$$
D(p||q) = CE(p||q) - H_{X \sim p}(X)
$$

## KL Divergence의 의미

만약 어느 메시지에 대해 $W \sim p$ 라고 하자. 메시지를 이진수로 표기할 때, 그 길이를 최소한으로 하는 인코딩(혹은 code)의 평균 길이는 $H(W)$로 주어진다. 그런데 우리가 $p$에 대한 code가 아니라 $q$에 대한 code를 사용하면 그 길이는 $H(W) + D(p||q)$ 가 된다. 이때 $D(p||q)$는 정확한 분포를 사용하지 않았기 때문에 발생하는 비효율이다.

## References
(1) Thomas M. Cover, Joy A. Thomas, Elements of Information Theory 2nd ed.

