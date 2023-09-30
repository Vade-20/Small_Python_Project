import curses
from curses import wrapper

NUM_OF_COL = 7 # Max 25

PLAYER_TURN = 1 # Only 1 or 2

def rules(stdsrc):
    stdsrc.clear()
    rules = '''
                            Four in a Row
        Two players take turns dropping tiles into one of seven columns, trying
        to make four in a row horizontally, vertically, or diagonally.
        Press any key to continue'''
    
    stdsrc.addstr(rules)
    stdsrc.refresh()
    stdsrc.getch()
    
    
def printing_board(stdsrc,board):
    global PLAYER_TURN
    stdsrc.clear()
    final_board = '    '
    for i in range(1,NUM_OF_COL+1):
        final_board += f'{str(i).ljust(4)}'
    final_board += '\n   +'+'---|'*NUM_OF_COL+'\n'
    
    for i in range(NUM_OF_COL):
        final_board += f'{" ".ljust(3)}|'
        for j in range(NUM_OF_COL):
            final_board += ' '+board[i][j]+' |'        
        final_board += '\n'
    final_board += '   |'+'___|'*NUM_OF_COL+'\n\n'
    
    if PLAYER_TURN == 1:
        final_board += 'Player X, enter a column or QUIT\n >'
    elif PLAYER_TURN == 0:
        final_board += 'Player 0, enter a column or QUIT\n >'
    stdsrc.addstr(final_board)
    stdsrc.refresh()
    
    
def playing_the_game(move):
    global board 
    move  = int(move)-1 
    pos = NUM_OF_COL-1
    while True:
        if board[pos][move] not in ['X','O']:
            if PLAYER_TURN == 1:
                board[pos][move] = 'O'
            elif PLAYER_TURN == 0:
                board[pos][move] = 'X'
        else:
            pos -= 1
            continue
        break


def tie_condition(stdsrc,board):
    not_empty_board = []
    for i in board:
        if i in ['X','O']:
            not_empty_board.append(i)
    
    if len(not_empty_board) == len(board):
        stdsrc.addstr("\nIt's a Tie.\nPress any key to exit.\n")
        stdsrc.getch()
        quit() 
    
    
def win(stdsrc,board):
    x_win = 'XXXX'
    o_win = 'OOOO'
    
    for i in board:
        board_elements = ''.join(i)
        if x_win in board_elements:
            stdsrc.addstr("\nCongratulations X Wins The Game.\nPress any key to exit.\n")
            stdsrc.getch()
            quit()  
        elif o_win in board_elements:
            stdsrc.addstr("\nCongratulations O Wins The Game.\nPress any key to exit.\n")
            stdsrc.getch()
            quit()
               
    for i in range(NUM_OF_COL):
        board_elements = ''
        for j in range(NUM_OF_COL):
            board_elements += board[j][i]
            
        if x_win in board_elements:
            stdsrc.addstr("\nCongratulations X Wins The Game.\nPress any key to exit.\n")
            stdsrc.getch()
            quit()       
        elif o_win in board_elements:
            stdsrc.addstr("\nCongratulations O Wins The Game.\nPress any key to exit.\n")
            stdsrc.getch()
            quit()
            
            
    board_tan45 = []    
    for i in range(NUM_OF_COL):
        rough_var = 0
        board_elements = ''
        i += 1
        while i != 0 :
            i -= 1
            board_elements += board[rough_var][i]
            rough_var += 1
        board_tan45.append(board_elements)    
        if x_win in board_elements:
            stdsrc.addstr("\nCongratulations X Wins The Game.\nPress any key to exit.\n")
            stdsrc.getch()
            quit()  
        elif o_win in board_elements:
            stdsrc.addstr("\nCongratulations O Wins The Game.\nPress any key to exit.\n")
            stdsrc.getch()
            quit()

    for i in range(1,NUM_OF_COL):
        rough_var = NUM_OF_COL-1
        board_elements = ''
        while i != NUM_OF_COL:
            board_elements += board[i][rough_var]
            i += 1
            rough_var -= 1
        board_tan45.append(board_elements)
        if x_win in board_elements:
            stdsrc.addstr("\nCongratulations X Wins The Game.\nPress any key to exit.\n")
            stdsrc.getch()
            quit()  
        elif o_win in board_elements:
            stdsrc.addstr("\nCongratulations O Wins The Game.\nPress any key to exit.\n")
            stdsrc.getch()
            quit()
                   
            
    board_tan135 = []        
    for i in range(NUM_OF_COL-1,-1,-1):
        rough_var = 0
        board_elements = ''
        while i != NUM_OF_COL :
            board_elements += board[i][rough_var]
            i += 1
            rough_var += 1
            
        board_tan135.append(board_elements)   
        if x_win in board_elements:
            stdsrc.addstr("\nCongratulations X Wins The Game.\nPress any key to exit.\n")
            stdsrc.getch()
            quit()  
        elif o_win in board_elements:
            stdsrc.addstr("\nCongratulations O Wins The Game.\nPress any key to exit.\n")
            stdsrc.getch()
            quit()
            

    for i in range(1,NUM_OF_COL):
        rough_var = 1
        board_elements = ''
        while i != NUM_OF_COL:
            board_elements += board[rough_var][i]
            i += 1
            rough_var += 1
        board_tan135.append(board_elements)
        if x_win in board_elements:
            stdsrc.addstr("\nCongratulations X Wins The Game.\nPress any key to exit.\n")
            stdsrc.getch()
            quit()  
        elif o_win in board_elements:
            stdsrc.addstr("\nCongratulations O Wins The Game.\nPress any key to exit.\n")
            quit()
    
          
@wrapper
def main(stdsrc):
    global board,PLAYER_TURN
    curses.echo()
    board = [['-' for j in range(NUM_OF_COL)] for i in range(NUM_OF_COL)]
    rules(stdsrc)
    
    while True:
        printing_board(stdsrc,board)
        win(stdsrc,board)
        tie_condition(stdsrc,board)
        move = stdsrc.getstr().decode(encoding='utf-8')
        if not move.isdigit():
            continue
        elif int(move) not in range(1,NUM_OF_COL+1):
            continue
        
        PLAYER_TURN = 0 if PLAYER_TURN == 1 else 1
        playing_the_game(move)

        