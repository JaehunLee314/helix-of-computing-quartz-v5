**Prerequisites:** [[Category]], [[Functor]]

## Adjoints의 정의

어느 두 category $C, D$와 functor $L \in C \Rightarrow D$, $R \in D \Rightarrow C$ 에 대해 다음 두 조건이 성립할 때 $L$이 $R$의 left adjoint 혹은 $R$이 $L$의 right adjoint 라고 하고 $L \dashv R$ 이라고 적는다.

*(Isomorphism)*
$$
c \in ob\ C, d \in ob\ D \to (c \Rightarrow_C R(d)) \cong (L(c) \Rightarrow_D d)
$$
*(Naturality)*  
$c \in ob\ C, d \in ob\ D$에 대해 $(c \Rightarrow_C R(d)) \rightarrow (L(c) \Rightarrow_D d)$ 인 isomorphism $\alpha_{c, d}$를 가정하자. 이때 왼쪽 그림과 같은 $f, g, h$에 대해 오른쪽의 식이 성립한다.

$$
\begin{array}{ccc} \mathcal{C} & \qquad & \mathcal{D} \\ c' & \xrightarrow{\in L} & L(c') \\ \ \bigg\downarrow \scriptstyle{f} & & \quad \bigg\downarrow \scriptstyle{L(f)} \\ c & \xrightarrow{\in L} & L(c) \\ \ \bigg\downarrow \scriptstyle{h} & & \qquad \bigg\downarrow \scriptstyle{\alpha_{c, d}(h)} \\ R(d) & \xleftarrow{\in R} & d \\ \quad \bigg\downarrow \scriptstyle{R(g)} & & \ \bigg\downarrow \scriptstyle{g} \\ R(d') & \xleftarrow{\in R} & d' \end{array}
\qquad \qquad \alpha_{c', d'}(f;h;R(g)) = L(f);\alpha_{c, d}(h);g
$$

## Adjoints의 다른 정의

다음과 같은 hom-functor $C(-, R(-)), D(L(-), -) \in C^{op} \times D \Rightarrow \text{Set}$를 생각하자. 그러면 $L \dashv R$인 것과 $C(-, R(-))$에서 $D(L(-), -)$로 가는 natural isomorphism $\alpha$가 존재하는 것은 동치이다. 이때 naturality condition은 다음 commutative diagram으로 주어진다.

$$
\begin{array}{ccc} 
C(c, R(d)) & \stackrel{\alpha_{c, d}}{\longrightarrow} & D(L(c), d) \\
\llap{\scriptstyle C(f, R(g))}\bigg\downarrow & & \bigg\downarrow\rlap{\scriptstyle \ D(L(f), g)} \\ 
C(c', R(d')) & \stackrel{\alpha_{c', d'}}{\longrightarrow} & D(L(c'), d')
\end{array}
$$

## Example: Currying

### Motivation

Currying은 다음과 같은 직관에서 출발한다. 어떤 이변수함수 $f(x, y) = 2x^2+ y^2$을 생각해 보자. 이때 다음과 같이 결과값이 함수인 함수를 정의할 수 있다.

$$
p(x) = (t \mapsto 2x^2 + t^2)
$$

(즉, $p(x) = g \ s.t. \ g(t) = 2x^2 + t^2$) 그렇다면 이변수함수는 다음과 같이 함수의 연속된 적용으로 적을 수 있다.

$$
f(x, y) = p(x)(y)=2x^2+y^2
$$

이와 같이 다변수함수를 함수의 연속된 적용으로 적는 것을 Currying이라고 하고, 그 반대를 Uncurrying 이라고 한다. 이제 Currying과 adjoints의 관계성을 살펴보자.

### Isomorphism

일반적으로 집합 $A, B, C$에 대해 일반적으로 다음이 성립한다.

$$(A \Rightarrow_{\text{Set}} (B \Rightarrow_{\text{Set}} C)) \cong (A \times B \Rightarrow_{\text{Set}} C)$$

즉 $A \times B$를 입력으로 받아 $C$를 출력하는 함수와, $A$를 입력으로 받아 $B$에서 $C$로 가는 함수를 출력하는 함수 간에 일대일 대응이 존재한다. 구체적으로 $\Phi_{A, C}$ 를 다음과 같이 정의하자.

$$
f \in A \Rightarrow_{\text{Set}} (B \Rightarrow_{\text{Set}} C) \to \Phi_{A, C}(f) = ((t, t') \mapsto f(t)(t'))
$$

또한 그 inverse $\Phi_{A, C}^{-1}$를 다음과 같이 정의하자.

$$
g \in A \times B \Rightarrow_{\text{Set}} C \to \Phi_{A, C}^{-1}(g) = (t \mapsto t' \mapsto g(t, t'))
$$

그러면 둘의 합성은 다음과 같이 된다.

$$
\Phi_{A, C}^{-1}(\Phi_{A, C}(f))(a)(b) = \Phi_{A, C}(f)(a, b) = f(a)(b) \quad \therefore \Phi_{A, C}^{-1}(\Phi_{A, C}(f)) = f
$$
$$
\Phi_{A, C}(\Phi_{A, C}^{-1}(g))(a, b) = \Phi_{A, C}^{-1}(g)(a)(b) = g(a, b) \quad \therefore \Phi_{A, C}(\Phi_{A, C}^{-1}(g)) = g
$$


따라서 이 둘은 실제로 inverse 이므로 앞선 두 집합은 isomorphic 하다.

### Naturality

이제 $L_B, R_B \in \text{Set} \Rightarrow_{\text{Cat}} \text{Set}$을 집합 $X$와 함수 $f \in X' \Rightarrow_{\text{Set}} X$ 에 대해서 다음과 같이 정의하자.

*(Object-wise)*
$$
L_B(X) = X \times B \qquad R_B(X) = (B \Rightarrow_{\text{Set}} X)
$$
*(Morphism-wise)*
$$
L_B(f) \in X' \times B \Rightarrow_{\text{Set}} X \times B \quad s.t. \quad L_B(f)(x, b) = (f(x), b)
$$
$$
R_B(f) \in (B \Rightarrow_{\text{Set}} X') \Rightarrow_{\text{Set}} (B \Rightarrow_{\text{Set}} X) \quad s.t. \quad R_B(f)(u) = u ; f
$$

이하에서 아래첨자 $B$는 생략한다. 이제 아래 그림을 생각해 보자.

$$
\begin{array}{ccc} \text{Set} & \qquad & \text{Set} \\ A' & \xrightarrow{\in L} & A' \times B \\ \ \bigg\downarrow \scriptstyle{f} & & \quad \bigg\downarrow \scriptstyle{L(f)} \\ A & \xrightarrow{\in L} & A  \times B \\ \ \bigg\downarrow \scriptstyle{h} & & \qquad \bigg\downarrow \scriptstyle{\Phi_{A, C}(h)} \\ B \Rightarrow_{\text{Set}} C & \xleftarrow{\in R} & C \\ \quad \bigg\downarrow \scriptstyle{R(g)} & & \ \bigg\downarrow \scriptstyle{g} \\ B \Rightarrow_{\text{Set}} C' & \xleftarrow{\in R} & C' \end{array}
$$

이때 $\Phi_{A', C'}(f;h;R(g)) = L(f);\Phi_{A, C}(h);g$ 인지 살펴보자. 

$$
\begin{aligned} \Phi_{A', C'}(f ; h ; R(g))(a', b) &= (f ; h ; R(g))(a')(b) && \text{(by definition of } \Phi \text{)} \\ &= R(g)((f ; h)(a'))(b) && \text{(evaluating the composition at } a' \text{)} \\ &= R(g)(h(f(a')))(b) && \text{(evaluating } f ; h \text{)} \\ &= (h(f(a')) ; g)(b) && \text{(by definition of } R(g) \text{ acting on a function)} \\ &= g(h(f(a'))(b)) && \text{(evaluating the composition at } b \text{)} \end{aligned}
$$

$$
\begin{aligned} (L(f) ; \Phi_{A, C}(h) ; g)(a', b) &= (\Phi_{A, C}(h) ; g)(L(f)(a', b)) && \text{(evaluating the first composition)} \\ &= (\Phi_{A, C}(h) ; g)(f(a'), b) && \text{(by definition of } L(f) \text{)} \\ &= g(\Phi_{A, C}(h)(f(a'), b)) && \text{(evaluating the second composition)} \\ &= g(h(f(a'))(b)) && \text{(by definition of } \Phi \text{)} \end{aligned}
$$

따라서 naturality 가 성립한다. 즉, $L_B \dashv R_B$ 이다. 

## References
(1) Brendan Fong, David I. Spivak, Seven Sketches in Compositionality