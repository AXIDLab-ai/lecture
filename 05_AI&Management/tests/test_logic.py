import numpy as np

from lab_logic import (
    activate,
    activation_array,
    activation_derivative,
    cosine_similarity,
    l2_penalty,
    nearest_words,
    weighted_sum,
)


def test_neuron_example():
    z = weighted_sum(3, 2, -0.4, 0.8, -0.1)
    assert round(z, 8) == 0.3
    assert activate(z, "ReLU") == z


def test_l2_example():
    assert l2_penalty([4, 0], 0.1) == 1.6
    assert l2_penalty([2, 2], 0.1) == 0.8


def test_cosine_and_neighbors():
    assert round(cosine_similarity([1, 0], [1, 0]), 8) == 1.0
    assert nearest_words("three", 1)[0][0] in {"third", "iii", "two"}


def test_activation_simulator():
    values = np.array([-2.0, 0.0, 2.0])
    assert activation_array(values, "ReLU").tolist() == [0.0, 0.0, 2.0]
    assert activation_derivative(values, "ReLU").tolist() == [0.0, 0.0, 1.0]
    assert activation_array(values, "Leaky ReLU").tolist() == [-0.2, 0.0, 2.0]
