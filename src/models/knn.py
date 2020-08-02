from typing import List
from ..lib.table import Table
import math
from ramda import map
from ..lib.dataset import Dataset

Vector = List[int]


class KNearestNeighbor:
    def __init__(self, data: Dataset):
        self.data = data
        self.dimensions = len(data.features)

    def __get_distances(self, point: Vector):
        return [(self.__get_distance(tup[0], point), tup) for tup in self.data.feature_values]

    def __get_distance(self, pointA: Vector, pointB: Vector):
        return math.sqrt(sum([(a - b) ** 2 for a, b in zip(pointA, pointB)]))

    def get_nearest(self, point: Vector, k: int):
        if len(point) != self.dimensions:
            raise Exception('Input point dimension mismatch.')

        distances = self.__get_distances(point)
        sorted_distances = sorted(distances, key=lambda tup: tup[0])
        nearest_neighbors = sorted_distances[:k]

        sum_of_labels = sum([tup[1][1] for tup in nearest_neighbors])

        guess = 1 if sum_of_labels > 0 else -1

        return guess
