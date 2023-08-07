from tqdm import tqdm
from random import randint

print('Million Dice Roll Statistics Simulator')
while True:
    try:
        n = int(input('Enter how many six-sided dice you want to roll : '))
    except ValueError:
        continue
    break

num_of_possible_outcomes = {}

for i in tqdm(range(1_000_000),colour='red'):
    rand = 0
    for j in range(1,n+1):
        rand += randint(1,6)
    num_of_possible_outcomes.setdefault(rand,0)
    num_of_possible_outcomes[rand] += 1
    
print('\nTotal\t-\tRolls     \t-\tPercentage')
for i in range(n,n*6+1):
    print(f'{i}\t-\t{num_of_possible_outcomes.get(i,0)} rolls \t-\t{(num_of_possible_outcomes.get(i,0)*100)/1_000_000}%')

    


