import random
import curses
from curses import wrapper

NUM_OF_ROWS = 4
NUM_OF_COLS = 4

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
    rules = f'''
RULES OF 2048 ~
Certainly, here are the rules of the game 2048 presented in bullet points:

- **Objective**: The goal of 2048 is to reach the tile with the number 2048 by sliding and combining numbered tiles on a 4x4 grid.

- **Starting Grid**: The game starts with a {NUM_OF_ROWS}x{NUM_OF_COLS} grid that contains two tiles, each with the number 2.

- **Tile Movement**: You can move tiles in four directions: up, down, left, and right using WASD keys.

- **Tile Combining**: When two tiles with the same number collide while moving in a direction, they merge into one tile with a number that is the sum of the two original tiles. For example, two tiles with '2' will merge into one tile with '4'.

- **Random Tile Generation**: After each move, a new tile with a value of 2 or 4 appears on the grid at a random empty spot.

- **Winning**: You win the game when you create a tile with the number 2048 by merging tiles. 

- **Losing**: The game ends when the grid is full.

- **Scoring**: Your score is calculated based on the value of the tiles you combine. Each merge adds the value of the merged tiles to your score. For example, merging two '4' tiles would give you 8 points.
 
PRESS ENTER TO  CONTINUE'''

    stdsrc.addstr(5,5,rules,curses.color_pair(1))
    stdsrc.getch()
    stdsrc.clear()
    stdsrc.refresh()

def moves(board,move,stdsrc):
    direction = {'w':up,'s':down,'a':left,'d':right}
    direction.get(move)(board)

                            
@wrapper
def main(stdsrc):
    board = {(i,j):' ' for i in range(NUM_OF_ROWS) for j in range(NUM_OF_COLS)}
    board[random.randint(0,NUM_OF_ROWS-1),random.randint(0,NUM_OF_COLS-1)] = '2'
    board[random.randint(0,NUM_OF_ROWS-1),random.randint(0,NUM_OF_COLS-1)] = '2'
    
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.echo()
    stdsrc.clear()
    stdsrc.refresh()
    
    rules(stdsrc)
    while True:
        losing = [int(board.get(i)) for i in board if board[i]!=' ']
        if 2048 in losing:
            stdsrc.clear()
            stdsrc.addstr(10,10,"YOU WIN!!!!!!!!!!!!!!!!",curses.color_pair(1))
            stdsrc.addstr(12,10,f"Your score is {sum(losing)}",curses.color_pair(1))
            stdsrc.addstr(14,10,"Press enter to exit",curses.color_pair(1))
            stdsrc.getch()
            quit()
            
        if len(losing)>=NUM_OF_COLS*NUM_OF_ROWS:
            stdsrc.clear()
            stdsrc.addstr(10,10,"GAME OVER YOU LOSE!!!!!!!!!!!!!!!!",curses.color_pair(1))
            stdsrc.addstr(12,10,f"Your score is {sum(losing)}",curses.color_pair(1))
            stdsrc.addstr(14,10,"Press enter to exit",curses.color_pair(1))
            stdsrc.getch()
            quit()
            
        get_board(stdsrc,board)
        stdsrc.addstr(f'Your score:{sum(losing)}\nEnter move: (WASD or Q to quit) : ',curses.color_pair(1))
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
                if random.randint(1,100)<81:
                    board[(row_,col_)] = '2'
                else:
                    board[(row_,col_)] = '4'
                break
        
