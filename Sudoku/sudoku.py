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

def instances_left():
    num_of_instances = {}
    for i in entry_list:
        for j in i:
            value = j.get()
            if value != '':
                num_of_instances.setdefault(value,9)
                num_of_instances[value] -= 1
            
    str_num_of_instances = ''
    for i in range(1,10):
        str_num_of_instances += f'{i}:{num_of_instances[str(i)]}    '
        
    instance = Label(root, text=f'{str_num_of_instances}', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '15'), bd=3, relief='solid',justify='center')
    instance.grid(row=15, column=0, columnspan=14,sticky=W+E)     
    
def new_game():
    for i in entry_list:
        for j in i:
            j.config(state='normal')
            j.delete(0,END)
            
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
            
    instances_left()
                  
    l1 = Label(root, text='Sudoku', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '40'), bd=3, relief='solid',justify='center')
    l1.grid(row=0, column=0, columnspan=14,sticky=W+E)
   
   
def animation_of_button(event):
    if 'Enter' in str(event):
        b1.config(fg='black',relief='solid')   
    else:
        b1.config(fg=FONT_COLOR,relief='raised')


def show_row_column(event,box):
    for i in entry_list:
        for j in i:
            if str(j['state']) == 'readonly':
                j.config(readonlybackground='grey94')
            j.config(bg=BACKGROUND_COLOR)
    
    for i in entry_list:
        if box in i:
            for j in i:
                if str(j['state']) == 'readonly':
                    j.config(readonlybackground='light grey')
                j.config(bg='light grey')     
    
    for i in range(9):
        column = [entry_list[j][i] for j in range(9)]
        if box in column:
            for j in column:
                if str(j['state']) == 'readonly':
                    j.config(readonlybackground='light grey')
                j.config(bg='light grey')
                 
                     
def winining_condition(event):
    global b1
    
    instances_left()
    box = []
    for entry in entry_list:
        box__= []
        for i in entry:
            if i['state'] == 'readonly':
                i.config(readonlybackground='grey94')
            i.config(bg=BACKGROUND_COLOR)
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

        
vcmd = (root.register(validate_input), '%P')
entry_list = []

l1 = Label(root, text='Sudoku', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '40'), bd=3, relief='solid',justify='center')
l1.grid(row=0, column=0, columnspan=14,sticky=W+E)
l2 = Label(root, text='      ', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '2'), bd=3, relief='sunken',justify='center')
l2.grid(row=1, column=0, columnspan=14,sticky=W+E)
b1 = Button(root,text = 'NEW GAME',fg=FONT_COLOR,bg = BACKGROUND_COLOR,font= ('Times New Roman', '15'),command=new_game,width=15,relief='raised',justify='center')
b1.grid(row=16,column=0,columnspan=14,sticky=W+E)     
b1.bind('<Enter>',animation_of_button)    
b1.bind('<Leave>',animation_of_button)   
 
for i in range(2,14):
    if i in [5,9,13]:
        l_ = Label(root, text='-'*110, fg=FONT_COLOR ,bg=BACKGROUND_COLOR ,font=('Times', '10'), bd=3, relief='flat')
        l_.grid(row=i, column=0, columnspan=14,sticky=W+E)
    else:
        dummy_list = []
        for j in range(2,14):
            if j in [5,9,13]:
                l__ = Label(root, text='|', fg=FONT_COLOR,bg=BACKGROUND_COLOR  ,font=('Times', '10'), bd=3, relief='flat')
                l__.grid(row=i, column=j, sticky=W+E)
            else:
                e1 = Entry(root, fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '10'), bd=3, relief='groove',width=5,justify='center',validate='key',validatecommand=vcmd)
                e1.grid(row=i, column=j)
                e1.bind('<Button-1>',lambda event,box=e1:show_row_column(event,box))
                dummy_list.append(e1)
        entry_list.append(dummy_list)
        


with open(r'Mini_python_project\Sudoku\sudokupuzzles.txt','r') as f:
    puzzles = f.readlines()

puzzle = choice(puzzles).strip()
num_of_instances = {}
use_less = 0
for i in range(9):
    for j in range(9):
        
        value = puzzle[use_less]
        if value != '.':
            num_of_instances.setdefault(value,9)
            num_of_instances[value] -= 1
            entry_list[i][j].insert(0,value)
            entry_list[i][j].config(state='readonly')
        else:
            entry_list[i][j].insert(0,'')
            
        use_less+=1

str_num_of_instances = ''
for i in range(1,10):
    str_num_of_instances += f'{i}:{num_of_instances[str(i)]}    '
instance = Label(root, text=f'{str_num_of_instances}', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '15'), bd=3, relief='solid',justify='center')
instance.grid(row=15, column=0, columnspan=14,sticky=W+E)     

root.bind('<Key>',winining_condition)
mainloop()