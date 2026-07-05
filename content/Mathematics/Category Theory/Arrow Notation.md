# Arrow

Arrow(화살표)는 domain(정의역), codomain(공역), name(이름)으로 정의되는 대상이다. 어느 arrow의 domain이 $x$, codomain이 $y$, name이 $f$일때 이를 다음과 같이 표기한다.

$$
x \xrightarrow{f} y
$$
편의상 다음의 표기법을 함께 사용한다.

- $dom\ f = x$
- $codom\ f = y$

필요한 경우 arrow의 name은 생략하고 표기할 수 있다. 

## Arrow under Collection

Arrow의 collection $G$를 가정하자. 이제 다음과 같이 정의한다.

- $x \Rightarrow_G y = \{ f | x \xrightarrow{f} y \in G \}$
- $(x \Rightarrow_G) = \{ f | \exists y, x \xrightarrow{f} y \in G\}$
- $(\Rightarrow_G y) = \{ f | \exists x, x \xrightarrow{f} y \in G\}$
- $arr\ G = \{ f | \exists x, \exists y, x \xrightarrow{f} y \in G\}$

이제 $X, Y$가 각각 domain과 codomain의 collection 이라고 하자. 그러면 다음과 같이 정의한다.

- $x \Rightarrow_G Y = \{ f | y \in Y, x \xrightarrow{f} y \in G\}$
- $X \Rightarrow_G y = \{ f | x \in X, x \xrightarrow{f} y \in G\}$
- $(\Rightarrow_G Y) = \{ f | \exists x, y \in Y, x \xrightarrow{f} y \in G\}$
- $(X \Rightarrow_G) = \{ f | \exists y, x \in X, x \xrightarrow{f} y \in G\}$
- $X \Rightarrow_G Y = \{ f | x \in X, y \in Y, x \xrightarrow{f} y \in G\}$

## Arrow Bundle

만약 collection $F$에 대해 $F \subseteq x \Rightarrow_G y$ 라면 다음과 같이 적는다.

$$
x \xRightarrow{F}_G y
$$

이러한 $F$를 arrow bundle이라고 한다.

## Footnote
- Category theory의 formulation은 first-order logic을 사용한다. 
- Category theory에서 collection은 가능한 모든 set의 collection과 같이 일상적인 집합론에서 벗어나는 대상을 포함한다. 따라서 이곳에서 사용되는 포함기호 $\in$은 집합론을 가정하지는 않는다.

## References
(1) Brendan Fong, David I. Spivak, Seven Sketches in Compositionality  
(2) Mac Lane, Categories for the Working Mathematicians

