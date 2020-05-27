from typing import List, Tuple, Any, Dict

Row = List[Any]


class Table:
    def __init__(self, headers: List[str], items: List[Row] = []):
        self.headers = headers
        self.rows = list(map(lambda row: dict(zip(headers, row)), items))
