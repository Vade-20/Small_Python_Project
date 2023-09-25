import csv,re
f = open('Mini_python_project\Periodic_table\periodictable.csv', 'r',encoding='utf-8')
elements = list(csv.reader(f))

ALL_COLUMNS = ['Atomic Number', 'Symbol', 'Element', 'Origin of name',
               'Group', 'Period', 'Atomic weight', 'Density',
               'Melting point', 'Boiling point',
               'Specific heat capacity', 'Electronegativity',
               'Abundance in earth\'s crust']
ALL_UNITS = ['']*6+[' u',' g/cm^3',' K',' K',' J/(g*K)','',' mg/kg']
print(ALL_UNITS)

print('Periodic Table of Elements\n')
print('''            Periodic Table of Elements
      1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
    1 H                                                  He
    2 Li Be                               B  C  N  O  F  Ne
    3 Na Mg                               Al Si P  S  Cl Ar
    4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
    5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
    6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
    7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

            Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
            Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')

while True:
    print('-'*60)
    ans = input('Enter a symbol or atomic number to examine, or QUIT to quit:').lower().strip()
    print('')
    if ans=='quit':
        quit()
    if ans.isdigit() and ans  in [i[0] for i in elements]:
        for i in elements:
            if ans == i[0]:
                element = i
        for i in range(len(element)):
            print(f"{ALL_COLUMNS[i].rjust(30)} : {element[i]}{ALL_UNITS[i]}")
    elif ans.isalpha() and ans in [i[1].lower() for i in elements]:
        for i in elements:
            if ans == i[1].lower():
                element = i
        for i in range(len(element)):
            element[i] = re.sub(r'\[(I|V|X)+\]', '', element[i])
            print(f"{ALL_COLUMNS[i].rjust(30)} : {element[i]}{ALL_UNITS[i]}")
    else:
        continue
    