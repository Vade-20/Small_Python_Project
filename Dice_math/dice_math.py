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

                
def main(stdsrc):
    sleep(5)
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


if __name__ == '__main__':
        process = Process(target=wrapper(main))
        process.start()
        process.join(timeout=1)

        if process.is_alive():
                print("Process took too long, terminating...")
                quit()
                process.terminate()
                process.join()
        else:
                print("Process completed successfully.")
