**Prerequisites:** [[Natural Transformation]]. [[Hom-Functor]], [[Universal Arrow]]
## Yoneda Lemma

Yoneda lemma는 다음과 같이 주어진다.

**Lemma. Yoneda Lemma**
Functor $K \in D \Rightarrow \text{Set}$와 $r \in ob\ D$를 가정하자. 또한 $D$의 임의의 hom-set $x \Rightarrow_D y$가 모두 small set이라고 하자. 그러면 다음과 같은 bijection $\gamma$가 존재하며,

$$
\gamma \in (D(r, -) \Rightarrow_{\text{Set}^D} K) \Rightarrow K(r)
$$

아래와 같이 정의된다.

$$
\gamma(\alpha) = \alpha_r(id_r)
$$

따라서 다음이 성립한다.

$$
D(r, -) \Rightarrow_{\text{Set}^D} K \cong K(r)
$$

*Proof.*
이 보조정리를 증명하기 위해서는 위와 같이 정의되는 $\gamma$가 injective 하고 surjective 함을 보여야 한다. 이를 보이기 위해 먼저 다음이 필요하다.

*(Property of $\alpha$)*
임의의 $\alpha \in D(r, -) \Rightarrow_{\text{Set}^D} K$와, 임의의 $d \in ob\ D, f' \in r \Rightarrow_D d$에 대해 다음 식이 성립한다.

$$
\alpha_{d}(f') = K(f')(\alpha_r(id_r))
$$

그 증명은 다음과 같다. $\alpha$는 natural transformation이므로 다음 diagram이 commute 한다.

$$
\begin{array}{ccccc} 
D & \qquad \qquad & & \text{Set} & \\ 
r & \qquad \qquad & D(r, r) & \stackrel{\alpha_r}{\longrightarrow} & K(r) \\ 
\llap{\scriptstyle g}\bigg\downarrow & & \llap{\scriptstyle D(r, g)}\bigg\downarrow & & \bigg\downarrow\rlap{\scriptstyle \ K(g)} \\ d & \qquad \qquad & D(r, d) & \stackrel{\alpha_{d}}{\longrightarrow} & K(d)
\end{array}
$$

또한 $id_r \in ob\ D(r, r)$이므로 다음의 두 식이 같아야 한다.

$$
(\alpha_r ; K(g))(id_r) = K(g)(\alpha_r(id_r))
$$
$$
(D(r, g);\alpha_{d})(id_r) = \alpha_{d}(g)
$$

이들을 연립하면 원하는 결과를 얻는다.

이후의 증명의 개요는 이렇다. $\alpha_{d}(f') = K(f')(\alpha_r(id_r))$는 $\alpha$의 구체적인 값이 오직 $\alpha_r(id_r)$에 의해서 정의된다는 뜻이다. 따라서 임의의 $\alpha$와 $\alpha_r(id_r)$간에 일대일 대응 $\gamma(\alpha)=\alpha_r(id_r)$가 존재할 것이라고 추측할 수 있다. 이를 구체적으로 보이기 위해 $\gamma$의 injectivity와 surjectivity를 보이자.

*(Injectivity)* 
만약 $\alpha \neq \beta$이면 $\gamma(\alpha) \neq \gamma(\beta)$임을, 동등하게 $\gamma(\alpha)=\gamma(\beta)$이면 $\alpha=\beta$임을 보여야 한다. 이를 위해 $\gamma(\alpha)=\gamma(\beta)$라고 가정하자. 그러면 정의에 의해 다음이 성립한다.

$$
\gamma(\alpha) = \alpha_r(id_r) = \beta_r(id_r) = \gamma(\beta)
$$

따라서 앞서서 살펴본 바에 의해 임의의 $d \in ob\ D, f' \in r \Rightarrow_D d$에 대해 다음이 성립한다.

$$
\alpha_d(f')=K(f')(\alpha_r(id_r)) = K(f')(\beta_r(id_r))=\beta_d(f')
$$

따라서 임의의 $d, f'$에 대해 $\alpha_d(f') = \beta_d(f')$이므로 $\alpha = \beta$이다.

*(Surjectivity)*
모든 $w \in K(r)$에 대해 $w = \gamma(\alpha)$가 되도록 하는 $\alpha$가 존재함을 보여야 한다. 이때 $\alpha$를 임의의 $d \in ob\ D, f' \in r \Rightarrow_D d$에 대해 다음을 만족하도록 정의한다고 해 보자.

$$
\alpha_r(id_r) = w \quad and \quad \alpha_d(f') = K(f')(w)
$$

이제 이러한 $\alpha$가 naturality를 만족한다면 surjectivity를 보이기에 충분하다. 이때의 naturality condition은 $d, d' \in ob\ D, g \in d \Rightarrow_D d'$에 대해 아래와 같이 주어진다.

$$
D(r, g) ; \alpha_{d'} = \alpha_d ; K(g)
$$

이제 임의의 $f' \in r \Rightarrow d$에 대해 다음 두 식을 얻을 수 있다.

$$
(D(r, g) ; \alpha_{d'})(f') = \alpha_{d'}(f';g) = K(f';g)(w)
$$
$$
(\alpha_d ; K(g))(f')=K(g)(\alpha_d(f')) =K(g)(K(f')(w)) = (K(f');K(g))(w)=K(f';g)(w)
$$

이 둘이 같음으로 $\alpha$는 natural 하다. 

이들 결과를 조합하면 $\gamma$는 bijective함을 알 수 있다. $\boxed{}$

## Yoneda Lemma and Universal Arrow

![[YonedaLemma.png]]

위 그림과 같은 상황을 고려해 보자. 이때 $* = \{ \bullet \}$와 같이 원소를 하나 가지는 임의의 집합이라고 하자. 그러면 $*$에서 어떤 집합으로 가는 함수는, 그 집합의 원소 하나를 선택하는 것으로 정의된다. 즉 임의의 $d \in ob\ D$에 대해서 다음이 성립한다. 

$$
(* \Rightarrow K(d)) \cong K(d)
$$

이와 같은 bijection을 $s_d \in K(d) \Rightarrow (* \Rightarrow K(d))$로 정의하자. 이제 앞선 증명에서 다음의 식이 성립했다.

$$
\alpha_{d}(f') = K(f')(\alpha_r(id_r))
$$

그러면 이 식은 동등하게 아래와 같이 적을 수 있다.

$$
s_d(\alpha_d(f')) = s_r(\alpha_r(id_r)) ; K(f')
$$

이는 universal arrow의 식과 거의 유사하다. 실제로 만약 $\alpha$가 natural isomorphsim이라면 $(r, s_r(\alpha_r(id_r))$은 $*$에서 $K$로 가는 universal arrow이다. 따라서 Yoneda lemma는 완화된 조건에서의 universal arrow를 설명하는 것으로 볼 수 있다.

## Yoneda Functor

Yoneda lemma에서 $K = D(d, -)$라 두면 다음의 bijection $\gamma$가 존재한다.

$$
\gamma \in (D(r, -) \Rightarrow_{\text{Set}^D} D(d, -)) \Rightarrow D(d, r)
$$

이로부터 Functor $Y \in D^{op} \Rightarrow \text{Set}^D$를 생각하자. 이때 $r \in ob\ D, h \in d \Rightarrow_D r$에 대해 다음과 같이 정의하자.

$$
Y(r) = D(r, -) \qquad Y(h^{op}) = \gamma^{-1}(h)
$$

이때 $\gamma$가 bijection이므로 $Y$는 full and faithful functor이다. 이러한 $Y$를 Yoneda functor 혹은 Yoneda embedding 이라고 한다. 

## Footnote
- Small set에 관한 자세한 논의는 참고문헌 (1)의 21-30pp를 볼 것.

## References
(1) Mac Lane, Categories for the Working Mathematicians