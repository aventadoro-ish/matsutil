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

	def __str__(self, index_len = 4, int_repr_base = 10):
		result: str = ''
		max_column_len: List[int] = [0] * self.get_columns()
		rows = [i for i in self]

		for row in [self.column_names] + rows:
			for cell_idx, cell in enumerate(row):
				if str(cell).__len__() > max_column_len[cell_idx]:
					max_column_len[cell_idx] = str(cell).__len__()

		result = ' ' * index_len + '|'

		partition = '-' * (result.__len__()-1) + '+'
		for i in max_column_len:
			partition += '-' * i + '+'
		partition = partition[:-1]

		for col_idx, column in enumerate(self.column_names):
			result += '{:^{}}'.format(str(column), max_column_len[col_idx]) + '|'

		result = result[:-1]
		result += '\n'
		result += partition + '\n'

		for row_idx, row in enumerate(rows):
			result += str(row_idx).zfill(index_len) + '|'
			for cell_idx, cell in enumerate(row):
				result += '{:^{}}'.format(str(cell), max_column_len[cell_idx]) + '|'

			result = result[:-1]
			result += '\n'

		return result

	def get_columns(self) -> int:
		return self.column_names.__len__()

	def get_rows(self) -> int:
		return self.__len__()

	def get_entry_by_column_id(self, column_id: int, search_for):
		result = []
		for i in self.table:
			if i[column_id] == search_for:
				result.append(i)

		return result

	def get_entry_by_column_name(self, column_name: str, search_for):
		column_idx = self.column_names.index(column_name)
		return self.get_entry_by_column_id(column_idx, search_for)

