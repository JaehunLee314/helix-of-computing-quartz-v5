**Prerequisites:** [[Notation for Arrow and Logic]], [[Category]], [[Functor]]

## Covariant Hom-Functor

어느 category $C$를 생각하자. 만약 모든 $x \in ob\ C$에 대해 $a \Rightarrow_C x \in ob\ \text{Set}$ 이라면, 즉 이 category의 hom-set이 항상 small set 이라면 다음과 같은 functor를 정의할 수 있다.

$$
C(a, -) \in C \Rightarrow \text{Set}
$$

구체적으로 어느 object $b \in ob\ C$에 대해서는 다음과 같이 정의되며

$$
C(a, -)(b) = (a \Rightarrow_C b)
$$

어느 morphism $f \in c \Rightarrow_C c'$에 대해서는 다음과 같이 정의된다.

$$
C(a, -)(f) = \alpha \in (a \Rightarrow_C c) \Rightarrow_{\text{Set}} (a \Rightarrow c')\quad s.t. \quad \alpha(w) = w;f
$$

## Contravariant Hom-Functor

비슷하게 category $C$에 대한 contravariant hom-functor는 다음과 같이 정의된다.

$$
C(-, b) \in C^{op} \Rightarrow \text{Set}
$$

Object $a \in ob\ C$에 대해서는 다음과 같이 정의되며

$$
C(-, b)(a) = (a \Rightarrow_C b)
$$

어느 morphism $f \in c \Rightarrow_C c'$에 대해서는 다음과 같이 정의된다. 

$$
C(-, b)(f^{op}) = \alpha \in (c' \Rightarrow_C b) \Rightarrow_{\text{Set}} (c \Rightarrow_C b)\quad s.t. \quad \alpha(w) = f;w
$$

## Footnote
- 만약 hom-set이 large set인 경우 그러한 hom-set을 담을 수 있는 $\text{Ens}$ category를 정의하여 $\text{Set}$ 대신 사용한다. 자세한 것은 참고문헌 (1)을 볼 것.
- 가독성을 높이기 위해 $(x \Rightarrow_C)$와 같은 double arrow는 arrow collection을 표현하기 위해서만 사용하므로 hom-functor $C(x, -)$와 동일한 의미를 가지지 않는다. 전자는 collection이고 후자는 functor이다.

## References
(1) Mac Lane, Categories for the Working Mathematicians

