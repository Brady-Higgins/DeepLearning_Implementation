# Implementation of a Linear Regression Algorithm

## Math
*Mean Squared Error = MSE*

MSE= $\frac{1}{n} \sum_{i=0}^{n} (y_i - \hat{y}_i)^2$ &nbsp;&nbsp;&nbsp;     (1.1)  
MSE= $\frac{1}{n} \sum_{i=0}^{n} (y_i - (m*x_i + b))^2$&nbsp;&nbsp;&nbsp;(1.2)  

**Take the partial derivative with respect to the gradient (m)**  
$\frac{\partial MSE}{\partial b} = \frac{-2}{n} \sum_{i=0}^{n} ( x_i * (y_i - (m*x_i + b))$  &nbsp;&nbsp;&nbsp; (1.3)  
**Take the partial derivative with respect to the bias parameter (b)**  
$\frac{\partial MSE}{\partial b} = \frac{-2}{n} \sum_{i=0}^{n} ((y_i - (m*x_i + b))$$ &nbsp;&nbsp;&nbsp;(1.4)

**Solving for gradient descent**  
m = m - $L * \frac{\partial MSE}{\partial m}$  
b = b - $L * \frac{\partial MSE}{\partial b}$

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
  

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Linear_regression.svg/800px-Linear_regression.svg.png)