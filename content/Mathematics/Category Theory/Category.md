**Prerequisites:** [[Notation for Arrow and Logic]]

> A mathematician is a machine for turning coffee into theorems.

## Graph

Graph $G$는 arrow의 collection이다. 이때 다음과 같은 표기법을 사용한다.

*(Arrows, Morphisms)*
$$
arr\ G = hom\ G
$$
*(Objects)*
$$
ob\ G = \{ z | \exists f \in G, dom\ f = z \lor codom\ f = z\}
$$

## Category

Category $C$는 composition($;$)과 identity($id$)가 정의된 graph이다.

- *(Composition)* $; \in \{ (f, g) | f, g \in hom\ C, codom\ f = dom\ g \} \Rightarrow hom\ C$
- *(Identity)* $id \in ob\ C \Rightarrow hom\ C$

이때 이들은 다음을 만족해야 한다.

*(Compositionality)*
$$
f \in x \Rightarrow_C y, g \in y \Rightarrow_C z \to f ; g \in x \Rightarrow_C z
$$
*(Associativity)*
$$
(f ; g) ; h = f;(g;h)
$$
*(Unitarity)*
$$
f \in x \Rightarrow_C y \to id_x ; f = f ; id_y = f
$$

## Category의 예시

| Name          | Objects      | Morphisms             | Sidenote                    |
| ------------- | ------------ | --------------------- | --------------------------- |
| $\text{Set}$  | set          | function              | small sets만 포함              |
| $\text{Vect}$ | vector space | linear transformation |                             |
| $\text{Cat}$  | category     | functor               | 모든 small category의 category |

## Opposite Category

> A comathematician is a device for turning cotheorems into ffee.

어느 category $C$에 대한 opposite category $C^{op}$는 화살표의 방향을 반대로 바꾼 것이다.

- *(Objects)* $ob\ C^{op} = ob\ C$
- *(Morphisms)* $f \in x \Rightarrow_C y$가 존재하면 $f^{op} \in y \Rightarrow_{C^{op}} x$가 존재한다.
- *(Composition)* $C$에서 $f ; g = h$ 이면 $C^{op}$ 에서 $g^{op} ; f^{op} = h^{op}$ 이다.
- *(Identity)* $id_x \in C$ 이면 $id_x \in C^{op}$ 이다. 즉 identity는 서로 같다.

## Free Category

어떤 그래프 $G$로부터 category를 정의할 수 있다. (Vector의 집합 $B$에서 vector space $span\ B$ 를 정의하는 것과 유사하다.) 구체적으로 $Free(G)$ 는 다음과 같이 정의된다.

- *(Objects)* $Free(G)$의 objects는 그래프 $G$의 objects와 같다.
- *(Morphisms)* $Free(G)$의 morphism은 그래프 $G$에서의 path 로 정의되며, path의 시작점을 domain, 종점을 codomain으로 한다.
- *(Composition)* $Free(G)$의 composition은 두 path를 서로 잇는 것으로 정의한다.
- *(Identity)* $Free(G)$의 identity는 arrow 없이 object 하나로 정의되는 path로 정의한다.

예를 들어 그래프 $G$가 다음과 같다고 해 보자.

$$
G = \boxed{1 \to 2 \to 3}
$$

이 그래프 상에 존재하는 path를 다음과 같이 $Free(G)$에 대응시킬 수 있다.

| Path            | Morphisms in $Free(G)$                |
| --------------- | ------------------------------------- |
| $1$             | $id_1 \in 1 \Rightarrow_{Free(G)} 1$  |
| $2$             | $id_2 \in 2 \Rightarrow_{Free(G)} 2$  |
| $3$             | $id_3 \in 3 \Rightarrow_{Free(G)} 3$  |
| $1 \to 2$       | $f \in 1 \Rightarrow_{Free(G)} 2$     |
| $2 \to 3$       | $g \in 2 \Rightarrow_{Free(G)} 3$     |
| $1 \to 2 \to 3$ | $f ; g \in 1 \Rightarrow_{Free(G)} 3$ |

이것이 category의 조건을 만족한다는 것을 보이는 것은 어렵지 않다. 일반적으로 이를 다음과 같이 표기한다.

$$
Free(\boxed{1 \to 2 \to 3})
$$

## Footnote
- $hom$ 이라는 표기법은 category theory가 탄생한 대수학에서 온 것으로 본래 구조를 보존하는 mapping을 의미한다. 이곳에서는 임의의 mapping을 지칭하는 용어로 쓰인다.
- 일반적으로 $f \in x \Rightarrow_C y$ 는 $f \in C(x, y),\ f \in hom_C (x, y),\ f : x \to y$ 등으로 표기하며, hom-set 이라고 부른다.

## References
(1) Brendan Fong, David I. Spivak, Seven Sketches in Compositionality  
(2) Mac Lane, Categories for the Working Mathematicians
(3) Path (graph theory), Wikipedia (https://en.wikipedia.org/wiki/Path_(graph_theory))