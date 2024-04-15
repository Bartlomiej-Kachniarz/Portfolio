"""Module for Multi-Layer Perceptron and Perceptron classes."""

import numpy as np
import setuptools
from numpy.core.multiarray import array as array


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


class MultiLayerPerceptron(Perceptron):
    """A multilayer perceptron model that uses perceptron class as a parent.
    Attributes:
        layers: np.array with the number of elements in each layer.
        bias: the bias term. The same bias is applied to all neurons.
        eta: learning rate.
    """

    def __init__(self, layers: np.array, bias: float = 1) -> None:
        self.layers = np.array(layers, dtype=int)
        self.bias = bias
        self.network = []  # array of arrays of neurons
        self.values = []  # array of outputs

        for i, _ in enumerate(self.layers):
            self.network.append([])
            self.values.append([])
            self.values[i] = [0.0 for j in range(self.layers[i])]
            if i > 0:  # network[0] is the input layer, so it has 0 neurons
                for j in range(self.layers[i]):
                    self.network[i].append(Perceptron(no_of_inputs=self.layers[i - 1], bias=self.bias))

        self.network = np.array([np.array(x) for x in self.network], dtype=float)
        self.values = np.array([np.array(x) for x in self.values], dtype=float)

    def set_weights(self, w_init: np.array):
        """Writes weights to the network."""
        for i, _ in enumerate(w_init):
            for j, _ in enumerate(w_init[i]):
                self.network[i + 1][j].set_weights(w_init[i][j])

        self.weights = w_init

    def get_weights(self):
        """Print weights of the network."""
        for i in range(1, len(self.network)):
            for j in range(self.layers[i]):
                print(f"Layer: {i + 1}. Neuron: {j}. Weights: {self.weights[i][j]}")

    def run(self, x):
        """Runs the model."""
        x = np.array(x, dtype=float)
        self.values[0] = x
        for i in range(1, len(self.network)):
            for j in range(self.layers[i]):
                self.values[i][j] = self.network[i][j].run(self.values[i - 1])
        return self.values[-1]


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
