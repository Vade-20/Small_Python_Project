import curses
import random
from curses import wrapper
from curses.textpad import rectangle

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
        'P' : curses.color_pair(5),
        'C' : curses.color_pair(6),}
        return COLORS.get(a)

BORDER_WIDTH = 20  # max width 115
BORDER_HEIGHT = 20 # max height 25
BLOCK = chr(9608)
chances = 30

def main_screen(stdsrc):
    pass

@wrapper
def main(stdsrc):
    stdsrc.clear()
    stdsrc.refresh()
    curses.echo()
    blocks = [(i,j,random.choice(['Y', 'R', 'B', 'G', 'P', 'C'])) for i in range(5,BORDER_HEIGHT) for j in range(2,BORDER_WIDTH)]
    while chances!=0:
        stdsrc.addstr(0,0,''' Rules ~
    Set the upper left color/shape, which fills in all the adjacent squares of that color/shape. 
    Try to make the entire board the same color/shape.\n\n\n>''',curses.A_BOLD)
        rectangle(stdsrc,4,1,BORDER_HEIGHT,BORDER_WIDTH)
        for i in blocks:
            stdsrc.addstr(i[0],i[1],BLOCK,get_colours(i[2]))
        same_color_block = [blocks[0]]
        stdsrc.addstr(BORDER_HEIGHT+1,1,f'Choose one of')
        stdsrc.addstr(' (R)ed',get_colours('R'))
        stdsrc.addstr(' (Y)ellow',get_colours('Y'))
        stdsrc.addstr(' (B)lue',get_colours('B'))
        stdsrc.addstr(' (G)reen',get_colours('G'))
        stdsrc.addstr(' (P)urple',get_colours('P'))
        stdsrc.addstr(' (C)yan',get_colours('C'))
        stdsrc.addstr(' (Q)uit : ')
        ans = stdsrc.getstr().decode(encoding='utf-8')
        break
    print(ans)    
    stdsrc.getch()
    