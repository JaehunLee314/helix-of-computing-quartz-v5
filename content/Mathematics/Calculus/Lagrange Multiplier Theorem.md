**Theorem. Lagrange Multiplier Theorem**
어느 미분가능한 함수 $f: R^n \to R$을 가정하자. 이때 어떤 연속적으로 미분가능한 함수 $g: R^n \to R$의 level curve $A = \{ x | g(x) = k\} \subseteq R^n$를 생각하자. 이제 $f_A$가 $f$를 $A$로 restriction 하여 얻은 함수이면,  $x^*$가 $f_A$의 극점(extreme point)이고 $\nabla g(x^*) \neq 0$일 때 $\nabla f(x^*)\ //\ \nabla g(x^*)$가 성립한다.

*proof.*
이를 증명하기 위해 다음과 같은 조건에 의해 정의되는 곡선 $r: R \to R^n$을 생각하자.

- $t \in R \to g(r(t)) = k$
- $r(0) = x^*$

그러면 $r$의 정의에 의해 다음 식이 성립한다.

$$
0 = \frac{d}{dt} g(r(t)) = \frac{\partial g(r(t))}{\partial (r(t))} \frac{\partial r(t)}{\partial t} = \nabla g(r(t)) \cdot r'(t)
$$

이때 $t = 0$이라고 두면 $\nabla g(x^*) \cdot r'(0) = 0 \cdots (1)$을 얻는다. 또한 극점의 성질에 의해 다음 식이 성립한다.

$$
0 = \left . \frac{d}{dt}f(r(t)) \right |_{t = 0} = \nabla f(x^*) \cdot r'(0) \cdots (2)
$$

이제 앞선 조건을 만족하는 모든 $r$에 대해 이들 식이 성립한다는 사실을 고려하자. 그러면 우리는 가능한 모든 $r'(0)$에 대해 다음이 성립한다는 것을 알 수 있다.

$$
r'(0) \perp \nabla f(x^*) \qquad r'(0) \perp \nabla g(x^*)
$$

만약 $r'(0)$가 $n-1$차원 공간을 구성한다면 이와 수직인 $n$차원 벡터는 반드시 하나의 직선상에 위치해야 한다. 그런데 음함수 정리에 의해 실제로 $r'(0)$가 $n-1$차원 공간을 구성함이 알려져 있다. 따라서 두 미분은 같은 직선 상에 놓임으로 평행하다. $\boxed{}$

## References
(1) Stewart, 미분적분학
(2) Wikipedia, Lagrange multiplier, https://en.wikipedia.org/wiki/Lagrange_multiplier