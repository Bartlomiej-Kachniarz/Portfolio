"""Module for Multi-Layer Perceptron and Perceptron classes."""

import numpy as np


class Perceptron:
    """Class defining MLP model"""

    def __init__(self, no_of_inputs: int, bias: float = 1.0) -> None:
        """Constructor"""
        self.no_of_inputs = no_of_inputs
        self.bias = bias
        self.weights = (np.random.rand(self.no_of_inputs + 1) * 2) - 1

    def run(self, x: np.array) -> np.array:
        """Runs the MLP model

        Args:
            x (numpy.array): values
        """
        x_sum = np.dot(np.append(x, self.bias), self.weights)
        return self.sigmoid(x_sum)

    def sigmoid(self, arr: np.array) -> np.array:
        """Sigmoid activation function"""
        return 1 / (1 + np.exp(-arr))

    def set_weights(self, w_init: np.array):
        """Sets weights to both neurons and bias."""
        self.weights = np.array(w_init)


class MultiLayerPerceptron:
    """A multilayer perceptron model that uses perceptron class as a parent.
    Attributes:
        layers: np.array with the number of elements in each layer.
        bias: the bias term. The same bias is applied to all neurons.
        eta: learning rate.
    """

    def __init__(self, layers: np.array, bias: float = 1, eta: float = 0.5) -> None:
        self.layers = np.array(layers, dtype=object)
        self.bias = bias
        self.network = []  # array of arrays of neurons
        self.values = []  # array of outputs
        self.weights = []  # array of weights
        self.delta = []  # array of arrays of error terms
        self.eta = eta

        for layer, _ in enumerate(self.layers):
            self.network.append([])
            self.values.append([])
            self.delta.append([])
            self.values[layer] = [0.0 for _ in range(self.layers[layer])]
            self.delta[layer] = [0.0 for _ in range(self.layers[layer])]
            if layer > 0:  # network[0] is the input layer, so it has 0 neurons
                for _ in range(self.layers[layer]):
                    self.network[layer].append(Perceptron(no_of_inputs=self.layers[layer - 1], bias=self.bias))

        self.network = np.array([np.array(x) for x in self.network], dtype=object)
        self.values = np.array([np.array(x) for x in self.values], dtype=object)
        self.delta = np.array([np.array(x) for x in self.delta], dtype=object)

    def set_weights(self, w_init: np.array):
        """Writes weights to the network."""
        for layer, _ in enumerate(w_init):
            for neuron, _ in enumerate(w_init[layer]):
                self.network[layer + 1][neuron].set_weights(w_init[layer][neuron])

        self.weights = w_init

    def get_weights(self):
        """Print weights of the network."""
        print()
        for layer in range(1, len(self.network)):
            for neuron in range(self.layers[layer]):
                print(f"Layer: {layer + 1}. Neuron: {neuron}. Weights: {self.network[layer][neuron].weights}")
        print()

    def run(self, x):
        """Runs the model."""
        x = np.array(x, dtype=object)
        self.values[0] = x
        for layer in range(1, len(self.network)):
            for neuron in range(self.layers[layer]):
                self.values[layer][neuron] = self.network[layer][neuron].run(self.values[layer - 1])
        return self.values[-1]

    def back_propagation(self, x, y):
        """Runs the training algorithm."""
        x = np.array(x, dtype=object)
        y = np.array(y, dtype=object)

        # step 1: feed a sample to the network:
        y_hat = self.run(x)

        # step 2: calculate the MSE error
        error = y - y_hat
        mse_error = sum(error**2) / self.layers[-1]

        # step 3: calculate the output error terms
        self.delta[-1] = y_hat * (1 - y_hat) * (error)

        # step 4: calculate the error term on each unit on each layer
        for layer in reversed(range(1, len(self.network) - 1)):  # backwards
            for h, _ in enumerate(self.network[layer]):
                fwd_error = 0.0
                for k in range(self.layers[layer + 1]):
                    fwd_error += self.network[layer + 1][k].weights[h] * self.delta[layer + 1][k]
                    self.delta[layer][h] = self.values[layer][h] * (1 - self.values[layer][h]) * fwd_error

        # step 5: calculate the deltas and update the weights
        for layer in range(1, len(self.network)):
            for neuron in range(self.layers[layer]):
                for k in range(self.layers[layer - 1] + 1):
                    if k == self.layers[layer - 1]:
                        delta = self.eta * self.delta[layer][neuron] * self.bias
                    else:
                        delta = self.eta * self.delta[layer][neuron] * self.values[layer - 1][k]
                    self.network[layer][neuron].weights[k] += delta
        return mse_error


if __name__ == "__main__":
    # Run some tests:

    p_model = Perceptron(no_of_inputs=2)

    # Emulating AND logical gate:
    p_model.set_weights(np.array([10, 10, -15]))

    print("\nAND gate:")
    print(f"[0, 0]: 0; {p_model.run([0, 0]):.10f}")
    print(f"[1, 0]: 0; {p_model.run([1, 0]):.10f}")
    print(f"[0, 1]: 0; {p_model.run([0, 1]):.10f}")
    print(f"[1, 1]: 1; {p_model.run([1, 1]):.10f}")

    # Emulating OR logical gate:
    p_model.set_weights(np.array([10, 10, -5]))

    print("\nOR gate:")
    print(f"[0, 0]: 0; {p_model.run([0, 0]):.10f}")
    print(f"[1, 0]: 1; {p_model.run([1, 0]):.10f}")
    print(f"[0, 1]: 1; {p_model.run([0, 1]):.10f}")
    print(f"[1, 1]: 1; {p_model.run([1, 1]):.10f}")

    # Emulating NOR logical gate:
    p_model.set_weights(np.array([-10, -10, 5]))

    print("\nNOR gate:")
    print(f"[0, 0]: 1; {p_model.run([0, 0]):.10f}")
    print(f"[1, 0]: 0; {p_model.run([1, 0]):.10f}")
    print(f"[0, 1]: 0; {p_model.run([0, 1]):.10f}")
    print(f"[1, 1]: 0; {p_model.run([1, 1]):.10f}")

    # Emulating NAND logical gate:
    p_model.set_weights(np.array([-10, -10, 15]))

    print("\nNAND gate:")
    print(f"[0, 0]: 1; {p_model.run([0, 0]):.10f}")
    print(f"[1, 0]: 1; {p_model.run([1, 0]):.10f}")
    print(f"[0, 1]: 1; {p_model.run([0, 1]):.10f}")
    print(f"[1, 1]: 0; {p_model.run([1, 1]):.10f}")

    mlp_model = MultiLayerPerceptron(layers=[2, 2, 1])
    mlp_model.set_weights([[[-10, -10, 15], [15, 15, -10]], [[10, 10, -15]]])
    mlp_model.get_weights()
    print("\nXOR gate:")
    print(f"[0, 0]: 0: {mlp_model.run([0, 0])[0]:.10f}")
    print(f"[1, 0]: 1: {mlp_model.run([1, 0])[0]:.10f}")
    print(f"[0, 1]: 1: {mlp_model.run([0, 1])[0]:.10f}")
    print(f"[1, 1]: 0: {mlp_model.run([1, 1])[0]:.10f}")

    mlp_true_model = MultiLayerPerceptron(layers=[2, 2, 1])
    print("\nTraining neural network as a XOR logical gate...")
    for i in range(3000):
        mse = 0.0
        mse += mlp_true_model.back_propagation([0, 0], [0])
        mse += mlp_true_model.back_propagation([1, 0], [1])
        mse += mlp_true_model.back_propagation([0, 1], [1])
        mse += mlp_true_model.back_propagation([1, 1], [0])
        if i % 100 == 0:
            print(f"MSE in epoch: {i} is: {mse}")

    mlp_true_model.get_weights()
    print("\nXOR gate:")
    print(f"[0, 0]: 0: {mlp_true_model.run([0, 0])[0]:.10f}")
    print(f"[1, 0]: 1: {mlp_true_model.run([1, 0])[0]:.10f}")
    print(f"[0, 1]: 1: {mlp_true_model.run([0, 1])[0]:.10f}")
    print(f"[1, 1]: 0: {mlp_true_model.run([1, 1])[0]:.10f}")
