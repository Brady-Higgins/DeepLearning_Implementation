# Implementation of a Linear Regression Algorithm

## Math
*Mean Squared Error = MSE*  

MSE = <sup>1</sup>&frasl;<sub>n</sub> ∑<sub>i=0</sub><sup>n</sup> (y<sub>i</sub> - &ycirc;<sub>i</sub>)<sup>2</sup>
 &nbsp;&nbsp;&nbsp;     (1.1)  
MSE = <sup>1</sup>&frasl;<sub>n</sub> ∑<sub>i=0</sub><sup>n</sup> (y<sub>i</sub> - (mx<sub>i</sub> + b))<sup>2</sup> (1.2)



**Take the partial derivative with respect to the gradient (m)**  
<sup>∂MSE</sup>&frasl;<sub>∂m</sub> = <sup>-2</sup>&frasl;<sub>n</sub> ∑<sub>i=0</sub><sup>n</sup> (x<sub>i</sub>(y<sub>i</sub> - (mx<sub>i</sub> + b)))  &nbsp;&nbsp;&nbsp; (1.3)  
**Take the partial derivative with respect to the bias parameter (b)**  
<sup>∂MSE</sup>&frasl;<sub>∂b</sub> = <sup>-2</sup>&frasl;<sub>n</sub> ∑<sub>i=0</sub><sup>n</sup> (y<sub>i</sub> - (mx<sub>i</sub> + b)) &nbsp;&nbsp;&nbsp;(1.4)

**Solving for gradient descent**  
m = m - L * <sup>∂MSE</sup>&frasl;<sub>∂m</sub><br>
b = b - L * <sup>∂MSE</sup>&frasl;<sub>∂b</sub>

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
  

Note: I'm never writing math with html ever again