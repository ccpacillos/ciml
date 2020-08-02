from ..lib.dataset import Dataset
from ..models.knn import KNearestNeighbor

data = Dataset(['easy', 'ai', 'sys', 'thy', 'morning'], [
    ([1, 1, 0, 1, 0], 1),
    ([0, 1, 0, 0, 0], 1),
    ([0, 1, 1, 0, 1], 1),
    ([1, 1, 0, 1, 0], 1),
    ([0, 0, 0, 0, 1], 1),
    ([0, 1, 0, 1, 0], 1),
    ([1, 1, 1, 0, 1], -1),
    ([0, 0, 1, 0, 1], -1),
    ([0, 0, 1, 1, 0], -1),
    ([1, 0, 1, 0, 0], -1),
    ([0, 0, 0, 1, 0], 1),
    ([1, 1, 0, 0, 0], 1),
    ([0, 1, 0, 1, 0], 1),
    ([1, 0, 0, 1, 1], 1),
    ([0, 0, 1, 1, 0], -1),
    ([1, 0, 1, 0, 1], -1)
])

test_points = [
    ([1, 1, 0, 1, 0], 1),
    ([1, 1, 1, 1, 1], 1),
    ([0, 1, 1, 0, 1], -1),
    ([1, 0, 1, 0, 1], -1)
]

knn = KNearestNeighbor(data)

print(knn.get_nearest([0, 1, 1, 0, 1], 3))
