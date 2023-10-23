from tkinter import *
from tkinter import scrolledtext 

try:
    import pyttsx3
except ImportError:
    print('The pyttsx3 module needs to be installed to run this')
    print('program. On Windows, open a Command Prompt and run:')
    print('pip install pyttsx3')
    print('On macOS and Linux, open a Terminal and run:')
    print('pip3 install pyttsx3')
    quit()


def validate_input(value):
    if value.isdigit():
        return True
    else:
        return False
    
engine = pyttsx3.init()  # Initialize the TTS engine.
root = Tk()
root.title('Text to speech ')
BACKGROUND_COLOR = 'light blue'
FONT_COLOR = 'blue'

vcmd = (root.register(validate_input), '%P')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')

num_of_voices = []
for voice in voices:
     num_of_voices.append((voice.name,voice.id))

def speak():
    a = t1.get(1.0,END)
    engine.say(a)
    engine.runAndWait()

def back():
    for i in num_of_voices:
        if i[0] == option_var:
            engine.setProperty('voice', i[1])
    rate = int(spin_3.get())
    volume = int(spin_4.get())/10
    engine.setProperty('rate',rate)
    engine.setProperty('volume',volume)
    main()
    

def clear_screen() :
    widget = root.winfo_children()
    for item in widget :
        if item.winfo_children() :
            widget.extend(item.winfo_children())
    for item in widget:
        item.destroy()

def setting():
    global option_2,spin_3,spin_4,option_var
    
    root.geometry('670x220')
    clear_screen()
    
    l1 = Label(root, text='Settings', fg=FONT_COLOR, bg=BACKGROUND_COLOR , padx=10,font=('Times', '30'), bd=3, relief='sunken')
    l1.grid(row=0, column=0, columnspan=2,sticky=W+E)
    l_ = Label(root, text='                  ', fg=FONT_COLOR, bg=BACKGROUND_COLOR ,  bd=3, relief='sunken')
    l_.grid(row=1, column=0, columnspan=2,sticky=W+E)
    
    l2 = Label(root, text='Voices  --->', fg=FONT_COLOR, bg=BACKGROUND_COLOR , padx=50, font=('Times New Roman',18), bd=3, relief='sunken')
    l2.grid(row=2, column=0,sticky=W+E)
    l3 = Label(root, text='Rate    --->', fg=FONT_COLOR, bg=BACKGROUND_COLOR , padx=50, font=('Times New Roman', 18), bd=3, relief='sunken')
    l3.grid(row=3, column=0, sticky=W+E)
    l4 = Label(root, text='Volume --->', fg=FONT_COLOR, bg=BACKGROUND_COLOR , padx=50, font=('Times New Roman', 18), bd=3, relief='sunken')
    l4.grid(row=4, column=0, sticky=W+E)

    option_var = StringVar()
    option_2 = OptionMenu(root, option_var, *[i[0] for i in num_of_voices])
    option_2.config(fg=FONT_COLOR, bg=BACKGROUND_COLOR , font=('Times', '15'), width=40, relief='sunken')
    option_2.grid(row=2, column=1)
    option_var.set(num_of_voices[0][0])

    spin_3 = Spinbox(root, from_= 0, to = 4000,validate="key", validatecommand=vcmd,justify='center',font=('Times New Roman',15),fg=FONT_COLOR, bg=BACKGROUND_COLOR ) 
    spin_3.grid(row=3,column=1,sticky=W+E)
    spin_3.insert(0,rate)
    
    spin_4 = Spinbox(root, from_= 0, to = 100,validate="key", validatecommand=vcmd,justify='center',font=('Times New Roman',15),fg=FONT_COLOR, bg=BACKGROUND_COLOR ) 
    spin_4.grid(row=4,column=1,sticky=W+E)
    spin_4.insert(0,round(volume*10))
    
    b1 = Button(root,text = 'BACK',fg=FONT_COLOR,bg = BACKGROUND_COLOR,font= ('Times New Roman', '15'),command=back,width=15,relief='raised',justify='center')
    b1.grid(row=5,column=0,columnspan=2,sticky=W+E)
    

def main():
    global t1
    root.geometry('1035x380')
    clear_screen()
    l1 = Label(root, text='Text to speech converter', fg=FONT_COLOR, bg=BACKGROUND_COLOR , padx=250, font=('Times', '40'), bd=3, relief='sunken')
    l1.grid(row=0, column=0, columnspan=6)
    l_ = Label(root, text='                  ', fg=FONT_COLOR, bg=BACKGROUND_COLOR , padx=250, bd=3, relief='sunken')
    l_.grid(row=1, column=0, columnspan=6,sticky=W+E)
    l__ = Label(root, text='                  ', fg=FONT_COLOR, bg=BACKGROUND_COLOR , padx=250, bd=3, relief='sunken')
    l__.grid(row=5, column=0, columnspan=6,sticky=W+E)

    t1 = scrolledtext.ScrolledText(root, wrap = WORD, width = 40, height = 10, font = ("Times New Roman",15)) 
    t1.insert(1.0,'Text here')
    t1.grid(row=2,column=0,columnspan=6,rowspan=3,sticky=W+E)
    

    b1 = Button(root,text = 'Speak',fg=FONT_COLOR,bg = BACKGROUND_COLOR,font= ('Times New Roman', '15'),command=speak,width=15,relief='raised')
    b1.grid(row=6,column=3,sticky=W+E)
    b2 = Button(root,text = 'Settings',fg=FONT_COLOR,bg = BACKGROUND_COLOR,font= ('Times New Roman', '15'),command=setting,relief='raised')
    b2.grid(row=0,column=5)
    
main()
mainloop()



