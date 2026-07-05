**Prerequisites**: [[Category]]

## Functor의 정의

어느 category $C$에서 $D$로 가는 functor $F \in C \Rightarrow D$ 는 object의 mapping $F_{ob} \in ob\ C \Rightarrow ob\ D$ 와 morphism의 mapping $F_{hom} \in hom\ C \Rightarrow hom\ D$ 로 구성된다. 이때 functor는 다음을 만족해야 한다.

- *(Preserving Identity)* $c \in ob\ C \to F_{ob}(id_c) = id_{F(c)}$
- *(Preserving Composition)* $f \in c_1 \Rightarrow_C c_2, g \in c_2 \Rightarrow c_3 \to F_{hom} (f ; g) = F_{hom} (f) ;  F_{hom} (g)$

Functor를 적을 때 아래첨자는 일반적으로 생략된다. 

## Functor Image

Functor $F \in C \Rightarrow D$에 대한 image $F(C)$는 다음과 같은 graph로 정의된다. 이때 $F(C)$가 반드시 category인 것은 아니다.

- $ob\ F(C) = \{d | c \in ob\ C, d = F(c)\}$
- $arr\ F(C) = \{g | f \in hom\ C, g = F(f)\}$

## Indexing Category and Diagram

Category $J, C$ 사이의 functor $D \in J \Rightarrow C$가 있다고 가정하자. 이때 우리는 $D$가 $C$의 subgraph $D(J)$에 index를 부여하는 것으로 생각할 수 있다.

예를 들어 다음과 같이 $J, C$가 정의되고, $D$가 다음의 표와 같이 정의된다고 하자.

$$
J = \boxed{1 \xrightarrow{f} 2 \xrightarrow{g} 3} \qquad C = \boxed{a \substack{\xrightarrow{p} \\[-1em] \xleftarrow[q]{}} b \xrightarrow{r} c \xrightarrow{z} d }
$$
$$
\begin{array}{|c|c|}
	\hline
	X & D(X) \\
	\hline
	1 & a \\
	2 & b \\
	3 & c \\
	f & p \\
	g & r \\
	\hline
\end{array}
$$

이는 다음과 같이 라벨링되어 있는 $C$를 정의한 것과 다르지 않다. 라벨은 아래첨자로 표기했다.

$$
C_{labeled} = \boxed{a_{[1]} \substack{\xrightarrow{p_{[f]}} \\[-1em] \xleftarrow[q]{}} b_{[2]} \xrightarrow{r_{[g]}} c_{[3]} \xrightarrow{z} d }
$$

이처럼 $D$는 $J$의 구조를 갖춘 $C$의 부분 $D(C)$를 선택하여 index를 부여한다. 따라서 $J$를 indexing category 라고 하고 $D$를 diagram이라고 한다. 

## Functor의 예시

- 어느 두 preorder category $P, Q$에 대해 임의의 functor $F$는 monotonic function이다.
- 어떤 자료형 $T$를 그 자료형의 list type $[T]$로 변환하는 functor를 생각할 수 있다. 이때 $T$에서의 함수는 $[T]$에서 element-wise application을 통해 정의된다.

## References
(1) Brendan Fong, David I. Spivak, Seven Sketches in Compositionality