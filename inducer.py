from typing import List
import table
import tree


class Inducer:
    model: tree.Tree

    def __init__(self, data: table.Table, features: List[str]):
        print(data)

    def __train__(self):
        print(self.model)
