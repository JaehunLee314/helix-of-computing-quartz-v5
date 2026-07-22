**Prerequisites:** [[PAC Learnability]], [[Uniform Convergence]], [[VC Dimension]]

## Fundamental Theorem of PAC Learning

**Theorem. Fundamental Theorem of PAC Learning**
Loss function이 0-1 loss이고 가설 집합이 $H \subseteq \mathcal{X} \Rightarrow \{0, 1\}$이라 할 때 다음이 서로 동치이다.

1. $H$가 uniform convergence property를 가진다.
2. Learning algorithm $A$의 가설 집합이 $H$이고 $A$가 ERM rule이면 $A$는 APAC learnable 하다.
3. Learning algorithm $A$의 가설 집합이 $H$이고 $A$가 ERM rule이면 $A$는 PAC learnable 하다.
4. $H$가 유한한 VC dimension을 가진다.

*Proof Outline.*
(1)에서 (2)로 가는 증명은 정의를 적용하는 것으로 증명할 수 있다. (자세한 내용은 참고문헌 (1)의 chapter 4를 볼 것.) (2)에서 (3)으로 가는 증명은 정의에 의해 자명하다. (3)에서 (4)는 no-free-lunch theorem에 의해 성립한다. (4)에서 (1)로 가는 증명은 만약 $H$의 VC dimension이 유한하면 $H$의 실질적인 크기는 제한된다는 사실을 이용한다. 구체적인 증명은 어렵다. 참고문헌 (1)의 챕터 6을 볼 것.

Sample complexity가 명시적으로 주어지는 경우 다음과 같은 정리가 성립한다.

**Theorem. Fundamental Theorem of PAC Learning - Quantitative Version**
Loss function이 0-1 loss이고 가설 집합이 $H \subseteq \mathcal{X} \Rightarrow \{0, 1\}$이라 하자. 또한 $VCDim(H) = d < \infty$라고 두자. 그러면 다음을 모두 성립하도록 하는 적당한 상수 $C_1, C_2$가 존재한다.

1. $H$가 uniform convergence property를 가지며 sample complexity $m_H^{UC}$에 대해 다음이 성립한다.
$$
C_1 \frac{d + log(1/\delta)}{\epsilon^2} \leq m_H^{UC}(\epsilon, \delta) \leq C_2 \frac{d + log(1/\delta)}{\epsilon^2}
$$
2. $H$가 APAC learnable하며 sample complexity $m_H$에 대해 다음이 성립한다.
$$
C_1 \frac{d + log(1/\delta)}{\epsilon^2} \leq m_H(\epsilon, \delta) \leq C_2 \frac{d + log(1/\delta)}{\epsilon^2}
$$
3. $H$가 PAC learnable하며 sample complexity $m_H$에 대해 다음이 성립한다.
$$
C_1 \frac{d + log(1/\delta)}{\epsilon} \leq m_H^{UC}(\epsilon, \delta) \leq C_2 \frac{dlog(1/\epsilon) + log(1/\delta)}{\epsilon}
$$

## References
(1) Shalev-Shwartz, Ben-David, *Understanding Machine Learning*  