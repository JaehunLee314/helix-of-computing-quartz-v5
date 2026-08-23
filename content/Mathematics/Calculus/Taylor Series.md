## Motivation

임의의 함수 $f$를 이해하는 방법 중 하나는 이 함수를 다항함수로 표현하는 것이다. 어떤 경우에 $f$는 유한한 항으로 표현될 수 있지만 대부분의 경우에는 그렇지 않다. 따라서 우리는 $f$를 다항함수로 표현하는 방법과 그때 발생하는 오차에 대해 살펴보아야 한다.

## Single-variable Case

어느 지점 $a \in \mathbb{R}$에서 $N$번 미분가능한 함수 $f : \mathbb{R} \to \mathbb{R}$을 생각하자. 그러면 다음과 같은 함수 $R : \mathbb{R} \to \mathbb{R}$을 정의할 수 있다.

$$
f(x) = \sum_{n=0}^N \frac{f^{(n)}(a)}{n!}(x-a)^n + R(x)
$$

이때 $R$은 다항근사의 오차항이다. 이때 다음이 성립한다는 것이 알려져 있는데, 이를 테일러 정리(Taylor's theorem)라고 한다.

$$
\lim_{x \to a} \frac{R(x)}{(x-a)^N} = 0
$$

## Multi-variable Case

다변수 함수의 경우 식이 다소 복잡하므로 여기서는 이차항까지만 살펴본다. 

어느 지점 $a \in \mathbb{R}^n$에서 $N$번 미분가능한 함수 $f : \mathbb{R}^n \to \mathbb{R}$을 생각하자. 그러면 다음과 같은 함수 $R : \mathbb{R}^n \to \mathbb{R}$을 정의할 수 있다.

$$
f(x) = f(a) + \nabla f(a)^T (x-a) + \frac{1}{2!}(x-a)^T \nabla^2 f(a) (x-a) + R(x)
$$

이때 $R$은 다음을 만족한다.

$$
\lim_{x \to a} \frac{R(x)}{||x-a||^2} = 0
$$

## References
- Wikipedia, Taylor series (https://en.wikipedia.org/wiki/Taylor_series)
- Wikipedia, Taylor's theorem (https://en.wikipedia.org/wiki/Taylor's_theorem)