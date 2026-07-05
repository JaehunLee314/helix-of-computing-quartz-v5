## Numerator Layout

|                        | $y \in R^{1 \times 1}$                                                            | $y \in R^{n \times 1}$                                                         | $y \in R^{n \times m}$                                                            |
| ---------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| $x \in R^{1 \times 1}$ | $$\frac{\partial y}{\partial x}$$                                                 | $$(\frac{\partial y}{\partial x})_{i, 1} = \frac{\partial y_i}{\partial x}$$   | $$(\frac{\partial y}{\partial x})_{i, j} = \frac{\partial y_{i, j}}{\partial x}$$ |
| $x \in R^{m \times 1}$ | $$(\frac{\partial y}{\partial x})_{1, j} = \frac{\partial y}{\partial x_j}$$      | $$(\frac{\partial y}{\partial x})_{i, j} = \frac{\partial y_i}{\partial x_j}$$ |                                                                                   |
| $x \in R^{m \times n}$ | $$(\frac{\partial y}{\partial x})_{i, j} = \frac{\partial y}{\partial x_{j, i}}$$ |                                                                                |                                                                                   |

- Some texts use $\frac{\partial y}{\partial x^T}$ to represent $(\frac{\partial y}{\partial x})^T$.

## In Relation to the Gradient

Suppose $x \in R^{m \times 1}$ and $y \in R$ s.t. $y = f(x)$. Then the gradient is defined as follows.

$$
\nabla f(x) = (\frac{\partial y}{\partial x})^T
$$

Also we can define the Hessian as follows.

$$
\nabla^2f(x) = (\frac{\partial}{\partial x}(\frac{\partial y}{\partial x})^T)^T
$$

Because of the Clairaut's theorem, usually we use the following form.

$$
\nabla^2f(x) = \frac{\partial}{\partial x}(\frac{\partial y}{\partial x})^T
$$

## In Relation to Jacobian Matrix

Suppose $x \in R^{n \times 1}$ and $y \in R^{m \times 1}$ s.t. $y = f(x)$. Then the Jacobian matrix is defined as follows.

$$
J_f (x) = \frac{\partial y}{\partial x}
$$

## In Relation to the Chain Rule

For any possible combination of shapes for $x, y, z$, the following chain rule holds.

$$
\frac{\partial z}{\partial x} = \frac{\partial z}{\partial y} \frac{\partial y}{\partial x}
$$

## References
(1) Matrix Calculus, Wikipedia (https://en.wikipedia.org/wiki/Matrix_calculus)  
(2) Jacobian matrix and determinant, Wikipedia (https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant)