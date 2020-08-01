from typing import List
from ..lib.table import Table
import math


class KNearestNeighbor:
    def __init__(self, data: Table):
        self.training_data = data

    def __get_distances(self, point: List[int]):
        return [self.__get_distance(a, point) for a in self.training_data]

    def __get_distance(self, pointA: List[int], pointB: List[int]):
        if len(pointA) != len(pointB):
            raise Exception('Points does not match dimensions.')
        return math.sqrt(sum([(a - b) ** 2 for a, b in zip(pointB, pointB)]))
