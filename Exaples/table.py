from Table import Table
import random


table = Table('name', 'age', 'sex')
table.append('Dude', 15, 'M')
table.append('Valya', 19, 'F')
table.append('Igor', 50, 'No')
print()

e = table.entry_by_value('Valya', 'name')
print(f'before: {e}')
table.change_cell_value(e, 'name', 'Julia')
print(f'after: {table.entry_by_id(1)}')
print()


name_pool = ('Ivan', 'Igor', 'Julia', 'Randy', 'Brad')
age_range = (18, 50)
sex_pool = ('F', 'M', '*', '-')

for i in range(15):
    name = random.choice(name_pool)
    sex = random.choice(sex_pool)
    age = random.randint(*age_range)

    table.append(name, age, sex)

print(table)
