import random 
import shutil
from time import sleep

MAX_DUCK = 90
all_ducks = {}
x_max,y_max = shutil.get_terminal_size()
DESNSITY = 10
    
def get_duck():
    global all_ducks
    
    duck = []
    size = random.randint(2,3)
    if random.randint(0,1)==1:
        #face
        duck.append(' ('+' '*(size-2)+random.choice(['``',"''",'^^','""','**'])+random.choice(['<','='])) # back_head + space depending on the size of the duck+eyes+mouth
        #body
        duck.append(f"({random.choice(['^','<','>','v'])}{' '*(size)})")
        #legs
        duck.append(f" ^{' '*(size-2)}^  ")
    else:
        #face
        duck.append(random.choice(['>','='])+random.choice(['``',"''",'^^','""','**'])+' '*(size-2)+') ')# mouth+eyes+space depending on the size of the duck+back_head
        #body
        duck.append(f"({' '*(size)}{random.choice(['^','<','>','v'])})")
        #legs
        duck.append(f" ^{' '*(size-1)}^ ")
    
    if all_ducks=={}:
        all_ducks[random.randint(0,x_max-11)]=duck
    else:
        while True:
            x_corr = random.randint(0,x_max-11)
            if any([x_corr in range(i,i+11) for i in all_ducks]):
                continue
            else:
                all_ducks[random.randint(0,x_max-11)]=duck
                break
 
while True:
    all_duck_in_ascending_order = {}
    
    if  len(all_ducks)<MAX_DUCK:
        get_duck()
        
    for i in sorted(all_ducks):
        all_duck_in_ascending_order[i] = all_ducks[i]
        
    rough = 0
    for i in range(0,x_max):
        i += rough
        if i==x_max:
            break
        if i in all_duck_in_ascending_order:
            rough+=8
            value = all_ducks[i].pop(0)
            print(value,end='',flush=True)
        else:
            print(' ',end='',flush=True)
    
    for i in all_duck_in_ascending_order:
        if all_ducks[i]==[]:
            all_ducks.pop(i)          
    print('')
    sleep(0.2)
    
