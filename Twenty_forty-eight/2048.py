import random
import curses
from curses import wrapper
from time import sleep
from pprint import pprint
NUM_OF_ROWS = 4
NUM_OF_COLS = 4

def get_colours(a):
    color_codes = {
    '1': "\033[31m",           #red
    '2': "\033[38;5;208m",     #orange
    '3': "\033[33m",           #yellow 
    '4': "\033[32m",           #green
    '5': "\033[34m",           #blue
    '6': "\033[38;5;54m",      #indigo
    '7': "\033[38;5;128m",     #violet
    "reset": "\033[0m"
}
    return color_codes.get(a)

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

def up(board):
    for i in range(NUM_OF_ROWS):
        for j in range(NUM_OF_COLS):
            if board.get((i,j))!=' ':
                num_u = 1
                num_l = 0
                while True:
                    if board.get((i-num_u,j))==' ':
                        board[(i-num_u,j)] = board[(i-num_l,j)]
                        board[(i-num_l,j)] = ' '
                        num_u += 1
                        num_l += 1
                        continue
                    elif board.get((i-num_u,j))==board[(i-num_l,j)]:
                        board[(i-num_u,j)] = str(2*int( board[(i-num_u,j)]))
                        board[(i-num_l,j)] = ' '
                    break   

def down(board):
    for i in range(NUM_OF_ROWS-1,-1,-1):
        for j in range(NUM_OF_COLS-1,-1,-1):
            if board.get((i,j))!=' ':
                num_u = 1
                num_l = 0
                while True:
                    if board.get((i+num_u,j))==' ':
                        board[(i+num_u,j)] = board[(i+num_l,j)]
                        board[(i+num_l,j)] = ' '
                        num_u += 1
                        num_l += 1
                        continue
                    elif board.get((i+num_u,j))==board.get((i+num_l,j)):
                        board[(i+num_u,j)] = str(2*int( board[(i+num_u,j)]))
                        board[(i+num_l,j)] = ' '
                    break

def left(board):
    for j in range(0,NUM_OF_COLS):
        for i in range(0,NUM_OF_ROWS):
            if board.get((i,j))!=' ':
                num_u = 1
                num_l = 0
                while True:
                    if board.get((i,j-num_u))==' ':
                        board[(i,j-num_u)] = board[(i,j-num_l)]
                        board[(i,j-num_l)] = ' '
                        num_u += 1
                        num_l += 1
                        continue
                    elif board.get((i,j-num_u))==board.get((i,j-num_l)):
                        board[(i,j-num_u)] = str(2*int( board[(i,j-num_u)]))
                        board[(i,j-num_l)] = ' '
                    break
                
def right(board):
    for j in range(NUM_OF_COLS-1,-1,-1):
        for i in range(NUM_OF_ROWS-1,-1,-1):
            if board.get((i,j))!=' ':
                num_u = 1
                num_l = 0
                while True:
                    if board.get((i,j+num_u))==' ':
                        board[(i,j+num_u)] = board[(i,j+num_l)]
                        board[(i,j+num_l)] = ' '
                        num_u += 1
                        num_l += 1
                        continue
                    elif board.get((i,j+num_u))==board.get((i,j+num_l)):
                        board[(i,j+num_u)] = str(2*int( board[(i,j+num_u)]))
                        board[(i,j+num_l)] = ' '
                    break
        
    
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
    direction = {'w':up,'s':down,'a':left,'d':right}
    direction.get(move)(board)

                            
@wrapper
def main(stdsrc):
    board = {(i,j):' ' for i in range(NUM_OF_ROWS) for j in range(NUM_OF_COLS)}
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