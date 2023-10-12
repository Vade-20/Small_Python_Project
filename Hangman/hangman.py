from hangman_visual import visuals
import json
import random
from PyDictionary import PyDictionary
import curses
from curses import wrapper

dictionary = PyDictionary()

def get_a_word():
    try:
        with open(r'words.json', 'r',encoding='utf-8') as f:
            data = list(json.load(f))
    except FileNotFoundError:
        print('Please change directory to where the words.json is located.')
        quit()
        
    random_word = random.choice(data).lower()
    meaning = dictionary.meaning(random_word, disable_errors=True)
    count = 0
    while meaning is None:
        if count == 5:
            meaning = {"Internet connection unavailable":["Please establish an internet connection to retrieve the meaning of the word."]}
            break
        random_word = random.choice(data).lower()
        meaning = dictionary.meaning(random_word, disable_errors=True)
        count += 1
    meaning_type = list(meaning.keys())[0]
    meaning = ','.join(meaning[meaning_type])
    return (random_word,meaning_type,meaning)


@wrapper
def main(stdsrc):
    stdsrc.clear()
    curses.echo()
    curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    YELLOW = curses.color_pair(1)
    RED = curses.color_pair(2)
    stdsrc.addstr(3,2,"HANGMAN THE GAME",RED)
    stdsrc.refresh()
    
    visuals_window = curses.newwin(10,30,5,5)
    visuals_constant = 7
    visuals_window.addstr(2,5,f'{visuals[visuals_constant]}',YELLOW)
    visuals_window.border()
    visuals_window.refresh()
    
    word_already_used = ['Missed letters-']
    word_used_win = curses.newwin(10,21,5,40)
    word_used_win.addstr(1,2,f'{word_already_used[0]}',YELLOW)
    word_used_win.border()
    word_used_win.refresh()
    
    stdsrc.addstr(19,5,f'LOADING.....',RED)
    stdsrc.refresh()
    word = get_a_word()
    
    mising_words = '_ '*len(word[0])
    mising_words_win = curses.newwin(1,30,17,5)
    mising_words_win.addstr(mising_words,YELLOW)
    mising_words_win.refresh()
    
    stdsrc.addstr(19,5,f'Definition : {word[1]} : {word[2]}',RED)
    stdsrc.refresh()
    word = ''.join([f'{i} ' for i in word[0]])
        
    while visuals_constant>0:
        stdsrc.addstr(21,5,f'Guess a letter\n     >',RED)
        ans = chr(stdsrc.getch())
        stdsrc.addstr(21,5,f'Guess a letter\n     > ',RED)

        if not ans.isalpha() or ans.upper() in word_already_used:
            continue
        
        if ans in word:
            mising_words = list(mising_words)
            for i in range(0,len(word)-1):
                if word[i] == ans:
                    mising_words[i] = ans
            mising_words = ''.join(mising_words)
            mising_words_win.clear()
            mising_words_win.addstr(mising_words,YELLOW)
            mising_words_win.refresh()
        else:
            visuals_constant -= 1
            visuals_window.clear()
            visuals_window.addstr(2,5,f'{visuals[visuals_constant]}',YELLOW)
            visuals_window.border()
            visuals_window.refresh()
            
            word_already_used.append(ans.upper())
            word_used_win.clear()
            for i,j in enumerate(word_already_used,start=1):
                word_used_win.addstr(i,2,j,YELLOW)
            word_used_win.border()
            word_used_win.refresh()
        
        if visuals_constant == 0:
            word = word.replace(' ','')
            stdsrc.addstr(22,5,f'YOU LOSE!!!!!!. The word is {word}\n     Press any key to exit.',YELLOW)
            stdsrc.getch()
        elif mising_words==word:
            word = word.replace(' ','')
            stdsrc.addstr(22,5,f'YOU WIN!!!!!!. The word is {word}\n     Press any key to exit.',YELLOW)
            stdsrc.getch()
            quit()
    
            
            

