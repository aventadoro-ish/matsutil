from typing import List


class TableIterator:
    def __init__(self, table):
        self.table = table
        self.index = 0

    def __next__(self):
        """Returns the next value from team object's lists """
        if self.index < self.table.__len__():
            result = self.table.table[self.index]
            self.index += 1
            return result

        # End of Iteration
        raise StopIteration


class TableColumnFormatException(Exception):
    def __init__(self, expected: List[str], received: List[str]):
        self.expected = expected
        self.received = received

    def __str__(self):
        return 'expected columns: ' + str(self.expected) + '; received: ' + str(self.received)


class Table:
    def __init__(self, column_names: List[str]):
        self.column_names = column_names
        self.table: List[List[object]] = []

    def __add__(self, entry: List[object]):
        if entry.__len__() != self.column_names.__len__():
            raise Table.TableColumnFormatException(self.column_names, entry)
        self.table.append(entry)

    def __len__(self):
        return self.table.__len__()

    def __iter__(self):
        return TableIterator(self)

    def get_entry_by_column_id(self, column_id: int, search_for):
        result = []
        print(self.table)
        for i in self.table:
            if i[column_id] == search_for:
                result.append(i)

        return result

    def get_entry_by_column_name(self, column_name: str, search_for):
        column_idx = self.column_names.index(column_name)
        return self.get_entry_by_column_id(column_idx, search_for)


