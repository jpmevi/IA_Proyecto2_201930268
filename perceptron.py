import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.01):
        np.random.seed(42)
        self.learning_rate = learning_rate
        self.weights = np.random.uniform(-0.01, 0.01, input_size + 1)

    def predict(self, x):
        x_with_bias = np.insert(x, 0, 1)
        summation = np.dot(self.weights, x_with_bias)
        return 1 if summation >= 0 else -1  # Función de activación escalón

    def train(self, X, y, epochs):
        print("Learning rate dentro de Perceptron (train):", self.learning_rate)
        errors = []
        for epoch in range(epochs):
            total_error = 0
            for xi, target in zip(X, y):
                prediction = self.predict(xi)
                update = self.learning_rate * (target - prediction)
                self.weights[1:] += update * xi
                self.weights[0] += update
                total_error += int(update != 0)
            errors.append(total_error)
        return errors
