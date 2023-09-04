import curses
from curses import wrapper
from random import randint
from time import sleep

forest = [[i,j,' '] for i in range(0,29) for j in range(0,119)]
option = ['A','W']
Grow_Chance = 1
Ligtening_Chance = 5
grow_var = [i for i in range(1,Grow_Chance+1)]
light_var = [i for i in range(1,Ligtening_Chance+1)]

@wrapper
def main(stdsrc):
    global forest
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    RED = curses.color_pair(1)
    GREEN = curses.color_pair(2)
    stdsrc.clear()
    stdsrc.refresh()
    stdsrc.addstr(29,5,f'Grow chance : {Grow_Chance}% \t Lightening chance : {Ligtening_Chance}%\n\tPress CTRL+C to QUIT')
    while True:
        try:
            for i in range(len(forest)):
                rand = randint(0,100)
                if forest[i][2] ==' ':
                    if rand in grow_var:
                        forest[i][2] = 'A'
                        stdsrc.addstr(forest[i][0],forest[i][1],forest[i][2],GREEN)
                elif forest[i][2] == 'A':
                    if rand in light_var:
                        forest[i][2] = 'W'
                        stdsrc.addstr(forest[i][0],forest[i][1],forest[i][2],RED)
                elif forest[i][2] == 'W':
                    try:
                        for j in range(-1,2):
                            if forest[i+j][2]=='A':
                                forest[i+j][2] = 'W'
                                stdsrc.addstr(forest[i+j][0],forest[i+j][1],forest[i+j][2],RED)
                        for j in range(-119,130,120):
                            if forest[i+j][2]=='A':
                                forest[i+j][2] = 'W'
                                stdsrc.addstr(forest[i+j][0],forest[i+j][1],forest[i+j][2],RED)
                    except IndexError:
                        pass
                    forest[i][2] = ' '
                    stdsrc.addstr(forest[i][0],forest[i][1],forest[i][2])
            stdsrc.refresh()
            sleep(0.5)
        except KeyboardInterrupt:
            break 