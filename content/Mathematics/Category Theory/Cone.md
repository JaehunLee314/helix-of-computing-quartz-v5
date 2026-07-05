**Prerequisites:** [[Category]], [[Functor]]
## Single Cone

Diagram $D \in J \Rightarrow C$가 있을 때 어떤 $c \in ob\ C$와 $a \in ob\ J \Rightarrow hom\ C$에 대해 다음 조건이 성립한다면 $(c, a)$를 $D$ 위의 cone 이라고 한다.

- $j \in ob\ J \to a_j \in c \Rightarrow_C D(j)$
$$
\begin{array}{ccccccc} & & & c & & & \\ & ^{a_1}\swarrow & & \downarrow \scriptstyle{a_j} & & \searrow^{a_n} & \\ D(1) & & \dots & D(j) & \dots & & D(n) \end{array}
$$

- $f \in j \Rightarrow_J k \to a_k = a_j ; D(f)$ 
$$
\begin{array}{ccccc} J & \qquad \qquad \qquad & & C & \\ & & & c & \\ & & ^{a_i} \swarrow & & \searrow^{a_j} \\ i \xrightarrow{f} j & & D(i) & \xrightarrow{D(f)} & D(j) \end{array}
$$

## Cone Category

어느 diagram $D \in J \Rightarrow C$에 대해 cone category $Cone\ D$는 다음과 같이 정의된다.

### Objects of $Cone\ D$

$ob\ Cone\ D$는 $D$ 위의 가능한 모든 cone이다.
### Morphisms of $Cone\ D$

$hom\ Cone\ D$는 $hom\ C$에서 유도되는 collection이다. 구체적으로 $h \in (c, a) \Rightarrow_{Cone\ D} (c', a')$은 다음과 동치이다.

- $\exists f \in c \Rightarrow_{C} c', (j \in ob\ J \to a_j = f;a_j')$
$$
\begin{array}{ccc} c & \xrightarrow{f} & c' \\ _{a_j} \searrow & & \swarrow _{a'_j} \\ & D(j) & \end{array}
$$

즉 두 cone $(c, a), (c', a')$간의 morphism이 $Cone\ D$에 존재할 조건은 $a_j = f;a_j'$ 이 성립하는 $f \in c \Rightarrow_C c'$ 가 존재하는 것이다.

## References
(1) Brendan Fong, David I. Spivak, Seven Sketches in Compositionality