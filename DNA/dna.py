from random import randint
from time import sleep

index = -1
PAUSE = 0.1
DNA = [
    '          ##',  # Index 0 has no {}.
    '        #{}--{}#',
    '       #{}----{}#',
    '      #{}------{}#',
    '     #{}-------{}#',
    '    #{}-------{}#',
    '    #{}------{}#',
    '     #{}----{}#',
    '     #{}--{}#',
    '       ##',  # Index 9 has no {}.
    '     #{}--{}#',
    '     #{}----{}#',
    '    #{}------{}#',
    '    #{}-------{}#',
    '     #{}-------{}#',
    '      #{}------{}#',
    '       #{}----{}#',
    '        #{}--{}#']

color_codes = {
    'R': "\033[31m",           #red
    'Y': "\033[33m",           #yellow 
    'G': "\033[32m",           #green
    'B': "\033[34m",           #blue
    'I': "\033[38;5;54m",      #indigo
    "reset": "\033[0m"
}
    
def color_text(text,color):
    return f"{color_codes[color]}{text}{color_codes['reset']}"

try:
    while True:
        index += 1
        if index == len(DNA):
            index = 0
        
        if index in [0,9]:
            print(color_text(DNA[index],'Y'))
        else:
            randomSelection = randint(1,4)
            if randomSelection == 1:
                leftNucleotide, rightNucleotide = 'A', 'T'
                color_combo = ['G','I']
            elif randomSelection == 2:
                leftNucleotide, rightNucleotide = 'T', 'A'
                color_combo = ['I','G']
            elif randomSelection == 3:
                leftNucleotide, rightNucleotide = 'C', 'G'
                color_combo = ['R','B']
            elif randomSelection == 4:
                leftNucleotide, rightNucleotide = 'G', 'C'
                color_combo = ['B','R']
            dna = DNA[index].format(leftNucleotide, rightNucleotide)
            inital = 0
            num = 0 
            for i in dna:
                if i == '#':
                    print(color_text(i,'Y'),end='')
                elif i in ['A','T','G','C',]:
                    print(color_text(i,color_combo[inital]),end='')
                    inital += 1
                elif i == '-':
                    if num < len([i for i in dna if i == '-'])/2:
                        print(color_text(i,color_combo[0]),end='')
                    else:
                        print(color_text(i,color_combo[1]),end='')
                    num += 1
                else:
                    print(i,end='')
            print()           
        sleep(PAUSE)
except KeyboardInterrupt:
    quit()