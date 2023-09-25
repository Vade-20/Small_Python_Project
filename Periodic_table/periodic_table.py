import csv
f = open('Mini_python_project\Periodic_table\periodictable.csv', 'r',encoding='utf-8')
ALL_COLUMNS = ['Atomic Number', 'Symbol', 'Element', 'Origin of name',
               'Group', 'Period', 'Atomic weight', 'Density',
               'Melting point', 'Boiling point',
               'Specific heat capacity', 'Electronegativity',
               'Abundance in earth\'s crust']

elements = list(csv.reader(f))
for i in elements:
    print(i)