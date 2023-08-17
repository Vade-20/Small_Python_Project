import curses
from curses import wrapper
import random
import time


def get_colours(col_num):        
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
    return curses.color_pair(col_num)


def seaweed(stdsrc):
    seaweed_1 = curses.newwin(20,1,11,5)
    s = ''
    for i in range(1,20):
        rand = random.choice(['(',')'])
        s += rand
    seaweed_1.addstr(s,get_colours(4))
    seaweed_1.refresh()
    time.sleep(1)
    
@wrapper
def tank(stdsrc):
    curses.curs_set(0)
    stdsrc.clear()
    stdsrc.refresh()
    y,x = 30,120
    ground = curses.newwin(2,120,28,0)
    ground.addstr('░'*119+' '+'░'*119,get_colours(1))
    ground.refresh()

    stdsrc.getch()
