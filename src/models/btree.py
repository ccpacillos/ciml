from typing import List
from ..lib.tree import Tree
from ..lib.table import Table
from .. import data
from statistics import mode


def train(data: Table):
    labels = map(lambda i: 'like' if i['rating'] >= 0 else 'nah', data.rows)
    guess = mode(labels)

    if len(set(labels)) == 1 or len(data.headers) == 0:
        return Tree(value=guess)

    print('Data ambiguous and features not empty, continue.')
