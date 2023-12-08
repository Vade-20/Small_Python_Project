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

def get_direction(x,y):
    if y-1 > 0 : 
        if screen[y-1][x] == '':
            up = False
        else:
            up = True 
    else: 
        up = False
    
    if y+1 < y_screen :
        if screen[y+1][x] == '':
            down = False
        else:
            down = True
    else: 
        down = False
    
    if x-1 > 0 : 
        if screen[y][x-1] == '':
            left = False
        else:
            left = True
    else: 
        left = False
    
    if x+1 < x_screen :
        if screen[y][x+1] == '':
            right = True
        else:
            right = True
    else:
        right = False
    
    return [up,down,left,right]
    
def get_character(x,y,char):
    direction = get_direction(x,y)
    up,down,left,right = direction

    #For 3 Directional 
    if False not in direction:
        return CROSS_CHAR
    elif False not in direction[:2]:
        return UP_DOWN_LEFT_CHAR
    elif False not in direction[:1]+[direction[3]]:
        return UP_DOWN_RIGHT_CHAR
    elif False not in direction[1:]:
        return DOWN_LEFT_RIGHT_CHAR
    elif False not in [direction[0]] + direction[2:]:
        return UP_LEFT_RIGHT_CHAR
    elif False not in [up, right]:
        return UP_RIGHT_CHAR
    elif False not in [up, left]:
        return UP_LEFT_CHAR
    elif False not in [down, right]:
        return DOWN_RIGHT_CHAR
    elif False not in [down ,left]:
        return DOWN_RIGHT_CHAR
    else:
        if char in ['w','s']:
            return UP_DOWN_CHAR
        elif char in ['a','d']:
            return LEFT_RIGHT_CHAR
    
@wrapper
def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    curses.curs_set(0)
    
    x,y = 0,0
    stdscr.addstr(y,x,LEFT_RIGHT_CHAR)
    while True:
        try:    
            ch = stdscr.getkey().lower()
            if ch == 'w':
                y -= 1
                if y < 0:
                    y += 1
                    continue
                text = get_character(x,y,ch)
                screen[y][x] = text
                stdscr.addstr(y,x,text)
            
            if ch == 's':
                y += 1
                if y > y_screen-1:
                    y -= 1
                    continue
                text = get_character(x,y,ch)
                screen[y][x] = text
                stdscr.addstr(y,x,text)
                             
            if ch == 'a':
                x -= 1
                if x < 0:
                    x += 1
                    continue
                text = get_character(x,y,ch)
                screen[y][x] = text
                stdscr.addstr(y,x,text)
                    
            if ch == 'd':
                x += 1
                if x > x_screen-1:
                    x -= 1
                    continue
                text = get_character(x,y,ch)
                screen[y][x] = text
                stdscr.addstr(y,x,text)
                
        except KeyboardInterrupt:
            break
