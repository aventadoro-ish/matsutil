from typing import List


class Table:
    """
    TODO: docstring
    """
    def __init__(self, *args):
        self.entry_format = tuple(args)
        self.table = []

    def __str__(self):
        max_col_lengths = [0] * len(self.entry_format)
        for entry in (*self, self.entry_format):
            # TODO: reformat this nested loop
            for idx, cell in enumerate(entry):
                max_col_lengths[idx] = max(max_col_lengths[idx], len(str(cell)))

        # print headers and separator
        # TODO: [headers, separator, line_0, line_1 ... line_n] - ???
        headers = separator = ''
        for idx, header in enumerate(self.entry_format):
            # center header inside printed cell
            headers += f'{str(self.entry_format[idx]):^{max_col_lengths[idx]}}|'
            separator += '-' * max_col_lengths[idx] + '+'

        output = headers[:-1] + '\n' + separator[:-1] + '\n'

        # lines
        for entry in self:
            for idx, cell in enumerate(entry):
                # center cell text inside printed cell
                output += f'{str(cell):^{max_col_lengths[idx]}}|'

            output = output[:-1] + '\n'

        return output[:-1]

    def __iter__(self):
        for entry in self.table:
            yield entry

    def __getitem__(self, item):
        return self.table[item]

    def __len__(self) -> int:
        """
        Get number of entries (rows) in this table
        :return: int
        :rtype:
        """
        return len(self.table)

    def append(self, *args) -> int:
        """
        Add new entry to the table. Return this entry id
        :raises IndexError if fields do not match table format
        :param args: fields according to table format
        :type args:
        :return: this entry id
        :rtype:
        """
        if len(args) != len(self.entry_format):
            raise IndexError

        self.table.append(list(args))
        return len(self.table)-1

    def entry_by_id(self, id_: int) -> List[object]:
        """
        Get curtain row
        :param id_: row number
        :type id_: int
        :return: entry with given id_ (row)
        :rtype:
        """
        return self.table[id_]

    def entry_by_value(self, value, column) -> List[object]:
        """
        Returns entry that has value in certain column (or column id, if int passed)
        :raises IndexError if search failed
        :raises ValueError if search passed column does not exist
        :param value: search for
        :type value:
        :param column: column in which to search (or col_id if int is passed)
        :type column:
        :return: first entry found
        :rtype: List[object]
        """
        if type(column) is not int:
            column = self.entry_format.index(column)

        # TODO: rewrite
        for entry in self:
            if entry[column] == value:
                return entry
        raise IndexError

    def entries_by_value(self, value, column) -> List[List[object]]:
        """
        Get all entries that match given value in given column.
        If type of column is int, it is interpreted as row id.
        :raises IndexError if such entries do not exist.
        :raises ValueError if such column does not exist.
        :param value: search for
        :type value:
        :param column: column in which to search for
        :type column:
        :return: list of entries that match given value in given column
        :rtype: List[List[object]]
        """
        output = []

        if type(column) is not int:
            column = self.entry_format.index(column)

        # TODO: rewrite for loop
        for entry in self:
            if entry[column] == value:
                output.append(entry)

        if len(output) != 0:
            return output

        raise IndexError

    def change_cell_value(self, entries: List, column, new_val):
        """
        Change cell value of one or more entry in a given column to new value.
        :param entries: one or more entry that needs to be changed
        :type entries: List[object] or List[List[objects]]
        :param column: name of the column or column id
        :type column: str or int
        :param new_val: new cell value
        :type new_val:
        :return:
        :rtype:
        """
        if type(column) is not int:
            column = self.entry_format.index(column)

        if type(entries) is not List[List]:
            entries[column] = new_val
        else:
            for entry in entries:
                entry[column] = new_val

    def column(self, column) -> List[object]:
        """
        Get all cells in a given column
        :param column: name of the column or column id
        :type column: str or int
        :return: list of cells
        :rtype: List[object]
        """
        if type(column) is not int:
            column = self.entry_format.index(column)

        output = []
        for entry in self:
            output.append(entry[column])

        return output
