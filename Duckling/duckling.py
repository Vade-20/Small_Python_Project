import curses 
from curses import wrapper
import random 
import shutil


MAX_DUCK = 2
all_ducks = []
x_max,y_max = shutil.get_terminal_size()
    
def get_duck():
    global all_ducks
    
    duck = []
    size = random.randint(2,4)
    if random.randint(0,1)==1:
        #face
        duck.append(' ('+' '*(size-2)+random.choice(['``',"''",'^^','""','**'])+random.choice(['<','='])) # back_head + space depending on the size of the duck+eyes+mouth
        #body
        duck.append(f"({random.choice(['^','<','>','v'])}{' '*(size-1)})")
        #legs
        duck.append(f" ^{' '*(size-2)}^")
    else:
        #face
        duck.append(random.choice(['>','=']))+random.choice(['``',"''",'^^','""','**']+' '*(size-2)+') ')# mouth+eyes+space depending on the size of the duck+back_head
        #body
        duck.append(f"({' '*(size-1)}){random.choice(['^','<','>','v'])}")
        #legs
        duck.append(f" ^{' '*(size-2)}^")
    
    if all_ducks==[]:
        all_ducks.append({(random.ranint(0,x_max-11),random.ranint(0,y_max-4)):duck})
    else:
        while True:
            x_corr = random.ranint(0,x_max-11)
            y_corr = random.ranint(0,y_max-4)
            if any([x_corr in range(i[0],i[0]+11) and y_corr in range(i[1],i[1]+4) for i in all_ducks]):
                continue
            else:
                all_ducks.append({(x_corr,y_corr):duck})
                break
                
                    
@wrapper
def main(stdsrc):
    stdsrc.clear()
    stdsrc.refresh()
    while len(all_ducks)<MAX_DUCK:
        get_duck()
    
    