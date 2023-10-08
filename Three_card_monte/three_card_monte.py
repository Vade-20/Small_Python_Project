import curses
from curses import wrapper
import random
import time


NUMBER_OF_CARDS = 3
SPEED = 1

def random_card():
    deck_of_cards = [('A', '♥'),(2, '♥'),(3, '♥'),(4, '♥'),(5, '♥'),(6, '♥'),(7, '♥'),(8, '♥'),(9, '♥'),(10, '♥'),('J', '♥'),('Q', '♥'),('K', '♥'),
                    ('A', '♦'),(2, '♦'),(3, '♦'),(4, '♦'),(5, '♦'),(6, '♦'),(7, '♦'),(8, '♦'),(9, '♦'),(10, '♦'),('J', '♦'),('Q', '♦'),('K', '♦'),
                    ('A', '♠'),(2, '♠'),(3, '♠'),(4, '♠'),(5, '♠'),(6, '♠'),(7, '♠'),(8, '♠'),(9, '♠'),(10, '♠'),('J', '♠'),('Q', '♠'),('K', '♠'),
                    ('A', '♣'),(2, '♣'),(3, '♣'),(4, '♣'),(5, '♣'),(6, '♣'),(7, '♣'),(8, '♣'),(9, '♣'),(10, '♣'),('J', '♣'),('Q', '♣'),('K', '♣')]
    
    rand_cards = [('Q', '♥')]
    for i in range(NUMBER_OF_CARDS-1):
        while True:
            use_less = random.choice(deck_of_cards)
            if use_less==('Q', '♥'):
                continue
            else:
                rand_cards.append(use_less)
                break
    random.shuffle(rand_cards)
    return rand_cards

def resting(cards=None):
    if cards is not None:
        printing_format = ''
        
        printing_format += ' ____\t'+'\n'
        
        if cards[0] not in  [10,'??']:
            printing_format += f'|{cards[0]}   |\t'+'\n'
        else:
            printing_format += f'|{cards[0]}  |\t'+'\n'
            
        printing_format+=f'| {cards[1]}  |\t'+'\n'
        if cards[0] not in  [10,'??']:
            printing_format+=f'|___{cards[0]}|\t'+'\n'
        else:
            printing_format+=f'|__{cards[0]}|\t'+'\n'
            
        return printing_format
    else:
        cards = ['??', '?']
        printing_format = ''
        
        printing_format += ' ____\t'+'\n'
        
        if cards[0] not in  [10,'??']:
            printing_format += f'|{cards[0]}   |\t'+'\n'
        else:
            printing_format += f'|{cards[0]}  |\t'+'\n'
            
        printing_format+=f'| {cards[1]}  |\t'+'\n'
        if cards[0] not in  [10,'??']:
            printing_format+=f'|___{cards[0]}|\t'+'\n'
        else:
            printing_format+=f'|__{cards[0]}|\t'+'\n'
            
        return printing_format
        
    
def printing_cards(stdsrc):
    stdsrc.clear()
    stdsrc.addstr('''Three-Card Monte

Find the red lady (the Queen of Hearts)! Keep an eye on how
the cards move.
Here are the cards-\n\n\n\n\n\n''')
    stdsrc.refresh()
    for i in pos_of_cards:
        x,y = pos_of_cards[i]
        cur_new = curses.newwin(5,10,y,x)
        cur_new.addstr(resting(i))
        cur_new.refresh()                

def printing_moving_cards(stdsrc):
    stdsrc.clear()
    stdsrc.addstr('''Three-Card Monte

Find the red lady (the Queen of Hearts)! Keep an eye on how
the cards move.
Here are the cards-\n\n\n\n\n\n''')
    stdsrc.refresh()
    for i in pos_of_cards:
        x,y = pos_of_cards[i]
        cur_new = curses.newwin(5,10,y,x)
        cur_new.addstr(resting())
        cur_new.refresh()      
        

@wrapper
def main(stdsrc):
    global pos_of_cards,SPEED
    while True:
        stdsrc.clear()
        curses.curs_set(0)
        curses.echo()
        stdsrc.refresh()
        cards = random_card() # For generating a random list of 3 cards where 1 card is queen of hearts 
        
        #creating positions of cards
        x = 5
        pos_of_cards = {}
        for i in cards:
            pos_of_cards[i] = [x,15]
            x += 12
            
        printing_cards(stdsrc)
        stdsrc.addstr('Press any key to continue...')
        stdsrc.getch()
        
        
        #This will make it random for each time the card are shuffled
        for i in range(random.randint(4,10) ):
            printing_moving_cards(stdsrc)
            movement_1 = random.choice([1,-1])
            movement_2 = -1 if movement_1==1 else 1
            card_1 = random.choice(cards)
            while True:
                card_2 = random.choice(cards)
                if card_2==card_1:continue
                else:break
            
            # FOR VERTICAL MOVEMENT GOING   
            for i in range(5):
                x,y = pos_of_cards[card_1]
                pos_of_cards[card_1] = [x,y+movement_1]
                x,y = pos_of_cards[card_2]
                pos_of_cards[card_2] = [x,y+movement_2]
                printing_moving_cards(stdsrc)
                time.sleep(0.1/SPEED)
            
            # FOR HORIZONTAL MOVEMENT  
            x_1,y_1 = pos_of_cards[card_1]
            x_2,y_2 = pos_of_cards[card_2]
            dummy_1,dummy_2 = x_1,x_2
            while x_1!=x_2:
                if x_1<x_2:
                    dummy_1 += 1
                    dummy_2 -= 1
                    x_1 +=1 
                else:
                    dummy_1 -= 1
                    dummy_2 += 1
                    x_1 -=1 
                pos_of_cards[card_1] = [dummy_1,y_1]
                pos_of_cards[card_2] = [dummy_2,y_2]
                printing_moving_cards(stdsrc)
                time.sleep(0.1/SPEED)
            
            # FOR VETICAL MOVEMENT RETURNING 
            movement_1 = 1 if movement_1==-1 else -1  
            movement_2 = 1 if movement_2==-1 else -1  
            for i in range(5):
                x,y = pos_of_cards[card_1]
                pos_of_cards[card_1] = [x,y+movement_1]
                x,y = pos_of_cards[card_2]
                pos_of_cards[card_2] = [x,y+movement_2]
                printing_moving_cards(stdsrc)
                time.sleep(0.1/SPEED)
            time.sleep(1/SPEED)  
        
        num = ''
        for i in range(1,NUMBER_OF_CARDS+1):
            num += f' {i}'+' '*10
        num +='\n\n'
        stdsrc.addstr(20,5,num)
        stdsrc.addstr(f'Which card has the Queen of Hearts? ({",".join([str(i) for i in range(1,NUMBER_OF_CARDS+1)])})\n>')
        ans = stdsrc.getstr().decode(encoding='utf-8')
        useless_list = sorted([pos_of_cards.get(i)[0] for i in pos_of_cards])
        use_ful_list = []
        for i in useless_list:
            for j in pos_of_cards:
                if pos_of_cards[j][0]==i:
                    use_ful_list.append(j)
                    break
        queen_of_heart = use_ful_list.index(('Q', '♥'))+1
        printing_cards(stdsrc)
        if int(ans) == queen_of_heart:
            stdsrc.addstr('YOU WIN.\nPress any key to continue to the next level')
            SPEED+=1
        else:
            stdsrc.addstr(f'You lose at level {SPEED} better luck next time\nPress any key to exit')
            stdsrc.getch()
            quit()
        stdsrc.refresh()
        stdsrc.getch()



