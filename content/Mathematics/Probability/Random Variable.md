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

예를 들어 확률변수 $X, Y, Z$에 대해서 $Z = X + Y$가 성립한다고 하자. 그러면 $P(X = x) > 0$일 때 조건부 확률은 다음과 같이 주어진다.

$$
P(Z = z | X = x) = \frac{P(Z = z, X = x)}{P(X = x)} = \frac{P(X+Y=z, X = x)}{P(X=x)} = \frac{P(x+Y=z, X = x)}{P(X=x)}
$$

이때 $X, Y$가 독립이라면 다음과 같이 된다.

$$
\frac{P(x+Y=z, X = x)}{P(X=x)} = \frac{P(x+Y=z)P(X=x)}{P(X=x)} =P(x + Y = z)
$$

## Practical Understanding of a Random Variable

일상적으로 우리는 변수를 정의할 때 그것이 가지는 의미를 통해 정의한다. 예를 들어 변수 $x$는 어느 삼각형의 한 변의 길이를 의미할 수 있다. 이와 같이 정의할 때 우리는 변수 하나를 어떤 고정된 의미의 대상 하나에 대응시키며, 각 변수 간의 관계를 이와 같은 의미론이 주는 함의에 의해 유도한다. 보다 형식적인 상황에서 이러한 행위는 변수를 어떤 논리적 맥락에 bounding 시키는 것으로 이해할 수 있다.

확률변수 역시 비슷하게 사용된다. 예를 들어서 $X$가 주사위의 값을 나타내는 확률변수라고 해 보자. 이때 우리는 변수가 '구체적인 하나의 값'을 가지는 것이 아니라 '우리의 믿음 속에 있는', 혹은 '반복된 실험을 통해 관측된' 각 주사위의 값이 나타날 개연성을 모두 포함한 대상이라고 생각할 수 있다. 이와 같은 해석은 우리가 충분한 지식을 가지고 있지 않은 어떤 대상에 숫자를 부여할 때 매우 유용하다.

이제 우리가 주사위를 실제로 굴려 $3$이 나왔다고 해 보자. (이와 같은 행위를 확률적 시행이라고 한다.) 만약 $X$가 여전히 같은 의미를 가진다면 $X$는 이제 불확실한 확률을 가지는 대상이 아니라 구체적인 값 $3$을 가지는 (혹은, $3$을 가질 확률이 $1$인) 변수로 이해하는 것이 적절하다. 수학적으로 앞서서 말한 $X$와 지금의 $X$는 다른 대상이다. 하지만 직관적으로 우리는 $X$가 확률적 시행에서 이루어진 관측을 통해 하나의 값으로 collapse 혹은 degeneration 되었다고 이해할 수 있다.

사실 우리는 이것을 조건부 확률을 통해 표현할 수 있다. 조건부 확률은 가정이 되는 확률변수의 실제 관측치가 주어질 때 결과가 되는 확률변수의 변화된 확률분포를 나타낸다. 앞선 경우를 살펴보면 우리는 다음과 같이 계산할 수 있다.

$$
P(X = x | X = 3) = \frac{P(X=x, X=3)}{P(X=3)} = \cases{
1 \quad (x = 3) \\
0 \quad (otherwise)
}
$$

이때 조건부 확률분포 $X|X=3$이 우리가 앞서 말한 '확률적 시행 이후의 확률변수'를 나타내는 수학적 표기법이다. 보다 일반적으로 만약 확률변수 $X$의 관측치에 의해 확률변수 $Y$의 확률분포가 $D(X)$로 결정된다면 $Y|X \sim D(X)$와 같이 적을 수 있다. 이때 $P(Y=y|X=x) = D(x)(y)$로 정의된다.

## Footnote
- 변수의 bounding은 formal logic이나 type theory를 살펴볼 것. 우리는 변수로 구성된 context와 그러한 context간의 calculus가 category를 이룬다고 말할 수도 있다.

## References
(1) Casella & Berger, Statistical Inference
