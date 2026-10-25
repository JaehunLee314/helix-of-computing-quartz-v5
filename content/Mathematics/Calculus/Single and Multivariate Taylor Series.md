**Prerequisites:** [[Differentiation]], [[Partial Derivative and Multivariate Chain Rule]]

[[Differentiation]]에서 미분가능성은 함수를 일차식으로 근사했을 때 오차가 $o(x - a)$라는 것이었다. 여러 번 미분가능한 함수는 더 높은 차수의 다항식으로 근사할 수 있고, 이때 오차는 더 빨리 감소한다.

## 테일러 정리

**정의. 테일러 다항식** 
실수 함수 $f$가 $a$에서 $N$번 미분가능하다고 하자. $N$차 테일러 다항식은 다음과 같다.

$$
T_N(x) = \sum_{n = 0}^N \frac{f^{(n)}(a)}{n!} (x-a)^n
$$

나머지항을 $R_N = f - T_N$이라고 한다.

**정리. 테일러 정리** 
$f$가 $a$에서 $N$번 미분가능하면 다음이 성립한다.

$$
f(x) = \sum_{n = 0}^N \frac{f^{(n)}(a)}{n!} (x-a)^n + \underset{x \to a}o((x-a)^N)
$$

$N = 1$인 경우가 [[Differentiation]]의 일차근사이다.

**정리. 테일러 전개의 유일성** 
$f$가 $a$에서 $N$번 미분가능하고 $f(x) = \sum_{n=0}^N c_n(x - a)^n + o_{x \to a}((x-a)^N)$ 이면 $c_n = \frac{f^{(n)}(a)}{n!}$ 이다.

즉 어떤 방법으로든 $o((x-a)^N)$ 오차의 다항식 근사를 찾으면 그것이 테일러 다항식이다.

**예시.**

- $e^x = 1 + x + \frac{x^2}{2} + o_{x \to 0}(x^2)$
- $\sin x = x + o_{x \to 0}(x^2)$
- $\cos x = 1 - \frac{x^2}{2} + o_{x \to 0}(x^3)$
- $\frac{1}{1 - x} = 1 + x + \cdots + x^N + \frac{x^{N+1}}{1 - x}$ 이고 마지막 항은 $o_{x \to 0}(x^N)$ 이므로, 유일성에 의해 도함수를 계산하지 않고도 테일러 다항식이 $1 + x + \cdots + x^N$ 임을 알 수 있다.

## 테일러 급수

$N \to \infty$로 보낸 급수를 테일러 급수라고 한다. 모든 $N$에서 $R_N(x) \in o_{x \to a}((x-a)^N)$ 이더라도 테일러 급수가 $f$로 수렴한다는 보장은 없다. 테일러 정리는 $x \to a$일 때의 성질이고, 수렴은 고정된 $x$에서 $N \to \infty$일 때의 성질이기 때문이다.

**예시.** $f(x) = e^{-1/x^2}$, $f(0) = 0$ 이면 모든 $n$에 대해 $f^{(n)}(0) = 0$ 이다. 따라서 $T_N = 0$ 이고 모든 $N$에서 $f(x) \in o_{x \to 0}(x^N)$ 이지만, $x \neq 0$이면 $f(x) \neq 0$ 이므로 테일러 급수는 $f$로 수렴하지 않는다.

## 다변수함수의 테일러 정리

이차까지만 살펴보자. $f: \mathbb{R}^n \to \mathbb{R}$이 $a$의 근방에서 $C^2$라고 하고, $\nabla^2 f(a)$를 $f$의 헤세 행렬이라고 하자.

**정리.** 다음이 성립한다.

$$
f(x) = f(a) + \nabla f(a)^{T}(x-a) + \frac{1}{2!}(x-a)^{T}\nabla^2 f(a)(x-a) + \underset{x \to a}o(\lVert x - a \rVert^2)
$$

## 참고문헌
(1) Wikipedia, [Taylor series](https://en.wikipedia.org/wiki/Taylor_series)  
(2) Wikipedia, [Taylor's theorem](https://en.wikipedia.org/wiki/Taylor%27s_theorem)  
(3) Walter Rudin, Principles of Mathematical Analysis
