from typing import List
from ..lib import tree, table
from .. import data


def train(data: table.Table):
    for i in data.rows:
        print(i)


train(data.trainingData)
