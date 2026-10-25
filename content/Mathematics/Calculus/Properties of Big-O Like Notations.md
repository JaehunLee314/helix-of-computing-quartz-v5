**Prerequisites:** [[Big-O Like Notations]], [[Uniform Big-O Like Notations]]

이 문서의 표기는 모두 같은 $L$에서의 것이므로 첨자를 생략하여 $O, o$로 적는다.

## Little-o의 성질

**정리. Little-o의 기본 성질** 

1. $e_1, e_2 \in o(g) \to e_1 + e_2 \in o(g)$
2. $L$ 근처에서 $|b(x)| \leq M$ 이면 $e \in o(g) \to b e \in o(g)$
3. $e_1 \in o(f), e_2 \in o(g) \to e_1 e_2 \in o(fg)$
4. $L$ 근처에서 $|g(x)| \leq M|h(x)|$ 이면 $e \in o(g) \to e \in o(h)$

성질 2와 4의 조건은 각각 $b \in O(1)$, $g \in O(h)$ 이다.

_증명._ $M > 0$이라고 하자. 각각 다음 부등식에서 따른다. $\delta$는 관련된 $\delta$들 중 가장 좁은 근방을 주는 것으로 잡는다.

1. $|e_1 + e_2| \leq \frac{\epsilon}{2}|g| + \frac{\epsilon}{2}|g| = \epsilon|g|$
2. $|b e| \leq M \cdot \frac{\epsilon}{M}|g| = \epsilon|g|$
3. $|e_1 e_2| \leq \epsilon|f| \cdot 1|g| = \epsilon|fg|$
4. $|e| \leq \frac{\epsilon}{M}|g| \leq \epsilon|h|$

$\blacksquare$

**예시.** $x \in O_{x \to 0}(1)$ 이므로, 성질 4에 의해 $e(x) \in o_{x \to 0}(x) \to e(x) \in o_{x \to 0}(1)$ 이다.

**예시.** $f(x) = g(x) + o(h(x))$ 이고 $g(x) = k(x) + o(h(x))$ 이면 $f(x) = k(x) + o(h(x))$ 이다. $f = g + e_1$, $g = k + e_2$ 이면 $f = k + (e_1 + e_2)$ 이고, 성질 1에 의해 $e_1 + e_2 \in o(h)$ 이기 때문이다.

## Big-O의 성질

**정리. Big-O의 기본 성질** 

1. $e_1, e_2 \in O(g) \to e_1 + e_2 \in O(g)$
2. $e_1 \in O(f), e_2 \in O(g) \to e_1 e_2 \in O(fg)$
3. $g \in O(h)$ 이면 $e \in O(g) \to e \in O(h)$

_증명._ 각각 $|e_1 + e_2| \leq (C_1 + C_2)|g|$, $|e_1 e_2| \leq C_1 C_2|fg|$, $|e| \leq C_1|g| \leq C_1 C_2|h|$ 에서 따른다. $\blacksquare$

## Big-O와 Little-o의 관계

$O$는 "어떤 상수배 이하", $o$는 "임의로 작은 상수배 이하"이다. 정의에서 $\exists C > 0$이 $\epsilon > 0 \to$으로 바뀐 것이 유일한 차이이다.

**정리.** 

1. $e \in o(g) \to e \in O(g)$
2. $f \in O(g) \iff \exists \beta \in O(1), f = \beta g$ 이고, $f \in o(g) \iff \exists \eta \in o(1), f = \eta g$
3. $e_1 \in O(f), e_2 \in o(g) \to e_1 e_2 \in o(fg)$
4. $f \in o(g), g \in O(h) \to f \in o(h)$ 이고, $f \in O(g), g \in o(h) \to f \in o(h)$

_증명._ 

1. $o$의 정의에서 $\epsilon = 1$로 둔다.
2. $g(x) \neq 0$인 곳에서 $\beta = f/g$, 그 밖에서 $\beta = 0$으로 둔다. $|f| \leq C|g|$ 이므로 $g(x) = 0$인 곳에서 $f(x) = 0$ 이다. $\eta$도 같다.
3. $|e_1 e_2| \leq C|f| \cdot \frac{\epsilon}{C}|g| = \epsilon|fg|$
4. $|f| \leq \frac{\epsilon}{C}|g| \leq \epsilon|h|$ 이고, $|f| \leq C|g| \leq C \cdot \frac{\epsilon}{C}|h|$ 이다.

$\blacksquare$

즉 $O(g)$는 "$g$ 곱하기 유계인 것", $o(g)$는 "$g$ 곱하기 $0$으로 가는 것"이다. Little-o의 성질 2와 4는 각각 성질 3과 4의 특수한 경우이다. 곱이나 추이에서 하나라도 $o$이면 결과는 $o$이다.

**정리.** $L$ 근처에서 $g(x) \neq 0$ 이면 $f \in o(g) \to f \notin \Omega(g)$ 이다. 특히 $f \in \Theta(g)$ 이면 $f \notin o(g)$ 이다.

_증명._ $|f| \geq C|g|$ 이고 $|f| \leq \frac{C}{2}|g|$ 이면 $g = 0$ 이다. $\blacksquare$

**예시.** $O(g)$가 $o(g)$와 $\Theta(g)$로 나뉘지는 않는다. $x \sin\frac{1}{x} \in O_{x \to 0}(x)$ 이지만, 비율 $\sin\frac{1}{x}$가 진동하므로 $o_{x \to 0}(x)$에도 $\Theta_{x \to 0}(x)$에도 속하지 않는다.

## 균등한 경우

위의 모든 성질은 [[Uniform Big-O Like Notations]]의 균등한 표기에 대해서도 성립한다. 증명에서 고른 $\delta$와 $C$가 매개변수와 무관하기 때문이다. 이때 성질의 조건에 있는 $M$, $C$도 매개변수와 무관해야 한다.

**예시.** $f$가 $[a, b]$에서 유계이고 $e(x, y) \in o_{x, y \in [a, b]}(1)$ 이면 $f(x)e(x, y) \in o_{x, y \in [a, b]}(1)$ 이다. 반면 $f$가 유계가 아니면 성립하지 않을 수 있다.
