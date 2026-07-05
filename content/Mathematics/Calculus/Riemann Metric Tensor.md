## Quadratic Form Distance

우리는 Euclidean space에서 두 지점 $x, y$ 간의 거리(a.k.a. L2-norm)가 다음과 같이 정의된다는 사실을 안다.

$$
dist^2(x, y) = (x-y)^T(x-y)
$$

그렇다면 보다 일반적으로 우리는 다음과 같은 거리를 정의해 볼 수 있다.

$$
dist^2(x, y) = (x-y)^T S (x-y) \quad (S \text{ is p.d.})
$$

이때 $S$ 가 p.d. (positive definite) 이라는 것은 $x \neq 0 \to x^T S x > 0$ 이라는 것이다. 우리는 이와 같은 거리를 quadratic form distance 라고 부른다. 이러한 거리 함수는 당연히 inner-product space를 구성하는 데 사용될 수 있다. (보다 정확히는 inner product를 정의함으로써 거리를 유도하게 된다.)

## Riemann Metric Tensor 

이제 어떤 manifold $M$을 생각해보자. Manifold의 가장 중요한 성질은 그것이 국소적으로 어떤 Euclidean space와 비슷하게 생겼다는 것이다.

이제 우리는 manifold의 어느 국소적인 지점에서 quadratic form distance를 사용해 inner-product space를 정의하는 것으로 manifold에서의 metric을 정의할 수 있다. 다시 말하면 manifold에서의 거리 함수의 이차근사로 quadratic form distance를 사용할 수 있다.

$$
dist_{M}^2 (v, w) = (v-w)^T S(v) (v-w) + o(|v-w|^2)
$$

다른 표기법으로, manifold $M$의 점 $v$ 주변 국소 좌표계의 미소 변위 성분 $dx_i$들에 대해 line segment $ds$는 다음과 같이 정의된다.

$$
ds^2 = \sum_{i, j} S_{i, j}(v) dx_i dx_j = dx^T S(v) dx
$$

따라서 $\gamma$는 $x$에서 $y$로 가는 geodesic 이라고 할 때 다음 적분이 $M$의 전역적인 거리로 주어진다.

$$dist_M(x, y) = \int_{\gamma} ds$$

이와 같은 $S$를 Riemann metric tensor 라고 부른다.

## Footnote
- 비슷하게 생겼다는 것은 위상동형(homeomorphic)이거나 나아가서는 미분동형이라는 뜻이다.
- 통계학에서 covariance matrix의 역행렬을 이용한 quadratic form distance 는 Mahalanobis distance 라고도 한다.

## References
(1) Metric tensor, wikipedia (https://en.wikipedia.org/wiki/Metric_tensor)  
(2) Manifold, wikipedia (https://en.wikipedia.org/wiki/Manifold)

