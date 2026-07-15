Vapnik-Chervonenkis dimension (VC dimension)에 대해 살펴보자.

## VC Dimension의 정의

VC dimension을 정의하기 위해서는 먼저 다음 두 개념을 정의해야 한다.

**Definition. Restriction** 
어느 함수 $f : A \to B$와 집합 $C \subseteq A$에 대해서 $f$의 $C$에 대한 restriction $f_C : C \to B$는 다음을 만족하는 함수이다.

$$
c \in C \to f_C(c) = f(c)
$$

**Definition. Shattering**
가설 집합 $H \subseteq A \Rightarrow B$과 $C \subseteq A$에 대해서 $H_C = \{f_C : C \to B | f \in H\}$ 라고 정의하자. 이때 다음이 성립하면 $H$가 $C$를 shatter 한다고 한다.

$$
|H_C|=|C \Rightarrow B|
$$

(여기서 $X \Rightarrow Y$는 $X$에서 $Y$로 가는 모든 함수의 집합이다.)

이제 VC Dimension은 다음과 같이 정의된다.

**Definition. VC Dimension**
가설 집합 $H \subseteq A \Rightarrow B$의 VC dimension $VCDim(H)$는 다음과 같이 정의된다.

$$
VCDim(H) = max \{ m | \exists C, C \subseteq A, |C|=m, H \text{ shatters } C \}
$$

우리는 이와 비슷하게 growth function을 정의할 수 있다.

**Definition. Growth Function**
가설 집합 $H \subseteq A \Rightarrow B$에 대해 growth function $\tau_H : N \to N$은 다음과 같이 정의된다.

$$
\tau_H(m)=\underset{C \subseteq A, |C|=m}{max} |H_C|
$$
