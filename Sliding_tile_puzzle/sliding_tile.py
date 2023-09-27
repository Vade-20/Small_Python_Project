import curses
import random
from curses import wrapper

def rules(stdsrc,color):
    stdsrc.clear()
    stdsrc.refresh()
    stdsrc.addstr(10,30,'''Sliding Tile Puzzle

                            Use the WASD keys to move the tiles
                            back into this original order:
                                1   2   3   4 
                                5   6   7   8
                                9  10  11  12
                                13 14  15
                            Press Enter to begin...''',color)
    stdsrc.getch()
    stdsrc.clear()
    stdsrc.refresh()
    
    
def print_board(stdsrc, board):
    stdsrc.clear()
    final_board = ''
    board_var = 0
    for i in range(4):
        final_board+='+----------'*4+'+\n'
        for j in range(5):
            if j != 2 :
                final_board += '|          '*4+'|\n'
            else:
                for k in range(4):
                    final_board += '|'+f'{board[board_var][k].center(10)}'
                board_var += 1
                final_board += '|\n'
    final_board+='+----------'*4+'+\n'
    stdsrc.addstr(final_board)
    return avaibale_moves(stdsrc,board)


def avaibale_moves(stdsrc,board):
    global empty_space,moves
    moves = ['W','S', 'D', 'A',]
    for i in range(4):
        for j in range(4):
            if board[i][j] ==' ':
                if i==0:moves[1] = ' '
                elif i==3:moves[0] = ' '
                
                if j==0:moves[2] = ' '
                elif j==3:moves[3] = ' '
                empty_space = (i,j)

                break
            
    stdsrc.addstr('\n'+' '*26+f'({moves[0]})\n')
    stdsrc.addstr(f'Enter WASD (or QUIT): ({moves[3]}) ({moves[1]}) ({moves[2]})\n >') 


def playing_the_game(move):
    global board,empty_space,moves
    
    if move=='W' and moves[0]=='W':
        board[empty_space[0]][empty_space[1]] = board[empty_space[0]+1][empty_space[1]]
        board[empty_space[0]+1][empty_space[1]] = ' '
    elif move=='S' and moves[1]=='S':
        board[empty_space[0]][empty_space[1]] = board[empty_space[0]-1][empty_space[1]]
        board[empty_space[0]-1][empty_space[1]] = ' '
    elif move=='D' and moves[2]=='D':
        board[empty_space[0]][empty_space[1]] = board[empty_space[0]][empty_space[1]-1]
        board[empty_space[0]][empty_space[1]-1] = ' '
    elif move=='A' and moves[3]=='A':
        board[empty_space[0]][empty_space[1]] = board[empty_space[0]][empty_space[1]+1]
        board[empty_space[0]][empty_space[1]+1] = ' '
        
        
def win_condition(board):
    win_board = [['1','2','3','4'],
                 ['5','6','7','8'],
                 ['9','10','11','12'],
                 ['13','14','15',' ']]  
    if board == win_board:
        return True
    else:
        return False

        
                    
@wrapper
def main(stdsrc):
    global board
    curses.echo()
    board = [' ']+[str(i) for i in range(1,16)]
    random.shuffle(board)
    board = [[board[0],board[1],board[2],board[3]],
             [board[4],board[5],board[6],board[7]],
             [board[8],board[9],board[10],board[11]],
             [board[12],board[13],board[14],board[15]]]
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN = curses.color_pair(1)
    rules(stdsrc,GREEN)
    while True:
        print_board(stdsrc,board)
        if win_condition(board):
            stdsrc.addstr('Congratulations!!! You won.\nPress Enter to exit.')
            stdsrc.getch()
            quit()
        move = stdsrc.getstr().decode(encoding='utf-8').upper()
        if move =='QUIT':
            print('Thank for playing!')
            quit()
        playing_the_game(move)
            
    