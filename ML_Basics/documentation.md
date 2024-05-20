# Implementation of a Linear Regression Algorithm

## Math
*Mean Squared Error = MSE*

\[
MSE = \frac{1}{n} \sum_{i=0}^{n} (y_i - \hat{y}_i)^2 \quad (1.1)
\]

\[
MSE = \frac{1}{n} \sum_{i=0}^{n} (y_i - (m \cdot x_i + b))^2 \quad (1.2)
\]

**Partial derivatives:**

\[
\frac{\partial MSE}{\partial m} = \frac{-2}{n} \sum_{i=0}^{n} (x_i \cdot (y_i - (m \cdot x_i + b))) \quad (1.3)
\]

\[
\frac{\partial MSE}{\partial b} = \frac{-2}{n} \sum_{i=0}^{n} (y_i - (m \cdot x_i + b)) \quad (1.4)
\]

**Gradient Descent:**


\[
m = m - L \cdot \frac{\partial MSE}{\partial m}
\]

\[
b = b - L \cdot \frac{\partial MSE}{\partial b}
\]

## Code implementation
``` 
gradient descent (m,b, data, L) =
    for data:
        m_gradient = plug into equation 1.3
        b_gradient = plug into equation 1.4
    m = m - m_gradient * L
    b = b - b_gradient * L
    return m,b

m,b = 0
L = 0.001
epochs = 300
for epochs{
    m,b = gradient_descent(m,b,data,L)
} ```
  