
class LinearRegression:
    def gradient_descent(m_now, b_now, data, L):
        m_gradient = 0
        b_gradient = 0
        n = len(data)
        for i in range(n):
            x = data.iloc[i].MedInc
            y = data.iloc[i].PRICE
            #partial derivate of Mean Squared Error (MSE) with respect to the gradient (m)
            m_gradient += -(2/n) * x * (y-(m_now * x + b_now))
            #partial derivate of Mean Squared Error (MSE) with respect to the bias parameter (b)
            b_gradient += -(2/n) * (y-(m_now * x + b_now))
        # subtract the gradient for gradient descent and multiply by the learning rate to remove strength of any 1 point
        m = m_now - m_gradient * L
        b = b_now - b_gradient * L
        return m,b
    def train(self,learning_rate, epochs, data):
        for i in range(epochs):
            if i % 10 == 0:
                print(f"Epoch:{i}")
            m, b = self.gradient_descent(m,b,data,L = learning_rate)