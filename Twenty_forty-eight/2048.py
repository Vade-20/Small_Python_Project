import random
import curses
from curses import wrapper


NUM_OF_ROWS = 4
NUM_OF_COLS = 4

def get_colours(a):
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(8, curses.COLOR_RED, curses.COLOR_WHITE)
        curses.init_pair(9, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(10, curses.COLOR_CYAN, curses.COLOR_BLACK)

        
        colors ={'2': curses.color_pair(7)
                ,'4':curses.color_pair(2)
                ,'8':curses.color_pair(3)
                ,'16':curses.color_pair(6)
                ,'32':curses.color_pair(4)
                ,'64':curses.color_pair(5)
                ,'128':curses.color_pair(7)
                ,'256':curses.color_pair(9)
                ,'512':curses.color_pair(10)
                ,'1024':curses.color_pair(11)
                ,'2048':curses.color_pair(8)}
        return colors.get(a)

def get_board(stdsrc,board):
    ans = ''
    for i in range(NUM_OF_ROWS):
        ans += '+-------'*NUM_OF_COLS+'+\n'
        ans += '|       '*NUM_OF_COLS+'|\n'
        for j in range(NUM_OF_COLS):
            ans += '|'
            ans += board.get((i,j)).center(7)
        
        ans += '|\n'+'|       '*NUM_OF_COLS+'|\n'
    ans += '+-------'*NUM_OF_COLS+'+\n'
    stdsrc.addstr(ans)
    stdsrc.refresh()            
            
    
def rules(stdsrc):
    rules = '''
Slide all the tiles on the board in one of four directions. Tiles with
like numbers will combine into larger-numbered tiles. A new 2 tile is
added to the board on each move. You win if you can create a 2048 tile.
You lose if the board fills up tiles and there is no more moves left.
Press Enter to begin...    '''
    stdsrc.addstr(5,5,rules,get_colours('128'))
    stdsrc.getch()
    stdsrc.clear()
    stdsrc.refresh()

@wrapper
def main(stdsrc):
    board = {(i,j):' ' for i in range(NUM_OF_ROWS) for j in range(NUM_OF_COLS)}
    stdsrc.clear()
    stdsrc.refresh()
    rules(stdsrc)
    while True:
        get_board(stdsrc,board)
        break
    stdsrc.getch()