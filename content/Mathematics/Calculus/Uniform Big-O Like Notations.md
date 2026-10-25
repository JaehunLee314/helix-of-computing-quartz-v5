**Prerequisites:** [[Big-O Like Notations]]

[[Big-O Like Notations]]의 표기는 한 함수가 한 점 근처에서 어떻게 행동하는지를 나타낸다. 식이 다른 변수(매개변수)에도 의존하면 정의의 $\delta$와 $C$는 매개변수마다 달라질 수 있다. 이들을 매개변수와 무관하게 잡을 수 있을 때 균등하다고 한다.

## Uniform Big-O Like Notation

**정의. Uniform Big-O Like Notation** 
집합 $P$와 함수 $e(p, s), g(p, s)$에 대해 다음과 같이 정의한다.

$$
e \in o_{P, L}(g) \iff \epsilon > 0 \to \exists \delta > 0, (p \in P, s \in N_\delta(L) \to |e(p, s)| \leq \epsilon|g(p, s)|)
$$

$$
e \in O_{P, L}(g) \iff \exists C > 0, \exists \delta > 0, (p \in P, s \in N_\delta(L) \to |e(p, s)| \leq C|g(p, s)|)
$$

$\Omega_{P, L}, \Theta_{P, L}$도 같은 방식으로 정의한다. $e$가 정의된 $(p, s)$만 생각하고, $L = 0$이면 $L$을 생략하여 $o_P$와 같이 적는다. $P$는 $\mathbb{R}^n$의 부분집합처럼 임의의 집합일 수 있고, $s \in \mathbb{R}^n$이면 근방은 노름으로 정의한다.

각 $p$를 고정하여 $e(p, \cdot) \in o_L(g(p, \cdot))$ 인 것과 비교하면 양화사의 순서만 다르다. 각 $p$에서의 경우는 $p$가 주어진 뒤 $\delta$를 고르므로 $\delta$가 $p$에 의존할 수 있지만, 균등한 경우는 $\delta$를 고른 뒤 $p$가 주어지므로 $\delta$가 $p$에 의존할 수 없다.

**정의. 변수를 사용한 Uniform Big-O Like Notation** 
$p, s$에 대한 식 $e(p, s), g(p, s)$에 대해 다음과 같이 정의한다.

$$
e(p, s) \in \underset{p \in P, s \to L}o (g(p, s)) \iff e \in o_{P, L}(g)
$$

한 줄로 적을 때는 $o_{p \in P, s \to L}(g(p, s))$와 같이 쓴다. $O, \Omega, \Theta$도 같다. 식 안에서 쓰는 경우도 [[Big-O Like Notations]]와 같이 해석한다.

**예시.** $x(t + s) = xt + xs$ 이고 $x \in [0, 1]$ 이면 $|xs| \leq |s|$ 이므로 다음이 성립한다.

$$
x(t + s) = xt + \underset{x \in [0, 1], s \to 0}o (1)
$$

반면 $x \in \mathbb{R}$ 이면 $|xs|$를 $x$와 무관하게 작게 만들 수 없으므로 균등하지 않다.

## 두 점 표기

집합 안의 두 점이 위치와 무관하게 가까워지는 경우는 자주 쓰이므로 따로 표기한다.

**정의. 두 점 표기** 
$I \subset \mathbb{R}^n$와 $x, y \in I$에 대한 식 $e(x, y), g(x, y)$에 대해 다음과 같이 정의한다.

$$
e(x, y) \in \underset{x, y \in I}o (g(x, y)) \iff e(x, x + s) \in \underset{x \in I, s \to 0}o (g(x, x + s))
$$

여기서 $x + s \in I$인 $s$만 생각한다. $O, \Omega, \Theta$도 같다.

이 정의는 거리 $\lVert y - x \rVert$가 작은 모든 쌍 $x, y \in I$에 대한 조건이므로 $x, y$는 대칭이다. 즉 $e(x, y) \in o_{x, y \in I}(g(x, y))$ 이면 $e(y, x) \in o_{x, y \in I}(g(y, x))$ 이다.

## 균등연속

**정의. 균등연속(Uniform Continuity)** 
함수 $f$가 $I$에서 다음을 만족하면 $I$에서 균등연속이라고 한다.

$$
f(y) = f(x) + \underset{x, y \in I}o (1)
$$

각 $x$에서 $f(y) = f(x) + o_{y \to x}(1)$ 인 것이 연속이다. 균등연속은 $f(y)$가 $f(x)$에 가까워지는 속도가 $x$와 무관하다는 것이다.

**예시.** $y^2 - x^2 = (x + y)(y - x)$ 이므로 $x^2$은 $[0, 1]$에서 균등연속이지만 $\mathbb{R}$에서는 균등연속이 아니다. $\mathbb{R}$에서는 $|x + y|$가 유계가 아니기 때문이다.

**정리. 하이네-칸토어 정리** 
$\mathbb{R}^n$의 유계인 닫힌 집합에서 연속인 함수는 그 집합에서 균등연속이다. 
_증명._ 참고문헌 (1)을 보라.

즉 유계인 닫힌 집합에서는 연속성이 균등성을 보장한다. 오차항의 균등성은 대부분 이 정리에 의존한다.

**따름정리.** $f(x, t)$가 $[a, b] \times [c, d]$에서 연속이면 다음이 성립한다.

$$
f(x, t + s) = f(x, t) + \underset{(x, t) \in [a, b] \times [c, d], s \to 0}o (1)
$$

_증명._ 하이네-칸토어 정리를 두 점 $(x, t), (x, t + s)$에 적용한다. $\blacksquare$

## 참고문헌
(1) Walter Rudin, Principles of Mathematical Analysis
