## Likelihood의 정의

어느 이산확률변수 $Z$가 $\theta$로 parameterize 되는 확률분포 $p^\theta$를 따른다고 하자. 즉 $Z \sim p^\theta$라 하자. 이때 likelihood $L$은 다음과 같이 정의된다. 

$$
L(\theta ; Z=z) = P(Z=z) = p^\theta(z)
$$

이때 확률이 $\theta$에 의존적임을 표기하기 위해 $P^\theta (Z=z)$ 라고 적으면 다음과 같이 표기할 수 있다.

$$
L(\theta;Z) = P^\theta(Z)
$$

한편 $Z$가 연속확률변수일 때 likelihood는 다음과 같이 정의된다.

$$
L(\theta;Z=z) = p^\theta(z)
$$

이때 $p^\theta$는 확률밀도함수이다. 

## 연속확률변수의 Likelihood Ratio

$Z$가 연속확률변수일 때 $p^\theta(z)$가 연속이면 다음이 성립한다.

$$
\lim_{\epsilon \to 0} \frac{P^\theta (z-\epsilon<Z<z+\epsilon)}{2\epsilon} = \lim_{\epsilon \to 0} \frac{P(Z < z + \epsilon) - P(Z < z - \epsilon)}{2\epsilon}=p^\theta(z)
$$
$$
\Rightarrow P^\theta (z-\epsilon<Z<z+\epsilon) \approx 2\epsilon p^\theta(z) = 2\epsilon L(\theta;Z=z)
$$

따라서 두 파라미터 $\theta_1, \theta_2$에 대한 likelihood의 비율은 다음과 같이 근사할 수 있다.

$$
\frac{L(\theta_1;Z)}{L(\theta_2;Z)} = \frac{2\epsilon p^{\theta_1}(z)}{2\epsilon p^{\theta_2}(z)} \approx \frac{P^{\theta_1} (z-\epsilon<Z<z+\epsilon)}{P^{\theta_2} (z-\epsilon<Z<z+\epsilon)}
$$

## Log Likelihood의 정의

Log-likelihood는 다음과 같이 정의된다.

$$
l(\theta ; Z) = log L(\theta ; Z)
$$

## Likelihood의 의미

$L(\theta;Z=z)$는 어느 관측 데이터 $z$가 주어질 때, parameter $\theta$가 가지는 일종의 개연성이다. 어느 두 $\theta_1, \theta_2$ 에 대해 $L(\theta_1; Z=z) > L(\theta_2; Z=z)$ 라면 실제 분포가 $\theta_1$으로부터 정의될 때 $z$를 관측할 확률이 실제 분포가 $\theta_2$로부터 정의될 때 $z$를 관측할 확률보다 크다.

## Footnote
- 통상적인 표기법 $L(\theta;Z)=P(Z|\theta)$에서 $\theta$는 크로네커 델타나 디렉 델타 함수를 확률분포로 가지는 deterministic random variable인 것으로 이해할 수 있다.

## References
(1) George Casella, Roger L. Berger, Statistical Inference 2ed.