from tkinter import *
from random import choice

root = Tk()
root.title('Sudoku')
FONT_COLOR = 'blue'
BACKGROUND_COLOR = 'white'
root.config(bg=BACKGROUND_COLOR)

global l1

def validate_input(value):
    if (value.isdigit() or value=='') and value !='0':
        return True
    else:
        return False

def new_game():
    for i in entry_list:
        for j in i:
            j.config(state='normal')
            j.delete(0,END)
    b1.destroy()
    l1 = Label(root, text='Sudoku', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '40'), bd=3, relief='solid',justify='center')
    l1.grid(row=0, column=0, columnspan=14,sticky=W+E)
   
def animation_of_button(event):
    if 'Enter' in str(event):
        b1.config(fg='black',relief='solid')   
    else:
        b1.config(fg=FONT_COLOR,relief='raised')
            

def winining_condition(event):
    global b1
    box = []
    for entry in entry_list:
        box__= []
        for i in entry:
            value = i.get()
            box__.append(value)
            if len(value) >1:
                i.delete(0,END)
                i.insert(0,value[0])
        box.append(box__)

    if  not len([j for i in box for j in i if j!=''])==81:
        return None
    
    for i in box:
        if not '' in i:
            if len(i) != len(set(i)):
                return None
            
    for i in range(9):
        new_box = [box[j][i] for j in range(9)]
        if not '' in new_box:
            if len(new_box) != len(set(new_box)):
                return None
    
    for i in range(3):
        var_1 = 3*i
        for j in range(3):
            var_2 = 3*j
            new_box = [box[var_1+k][var_2+l] for k in range(3) for l in range(3)]
            if not '' in new_box:
                if len(new_box) != len(set(new_box)):
                    return None     

    for i in entry_list:
        for j in i:
            j.config(state='readonly')
            
    l1.destroy()   
    l = Label(root, text='Congratulation!!!! You Won', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '30'), bd=3, relief='solid',justify='center')
    l.grid(row=0, column=0, columnspan=14,sticky=W+E)     
    b1 = Button(root,text = 'NEW GAME',fg=FONT_COLOR,bg = BACKGROUND_COLOR,font= ('Times New Roman', '15'),command=new_game,width=15,relief='raised',justify='center')
    b1.grid(row=15,column=0,columnspan=14,sticky=W+E)     
    b1.bind('<Enter>',animation_of_button)    
    b1.bind('<Leave>',animation_of_button)    
        
vcmd = (root.register(validate_input), '%P')
entry_list = []

l1 = Label(root, text='Sudoku', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '40'), bd=3, relief='solid',justify='center')
l1.grid(row=0, column=0, columnspan=14,sticky=W+E)
l2 = Label(root, text='      ', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '2'), bd=3, relief='sunken',justify='center')
l2.grid(row=1, column=0, columnspan=14,sticky=W+E)
for i in range(2,14):
    if i in [5,9,13]:
        l_ = Label(root, text='-'*110, fg=FONT_COLOR ,bg=BACKGROUND_COLOR ,font=('Times', '10'), bd=3, relief='flat')
        l_.grid(row=i, column=0, columnspan=14,sticky=W+E)
    else:
        dummy_list = []
        for j in range(2,14):
            if j in [5,9,13]:
                l1 = Label(root, text='|', fg=FONT_COLOR,bg=BACKGROUND_COLOR  ,font=('Times', '10'), bd=3, relief='flat')
                l1.grid(row=i, column=j, sticky=W+E)
            else:
                e1 = Entry(root, fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '10'), bd=3, relief='groove',width=5,justify='center',validate='key',validatecommand=vcmd)
                e1.grid(row=i, column=j)
                dummy_list.append(e1)
        entry_list.append(dummy_list)

pp = [[4,3,5,2,6,9,7,8,1],[6,8,2,5,7,1,4,9,3],[1,9,7,8,3,4,5,6,2],
    [8,2,6,1,9,5,3,4,7],[3,7,4,6,8,2,9,1,5],[9,5,1,7,4,3,6,2,8],
    [5,1,9,3,2,6,8,7,4],[2,4,8,9,5,7,1,3,6],[7,6,3,4,1,8,2,5,'']]

with open(r'Mini_python_project\Sudoku\sudokupuzzles.txt','r') as f:
    puzzles = f.readlines()


puzzle = choice(puzzles).strip()

use_less = 0
for i in range(9):
    for j in range(9):
        value = puzzle[use_less]
        if value != '.':
            entry_list[i][j].insert(0,value)
            entry_list[i][j].config(state='readonly')
        else:
            entry_list[i][j].insert(0,'')
            
        use_less+=1
        
root.bind('<Key>',winining_condition)
    
mainloop()