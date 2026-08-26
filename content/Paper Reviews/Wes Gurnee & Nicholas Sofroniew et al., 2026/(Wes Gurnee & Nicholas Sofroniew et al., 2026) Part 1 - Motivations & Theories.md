---
draft: "true"
---
*Paper Name: Verbalizable Representations Form a Global Workspace in Language Models [Link](https://transformer-circuits.pub/2026/workspace/index.html)*

## Motivation
*Related Sections in the Paper: 1*

이 논문의 동기는 다음과 같다. 인간이 *의식적으로 접근 가능한 정보*는 뇌가 처리하는 정보에 일부에 지나지 않는다. 가령 뇌는 심장박동을 관리하지만 우리가 의식적으로 심장박동을 인식하거나 조정할 수 있는 것은 아니다. 그렇다면 최신 언어 모델에서도 이와 같이 *의식적으로 접근 가능한 정보*와 그렇지 않은 정보가 구분될까?

## Theoretical Formulation of the Problem
*Related Sections in the Paper: 1.1*

저자들은 *의식적으로 접근 가능한 정보*라는 개념을 구체화하기 위해 그것을 이해하는 두 가지 관점인 access consciousness와 phenomenal consciousness을 제시한다.

먼저 access consciousness는 뇌가 처리하는 정보 중 논리적 추론에 사용되고, 사람의 행동과 발화를 직접적으로 통제하는 정보들을 말한다. Access consciousness라는 개념은 순전히 기능적인(functional) 개념으로 정보가 가지는 일련의 성질에 의해 결정된다.

반면 phenomenal consciousnes는 우리가 느끼는 주관적인 경험(subjective experience)를 말한다. 이것은 철학적인 개념으로 아직 과학적 실험의 대상이 되기에는 부적합하다. 또한 Access consciousness와 phenomenal consciousness의 관계는 논쟁적이며 명확하게 규명되지 않았다. 

이를 고려하여 저자들은 *의식적으로 접근 가능한 정보*를 access consciousness의 개념으로 한정한다. 이제 access consciousness가 가지는 성질에는 다음과 같은 것들이 있다.

1. 정보를 요청하면 그것을 언어적 (혹은 비언어적으로) 보고할 수 있다. 예를 들어서 "지금 무슨 생각을 하고 있나요?" 같은 질문에 답하는 것이 여기에 해당한다.
2. 정보가 top-down control의 대상이 된다. 즉 의도적으로 연상되거나, 의식 속에 남아 있거나, 잊혀질 수 있다.
3. 정보가 의도적인 추론의 매개체로 쓰인다. 
4. 정보의 유연한 일반화(flexible generalization)가 가능하다. 만약 정보가 다른 맥락 속에서 쓰이면 그에 적합한 특성을 얻게 된다.
5. 뇌에서 일어나는 처리 중 오직 일부의 정보만이 이곳에 속한다.

뇌과학의 이론 중 하나인 global workspace theory에서는 이러한 성질을 뇌가 가지고 있는 가설적인 구조로 설명하고자 한다. 이 이론에서 뇌는 비교적 독립적인 여러 프로세스들로 이루어지며 각 프로세스는 공유되는 작업공간인 global workspace에 경쟁적으로 접근한다. (컴퓨터의 프로세스들과 그들이 공유하는 메모리의 critical area에 대한 비유를 생각해 볼 수 있다.) 이때 global workspace는 access consciousness의 성질을 가진다. 이 논문의 제목은 이곳에서 유래했다.

## Jacobian Lens
*Related Sections in the Paper: 2.1*

Jacobian lens는 transformer layer의 계산을 linear transform으로 근사하여 중간 activation의 영향을 측정하는 수학적 방법이다.

Context length가 $T$인 transformer decoder에 대해 $h_{l, t} \in R^d$가 layer $l$, token position $t$에 대한 residual stream의 값이라고 하고 $f$가 마지막 레이어라고 하자. 또한 token position $t'$에서의 최종 출력값인 $p_{t'} \in R^{vocab}$은 다음과 같은 unembedding matrix $W_U$를 통해 계산된다고 하자.

$$
p_{t'} = \text{softmax}(W_U h_{f, t'})
$$

이때 transforemr decoder의 causal mask에 의해 $h_{f, t'}$는 어느 layer $l < f$의 activation $h_{l, 1}, ..., h_{l, t'}$에 의해 결정된다. 따라서 적당한 행렬 $A_{l, t, t'}$에 대해 다음과 같은 근사식을 생각해 볼 수 있다.

$$
h_{f, t'} \approx J_{l, t, t'} h_{l, t} \ (t \leq t')
$$

여기서 $A_{l, t, t'}$이 token position $t, t'$에 관계없이 일정하다고 가정하면  식은 다음과 같이 된다.

$$
h_{f, t'} \approx A_{l} h_{l, t} \ (t \leq t')
$$

이때 $h_{l, t}$가 평균이 0인 Gaussian을 따른다고 가정하면 Stein's lemma에 의해 least-square solution $A^*$와 다음과 같은 Jacobian이 일치한다.

$$
A^* = J_l = \underset{t, t \leq t', h_{l, 1:t'}}{E}[\frac{\partial h_{f, t'}}{h_{l, t}}]
$$

이로부터 Jacobian lens는 다음과 같이 계산된다.

$$
\text{lens}_l(h) = \text{softmax} (W_U J_l h)
$$

즉, Jacobian lens의 결과값은 layer $l$의 residual stream $h$가 주어질 때 기대되는 최종 출력 확률의 근사이다.

## The J-Space
*Related Sections in the Paper: 2.3, 2.5, A.8*
Jacobian leans의 식은 다음과 같이 풀어볼 수 있다. 여기서 $[A]_i$는 $A$의 $i$번째 행을, $[A]^j$는 $A$의 $j$번째 열을 의미한다.

$$
[\text{lens}_l (h)]_k = [\text{softmax}(W_UJ_l h)]_k = \frac{\exp([W_UJ_l]_k h)}{\sum_i \exp([W_UJ_l]_i h)}
$$

즉 어떤 vocabulary $k$에 주어지는 확률은 $[W_UJ_l]_k$와 $h$의 내적으로 주어지므로 우리는 $h$가 $W_UJ_l$의 각 행의 방향과 얼마나 일치하는지를 바탕으로 $h$가 결과에 미치는 영향을 해석할 수 있다.

구체적으로 $W_U J_l$이 다음과 같이 주어진다고 하자.

$$
W_U J_l = \begin{pmatrix}
v_1^T \\
v_2^T \\
\vdots \\
v_{vocab}^T \\
\end{pmatrix}
$$

...

## Footnote
- $h_{l, 1:T}$는 구체적으로 다음과 같다. transformer decoder layer $\text{layer}_l$은 $h_{l-1, 1:T}$를 입력으로 받는다. 이때 residual connection에 의해 $h_{l, 1:T}$는 $\text{layer}_l (h_{l-1, 1:T}) + h_{l-1, 1:T}$ 로 주어진다.