from typing import List, Tuple, Any, Dict
from ramda import pick, map, filter, difference

Row = List[Any]


class Table:
    rows = []

    def __init__(self, headers: List[str], items: List[Row] = [], rows: List[any] = []):
        self.headers = headers
        if (len(items) > 0):
            self.rows = list(map(lambda row: dict(zip(headers, row)), items))

        if(len(rows) > 0):
            self.rows = rows

    def get_values_by_headers(self, headers: List[str]):
        if len(difference(headers, self.headers)) > 0:
            raise Exception('Invalid headers.')

        new_rows = map(lambda row: pick(headers, row), self.rows)
        return Table(headers=headers, rows=new_rows)

    def filter(self, header: str, value: any):
        if len(difference([header], self.headers)) > 0:
            raise Exception('Invalid headers.')

        new_rows = filter(lambda row: row[header] == value, self.rows)
        return Table(headers=self.headers, rows=new_rows)

    def pick_columns(self, headers: List[str]):
        if len(difference(headers, self.headers)) > 0:
            raise Exception('Invalid headers.')

        new_rows = map(lambda row: pick(headers, row), self.rows)
        return Table(headers=headers, rows=new_rows)
