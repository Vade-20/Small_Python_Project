from tkinter import *
from random import choice

root = Tk()
root.title('Sudoku')
FONT_COLOR = 'blue'
BACKGROUND_COLOR = 'white'
root.config(bg=BACKGROUND_COLOR)

global l1

def validate_input_entry(value):
    if (value.isdigit() or value=='') and value !='0':
        return True
    else:
        return False


def numbers_on_board():
    # A list that will show the number of numbers on the board
    num_dict = {}
    for i in entry_list:
        for j in i:
            value = j.get()
            if value != '':
                num_dict.setdefault(value,0)
                num_dict[value] += 1
            
    numbers_on_board = 'Numbers\n\n'
    for i in range(1,10):
        numbers_on_board += f'{i}:{num_dict[str(i)]}\n'
        
    instance = Label(root, text=f'{numbers_on_board}', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '15'), bd=3, relief='ridge')
    instance.grid(row=1, column=14, rowspan=13,sticky=N)  
    
    
def normal_board(event=None):
    # Return the background of all the elements to default
    for i in entry_list:
        for j in i:
            if str(j['state']) == 'readonly':
                j.config(readonlybackground='grey94')
            j.config(bg=BACKGROUND_COLOR)
            
            
def new_game():
    # Will take a random sudoku puzzle from file 'sudokupuzzle.txt'
    for i in entry_list:
        for j in i:
            j.config(state='normal',bg=BACKGROUND_COLOR)
            j.delete(0,END)
            
    with open(r'Sudoku\sudokupuzzles.txt','r') as f:
        puzzles = f.readlines()

    puzzle = choice(puzzles).strip() # Return sudoku puzzle in the form of string with '.' as empty spaces
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
            
    numbers_on_board()             
    l1 = Label(root, text='Sudoku', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '40'), bd=3, relief='solid',justify='center')
    l1.grid(row=0, column=0, columnspan=15,sticky=W+E)
   
   
def animation_of_button(event):
    #When the mouse hover over the button the button color and font changes
    
    if 'Enter' in str(event):
        b1.config(fg='black',relief='solid')   
    else:
        b1.config(fg=FONT_COLOR,relief='raised')


def show_row_column(event,box):
    '''The function will verify if the input value complies with Sudoku rules. 
    If a violation is detected, it will change the background color of the affected elements to red.
    Additionally, it will highlight the background of numbers in different boxes, making it easier for the user to select the correct number.'''
    box_value = event.char
    normal_board()
    
    #Highlight the background
    for i in entry_list:
        for j in i:
            if box_value == j.get():
                if str(j['state']) == 'readonly':
                    j.config(readonlybackground='grey')
                else:
                    j.config(bg='grey')
    
    #check for row           
    for i in entry_list:
        if box in i:
            for j in i:
                if j != box and j.get() == box_value:
                    box.config(bg='red')
                    if str(j['state']) == 'readonly':j.config(readonlybackground='red')
                    else:j.config(bg='red')    
            break 
    
    #check for column
    for i in range(9):
        column = [entry_list[j][i] for j in range(9)]
        if box in column:
            for j in column:
                if j != box and j.get() == box_value:
                    box.config(bg='red')
                    if str(j['state']) == 'readonly': j.config(readonlybackground='red')
                    else: j.config(bg='red')  
            break
    
    #check for box                
    for i in range(3):
        var_1 = 3*i
        for j in range(3):
            var_2 = 3*j
            new_box = [entry_list[var_1+k][var_2+l] for k in range(3) for l in range(3)]
            if box in new_box:
                for l in new_box:
                    if l != box and l.get() == box_value:
                        box.config(bg='red')
                        if str(l['state']) == 'readonly': l.config(readonlybackground='red')
                        else: l.config(bg='red') 
                break

                     
def winining_condition(event):
    global b1
    # check if all the entries on the board are correct and if it is congratulate the player.
    
    numbers_on_board()
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
    l.grid(row=0, column=0, columnspan=15,sticky=W+E)     

        
vcmd = (root.register(validate_input_entry), '%P')
entry_list = []

l1 = Label(root, text='Sudoku', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '40'), bd=3, relief='solid',justify='center')
l1.grid(row=0, column=0, columnspan=15,sticky=W+E)
l2 = Label(root, text='      ', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,font=('Times', '2'), bd=3, relief='sunken',justify='center')
l2.grid(row=1, column=0, columnspan=14,sticky=W+E)
b1 = Button(root,text = 'NEW GAME',fg=FONT_COLOR,bg = BACKGROUND_COLOR,font= ('Times New Roman', '15'),command=new_game,width=15,relief='raised',justify='center')
b1.grid(row=16,column=0,columnspan=15,sticky=W+E) 
    
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
                e1.bind('<Key>',lambda event,box=e1:show_row_column(event,box))
                dummy_list.append(e1)
        entry_list.append(dummy_list)
        


with open(r'Sudoku\sudokupuzzles.txt','r') as f:
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

numbers_on_board()

root.bind('<Key>',winining_condition)
root.bind('<Button-1>',normal_board)
mainloop()