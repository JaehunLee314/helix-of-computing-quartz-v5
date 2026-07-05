**Prerequisites:** [[Category]], [[Functor]], [[Isomorphism]]

Natural Transformation에 대해 살펴보자.

## Natural Transformation의 정의
두 functor $F, G \in C \Rightarrow D$간의 natural transformation $\alpha$는 각 $c \in ob\ C$를 $\alpha_c \in F(c) \Rightarrow_D G(c)$로 대응시키는 함수이다. 이때 $\alpha_c$를 $\alpha$의 $c$-component 라고 한다. 또한 $\alpha$는 다음의 diagram이 commute 하도록 해야 한다. 이와 같은 조건을 naturality condition 이라고 한다.

$$
\begin{array}{ccccc} 
C & \qquad \qquad & & D & \\ 
x & \qquad \qquad & F(x) & \stackrel{\alpha_x}{\longrightarrow} & G(x) \\ 
\llap{\scriptstyle f}\bigg\downarrow & & \llap{\scriptstyle F(f)}\bigg\downarrow & & \bigg\downarrow\rlap{\scriptstyle \ G(f)} \\ y & \qquad \qquad & F(y) & \stackrel{\alpha_y}{\longrightarrow} & G(y)
\end{array}
$$

이를 수식으로 적으면 다음과 같다.

$$
F(f) ; \alpha_y = \alpha_x ; G(f)
$$

만약 각 $\alpha_c$가 isomorphism 이라면, $\alpha$를 natural isomorphism 이라고 한다.

## Natural Transformation의 의미

두 functor $F, G \in C \Rightarrow D$간의 natural trnasformation $\alpha$는 같은 구조 $C$에서 파생되는 두 functor image $F(C), G(C)$를 서로 이어주는 $D$의 morphism들의 indexed collection 이다. 이때 naturality condition은 $\alpha$에 의해 정의되는 mapping이 $f \in hom\ C$의 의미를 보존하도록 강제한다.

예를 들어서 $x$가 "느리다", $y$가 "빠르다"라는 단어이고 $f$는 반의어 관계를 나타낸다고 해 보자. 이때 $F$가 한국어를 영어로 번역하고 $G$가 한국어를 일본어로 번역한다면 예를 들어 다음과 같은 결과가 나올 것이다.

$$
\begin{array}{ccccc}
\text{Korean (C)} & \qquad \qquad & & \text{Translation (D)} & \\ \text{느리다} & \qquad \qquad & \text{slow} & \stackrel{\alpha_{\text{느리다}}}{\longrightarrow} & \text{遅い} \\ \llap{\scriptstyle f\ \text{(반의어)}}\bigg\downarrow & & \llap{\scriptstyle F(f)}\bigg\downarrow & & \bigg\downarrow\rlap{\scriptstyle \ G(f)} \\ \text{빠르다} & \qquad \qquad & \text{fast} & \stackrel{\alpha_{\text{빠르다}}}{\longrightarrow} & \text{速い} \end{array}
$$

이제 우리는 영어를 일본어로 대응시킨 뒤 (slow $\to$ 遅い) 반의어 관계를 적용시킨 것과 (遅い $\to$ 速い), 영어에 반의어 관계를 적용한 뒤 (slow $\to$ fast) 일본어에 대응시킨 것 (fast $\to$ 速い) 이 동일한 의미를 가지는 게 자연스럽다고 생각한다. 즉 이와 같은 commutativeness가 naturality condition이다.

## Functor Category

두 category $C, D$에 대해 functor category $D^C$는 다음과 같이 정의된다.

### Objects & Morphisms

$D^C$의 object는 $C \Rightarrow D$에 속하는 functor 이며, $D^C$의 morphism은 두 functor 간의 natural transformation 이다.

### Composition & Identity

$\alpha \in F \Rightarrow_{D^C} G, \beta \in G \Rightarrow_{D^C} H$ 라고 하자. 이때 $\alpha ; \beta = \gamma$ 는 다음을 만족하도록 정의된다.

$$
c \in ob\ C \to \alpha_c;\beta_c = \gamma_c
$$

한편 $id_F \in F \Rightarrow_{D^C} F$는 다음과 같이 정의된다.

$$
c \in ob\ C \to (id_F)_c = id_{F(c)}
$$

## References
(1) Brendan Fong, David I. Spivak, Seven Sketches in Compositionality