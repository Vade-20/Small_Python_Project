import curses
import random
from curses import wrapper,rectangle

def get_colours(a):
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
        
        COLORS = {
        'Y' : curses.color_pair(1),
        'R' : curses.color_pair(2),
        'B' : curses.color_pair(3),
        'G' : curses.color_pair(4),
        'M' : curses.color_pair(5),
        'C' : curses.color_pair(6),}
        return COLORS.get(a)

@wrapper
def main(stdsrc):
    stdsrc.clear()
    stdsrc.refresh()
    stdsrc.addstr(0,0,''' Rules ~
Set the upper left color/shape, which fills in all the adjacent squares of that color/shape. 
Try to make the entire board the same color/shape.''',get_colours('G'))
    stdsrc.getch()
    