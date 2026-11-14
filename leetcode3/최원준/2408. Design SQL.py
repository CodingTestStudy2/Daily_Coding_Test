
class SQL:

    def __init__(self, names: list[str], columns: list[int]):
        self.tables = {name: {} for name in names}
        self.columns = dict(zip(names, columns))
        self.next_id = {name: 1 for name in names}

    def ins(self, name: str, row: list[str]) -> bool:
        if name not in self.tables or len(row) != self.columns[name]:
            return False

        row_id = self.next_id[name]
        self.tables[name][row_id] = row
        self.next_id[name] += 1
        return True

    def rmv(self, name: str, rowId: int) -> None:
        if name in self.tables:
            self.tables[name].pop(rowId, None)

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tables:
            return "<null>"

        row = self.tables[name].get(rowId)

        if row is None or not 1 <= columnId <= self.columns[name]:
            return "<null>"

        return row[columnId - 1]

    def exp(self, name: str) -> list[str]:
        if name not in self.tables:
            return []

        return [
            f"{row_id},{','.join(row)}"
            for row_id, row in self.tables[name].items()
        ]
