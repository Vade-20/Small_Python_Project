from tkinter import *
import random
from math import inf as infinity

root = Tk()
root.title('Tic Tac Toe')
root.geometry('890x600')
BACKGROUND_COLOR = 'light blue'
FONT_COLOR = 'crimson'
READONLY_COLOR_BG = 'light blue'
READONLY_COLOR_FG = 'red'
max_player = 'X' 
num_of_turn = 0

root.config(bg=BACKGROUND_COLOR)
root.resizable(False,False)

def new_game(event=None):
    # State a new game of tic tac toe
    global turn
    l1 = Label(root, text='TIC TAC TOE', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '40'), bd=3, relief='solid',justify='center')
    l1.grid(row=0, column=0, columnspan=15,sticky=W+E)
    turn = False
    for i in boxes:
        for j in i:
            j.config(state='normal')
            j.delete(0,END)
    text = players[mode.get()][turn]
    l3 = Label(root, text=text, fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '15'),justify='center')
    l3.grid(row=1, column=6,columnspan=4)
    
def animation_of_button(event):
    #When the mouse hover over the button the button color and font changes
    if 'Enter' in str(event):
        b1.config(fg='black',relief='solid',bg='grey94')   
    else:
        b1.config(fg=FONT_COLOR,relief='raised',bg=BACKGROUND_COLOR)


def validate_input_entry(value):
    # check if the value is valid for the game
    if turn is False and value == 'X':
        return True
    elif turn is True and value == 'O':
        return True
    elif value == '':
        return True
    else:       
        return False
    

def wining_condition(board):
    # check if the somebody won the game or if it is a tie
    for i in range(0,9,3):
        if (board[i] == board[i+1] == board[i+2] ) and board[i] != '':
            return board[i]
    
    for i in range(0,3):
        if (board[i] == board[i+3] == board[i+6] ) and board[i] != '':
            return board[i]
    
    if (board[0] == board[4] == board[8] ) and board[4] != '':
            return board[4]
        
    if (board[2] == board[4] == board[6] ) and board[4] != '':
            return board[4]
        
    if '' not in board:
        return 'Tie'
    
    return False


def minimax(state, num_empty_squares, turn):

    player = 'X' if turn is True else 'O' 
    if player == 'O':
        best = [-1, -infinity]
    else:
        best = [-1, +infinity]

    win = wining_condition(state)
    if num_empty_squares == 0 or win != False:
        if win == 'O':
            score = 1
        elif win == 'X':
            score = -1
        elif win == 'Tie':
            score = 0
        return [-1, score]

    for position,possible_move in enumerate(state):
        if possible_move != '':
            continue
        state[position] = player
        score = minimax(state, num_empty_squares - 1, not turn)
        state[position] = ''
        score[0] = position

        if player == 'O':
            if score[1] > best[1]:
                best = score  # max value
        else:
            if score[1] < best[1]:
                best = score  # min value

    return best


def remove_empty_boxes():
    for i in boxes:
        for j in i:
            if j.get() == '' and j['state']=='disabled':
                j.config(state='normal')
                           
def adding_turn(event,box):
    if turn is False:
        game_play('X',box)
    else:
        game_play('O',box)
        
def game_play(value,box):
    global l3,turn,num_of_turn
    
    if value not in ['X','O']:
        value_1 = value.char.upper()
    else:
        value_1 = value 
    
    box.insert(0,value_1)
    box.config(state='disabled')
    num_of_turn += 1
    
    if not validate_input_entry(value_1):
        return None
    # Changes the label to show which player/computer turn it is
    l3.destroy()
    text = players[mode.get()][turn]
    l3 = Label(root, text=text, fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '15'),justify='center')
    l3.grid(row=1, column=6,columnspan=4)
    
    if mode.get() =='Computer Easy':
        turn = not turn
        while True:
            num_of_empty_spaces_left = len(['' for i in boxes for j in i if j.get()==''])
            if num_of_empty_spaces_left==0:
                break           #No empty spaces is left,it is a tie
            rand = boxes[random.randint(0,2)][random.randint(0,2)]
            if rand.get() == '':
                rand.insert(0,"O")
                rand.config(state='disabled')
                break
    elif mode.get() =='Computer Hard':
        turn = not turn
        num_empty_squares = len(['' for i in boxes for j in i if j.get() == ''])
        ans = minimax([j.get() for i in boxes for j in i],num_empty_squares,False)
        box = boxes[ans[0]//3][ans[0]%3]
        box.insert(0,"O")
        box.config(state='disabled')

    
    turn = not turn      
    win = wining_condition([j.get() for i in boxes for j in i])
    if win == 'Tie':
        for i in boxes:
            for j in i:
                j.config(state='disabled')
        l1 = Label(root, text=f"It's a Tie ", fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '40'), bd=3, relief='solid',justify='center')
        l1.grid(row=0, column=0, columnspan=15,sticky=W+E)
        
    elif win is not False:
        for i in  boxes:
            for j in i:
                j.config(state='disabled')
        num = 0 if win == 'X' else 1
        l1 = Label(root, text=f'Congratulation {players[mode.get()][num]} won the game', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '40'), bd=3, relief='solid',justify='center')
        l1.grid(row=0, column=0, columnspan=15,sticky=W+E)


vcmd = (root.register(validate_input_entry), '%P')
boxes = []
players = {'PvP':('Player 1', 'Player 2'),"Computer Easy":('Player', 'Computer'),"Computer Hard":('Player', 'Computer'),"Computer Impossible":('Player', 'Computer')}
turn = False

l1 = Label(root, text='TIC TAC TOE', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '40'), bd=3, relief='solid',justify='center')
l1.grid(row=0, column=0, columnspan=15,sticky=W+E)

l2 = Label(root, text='Game Mode---->', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '12'), bd=3, relief='solid',justify='center')
l2.grid(row=1, column=0,columnspan=2)
mode = StringVar()
options_list = ["PvP", "Computer Easy", "Computer Hard","Computer Impossible"] 
mode.set('Computer Hard')
o1 = OptionMenu(root,mode,*options_list,command=new_game)
o1.grid(row=1,column=2,columnspan=3) 
o1.config(fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '10'), bd=3, relief='raised',justify='center',width=20)

text = players[mode.get()][turn]
l3 = Label(root, text=text, fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '15'),justify='center')
l3.grid(row=1, column=6,columnspan=4)

b1 = Button(root,text = 'NEW GAME',fg=FONT_COLOR,bg = BACKGROUND_COLOR,font= ('Times New Roman', '15'),command=new_game,width=15,relief='raised',justify='center')
b1.grid(row=1,column=11,columnspan=3) 
b1.bind('<Enter>',animation_of_button)
b1.bind('<Leave>',animation_of_button)


for i in range(2,18):
    if i in [2,7,12,17]:
        Label(root, text='-'*220, fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '8'), bd=3, relief='flat',justify='center').grid(row=i, column=0, columnspan=15,sticky=W+E)
        if i==17:
            break
        box__ = []
        for j in [0,5,10]:
            e1 = Entry(root, fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '50'), bd=3, relief='groove',width=5,justify='center',
                       validate='key',validatecommand=vcmd,disabledbackground=READONLY_COLOR_BG,disabledforeground=READONLY_COLOR_FG)
            e1.grid(row=i+1, column=j,columnspan=5,rowspan=5)
            box__.append(e1)
            e1.bind('<Key>',lambda event,box=e1:game_play(event,box))
            e1.bind('<Button-1>',lambda event,box=e1:adding_turn(event,box))
        boxes.append(box__)
    else:
        Label(root, text='|', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '15'), bd=3, relief='flat',justify='center').grid(row=i, column=5)
        Label(root, text='|', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '15'), bd=3, relief='flat',justify='center').grid(row=i, column=9)
    
mainloop()
'''    elif mode.get() == "Computer Impossible":
        turn = not turn
        if num_of_turn == 1:
            for i in [boxes[0][0],boxes[0][2],boxes[2][0],boxes[2][2]]:
                if i.get() == 'X':
                    box = boxes[1][1]
                    box.insert(0,"O")
                    box.config(state='disabled')
        else:
            ans = minimax([j.get() for i in boxes for j in i],False)
            if ans['position'] is not None:
                box = boxes[ans['position']//3][ans['position']%3]
                box.insert(0,"O")
                box.config(state='disabled')'''
