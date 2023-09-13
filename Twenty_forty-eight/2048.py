import random
import curses
from curses import wrapper
from time import sleep
from pprint import pprint
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
        curses.init_pair(8, curses.COLOR_RED,curses.COLOR_WHITE)
        curses.init_pair(9, curses.COLOR_BLUE, curses.COLOR_WHITE)
        curses.init_pair(10, curses.COLOR_GREEN, curses.COLOR_WHITE)
        curses.init_pair(11, curses.COLOR_WHITE,curses.COLOR_RED)

        
        colors ={'2': curses.color_pair(7)
                ,'4':curses.color_pair(2)
                ,'8':curses.color_pair(3)
                ,'16':curses.color_pair(6)
                ,'32':curses.color_pair(4)
                ,'64':curses.color_pair(5)
                ,'128':curses.color_pair(1)
                ,'256':curses.color_pair(8)
                ,'512':curses.color_pair(9)
                ,'1024':curses.color_pair(10)
                ,'2048':curses.color_pair(11)}
        return colors.get(a)

def get_board(stdsrc,board):
    stdsrc.clear()
    stdsrc.refresh()
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

def moves(board,move,stdsrc):
    step = 1
    for i in range(NUM_OF_ROWS):
        for j in range(NUM_OF_COLS):
            if board.get((i,j))!=' ':
                num_u = 1
                num_l = 0
                if move =='w': 
                    while True:
                        if board.get((i-num_u,j))==' ':
                            board[(i-num_u,j)] = board[(i-num_l,j)]
                            board[(i-num_l,j)] = ' '
                            num_u += 1
                            num_l += 1
                            stdsrc.refresh()
                            continue
                        elif board.get((i-num_u,j))==board[(i-num_l,j)]:
                            board[(i-num_u,j)] = str(2*int( board[(i-num_u,j)]))
                            board[(i-num_l,j)] = ' '
                        break
                if move =='s': 
                    while True:
                        if board.get((i+num_u,j))==' ':
                            board[(i+num_u,j)] = board[(i+num_l,j)]
                            board[(i+num_l,j)] = ' '
                            num_u += 1
                            num_l += 1
                            stdsrc.refresh()
                            continue
                        elif board.get((i+num_u,j))==board[(i+num_l,j)]:
                            board[(i+num_u,j)] = str(2*int( board[(i+num_u,j)]))
                            board[(i+num_l,j)] = ' '
                        break
                if move =='d': 
                    while True:
                        if board.get((i,j+num_u))==' ':
                            board[(i,j+num_u)] = board[(i,j+num_l)]
                            board[(i,j+num_l)] = ' '
                            num_u += 1
                            num_l += 1
                            stdsrc.refresh()
                            continue
                        elif board.get((i,j+num_u))==board.get((i,j+num_l)):
                            board[(i,j+num_u)] = str(2*int( board[(i,j+num_u)]))
                            board[(i,j+num_l)] = ' '
                        break
                if move =='a': 
                    while True:
                        if board.get((i,j-num_u))==' ':
                            board[(i,j-num_u)] = board[(i,j-num_l)]
                            board[(i,j-num_l)] = ' '
                            num_u += 1
                            num_l += 1
                            stdsrc.refresh()
                            continue
                        elif board.get((i,j-num_u))==board.get((i,j-num_l)):
                            board[(i,j-num_u)] = str(2*int( board[(i,j-num_u)]))
                            board[(i,j-num_l)] = ' '
                        break

                            
@wrapper
def main(stdsrc):
    board = {(i,j):' ' for i in range(NUM_OF_ROWS) for j in range(NUM_OF_COLS)}
    pprint(board)
    board[random.randint(0,NUM_OF_ROWS-1),random.randint(0,NUM_OF_COLS-1)] = '2'
    board[random.randint(0,NUM_OF_ROWS-1),random.randint(0,NUM_OF_COLS-1)] = '2'
    curses.echo()
    stdsrc.clear()
    stdsrc.refresh()
    rules(stdsrc)
    while True:
        get_board(stdsrc,board)
        stdsrc.addstr('Enter move: (WASD or Q to quit) : ',get_colours('128'))
        ans = stdsrc.getstr().decode(encoding='utf-8')
        if ans.lower() not in ['w','a','s','d','q']:
            continue
        elif ans.lower()=='q':
            quit()
        moves(board,ans,stdsrc)
        while True:
            row_ = random.randint(0,NUM_OF_ROWS-1)
            col_ = random.randint(0,NUM_OF_COLS-1)
            if board.get((row_,col_))==' ':
                board[(row_,col_)] = '2'
                break
        
    stdsrc.getch()