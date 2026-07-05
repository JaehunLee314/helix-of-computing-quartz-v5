**Prerequisites:** [[Category]], [[Functor]], [[Cone]]

## Terminal Object

Category $C$의 object $t$에 대해 다음이 성립할 때 이를 terminal object라고 부른다.

$$
c \in ob\ C \to \exists! f, f \in c \Rightarrow t
$$

이제 아래가 성립한다.

**Theorem.** $C$의 terminal object $t$는 unique up to unique isomorphism 하다.

**Proof**. $t, t'$이 $C$의 terminal object라 하자. 그러면 정의에 의해 $a \in t \Rightarrow_C t'$인 $a$와 $b \in t' \Rightarrow_C t$인 $b$가 유일하게 존재한다. 이때 $a ; b \in t \Rightarrow_C t$ 이며 $id_t \in t \Rightarrow_C t$ 이므로 terminal object의 정의를 적용하면 $a;b = id_t$ 이며 비슷하게 $b;a = id_{t'}$ 이다. 이로부터 $a, b$가 isomorphism 이므로 $t \cong t'$ 이 성립하며 $a, b$가 유일함으로 terminal object는 unique up to unique isomorphism 이라고 할 수 있다.

## Limit

어느 $Cone\ D$에 대해 $lim\ D$는 $Cone\ D$의 terminal object이다.

## References
(1) Brendan Fong, David I. Spivak, Seven Sketches in Compositionality