import curses
from curses import wrapper
from shutil import get_terminal_size
from time import sleep

x_terminal,y_terminal = get_terminal_size()
PAUSE = 0.5

BOTTLE = ''' ||
 )(
|__|
|  |
|__|'''

@wrapper
def main(stdsrc):
    TOTAL_BOTTLES = 99
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    GREEN = curses.color_pair(1)
    YELLOW = curses.color_pair(2)
    adjust_y = 0
    try:
        while TOTAL_BOTTLES>0:
            stdsrc.clear()
            stdsrc.refresh()
            total_bottles = TOTAL_BOTTLES
            
            for i in range(0,25,6):
                for j in range(0,120,5):
                        cur_new = curses.newwin(5,5,i,j)
                        cur_new.addstr(BOTTLE,YELLOW)
                        cur_new.refresh()
                        total_bottles -= 1
                        if total_bottles < 0:
                            break
                if total_bottles<0:
                    break
                stdsrc.addstr(i+5,0,'-'*(x_terminal-1)+'\n')
                stdsrc.refresh()
            if TOTAL_BOTTLES<96:
                adjust_y = 20    
            stdsrc.addstr(24,21-adjust_y,f'{TOTAL_BOTTLES} bottles of milk on the wall,',GREEN)
            stdsrc.refresh()
            sleep(PAUSE)
            
            stdsrc.addstr(25,21-adjust_y,f"{TOTAL_BOTTLES} bottles of milk",GREEN)
            stdsrc.refresh()
            sleep(PAUSE)
            
            stdsrc.addstr(26,21-adjust_y,'Take one down, pass it around',GREEN)
            stdsrc.refresh()
            sleep(PAUSE)
            
            stdsrc.addstr(27,21-adjust_y,f'{TOTAL_BOTTLES-1} bottles of milk on the wall!',GREEN)
            stdsrc.refresh()
            sleep(PAUSE)
            
            TOTAL_BOTTLES -= 1
            
    except KeyboardInterrupt:
        quit()
            
        