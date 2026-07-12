## Random Variable의 정의

Random variable은 다음과 같이 정의된다.

**Definition. Random Variable**
Sample space가 $S$로 주어질 때 random variable $X$는 $S$에서 $\mathbb{R}$로 가는 함수이다. 이때 집합 $A \subseteq \mathbb{R}$에 대하여 다음과 같이 표기한다. ($X(S)$는 $X$의 image이다.)

$$
P(X \in A) = P(\{ s \in S | X(s) \in A\})
$$

만약 어떤 일차술어 $U$가 존재하여 $X \in A \leftrightarrow U(X)$라면 다음과 같이 표기한다.

$$
P(U(X)) = P(X \in A)
$$

Random variable에는 대표적으로 두 가지 종류가 있다.

**Definition. Discrete Random Variable and Continuous Random Variable**
Random variable $X : S \to \mathbb{R}$에 대해 $|X(S)| \leq |\mathbb{N}|$이면 $X$를 discrete random variable이라고 한다. 한편 이하에서 정의되는 확률밀도함수가 존재하면 $X$를 continuous random variable이라고 한다.

$X$가 discrete random variable일 때 함수 $p$가 다음과 같이 정의되면 이를 $X$의 확률질량함수라고 한다.

$$
p(x) = P(X=x)
$$

$X$가 continuous random variable일 때 함수 $f$가 다음과 같이 정의되면 이를 $X$의 확률밀도함수라고 한다.

$$
\int_{-\infty}^{x} f(t)dt = P(X \leq x)
$$

확률질량함수와 확률밀도함수를 통틀어 확률분포라고 한다. 만약 $X$가 확률분포 $h$를 가지면 $X \sim h$라고 적고 $X$가 확률분포 $h$를 따른다고 한다.

## Conditional Probability & Random Variables

**Definition. Conditional Probability & Random Variables**
확률변수 $X, Y : S \to \mathbb{R}$와 집합 $A, B \subseteq \mathbb{R}$에 대하여 conditional probability는 다음과 같이 정의된다.

$$
P(Y \in B | X \in A) = \frac{P(X \in A, Y \in B)}{P(X \in A)} \quad (P(X \in A) >0)
$$

만약 어떤 일차술어 $U, W$가 존재하여 $X \in A \leftrightarrow U(X), Y \in B \leftrightarrow W(Y)$라면 다음과 같이 표기한다.

$$
P(W(Y)|U(X)) = P(Y \in B | X \in A)
$$

## Example

확률변수 $X, Y, Z$에 대해서 $Z = X + Y$가 성립한다고 하자. 그러면 $P(X = x) > 0$일 때 조건부 확률은 다음과 같이 주어진다.

$$
P(Z = z | X = x) = \frac{P(Z = z, X = x)}{P(X = x)} = \frac{P(X+Y=z, X = x)}{P(X=x)} = \frac{P(x+Y=z, X = x)}{P(X=x)}
$$

이때 $X, Y$가 독립이라면 다음과 같이 된다.

$$
\frac{P(x+Y=z, X = x)}{P(X=x)} = \frac{P(x+Y=z)P(X=x)}{P(X=x)} =P(x + Y = z)
$$

## Footnote
- 보다 일반적인 정의에서 연속확률변수는 연속적인 cumulative distribution function에 의해 정의된다.

## References
(1) Casella & Berger, Statistical Inference
