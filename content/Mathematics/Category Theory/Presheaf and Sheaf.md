- **Prerequisites:** [[Functor]], [[Natural Transformation]]
## Motivation for Presheaf

Preorder category $C$의 object가 $\mathbb{R}$의 부분집합들이고, morphism이 subset relation라고 해 보자. 즉 다음이 성립하다고 해 보자.

$$
U \rightarrow_C W \iff U \subseteq W
$$

이와 같은 상황에서 어느 functor $P \in C^{op} \Rightarrow \text{Set}$을 다음과 같이 정의하자.

*(Object Mapping)*
$U \in ob\ C$이면 $P(U) = \{ f | f \in U \Rightarrow_{Set} \mathbb{R} \}$로 정의한다.

*(Morphsim Mapping)*
$U \subseteq W$이면, 즉 $r \in U \Rightarrow_C W$이면 $P(r^{op}) \in P(W) \Rightarrow_{\text{Set}} P(U)$는 다음과 같이 정의한다.

$$
P(r^{op})(f) = g \quad s.t.\quad g \in U \Rightarrow_{\text{Set}} \mathbb{R}, u \in U \to g(u) = f(u)
$$

일반적으로 이러한 mapping을 domain restriction이라고 하고 다음과 같이 적는다.

$$
P(r^{op})(f) = f|_{U}
$$

여기서 $P$는 다음의 두 가지 기능을 갖추고 있다.

### Instantiation of $C$ with $P$

$P$는 category $C$의 대상들을 구조를 보존한 채로 $\text{Set}$에서 표현 가능한 임의의 대상들로 옮긴다. 이는 $C$가 정한 구조를 만족하는 구체적인 자료를 만들어내는 과정이다. 

### Perspective Shifting of $P(C)$

$C$에서 어느 대상 $U$가 $W$보다 '작을'때, $P(C)$에서는 $P(W)$에서 $P(U)$로 가는 mapping이 존재한다. 이는 더 '큰' 관점인 $P(W)$로부터 더 '작은' 관점이 $P(U)$를 유도하는 것이다. 이처럼 $P$는 범위가 다른 관점 간의 변환을 제공하는 것으로 이해할 수 있다.

이러한 예시로부터 presheaf를 정의한다.

## Presheaf

Small category $C$위에 정의되는 presheaf $P$는 $P \in C^{op} \Rightarrow \text{Set}$과 같은 functor이다. 이때 다음과 같은 용어를 함께 사용한다.

- 어느 $c \in ob\ C$에 어느 대해 원소 $s \in P(c)$를 section of $P$ over $c$라고 한다. 또한 $P(c)$는 set of sections of $P$ over $c$라고 한다.
- 어느 $f \in c' \Rightarrow_C c$에 대해 $P(f^{op}) \in P(c) \Rightarrow P(c')$을 restriction map이라고 한다. 또한 $s \in P(c)$에 대해 $P(f^{op})(s) \in P(c')$를 $s$의 restriction along $f$라고 하고 $s |_f = P(f^{op})(s)$ 로 적는다.

한편 presheaf 간의 morphism은 natural transformation이다.

## Sheaf on Topological Spaces

앞서서 presheaf가 '큰' 관점에서 '작은' 관점으로의 restriction을 제공한다는 사실을 살펴보았다. 그러면 반대로 '작은' 관점을 조합하면 '큰' 관점을 만들 수 있지 않을까? Sheaf는 이와 같은 기능을 제공한다. 즉, sheaf는 presheaf인 동시에 '작은' 관점의 조합이 '큰' 관점이 되도록 한다. 이러한 조건을 sheaf condition이라고 부른다.

Presheaf는 어떤 small category $C$에 대해 정의되지만 sheaf에 위와 같은 성질을 부여하기 위해서는 $C$에 추가적인 성질이 부여되어야 한다. 이러한 성질을 만족하는 대표적인 대상이 topological space이다. 따라서 이곳에서는 topological space위에 정의되는 sheaf를 살펴보자. 

Topological space는 점들의 집합 $X$와 open set들의 집합 $Op\ X$로 구성된다. 이때 $Op\ X$는 subset relation을 통해 정의되는 preorder category이다. 이제 presheaf $P \in Op\ X \Rightarrow \text{Set}$를 생각해 보자. 'Motivation of Presheaf' 부분에서 살펴본 것과 유사하게 만약 $V, U \in Op\ X$이고 $V \subseteq U$라면 어느 $r \in V \Rightarrow_{Op\ X} U$과 $s \in P(U)$에 대해 다음과 같이 restriction map을 표기할 수 있다.

$$
P(r^{op})(s) = s|_r = s|_{V}
$$

이제 sheaf condition은 다음과 같이 정의된다.

*(Sheaf Condition)*
어느 cover $U = \bigcup_{i \in I} U_i$에 대하여 matching family $\{s_i \in P(U_i)\}_{i \in I}$는 다음을 만족하는 indexed set이며,

$$
i, j \in I \to \left . s_i \right |_{U_i \cap U_j} = \left . s_j \right |_{U_i \cap U_j}
$$

만약 $s \in P(U)$가 존재하여 $i \in I \to s |_{U_i} = s_i$ 라면 이러한 $s$를 gluing (i.e. gluing section) 이라고 한다. 
이제 어느 cover $U = \bigcup_{i} U_i$에서 정의되는 matching family에 대해 항상 유일하게 대응되는 gluing이 존재하면 $P$가 cover $U = \bigcup_{i} U_i$에 대해 sheaf condition을 만족한다고 한다. 만약 $P$가 존재하는 모든 cover에 대해 sheaf condition을 만족하면 P를 sheaf라고 한다.

## Meaning of a Sheaf

우리는 $s \in P(U)$에 대해 정의되는 restriction map $s|_V \in P(V)$를 $s$라는 대상을 더 '작은' 관점 $V$를 통해 관찰하는 것이라고 이해할 수 있다. 이제 어느 큰 관점 $U$를 그것을 이루는 작은 관점들로 분할한다고 해 보자. 그러면 이러한 작은 관점들은 $U$에 대한 cover를 구성한다.

이때 아래의 식,

$$
i, j \in I \to \left . s_i \right |_{U_i \cap U_j} = \left . s_j \right |_{U_i \cap U_j}
$$

두 관점의 교차점 $U_i \cap U_j$에서 대상 $s_i \in P(U_i)$와 $s_j \in P(U_j)$를 관찰한 것이 서로 같다는 것을 의미한다. 이것이 모든 $i, j$에 대해 성립함으로 matching family는 서로 인접한 관점들에서 바라볼 때 같은 것들을 모아둔 것이다. 이때 sheaf condition은 전역적인 관점 $U$에서 이러한 matching family와 모두 대응하는 하나의 대상 $s$가 유일하게 존재함을 보장한다. 따라서 우리는 sheaf condition을 다음과 같이 이해할 수 있다.

*(Sheaf Condition: Meaning)*
인접한 관점들에서 바라볼 때 같은 것들을 모아 두면 하나의 전역적인 대상과 대응된다. 나와 내 주변 사람들이 관찰한 결과가 같다면, 아주 먼 곳에서 바라보더라도 그 결과가 달라지지 않는다.

따라서 우리는 sheaf에서 지역적인 특성을 탐색하는 것 만으로도 전역적인 특성을 알 수 있도록 보장받는다.

## Footnote
- Preorder category는 두 object간의 morphism이 최대 1개 존재하는 category를 말한다. 
- Instantiation은 컴퓨터공학에서 추상적 자료형인 class를 실제 자료를 담고 있는 메모리 위의 대상인 instance로 바꾸는 과정을 말한다. 비슷한 단어로는 application(특히, lambda calculus에서) 이나 realization을 생각해볼 수 있다.
- Small category $C$가 sheaf를 정의하기 위한 추가적인 성질들을 만족할 때 $C$를 site라고 한다. 참고문헌 (1)이 이것에 대해 다루지 않음으로 이 글에서도 다루지 않았다.
- Topological space에 대한 구체적인 정의는 참고문헌 (1)의 234p 혹은 적당한 위상수학 교재를 볼 것.
- Small category $C$는 $ob\ C$와 $hom\ C$가 모두 small set인 category이다.

## References
(1) Brendan Fong, David I. Spivak, Seven Sketches in Compositionality