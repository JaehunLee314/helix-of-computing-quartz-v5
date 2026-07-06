## Universal Arrow

![[UniversalArrow.png]]
*(그림에서 $\to$는 하나의 morphim을, $\Rightarrow$는 두 object간에 정의된 모든 morphism의 hom-set을 의미한다.)*

**Definition. Universal Arrow**
Category $D$에서 $C로 가는 functor $S$와 어느 $c \in ob\ C$에 대하여 어느 $r \in ob\ D$과 $u \in c \Rightarrow_C S(r)$이 존재하여 모든 $f \in c \Rightarrow S(d)$에 대해 $f = u ; S(f')$인 $f' \in r \Rightarrow d$가 유일하게 존재하도록 한다면 이러한 $r, u$의 순서쌍 $(r, u)$를 $c$에서 $S$로 가는 universal arrow 라고 한다. 

## Properties of Universal Arrow

Universal arrow에 대해 다음 세 명제가 서로 동치이다.

1. $(r, u)$가 $c$에서 $S$로 가는 universal arrow이다.
2. 모든 $d \in ob\ D$에 대해 $\phi_d \in (r \Rightarrow_D d) \Rightarrow (c \Rightarrow_C S(d))$인 bijection $\phi_d$가 존재하며 $\phi_d(f') = u ; S(f')$ 으로 정의된다.
3. hom-functor $D(r, -)$에서 $C(c, S(-))$로 가는 natural isomorphim $\phi$가 존재하며 그 $d$-component가 $\phi_d(f') = u;S(f')$로 정의된다.

먼저 (1)과 (2)가 동치임을 보이자.

**Proposition 1.1.**
만약 모든 $d \in ob\ D$에 대해 $\phi_d \in (r \Rightarrow_D d) \Rightarrow (c \Rightarrow_C S(d))$인 bijection $\phi_d$가 존재하여 $\phi_d(f') = u ; S(f')$ 으로 정의되는 것과 $(r, u)$가 universal arrow인 것은 서로 동치이다.

*Proof.* 생략

이제 (2)와 (3)이 동치임을 보이자.

**Proposition 1.2.**
$\phi_d \in (r \Rightarrow_D d) \Rightarrow (c \Rightarrow_C S(d))$인 bijection $\phi_d$가 존재하여 $\phi_d(f') = u;S(f')$인 것과 hom-functor $D(r, -)$에서 $C(c, S(-))$로 가는 natural isomorphim $\phi$가 존재하여 그 $d$-component가 $\phi_d(f') = u;S(f')$로 정의되는 것은 동치이다. 

*Proof.*
*(전자에서 후자를 증명)*
가정에서 주어진 $\phi$가 모든 $d$에 대해 bijection이고 natural하면 이는 natural isomorphism이라고 할 수 있다. 가정에 의해 $\phi_d$가 bijection이므로 naturality만 보이면 충분하다. 이때 naturality는 다음 commutative diagram에 의해 정의된다.

$$
\begin{array}{ccccc} 
D & \qquad \qquad & & \text{Set or Ens} & \\ 
d & \qquad \qquad & D(r, d) & \stackrel{\phi_d}{\longrightarrow} & C(c, S(d)) \\ 
\llap{\scriptstyle g}\bigg\downarrow & & \llap{\scriptstyle D(r, g)}\bigg\downarrow & & \bigg\downarrow\rlap{\scriptstyle \ C(c, S(g))} \\ d' & \qquad \qquad & D(r, d') & \stackrel{\phi_{d'}}{\longrightarrow} & C(c, S(d'))
\end{array}
$$

이때 $f' \in r \Rightarrow_D d$에 대하여 다음 두 식이 같아야 한다.

$$
(\phi_d ; C(c, S(g)))(f') = C(c, S(g))(u ; S(f')) = u ; S(f');S(g)
$$
$$
(D(r, g);\phi_{d'})(f') = \phi_{d'}(f';g)=u;S(f';g)=u;S(f');S(g)
$$

두 결과가 같음으로 naturality가 성립한다.

*(후자에서 전자를 증명)*
$\phi$가 natural isomorphism 이므로 위의 diagram이 commute 한다. 이제 $d = r$이라고 두면 다음과 같이 된다.

$$
\begin{array}{ccccc} 
D & \qquad \qquad & & \text{Set or Ens} & \\ 
r & \qquad \qquad & D(r, r) & \stackrel{\phi_r}{\longrightarrow} & C(c, S(r)) \\ 
\llap{\scriptstyle g}\bigg\downarrow & & \llap{\scriptstyle D(r, g)}\bigg\downarrow & & \bigg\downarrow\rlap{\scriptstyle \ C(c, S(g))} \\ d' & \qquad \qquad & D(r, d') & \stackrel{\phi_{d'}}{\longrightarrow} & C(c, S(d'))
\end{array}
$$

이때 $id_r \in ob\ D(r, r)$에 대하여 다음 두 식이 같아야 한다.

$$
(\phi_r ; C(c, S(g)))(id_r) = C(c, S(g))(\phi_r(id_r)) =\phi_r (id_r);S(g)
$$
$$
(D(r, g);\phi_{d'})(id_r) = \phi_{d'}(id_r;g) = \phi_{d'}(g)
$$

따라서 아래 식이 성립해야 한다.

$$
\phi_r(id_r);S(g) = \phi_{d'}(g)
$$

이는 임의의 $d'$에 대해 성립함으로 전자를 증명한 것과 같다. $\boxed{}$

## References
(1) Mac Lane, Categories for the Working Mathematicians