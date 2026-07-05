## Variables

변수(variable)란 맥락(context)에 의해 제약되는 어느 문자를 말한다. 예를 들어서 우리는 $x$라는 변수를 제약하는 조건 $x \in R$을 사용하여 다음과 같은 논리식을 적을 수 있다.

$$
x \in R \to 0 \leq x^2
$$

이때 $x$는 제약된 조건 하에서 가능한 모든 값을 동시에 의미한다. 즉, 기호논리학적으로 말하면 위 식은 다음과 동치이다.

$$
\forall x. (x \in R \to 0 \leq x^2)
$$

따라서 우리는 변수의 치환(substitution)을 자연스럽게 아래와 같이 수행할 수 있다.

$$
x \in R \to 0 \leq x^2 \xrightarrow{x := -1} -1 \in R \to 0 \leq (-1)^2
$$


## Leibniz's Notation

어느 두 변수 $x, y$가 어떤 맥락에 의해 함수 관계 $y = f_{xy}(x)$를 가지고 $f_{xy}$의 미분이 $f_{xy}'$이라 할 때 우리는 다음과 같이 적는다.

$$
\frac{dy}{dx} = f_{xy}'(x)
$$

이제 이 식의 치환을 생각해 보자. 주의할 점은 좌변의 $dy/dx$는 *두 변수가 주어진 맥락 속에서 가지는 함수관계*를 나타내는 것이지, 두 변수를 직접 나타내는 것이 아니라는 것이다. 따라서 다음과 같다.

$$
\left . \frac{dy}{dx} \right |_{x := a} = f_{xy}'(a) \neq \frac{dy}{da}
$$

## Footnote
- 이곳에서 논의된 변수의 맥락과 치환은 type theory에서 사용되는 개념을 그대로 차용한 것이다.
- 라이프니츠 표기법에 대한 보다 진전된 논의는 [[Leibniz's Notation in Category Theory]]를 참고하라.



