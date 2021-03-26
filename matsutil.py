from table import Table

t = Table(['name', 'score'])
t.__add__(['Mat', 1])
t.__add__(['Valya', 2])
t.__add__(['Tima', 3])
t.__add__(['Ilya', 4])
t.__add__(['Mat', 5])
print(t.get_entry_by_column_name('name', 'Mat'))

print(t.__len__())

# print('\n'.join(dir(Table)))
for i in t:
    print(i[0])