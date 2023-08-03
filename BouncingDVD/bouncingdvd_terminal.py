import curses
from curses import wrapper
from time import sleep
from random import randint

def get_colours(a):
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
        return curses.color_pair(a)
@wrapper
def main(stdsrc):
        curses.curs_set(0)
        stdsrc.clear()
        stdsrc.refresh()
        colour = get_colours(2)
        y_max,x_max = stdsrc.getmaxyx()
        x_corr,y_corr= randint(0,x_max-5),randint(0,y_max-5)
        sign_x,sign_y = 1,1
        colour_num =0
        while True:
                y,x = stdsrc.getyx()
                if y>y_max-2:
                        colour_num += 1 
                        sign_y=-1
                elif y<1:
                        colour_num += 1
                        sign_y=1
                if x>x_max-4:
                        colour_num += 1
                        sign_x=-1
                elif x<2:
                        colour_num += 1
                        sign_x=1
                if colour_num==8:
                        colour_num=1
                colour = get_colours(colour_num)
                stdsrc.clear()
                stdsrc.addstr(y_corr,x_corr,'DVD',colour)
                x_corr,y_corr = x_corr+sign_x,y_corr+sign_y
                stdsrc.move(y_corr,x_corr)
                sleep(0.1)
                stdsrc.refresh()  
                                      


        
        