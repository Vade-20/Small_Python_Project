from multiprocessing import Process, Value
import curses
from curses import wrapper
from random import randint,choice,shuffle
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

All_dices = [D1, D1, D2a, D2b, D3a, D3b, D4, D4, D5, D5, D6a, D6b]
shuffle(All_dices)
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
        if x in range(position[0]-15,position[2]+15) and y in range(position[1]-11,position[3]+11):

                return False
        else:
                return True
        
def main(stdsrc,total_question,correct_answer,incorrect_answer,score):
    curses.echo()
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
        # below loop is for printing dices
        for i in dices:
                while True:
                        x,y = randint(0,110),randint(0,23) 
                        for j in positions:
                                if not dice_position(x,y,j):
                                        useless = 1
                                        break
                        else:
                                useless = 0
                        if useless == 1 :
                                continue
                        else:
                                break
                for j in i:
                        stdsrc.addstr(y,x,j)
                        y+=1
                positions.append((x,y,x+9,y+5)) #(topleft,bottomright)
        stdsrc.addstr(29,3,'Enter the sum')
        stdsrc.refresh()
        ans = stdsrc.getstr(29,18).decode(encoding='utf-8') 
        total_question.value += 1
        ans = int(ans) if ans.isdigit() else ans
        if ans == sum_total:
                correct_answer.value+=1
                score.value += 4
        else:
                incorrect_answer.value+=1
                score.value -=  1
        stdsrc.clear()
        stdsrc.refresh()    


if __name__ == '__main__':
        total_question = Value('i', 0)
        correct_answer = Value('i', 0)
        incorrect_answer = Value('i', 0)
        score  = Value('i', 0)
        process = Process(target=wrapper,args=(main,total_question,correct_answer,incorrect_answer,score))
        process.start()
        process.join(timeout=Duration_of_game+5)

        if process.is_alive():
                process.terminate()
                process.join()
                print("Times up")
                print('Total question answered :', total_question.value)
                print('Correct answer :', correct_answer.value)
                print('Incorrect answer :', incorrect_answer.value)
                print('Score:', score.value)
                sleep(10) 
                
