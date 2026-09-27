"""Pure functions for the Week 4 neural-network lab."""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np


def weighted_sum(x1: float, x2: float, w1: float, w2: float, bias: float) -> float:
    return (x1 * w1) + (x2 * w2) + bias


def activate(value: float, name: str) -> float:
    if name == "ReLU":
        return max(0.0, value)
    if name == "Sigmoid":
        return 1.0 / (1.0 + math.exp(-value))
    if name == "tanh":
        return math.tanh(value)
    raise ValueError(f"지원하지 않는 활성화 함수: {name}")


def activation_array(values: np.ndarray, name: str) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    if name == "ReLU":
        return np.maximum(0.0, values)
    if name == "Sigmoid":
        return 1.0 / (1.0 + np.exp(-values))
    if name == "tanh":
        return np.tanh(values)
    if name == "Leaky ReLU":
        return np.where(values >= 0, values, 0.1 * values)
    raise ValueError(f"지원하지 않는 활성화 함수: {name}")


def activation_derivative(values: np.ndarray, name: str) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    if name == "ReLU":
        return (values > 0).astype(float)
    if name == "Sigmoid":
        output = activation_array(values, name)
        return output * (1.0 - output)
    if name == "tanh":
        output = np.tanh(values)
        return 1.0 - output**2
    if name == "Leaky ReLU":
        return np.where(values >= 0, 1.0, 0.1)
    raise ValueError(f"지원하지 않는 활성화 함수: {name}")


def l2_penalty(weights: list[float] | np.ndarray, lambda_: float) -> float:
    values = np.asarray(weights, dtype=float)
    return float(lambda_ * np.sum(values**2))


def cosine_similarity(a: list[float] | np.ndarray, b: list[float] | np.ndarray) -> float:
    va = np.asarray(a, dtype=float)
    vb = np.asarray(b, dtype=float)
    denominator = float(np.linalg.norm(va) * np.linalg.norm(vb))
    if denominator == 0:
        return 0.0
    return float(np.dot(va, vb) / denominator)


@dataclass(frozen=True)
class ModelCandidate:
    name: str
    train_accuracy: float
    validation_accuracy: float
    monthly_cost: int

    @property
    def generalization_gap(self) -> float:
        return self.train_accuracy - self.validation_accuracy


MODEL_CANDIDATES = [
    ModelCandidate("모델 A", 0.91, 0.88, 1),
    ModelCandidate("모델 B", 0.99, 0.82, 3),
    ModelCandidate("모델 C", 0.94, 0.90, 2),
]


TOY_EMBEDDINGS: dict[str, list[float]] = {
    "three": [0.92, 0.14], "third": [0.86, 0.19], "iii": [0.82, 0.11],
    "two": [0.76, 0.08], "number": [0.71, 0.22], "rank": [0.67, 0.29],
    "orange": [-0.78, 0.38], "yellow": [-0.72, 0.48], "juice": [-0.61, 0.25],
    "fruit": [-0.66, 0.17], "lemon": [-0.59, 0.49], "color": [-0.48, 0.62],
    "apple": [-0.70, 0.05], "drink": [-0.43, 0.18], "sweet": [-0.54, 0.08],
    "bank": [0.08, -0.80], "money": [0.20, -0.75], "loan": [0.28, -0.69],
    "river": [-0.10, -0.62], "water": [-0.18, -0.54], "shore": [-0.06, -0.58],
    "customer": [0.44, 0.55], "buyer": [0.49, 0.50], "sales": [0.55, 0.46],
}


def nearest_words(word: str, top_k: int = 5) -> list[tuple[str, float]]:
    base = TOY_EMBEDDINGS[word]
    scored = [
        (candidate, cosine_similarity(base, vector))
        for candidate, vector in TOY_EMBEDDINGS.items()
        if candidate != word
    ]
    return sorted(scored, key=lambda item: item[1], reverse=True)[:top_k]
