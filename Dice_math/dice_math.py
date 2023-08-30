from multiprocessing import Process
import curses
from curses import wrapper
from random import randint,choice
from time import sleep
D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)

D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)

D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)

All_dices = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]
min_dices = 2
max_dices = 6
Duration_of_game = 30
Win_points = 4
Lose_points = 1


def random_dices():
        num_of_dices = randint(min_dices,max_dices)
        dices = []
        total = 0
        for i in range(num_of_dices):
                rand = choice(All_dices)
                total += rand[1]
                dices.append(rand[0])
        return (dices, total)

def dice_position(x,y,position):
        if x in range(position[0]-9,position[2]+9) or y in range(position[1]-5,position[3]+5):
                return False
        else:
                return True
        
def main(stdsrc):  
    global positions    
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    GREEN = curses.color_pair(1)
    stdsrc.clear()
    stdsrc.refresh()
    stdsrc.addstr(10,20,f'''                     Dice Math
                        Add up the sides of all the dice displayed on the screen. You have
                        {Duration_of_game} seconds to answer as many as possible. You get {Win_points} points for each
                        correct answer and lose {Lose_points} point for each incorrect answer.\n

                                    Press Enter to begin...''',GREEN)
    stdsrc.getch()
    stdsrc.clear()
    stdsrc.refresh()
    while True:
        dices,sum_total = random_dices()
        positions = []
        for i in dices:
                while True:
                        x,y = randint(0,110),randint(0,24)
                        if all([dice_position(x,y,i) for i in positions]):
                                break            
                for j in i:
                        stdsrc.addstr(y,x,j)
                        y+=1
                positions.append((x,y,x+9,y+5)) #(topleft,bottomright)
                        
        stdsrc.refresh()
        stdsrc.getch()
        stdsrc.clear()
        stdsrc.refresh()
        print('-'*100)
        


if __name__ == '__main__':
        process = Process(target=wrapper,args=(main,))
        process.start()
        process.join(timeout=10)

        if process.is_alive():
                print("Process took too long, terminating...")
                process.terminate()
                process.join()
        else:
                print("Process completed successfully.")
