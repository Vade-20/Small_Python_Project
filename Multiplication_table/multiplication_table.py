lower_limit = -7
higher_limit = 7

print('|'.rjust(3),end='')
for i in range(lower_limit,higher_limit+1):
    print(f'{i}'.rjust(5),end='')
print('')
print('+'.rjust(3,'-'),end='')
print('-'*5*len(range(lower_limit,higher_limit+1)))

for i in range(lower_limit,higher_limit+1):
    print(f'{i}'.rjust(2),end='|')
    for j in range(lower_limit,higher_limit+1):
        print(f'{i*j}'.rjust(5),end='')
    print()