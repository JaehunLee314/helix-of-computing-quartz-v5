**Prerequisites:** [[Numerator Layout of Matrix Calculus]]
## Linear Model

어느 확률변수 $x \in R^p, y \in R$이 결합확률분포 $p_{x, y}$ 를 따른다고 하자. 이제 이로부터 $n$개의 sample을 다음과 같이 독립적으로 추출했다고 하자.

$$
(x^{(1)}, y^{(1)}), ...., (x^{(n)}, y^{(n)}) \sim_{i.i.d} p_{x, y}
$$

이때 우리는 다음과 같은 선형 모델링을 생각할 수 있다.

$$
y \approx \beta_0 + \sum_{j = 1}^p \beta_j x_j \quad (x = (x_1\ x_2\ ...\ x_p)^T)
$$

즉, 각각의 sample에 대해서는 다음과 같다.

$$
y^{(i)} \approx \beta_0 + \sum_{j=1}^p \beta_jx^{(i)}_j = (\beta_0\ \beta_1 ... \beta_p) \begin{pmatrix} 1 \\ x^{(i)} \end{pmatrix}\ ...\ (1)
$$

이제 $\beta = (\beta_0\ \beta_1\ ... \ \beta_p)^T \in R^{p+1}$ 라고 하고 $X$, $Y$를 다음과 같이 정의하자. (이러한 $X$를 design matrix 라고도 한다.)

$$
X = \begin{pmatrix}
1\ (x^{(1)})^T \\
2\ (x^{(2)})^T \\
... \\
n\ (x^{(n)})^T \\
\end{pmatrix} \in R^{n \times (p+1)} \quad Y = (y_1\ y_2\ ...\ y_n)^T \in R^n
$$

이제 앞선 식 (1)은 다음과 같이 적을 수 있다.

$$
Y \approx X\beta
$$

## Interpretation of $col X$

$X$의 각 column은 다음과 같이 구성되어 있다.

$$
\begin{pmatrix}x^{(1)}_f \\ x^{(2)}_f \\ \vdots \\ x^{(n)}_f \end{pmatrix}
$$

따라서 어느 vector space에 대해 각 standard basis가 하나의 sample을 의미하고, 각 vector가 feature $f$를 사용한 sample의 representation을 의미한다고 하면 $X$의 column space는 모든 sample에 대한 known representation의 linear interpolation을 의미한다. 

한편 $Y$ 역시 이와 같은 vector space에 속하고, 따라서 $Y$는 sample에 알려지지 않은 어떤 feature를 사용한 데이터의 representation 이라고 할 수 있다.

## Least Square Method

이제 우리는 다음과 같은 loss function을 통해 $\beta$를 근사할 수 있다. 이때 $[X]_i$는 $X$의 $i$번째 행을 의미한다.

$$
RSS(\beta) = (Y-X\beta)^T(Y-X\beta) = \sum_{i=1}^n (y^{(i)} - [X]_i\beta)^2
$$
$$
\hat{\beta} = argmin_\beta\ RSS(\beta)
$$

이제 $RSS(\beta)$의 극점을 찾기 위해 미분하면 다음을 얻는다.

$$
\frac{\partial}{\partial \beta} RSS(\beta) = (I^T + I)(Y-X\beta)^T(-X)=-2X^T(Y-X\beta)
$$
$$
\frac{\partial}{\partial \beta}\frac{\partial}{\partial \beta^T} RSS(\beta) = \frac{\partial}{\partial \beta} (-2X^T(Y-X\beta))^T = \frac{\partial}{\partial \beta} (2X^T X\beta))^T = \frac{\partial}{\partial \beta} 2\beta^TX^T X = 2X^TX
$$

이제 Hessian이 positive definite이면 $RSS(\beta)$가 gradient가 0인 지점에서 극소값을 가진다. 그런데 만약 $X$의 column vector가 linearly independent 하다면 $X^TX$ 는 positive definite이다. 그 이유는 다음과 같다.

먼저,

$$
v^TX^TXv = (Xv)^TXv = |Xv|^2 \geq 0
$$

이고 $X$의 column이 linearly independent 함으로 $Xv = 0$은 오직 trivial solution $v = 0$만을 가진다. 따라서

$$
v \neq 0 \to vX^TXv > 0
$$

이므로 $X^TX$는 positive definite이다. 

앞선 해석을 고려하면 $X$의 column이 linearly independent하다는 것은 서로 다른 feature에 대한 data representation이 데이터의 서로 다른 특성을 잘 포착한다는 것이다. 일반적으로 $p \ll n$ 이고 각 feature가 충분히 representative 하다면 우리는 $X$의 column이 linearly independent 하다고 가정할 수 있다.

이 가정으로부터 $\beta$의 극솟값을 구하기 위해 gradient가 0 이라고 두면 다음과 같이 된다.

$$
X^T (Y-X\hat{\beta}) = 0 \to X^TY = X^TX\hat{\beta} \to (X^TX)^{-1}X^TY = \hat{\beta}
$$

이러한 $\hat{\beta}$가 유일하게 정의되기 때문에 이는 RSS를 통한 optimization에 대한 global minimun 이다.

## Note on Orthogonal Projection

$X$의 column이 linearly independent 할 때 벡터 $Y$로부터 $col X$로의 orthogonal projection은 다음과 같이 정의된다.

$$
proj_{col X} Y = X(X^TX)^{-1}X^T Y
$$

이때 다음이 성립한다.

$$
proj_{col X} Y = X\hat{\beta}
$$
$$
\Rightarrow X(X^TX)^{-1}X^TY = X\hat{\beta}
$$
$$
\Rightarrow X^TX(X^TX)^{-1}X^TY = X^TX\hat{\beta}
$$
$$
\Rightarrow X^TY = X^TX\hat{\beta}
$$
$$
\Rightarrow (X^TX)^{-1}X^TY = \hat{\beta}
$$

앞선 해석을 고려하면 RSS는 새로운 data representation $Y$를 알려진 data representation space $col X$로 사영시키는 과정이라고 할 수 있다.

## References
(1) Trevor Hastie et al, The Elements of Statistical Learning 2ed.


