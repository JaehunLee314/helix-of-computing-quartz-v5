**Prerequisites:** [[Category]], [[Adjoints]]

이 글은 참고문헌 (1)의 내용에 대한 리뷰이다. 자세한 내용은 해당 논문을 참고할 것.

## Intuitions about the Theorem

Lawvere's fixed point theorem은 Cartesian closed category를 전제하는 정리이다. 우리는 그 내용을 파악하기 위해 Cartesian closed category의 한 종류인 $\text{Set}$ category에 대해서 먼저 생각해 볼 것이다.

**Definition. Fixed Point (Set)**
어느 함수 $f \in X \Rightarrow X$에 대해 어느 $x \in X$는 $f(x) = x$가 되도록 하면 $x$를 $f$의 fixed point라고 한다.

**Definition. Fixed Point Property (Set)**
어느 집합 $Y$가 fixed point property를 가진다는 것은 가능한 모든 함수 $t \in Y \Rightarrow Y$가 fixed point를 가진다는 것이다. 

이제 $\text{Set}$ 위에서 Lawvere's fixed point theorem은 아래와 같다.

**Theorem. Lawvere's Fixed Point Theorem (Set)**
어느 집합 $A, Y$에 대해 surjection $g \in A \Rightarrow_{\text{Set}} (A \Rightarrow_{\text{Set}} Y)$가 존재하면 $Y$는 fixed point property를 갖는다. 즉, 모든 $t \in Y \Rightarrow_{\text{Set}} Y$는 fixed point를 갖는다.

*Proof.*
$\bar{g} \in A \times A \Rightarrow Y$를 다음과 같이 정의하자.

$$
a, x \in A \to\bar{g}(a, x) = g(x)(a)
$$

그러면 임의의 $f \in A \Rightarrow Y$에 대해서 어떤 $x \in A$가 존재하여 모든 $a \in A$에 대해 $\bar{g}(a, x) = f(a)$가 성립한다. 이제 임의의 $t \in Y \Rightarrow Y$를 가정하고 함수 $f \in A \Rightarrow Y$를 다음과 같이 정의하자.

$$
a \in A \to f(a) = (\delta;\bar{g};t)(a) = (\bar{g};t)(a, a) \quad (where\ a \in A \to \delta(a ) = (a, a))
$$

이와 같이 정의된 $f$는 $A$에서 $Y$로 가는 함수이므로 $g$의 surjectivity에 의해 $g(x^*) = f$가 되도록 하는 $x^* \in A$가 존재한다. 이것과 $\bar{g}$의 정의를 종합하면 다음 식을 얻는다.

$$
a \in A \to \bar{g}(a, x^*) = g(x^*)(a) = f(a) = (\bar{g};t)(a, a)
$$

그런데 $a = x^*$라고 두면 다음과 같이 된다.

$$
\bar{g}(x^*, x^*) = (\bar{g};t)(x^*, x^*) = t(\bar{g}(x^*, x^*))
$$

따라서 $t$의 fixed point는 $\bar{g}(x^*, x^*)$이다. $\boxed{}$

이 정리는 다음의 따름정리를 가진다.

**Corollary.** 집합 $Y$가 fixed point property를 가지지 않으면 surjective 한 $g \in A \Rightarrow Y^A$는 존재하지 않는다.

이 따름정리는 러셀의 역설, 칸토어의 대각선 논법 등을 포함하는 중요한 수학적 역설들의 일반화이다. 예를 들어 다음과 같다.

**Theorem. Cantor's Theorem**
어느 집합 $A$에서 그 power set $P(A)$로 가는 surjection은 존재하지 않는다. 

*Proof.* Power set $P(A)$와 exponential set $\{0, 1\}^A$간에 bijection이 존재하므로 $A$에서 $\{0, 1\}^A$로 가는 surjection이 존재하지 않음을 보이면 충분하다. 그런데 $not: \{0, 1\} \Rightarrow \{0, 1\}$을 $not(0) = 1, not(1) = 0$이 되도록 정의하면 $not$은 fixed point를 가지지 않는다. 따라서 $\{0, 1\}$이 fixed point property를 가지지 않음으로 앞서 살펴본 corollary에 의해 $A$에서 $\{0, 1\}^A$로 가는 surjection은 존재하지 않는다.

## Cartesian Closed Category

이제 Cartesian closed category의 정의를 살펴보자.

**Definition. Cartesian Closed Category (CCC)**
Cartesian closed category는 어느 category $C$와 functor $\mathbb{1}, \times, ()^{()}$로 정의된다. 이때 각 functor는 다음과 같은 right adjoints이다.

$$
\mathbf{!} \in C \Rightarrow \mathbf{1} \dashv  \mathbb{1} \in \mathbf{1} \Rightarrow C
$$
$$
\Delta \in C \Rightarrow C \times C \dashv \mathbb{\times} \in C \times C \Rightarrow C
$$
$$
A \in ob\ C \to A \times () \in C \Rightarrow C \dashv ()^A \in C\Rightarrow C
$$

여기서 category $\mathbf{1}$은 원소 하나를 가지는 category이고, $\Delta$는 diagonal functor 이다.

**Definition. Unit Object in CCC**
CCC $C$에서 unit object $1 \in ob\ C$는 $* \in ob\ \mathbb{1}$일 때 $1 = \mathbf{1}(*)$와 같이 정의한다.

## Lambda Transform

CCC $C$에 대해 다음이 성립한다.

$$
A \in ob\ C \to A \times () \in C \Rightarrow C \dashv ()^A \in C\Rightarrow C
$$

이때 adjoints의 정의를 고려하면 다음과 같은 bijection $\alpha_{X, Y}^A$가 존재한다.

$$
\alpha_{X, Y}^A \in (A \times X \Rightarrow Y) \Rightarrow (X \Rightarrow Y^A)
$$

그러면 다음과 같은 unit $\lambda^A_{X}$와 counit $\epsilon_X^A$를 정의할 수 있다.

$$
\lambda^A_{X} = \alpha_{X, A \times X}^A(id_{A \times X}) \in X \Rightarrow (A \times X)^A 
$$
$$
\epsilon_Y^A = (\alpha_{Y^A, Y}^A)^{-1}(id_{Y^A}) \in A \times Y^A \Rightarrow Y
$$

이제 다음과 같이 정의한다.

**Definition. $\lambda$-Transform**
어느 morphism $f \in A \times X \Rightarrow Y$의 $\lambda$-transform은 다음과 같은 morphism $h$로 정의한다.

$$
h = \lambda_X^A ; f^A \in X \Rightarrow Y^A
$$

이때 $f^A$는 $(A \times X)^A$에서 $Y^A$로 가는 함수이다. 

**Lemma.** 어느 $f \in A \times X \Rightarrow Y$의 $\lambda$-transform이 $h$인 것과 다음 diagram이 commute하는 것은 동치이다.

$$
\begin{array}{ccc} 
A \times X & & \\ 
\llap{\scriptstyle{A ×h}}\bigg\downarrow & \stackrel{f}{\searrow} & \\ 
A \times Y^A & \stackrel{\epsilon_Y^A}{\longrightarrow} & Y
\end{array}
$$

*proof.* 생략

## Point Surjectivity and Weakly Point Surjectivity

**Definition. Point Surjectivity**
CCC $C$의 어느 morphism $g \in X \Rightarrow Z$가 point surjective하다는 것은 모든 $z \in 1 \Rightarrow Z$에 대해 $x ; g = z$가 되도록 하는 $x \in 1 \Rightarrow X$가 존재한다는 것이다.

**Definition. Weakly Point Surjectivity**
CCC $C$의 어느 morphism $g \in X \Rightarrow Y^A$가 weakly point surjective하다는 것은 모든 $f \in A \Rightarrow Y$에 대하여 어떤 $x \in 1 \Rightarrow X$가 존재하여 모든 $a \in 1 \Rightarrow A$에 대해 $(a, x;g) ; \epsilon^A_Y = a;f$가 성립한다는 것이다. 이때 epsilon은 앞서서 정의한 counit이다.

Weakly point surjection은 아래 diagram으로도 정의할 수 있다. 이때 $\text{fst}$는 product의 first projection이다.

$$
\begin{array}{ccccc} 
1 \times 1 & \stackrel{(a, x)}{\longrightarrow} & A \times X & \stackrel{\text{fst}}{\longrightarrow} & A \\ 
& & \llap{\scriptstyle A × g}\bigg\downarrow & & \bigg\downarrow\rlap{\scriptstyle \ f} \\
& & A \times Y^A & \stackrel{\epsilon^A_Y}{\longrightarrow} & Y
\end{array}
$$

## Lawvere's Fixed Point Theorem

이제 주제의 정리를 살펴보자. 먼저 fixed point property는 다음과 같이 정의된다.

**Definition. Fixed Point Property**
CCC $C$의 어느 object $Y$가 fixed point property를 가진다는 것은 모든 $t \in Y \Rightarrow Y$에 대해 $y ; t = y$가 되도록 하는 $y \in 1 \Rightarrow Y$가 항상 존재한다는 것이다.

이제 정리는 다음과 같이 주어진다.

**Theorem. Lawvere's Fixed Point Theorem**
CCC $C$의 object $A, Y$에 대해 weakly point surjective한 morphism $g \in A \Rightarrow Y^A$가 존재하면 $Y$는 fixed point property를 갖는다.

*Proof.*
$\lambda$-transform이 $g$인 morphism $\bar{g} \in A \times A \Rightarrow Y$를 생각하자. 그러면 임의의 $f \in A \Rightarrow Y$에 대하여 어떤 $x \in 1 \Rightarrow A$가 존재하여 모든 $a \in 1 \Rightarrow A$에 대해 $(a, x);\bar{g} = a ; f$가 성립한다. 즉 어떤 $x$와 모든 $a$에 대해 다음 diagram이 commute 한다.

$$
\begin{array}{ccccc} 
1 \times 1 & \stackrel{(a, x)}{\longrightarrow}& A \times A & \stackrel{\text{fst}}{\longrightarrow} & A \\ 
& & \llap{\scriptstyle A × g}\bigg\downarrow & \stackrel{\bar{g}}{\searrow} & \bigg\downarrow\rlap{\scriptstyle \ f} \\
& & A \times Y^A & \stackrel{\epsilon^A_Y}{\longrightarrow} & Y
\end{array}
$$

이제 임의의 $t \in Y \Rightarrow Y$를 가정하고 $f \in A \Rightarrow Y$를 다음과 같이 정의하자.

$$
f = \delta ; \bar{g};t \quad (\text{where}\ \delta\ \text{is a diagonal morphism})
$$

그러면 $f$가 $A$에서 $Y$로 가는 morphism 이므로 $g$의 weak point surjectivity에 의해 다음이 성립하도록 하는 $x^* \in 1 \Rightarrow A$가 존재한다.

$$
(a, x^*);\bar{g} = (a, a);\bar{g} ; t
$$

이때 $a = x^*$라고 두면 $(x^*, x^*) ; \bar{g}$는 $t$의 fixed point이다. $\boxed{}$

물론 다음과 같은 따름정리 역시 주어진다.

**Corollary.** Object $Y$가 fixed point property를 가지지 않으면 weakly point surjective 한 $g \in A \Rightarrow Y^A$는 존재하지 않는다.

## Footnote
- 이 정리를 사용해 잘 알려진 paradox들을 증명하는 것은 참고문헌 (1)을 볼 것.

## References
(1) F. William Lawvere, Diagonal Arguments and Cartesian Closed Categories, 1969 (original), 2006 (reprint)

