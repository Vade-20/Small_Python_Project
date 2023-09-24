import random 
import shutil
from time import sleep

x_max,y_max = shutil.get_terminal_size()
DUCK_DENSITY = 0.05
duck_position = [None for _ in range(x_max//6)]

print("\033[33m")
print('Duckling')
print('Press CTRL+C to exit\n')

def get_duck(index):
    global duck_position
    duck = []
    size = random.randint(2,3)
    eyes = random.choice(['``',"''",'^^','""','**'])
    wing = random.choice(['^','<','>','v'])
    mouth = random.choice(['<','='])
    optional_space = ' '*(3-size)
    space = ' '
    if random.randint(0,1) == 1:
        face = space+'('
        face = face + eyes + mouth + space
        duck.append(face) # back_head + space depending on the size of the duck+eyes+mouth
        #body
        body = '(' + wing +space*(size-1)+')'+ space + optional_space
        duck.append(body)
        #legs  
        legs = space+f"^{space*(size-2)}^"+ space*2 + optional_space 
        duck.append(legs)
    else:
        #face
        face = mouth+eyes+')'+space*2
        duck.append(face)
        #body
        body =  space+'('+space*(size-1)+wing+')'+optional_space
        duck.append(body)
        #legs
        legs = space*2+f"^{space*(size-2)}^"+space+optional_space
        duck.append(legs) 
    duck.append(' '*6)
    duck_position[index] = duck


while True:
    try :
        for i in range(len(duck_position)):
            if duck_position[i] == None and random.random()<DUCK_DENSITY:
                get_duck(i)
                
        for i in range(len(duck_position)):
            if duck_position[i] != None:
                duck = duck_position[i].pop(0)
                print(duck,end='',flush=True)
                if duck_position[i] == []:
                    duck_position[i] = None
            else:
                print(' '*6,end='',flush=True)
        
        print('')             
        sleep(0.2)
        
    except KeyboardInterrupt:
        print("\nThank you")
        print("\033[0m")
        break    
