import curses
from curses import wrapper
import random
import time

bub_pov = [[random.randint(0,110),25],[random.randint(0,110),20]]
def get_colours(col_num):        
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
    return curses.color_pair(col_num)


def seaweed():
    sea_weeds = {"seaweed_1": (curses.newwin(19,1,11,5),18),
                "seaweed_2" : (curses.newwin(12,1,18,30),11),
                "seaweed_3" : (curses.newwin(7,1,23,75),6),
                "seaweed_4" : (curses.newwin(25,1,5,95),24)}
  
    for seaweed in sea_weeds:
        s = ''
        for _ in range(sea_weeds[seaweed][1]):
            rand = random.choice(['(',')'])
            s += rand
        sea_weeds[seaweed][0].addstr(s,get_colours(4))
        sea_weeds[seaweed][0].refresh()

def bubles(stdsrc):
    for i in bub_pov:
        stdsrc.addstr(i[1],i[0],' ')
        stdsrc.refresh()
        i[1] -= 1
        stdsrc.addstr(i[1],i[0],'0')
        stdsrc.refresh()
        if i[1]<8:
            stdsrc.addstr(i[1],i[0],' ')
            i[0] = random.randint(0,110)
            i[1] = 28
        
        
     
def ground():
    ground = curses.newwin(2,120,28,0)
    ground.addstr('░'*119+' '+'░'*119,get_colours(1))
    ground.refresh()

@wrapper
def tank(stdsrc):
    curses.curs_set(0)
    stdsrc.clear()
    stdsrc.refresh()
    y,x = 30,120
    while True:
        seaweed()
        ground()
        bubles(stdsrc)
        time.sleep(1)
    stdsrc.getch()
