from table import Table
import random


names = ['Mat', 'Valya', 'Tima', 'Ilya', 'Anton', 'Liza', 'Egor']
statuses = ['+', '-', '0', '=']


t = Table(['name', 'score', 'age', 'status'])

for i in range(15):
	this_name = random.choice(names)
	this_score = random.randrange(0, 15)
	this_age = random.randrange(18, 25)
	this_status = random.choice(statuses)

	t.__add__([this_name, this_score, this_age, this_status])

# print('\n'.join(dir(Table)))

print(t)

print(t.get_entry_by_column_name('status', '='))

# # iteration test:
# for i in t:
#     print(i[0])