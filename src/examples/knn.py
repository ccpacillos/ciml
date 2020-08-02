from ..lib.dataset import Dataset
from ..models.knn import KNearestNeighbor

training_data = Dataset(['easy', 'ai', 'sys', 'thy', 'morning'], [
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

knn = KNearestNeighbor(data=training_data, k=3)

print('guess = ' + str(knn.guess_label(test_points[0][0])))
