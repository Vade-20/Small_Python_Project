from tkinter import *
import random

root = Tk()
root.title('Tic Tac Toe')
root.geometry('890x600')
BACKGROUND_COLOR = 'light grey'
FONT_COLOR = 'blue'
root.config(bg=BACKGROUND_COLOR)

def new_game():
    pass

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
        
vcmd = (root.register(validate_input_entry), '%P')
board = [['','',''] for i in range(3)]

l1 = Label(root, text='TIC TAC TOE', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '40'), bd=3, relief='solid',justify='center')
l1.grid(row=0, column=0, columnspan=15,sticky=W+E)

l2 = Label(root, text='Game Mode---->', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '12'), bd=3, relief='solid',justify='center')
l2.grid(row=1, column=0,columnspan=2)
mode = StringVar()
options_list = ["Option 1", "Option 2", "Option 3", "Option 4"] 
mode.set('Select a game mode')
o1 = OptionMenu(root,mode,*options_list)
o1.grid(row=1,column=2,columnspan=3) 
o1.config(fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '10'), bd=3, relief='raised',justify='center',width=20)

l3 = Label(root, text=' '*70, fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '15'),justify='center')
l3.grid(row=1, column=6,columnspan=4)

b1 = Button(root,text = 'NEW GAME',fg=FONT_COLOR,bg = BACKGROUND_COLOR,font= ('Times New Roman', '15'),command=new_game,width=15,relief='raised',justify='center')
b1.grid(row=1,column=11,columnspan=3) 
b1.bind('<Enter>',animation_of_button)
b1.bind('<Leave>',animation_of_button)
'''b2 = Button(root,text = 'NEW GAME',fg=FONT_COLOR,bg = BACKGROUND_COLOR,font= ('Times New Roman', '15'),command=game_mode,width=15,relief='raised',justify='center')
b2.grid(row=16,column=0,columnspan=15) 
'''
for i in range(2,18):
    if i in [2,7,12,17]:
        Label(root, text='-'*220, fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '8'), bd=3, relief='flat',justify='center').grid(row=i, column=0, columnspan=15,sticky=W+E)
        if i==17:
            break
        for j in [0,5,10]:
            e1 = Entry(root, fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '50'), bd=3, relief='groove',width=5,justify='center',validate='key',validatecommand=vcmd)
            e1.grid(row=i+1, column=j,columnspan=5,rowspan=5)
    else:
        Label(root, text='|', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '15'), bd=3, relief='flat',justify='center').grid(row=i, column=5)
        Label(root, text='|', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '15'), bd=3, relief='flat',justify='center').grid(row=i, column=9)
    
    

mainloop()