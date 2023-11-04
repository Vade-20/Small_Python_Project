from tkinter import *
import random

root = Tk()
root.title('Tic Tac Toe')
root.geometry('890x600')
BACKGROUND_COLOR = 'light grey'
FONT_COLOR = 'blue'
root.config(bg=BACKGROUND_COLOR)

def new_game(event):
    for i in boxes:
        for j in i:
            j.delete(0,END)

def game_mode():
    pass

def animation_of_button(event):
    #When the mouse hover over the button the button color and font changes
    if 'Enter' in str(event):
        b1.config(fg='black',relief='solid',bg='grey94')   
    else:
        b1.config(fg=FONT_COLOR,relief='raised',bg=BACKGROUND_COLOR)

def validate_input_entry(value):
    if value.upper() in ['X','O','']:
        return True
    else:
        return False

def wining_condition():
    values_boxes = []
    for i in boxes:
        values___=[]
        for j in i:
            values___.append(j.get())
        values_boxes.append(values___)
        
    for i in values_boxes:
        set_value = list(set(i))
        if set_value[0] != '' and len(set_value) == 1:
            return set_value[0]
    
    for i in range(3):
        set_value = list(set([values_boxes[j][i] for j in range(3)]))
        if set_value[0] != '' and len(set_value) == 1:
            return set_value[0]
    
    
    set_value = list(set([values_boxes[i][i] for i in range(3)]))           
    if set_value[0] != '' and len(set_value) == 1:
        return set_value[0]

    
    set_value = list(set([values_boxes[0][2],values_boxes[1][1],values_boxes[2][0]]))        
    if set_value[0] != '' and len(set_value) == 1:
        return set_value[0]
    
    return None


def capital_entry(value,box):
    global l3,turn
    value = value.char.upper()
    box.delete(0,END)
    box.insert(0,value)
    if value not in ['X','O']:
        return None
    if mode.get() == 'PvP':
        l3.destroy()
        text = players[mode.get()][turn]
        l3 = Label(root, text=text, fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '15'),justify='center')
        l3.grid(row=1, column=6,columnspan=4)
        turn = not turn
    elif mode.get() =='Computer Easy':
        l3.destroy()
        text = players[mode.get()][turn]
        l3 = Label(root, text=text, fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '15'),justify='center')
        l3.grid(row=1, column=6,columnspan=4)
        while True:
            rand = boxes[random.randint(0,2)][random.randint(0,2)]
            if rand.get() == '':
                rand.delete(0,END)
                rand.insert(0,"O")
                break
            
    win = wining_condition()
    if win is not None:
        for i in boxes:
            for j in i:
                j.config(state='disabled')
        num = 0 if win == 'X' else 1
        l1 = Label(root, text=f'Congratulation {players[mode.get()][num]} won the game', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '40'), bd=3, relief='solid',justify='center')
        l1.grid(row=0, column=0, columnspan=15,sticky=W+E)

    
vcmd = (root.register(validate_input_entry), '%P')
boxes = []
players = {'PvP':('Player 1', 'Player 2'),"Computer Easy":('Player', 'Computer'),"Computer Hard":('Player', 'Computer')}
turn = True

l1 = Label(root, text='TIC TAC TOE', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '40'), bd=3, relief='solid',justify='center')
l1.grid(row=0, column=0, columnspan=15,sticky=W+E)

l2 = Label(root, text='Game Mode---->', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '12'), bd=3, relief='solid',justify='center')
l2.grid(row=1, column=0,columnspan=2)
mode = StringVar()
options_list = ["PvP", "Computer Easy", "Computer Hard"] 
mode.set('PvP')
o1 = OptionMenu(root,mode,*options_list,command=new_game)
o1.grid(row=1,column=2,columnspan=3) 
o1.config(fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '10'), bd=3, relief='raised',justify='center',width=20)

l3 = Label(root, text='Player 1', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '15'),justify='center')
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
            e1 = Entry(root, fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '50'), bd=3, relief='groove',width=5,justify='center',validate='key',validatecommand=vcmd)
            e1.grid(row=i+1, column=j,columnspan=5,rowspan=5)
            box__.append(e1)
            e1.bind('<Key>',lambda event,box=e1:capital_entry(event,box))
        boxes.append(box__)
    else:
        Label(root, text='|', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '15'), bd=3, relief='flat',justify='center').grid(row=i, column=5)
        Label(root, text='|', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '15'), bd=3, relief='flat',justify='center').grid(row=i, column=9)
    

mainloop()
