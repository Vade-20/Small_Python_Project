from random import randint
from time import sleep

index = -1
PAUSE = 0.1
DNA = [
    '         ##',  # Index 0 has no {}.
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',  # Index 9 has no {}.
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#']


try:
    while True:
        index += 1
        if index == len(DNA):
            index = 0
        
        if index in [0,9]:
            print(DNA[index])
        else:
            randomSelection = randint(1,4)
            if randomSelection == 1:
                leftNucleotide, rightNucleotide = 'A', 'T'
            elif randomSelection == 2:
                leftNucleotide, rightNucleotide = 'T', 'A'
            elif randomSelection == 3:
                leftNucleotide, rightNucleotide = 'C', 'G'
            elif randomSelection == 4:
                leftNucleotide, rightNucleotide = 'G', 'C'
            print(DNA[index].format(leftNucleotide, rightNucleotide))
        sleep(PAUSE)
except KeyboardInterrupt:
    quit()