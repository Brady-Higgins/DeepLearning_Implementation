# Implementation of a Linear Regression Algorithm

## Math

**Mean Squared Error (MSE):**

\[
\text{MSE} = \frac{1}{n} \sum_{i=0}^{n} (y_i - \hat{y}_i)^2 \quad (1.1)
\]

\[
\text{MSE} = \frac{1}{n} \sum_{i=0}^{n} (y_i - (mx_i + b))^2 \quad (1.2)
\]

**Partial derivatives:**

\[
\frac{\partial \text{MSE}}{\partial m} = \frac{-2}{n} \sum_{i=0}^{n} (x_i (y_i - (mx_i + b))) \quad (1.3)
\]

\[
\frac{\partial \text{MSE}}{\partial b} = \frac{-2}{n} \sum_{i=0}^{n} (y_i - (mx_i + b)) \quad (1.4)
\]

**Gradient Descent:**

Update rules:

\[
m = m - L \frac{\partial \text{MSE}}{\partial m}
\]

\[
b = b - L \frac{\partial \text{MSE}}{\partial b}
\]

## Code Implementation

```python
def gradient_descent(m, b, data, L):
    for x, y in data:
        m_gradient = -2 / len(data) * \sum_{i=0}^{n} (x (y - (mx + b)))
        b_gradient = -2 / len(data) * \sum_{i=0}^{n} (y - (mx + b))
        
    m -= m_gradient * L
    b -= b_gradient * L
    return m, b

m, b = 0, 0
L = 0.001
epochs = 300
for _ in range(epochs):
    m, b = gradient_descent(m, b, data, L)
