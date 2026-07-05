## Derivation of Information Entropy

Shannon은 그의 논문에서 다음과 같이 논한다.

> The fundamental problem of communication is that of reproducing at one point either exactly or approximately a message selected at another point. (...) **The significant aspect is that the actual message is one selected from a set of possible messages.** The system must be designed to operate for each possible selection, not just the one which will actually be chosen since this is unknown at the time of design. (1)

이로부터 그는 메시지를 선택하는 과정에서 발생하는 정보의 생산에 대한 이론을 구성했다. 

$\mathcal{M}$이 메시지의 유한한 집합이라고 하고 확률 변수 $M \sim P_M$ 이 $M \in \mathcal{M}$  이라고 하자. (즉, $M$의 codomain이 $\mathcal{M}$ 이라고 하자.) 이제 우리는 이 확률적 과정이 얼마만큼의 정보를 생산하는지 측정하는 함수 $H$를 정의하고자 한다. 여기서 $H$는 확률 변수에서 실수로 가는 함수이다.

Shannon은 $H$를 정의하기 위한 공리로 다음을 제시했다.

**연속성 공리**
$H(M)$는 $P_M(m)$에 대한 연속함수여야 한다.

**균등분포 공리**
만약 $P_M$이 균등분포라면 $H(M)$은 $|\mathcal{M}|$에 대한 단조증가함수여야 한다. 즉, 모든 메시지가 동일하게 가능하다면 가능한 메시지의 집합이 클 수록 생산되는 정보량은 동일하거나 커져야 한다.

**연쇄법칙 공리**
확률변수 $C \in \mathcal{C}$를 가정하자. 이제 $M$이 반드시 어떤 분류 $C$에 속한다고 하자. 정확히 말하면 $M$이 정해지면 $C$의 값이 반드시 결정론적으로 주어진다고 하자. 즉, $\exists l : \mathcal{M} \to \mathcal{C}, P_{C|M}(c|m) = 1\{c = l(m)\}$) 그렇다면 다음이 성립한다.

$$
H(M) = H(C) + E_C H(M|C)
$$

즉, 메시지를 생성하는 확률적 과정이 두 단계(분류를 선택하는 과정, 그 분류 안에서 메시지를 선택하는 과정)으로 나누어진다고 하면 $H$는 이것을 두 과정의 선형결합으로 표현한다.

이제 우리는 이것으로부터 다음 정리를 유도할 수 있다.

**Theorem. Uniqueness of Information Entropy**
연속성 공리, 균등분포 공리, 연쇄법칙 공리를 만족하는 $H$는 임의의 $K > 0$에 대해 다음과 같은 형태로 유일하게 존재한다.

$$
H(M) = K \cdot E_M [-log P(M)]
$$

이것의 증명은 이 글의 마지막 부분에 있다. 이 글의 나머지 부분에서 표준에 따라 $K = \log e / \log 2$로 둘 것이다. 물론, 이것은 정보량을 bit로 표현하게 해 준다.

## Some Examples

몇 가지 확률변수에 대해 정보 엔트로피가 어떻게 작동 하는지 살펴보자.

### Uniform Distribution

앞서서 우리는 균등분포 공리를 살펴본 바 있다. $M \in \mathcal{M}$ 이고 균등분포를 따른다고 가정하자. 그러면 다음의 계산이 성립한다.

$$
H(M) = E_M (-log_2 1 / |\mathcal{M}|) = log_2 |\mathcal{M}|
$$

따라서 $H(M)$이 $|\mathcal{M}|$에 대한 강한 단조증가함수라는 공리가 만족된다.

### Deterministic Process

단 하나의 값에 대해서 확률이 1인 결정론적 분포를 고려하자. 이때 어렵지 않게 $H(M) = 0$ 임을 알 수 있다. 즉, 결정론적 확률적 과정은 정보를 생산하지 않는다. 

여기서는 해석의 주의가 필요하다. 결정론적 과정을 통해 얻어진 결과값은 맥락에 따라 의미있는 정보를 담고 있을 수 있다. 하지만 결정론적 과정 그 자체가 메시지에 정보를 더해주지 않는다는 점이 중요하다. 반드시 하나의 값으로 고정되는 과정에서 추가되는 정보는 없다. 이것에 대한 자세한 설명은 [[KL Divergence]]에서 다룰 것이다.

## Note on Information Content

Information content는 정보 엔트로피에서 파생되는 개념으로 구체적인 확률적 event 하나가 가지는 정보의 량을 의미하며 다음과 같이 정의된다.

$$
i_M (m) = -log_2 P_M(m) \quad or \quad i(M) = -log_2 P(M)
$$

여기에는 몇 가지 유용한 성질이 있다. 예를 들어서 서로 독립인 두 확률변수 $X, Y$에 대해 다음이 성립한다.

$$
i_X(x) + i_Y(y) = i_{X, Y}(x, y)
$$

또한 반드시 일어나는 사건의 정보량은 0이며, 일어날 확률이 낮은 사건의 정보량은 매우 크다. 

자연스럽게 정보 엔트로피는 다음과 같이 정의된다.

$$
H(M) = E_M i(M)
$$

이 관점에서 정보 엔트로피는 각 event의 information content의 기댓값이다.

## Proof of the Uniqueness of Information Entropy

이 증명은 Shannon의 논문에서 기호를 바꾸고 이해를 돕기 위한 설명을 추가한 것이다. 증명은 균등분포에서의 증명과 일반적인 분포에서의 증명으로 나누어진다. 정보 엔트로피의 실용적 이해의 관점에서는 정보 엔트로피가 로그의 성질을 보인다는 것을 이해하는 것으로 충분하다.

### 균등분포에서의 증명

$n$개의 값에서 균등하게 선택하는 확률변수를 $U(n)$ 이라고 하자. 이제 다음을 생각해 보자.

$$
H(U(s^m))
$$

균등하게 $s^m$ 개를 선택하는 것은 $s$개의 문자를 균등하게 사용하여 길이 $m$의 문자열을 구성하는 확률적 과정과 동등하다. 따라서 우리는 첫 문자를 선택하는 것과, 그 다음 문자들을 선택하는 것으로 확률과정을 나눌 수 있다. (*필요하다면 이 과정의 수형도를 그려볼 것.*) 이때 연쇄법칙 공리를 고려하면 다음이 성립한다.

$$
H(U(s^m)) = H(U(s)) + E_{U(s)} H(U(s^{m-1})|U(s))
$$

그런데 문자들은 서로 독립적으로 선택되기 때문에, 다음과 같다.

$$
H(U(s^m)) = H(U(s)) + H(U(s^{m-1}))
$$

즉, 귀납적으로 다음이 성립한다.

$$
H(U(s^m)) = mH(U(s))
$$

이것은 로그함수의 그 성질과 매우 유사하다. 따라서 우리는 식의 조작을 통해 다음을 보일 것이다.

$$
0 < \epsilon \to\left | \frac{H(U(t))}{H(U(s))} - \frac{\log t}{\log s} \right | < 2\epsilon
$$

적당한 $s, m, t, n$에 대해 다음이 성립한다고 가정해 보자.

$$
s^m \leq t^n < s^{m+1} \cdots (1)
$$

이제 이 식에 로그를 취하고 $n \log s$로 나누면 다음을 얻는다.

$$
\frac{m}{n} \leq \frac{\log t}{\log s} < \frac{m}{n} + \frac{1}{n}
$$
$$
\Rightarrow \left | \frac{m}{n} - \frac{\log t}{\log s} \right | \leq \frac{1}{n} \cdots (2)
$$

한편 $H(U(n))$은 균등분포 공리에 의해 $n$에 대한 단조증가함수임으로 다음이 성립한다.

$$
H(U(s^m)) \leq H(U(t^n)) \leq H(U(s^{m+1}))
$$
$$
\Rightarrow mH(U(s)) \leq nH(U(t)) \leq (m+1)H(U(s))
$$

이제 식을 $nH(U(s))$로 나누면 다음이 성립한다.

$$
\Rightarrow \frac{m}{n} \leq \frac{H(U(t))}{H(U(s))} \leq \frac{m}{n} + \frac{1}{n}
$$
$$
\Rightarrow \left | \frac{m}{n} - \frac{H(U(t))}{H(U(s))} \right | \leq \frac{1}{n} \cdots (3)
$$

이제 (2)과 (3)를 삼각부등식을 사용해 연립하면 다음을 얻는다.

$$
\left | \frac{H(U(t))}{H(U(s))} - \frac{\log t}{\log s} \right | \leq \frac{2}{n} \cdots (4)
$$

이제 적당한 $n$을 선택하면 항상 그에 맞는 $s, m, t$가 존재하여 식 (1)을 만족시킬 수 있음으로 식 (4)는 다음과 같이 적을 수 있다.

$$
0 < \epsilon \to\left | \frac{H(U(t))}{H(U(s))} - \frac{\log t}{\log s} \right | < 2\epsilon
$$

즉 우리가 원하던 다음의 결론을 얻는다.

$$
H(U(t)) = K \log t
$$

### 일반적인 분포에서의 증명

이제 분포가 균등하지 않은 경우를 생각해 보자. 여기서 우리는 $m$개의 공 중 하나를 균등하게 고르는 확률적 과정을 생각한다. 이때 공에 $n$개의 색이 칠해져 있고 색 $i$가 칠해져 있는 공이 $w_i$개 있다고 하자. 그렇다면 공 하나를 고르는 과정은 먼저 어느 색 $i$를 확률 $w_i / \sum_j w_j$로 고른 후, 그 중의 공을 균등하게 선택하는 과정과 동등하다. 따라서 우리는 이것에 대해 연쇄법칙 공리를 적용할 수 있다.

먼저 색과 상관없이 공을 균등하게 고르는 과정에 대한 $H$는 앞선 증명의 결과를 그대로 사용할 수 있다. 따라서,

$$
H(U(m)) = K \log m
$$

이제 색을 고른 뒤 그 색의 공을 균등하게 뽑는 과정은 다음과 같이 적을 수 있다. 이때 색을 나타내는 확률변수를 $C$라고 하자.

$$
H(U(m)) = H(C) + E_C H(U(m)|C) = H(C)+\sum_i \frac{w_i}{m} H(U(w_i)) = H(C) + \sum_i \frac{w_i}{m} K \log w_i
$$
이제 두 식을 연립하면 다음을 얻는다.

$$
H(C) = K(\log m - \sum_i \frac{w_i}{m} \log w_i) = K\sum_i \frac{w_i}{m} \log \frac{m}{w_i} = -K\sum_i \frac{w_i}{m} \log \frac{w_i}{m}
$$

앞선 확률적 과정으로 고려하면 $p_C(i) = w_i/m$ 이므로 결과적으로 다음과 같다.

$$
H(C) = -K \sum_i p_C(i) \log P_C(i)
$$

따라서 우리는 확률이 유리수로 주어지는 분포에 대해 $H(C)$를 유도했다. 만약 확률이 무리수인 경우 우리는 그 확률에 대한 유리수 근사를 찾을 수 있다. 이제 연속성 공리에 의해 그러한 근사의 극한이 $H(C)$로 주어진다. 따라서 위의 식은 일반적인 확률에 대해서 성립한다. 결론적으로 어떤 이산확률변수에 대해 다음이 성립한다.

$$
H(M) = K E_M[-\log P(M)]
$$

## Footnote
- 메시지를 **생성**하는 과정과 LLM이 **생성**모델이라는 것 사이의 관계는 우연이 아니다.
- Information content가 독립변수의 결합분포에 대해 가지는 성질은 로그함수를 정의하는 성질(i.e. 코시의 함수 방정식)이다. 따라서 이것으로부터 정보 엔트로피를 유도하는 것이 더 쉽다. 다만 원전이 확률적 과정을 중요시한 것도 그 자체로 의의가 있다.

## References
(1) C. E. Shannon, A Mathematical Theory of Communication.  
(2) Thomas M. Cover, Joy A. Thomas, Elements of Information Theory 2nd ed.

