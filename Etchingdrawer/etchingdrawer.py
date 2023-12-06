import curses
from curses import wrapper
from shutil import get_terminal_size
from pprint import pprint

x_screen,y_screen = get_terminal_size()
screen = [['' for i in range(x_screen)] for j in range(y_screen)]
UP_DOWN_CHAR         = chr(9474)  # Character 9474 is '│'
LEFT_RIGHT_CHAR      = chr(9472)  # Character 9472 is '─'
DOWN_RIGHT_CHAR      = chr(9484)  # Character 9484 is '┌'
DOWN_LEFT_CHAR       = chr(9488)  # Character 9488 is '┐'
UP_RIGHT_CHAR        = chr(9492)  # Character 9492 is '└'
UP_LEFT_CHAR         = chr(9496)  # Character 9496 is '┘'
UP_DOWN_RIGHT_CHAR   = chr(9500)  # Character 9500 is '├'
UP_DOWN_LEFT_CHAR    = chr(9508)  # Character 9508 is '┤'
DOWN_LEFT_RIGHT_CHAR = chr(9516)  # Character 9516 is '┬'
UP_LEFT_RIGHT_CHAR   = chr(9524)  # Character 9524 is '┴'
CROSS_CHAR           = chr(9532)  # Character 9532 is '┼'
        
@wrapper
def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(0)
    
    x,y = 0,0
    stdscr.addstr(y,x,'-')
    while True:
        try:    
            try:
                ch = stdscr.getkey()
            except curses.error:
                ch = None
            if ch == 'KEY_LEFT':
                screen[y][x] = '_'
                x -= 1
                stdscr.addstr(y,x,'_')
            elif ch == 'KEY_RIGHT':
                screen[y][x] = '_'
                x += 1
                stdscr.addstr(y,x,'_')
            elif ch == 'KEY_UP':
                screen[y][x] = '|'
                y -= 1
                stdscr.addstr(y,x,'|')
            elif ch == 'KEY_DOWN':
                screen[y][x] = '|'
                y += 1
                stdscr.addstr(y,x,'|')
        except KeyboardInterrupt:
            print(screen)
            break
