from random import choice,shuffle    
        
def rules():
    rule = '''The Rules of \033[1m BlackJack \033[0m are:
    \033[1m 1. \033[0m The main objective of blackjack is \033[1m Beat The Dealer \033[0m but here the objective is to \033[1m Beat the Computer \033[0m
    \033[1m 2.  How do you beat the dealer?\033[0m 
            1.) By drawing a hand value that is higher than the dealer's hand value
            2.) By the dealer drawing a hand value that goes over 21.
            3.) By drawing a hand value of 21 on your first two cards, when the dealer does not. This is called Black Jack
    \033[1m 3. How do you lose to the dealer?\033[0m
            1.) Your hand value exceeds 21. It is called bust and once this happens you lose immediately even if the dealer 
                also have a bust hand.
            2.) The dealers hand has a greater value than yours at the end of the round
    \033[1m 4. How to find the hand value:\033[0m
            1.) 2 through 10 count at face value.
            2.) Face cards (J,Q,K) count as 10.
            3.) Ace can count as a 1 or an 11 depending on which value helps the hand the most.
    \033[1m 5. Starting the game \033[0m When the game start you are dealt with 2 up facing card and the dealer has one upfacing card
                while the other is facing down.
    \033[1m 6.  Player decides how to play hand \033[0m
            \033[1m 1.) Stand \033[0m : If your first two cards are acceptable, you can stand and the dealer will reveal his card.
            \033[1m 2.) Hit \033[0m : If you would like more cards to improve your hand total, the dealer will deal you more cards,
                    one at a time, until you either “bust” (go over 21) or you choose to stand.
            \033[1m 3.) Double Down \033[0m :  If you have a hand total that is advantageous to you but you need to 
                take an additional card you can double your initial wager and the dealer will deal you only 1 additional card. 
                You cant take more cards after Doubling Down
            \033[1m 4.) Yield \033[0m: If you don't like your initial hand, you have the option of giving it up in exchange for half 
                    your original bet back.
    \033[1m 7. \033[0m If  the dealer hand's total is 17 or more, it must stand. If the total is 16 or under, then they must take a card. 
            The dealer must continue to take cards until the total is 17 or more, at which point the dealer must stand.
    \033[1m 8. Payoff:\033[0m
            1.) If you win,then your bet money increase by 100%
            2.) If you win with black jack,then your bet money increase by 150%
            3.) If you lose,then you lose your bet money
            4.) If you tie,then your bet money is returned
    '''
    print(rule)


class Members:
    def __init__(self,*args):
        self.cards = args
        self.cards_total = 0
        self.totaling()
        
    def totaling(self):
        num_of_a = 0
        self.cards_total = 0
        for i in self.cards:
            if i[0] in ['K','Q','J']:
                self.cards_total+=10
            elif i[0] not in ['A','??']:
                self.cards_total+=i[0]
            elif i[0]=='A':
                self.cards_total+=11
                num_of_a+=1
        
        while num_of_a>0 and self.cards_total>21:
            self.cards_total-=10
            num_of_a-=1
              
    def printing_cards(self):
        cards = self.cards
        size = len(cards)
        print(' ____\t'*size)
        for i in range(size):
            if cards[i][0] not in [10,'??']:
                print(f'|{cards[i][0]}   |\t',end='')
            else:
                print(f'|{cards[i][0]}  |\t',end='')
        print()
        for i in range(size):
            print(f'| {cards[i][1]}  |\t',end='')
        print()
        for i in range(size):
            if cards[i][0] not in [10,'??']:
                print(f'|___{cards[i][0]}|\t',end='')
            else:
                print(f'|__{cards[i][0]}|\t',end='')
        print()
          
    def add_card(self):
        card = random_card()
        print(f'takes {card[0]} of {card[1]} from the deck')
        self.cards = list(self.cards)
        if '??' in [i[0] for i in self.cards]:
            self.cards.pop()
        self.cards.append(card)
        self.totaling()
                      
    
class Dealer(Members):
    dealer_card = '???'
    def __init__(self, *args):
        super().__init__(*args)
        if len(self.cards)==1:
            self.cards=(self.cards[0],('??','?'))
        Dealer.dealer_card='???'
            
    def add_card(self):
        print('Dealer',end=' ')
        super().add_card()
        Dealer.dealer_card=self.cards_total
    
    
class Player(Members):
    total_money = 10_000

    def add_card(self):
        print('Player',end=' ')
        super().add_card()
        
    def new_cards(self):
        self.cards = (random_card(),random_card())
    
    def standing(self,dealer:Dealer,bet:int):
        global player
        dealer.add_card()
        printing_format()
        input('Press Enter to continue:')
        while dealer.cards_total<17:
            dealer.add_card()
            printing_format()
            input('Press Enter to continue:')
        if dealer.cards_total>21:
            print("You Win!!")
            player.total_money+=bet             
        elif self.cards_total<dealer.cards_total:
            print('You Lost!!')
            player.total_money-=bet
        elif self.cards_total>dealer.cards_total:
            print("You Win!!")
            player.total_money+=bet
        elif self.cards_total==dealer.cards_total:
            print('It\'s a tie, the bet is returned to you.')
        print('\n')
     
    def Hit(self):
        player.add_card()
        printing_format()
    
    def Double_Down(self):
        global bet,player,ch
        bet = int(bet)
        upper_rand = bet if self.cards_total<bet else self.cards_total
        
        while True:
            more_bet = input(f'How much more do you want to bet (1-{upper_rand}): ')
            if more_bet not in [str(i) for i in range(1,upper_rand+1)]:
                continue
            break
        
        player.add_card()
        player.totaling()
        bet = str(bet + int(more_bet))
        ch = 's'
        printing_format()
          
    def Yield(self):
        global player,bet,ch
        bet = int(bet)
        print('\n')
        print('You surrendered,half of the bet money is taken away')
        player.total_money -= int(bet/2)
        print('Bet : ',bet)
        print('Money Left: ',player.total_money)
        input('Press Enter to continue:')
        
    
    
    
def random_card():
    deck_of_cards = [('A', '♥'),(2, '♥'),(3, '♥'),(4, '♥'),(5, '♥'),(6, '♥'),(7, '♥'),(8, '♥'),(9, '♥'),(10, '♥'),('J', '♥'),('Q', '♥'),('K', '♥'),
                    ('A', '♦'),(2, '♦'),(3, '♦'),(4, '♦'),(5, '♦'),(6, '♦'),(7, '♦'),(8, '♦'),(9, '♦'),(10, '♦'),('J', '♦'),('Q', '♦'),('K', '♦'),
                    ('A', '♠'),(2, '♠'),(3, '♠'),(4, '♠'),(5, '♠'),(6, '♠'),(7, '♠'),(8, '♠'),(9, '♠'),(10, '♠'),('J', '♠'),('Q', '♠'),('K', '♠'),
                    ('A', '♣'),(2, '♣'),(3, '♣'),(4, '♣'),(5, '♣'),(6, '♣'),(7, '♣'),(8, '♣'),(9, '♣'),(10, '♣'),('J', '♣'),('Q', '♣'),('K', '♣')]*8
    
    shuffle(deck_of_cards)
    return deck_of_cards.pop()


def printing_format():
        print('Dealer:',dealer.dealer_card)
        dealer.printing_cards()
        print()
        print('Player',player.cards_total)
        player.printing_cards()
        print('\n') 


print('\033[1m Welcome to BlackJack \033[0m')
if input('Do you want to read the rules (Y/N)? ').lower().startswith('y'):
    rules()

player = Player(random_card(),random_card())
choice_dict = {'s':player.standing,'h':player.Hit,'d':player.Double_Down,'y':player.Yield}

print('\n')    
while player.total_money>0: 
    dealer = Dealer(random_card())
    print("Money Left:",player.total_money)
    
    while True:
        bet = input(f'How much do you want to bet?(1-{player.total_money}) or QUIT : ')    
        if not bet.isdigit() and not bet.lower().startswith('q') :
            continue
        elif bet.lower().startswith('q'):
            print('Thank For Playing')
            print(f'Your end total is {player.total_money}')
            quit()
        elif int(bet) not in range(1,player.total_money+1):
                continue    
        break
    
    if player.cards_total==21:
        print(r"It's a BlackJack,if you win you will get 150% of your bet")
        bet = int(bet)+int(int(bet)/2)
        choice_dict.get('s')(dealer,bet)  
        player.new_cards()
        player.totaling()
        continue       
        
    print('Bet: ',bet,'\n')
    printing_format()
    
    while True:
        while True:
            ch = input('(H)it, (S)tand, (D)ouble down, (Y)ield : ').lower()[0]
            if ch not in ['h','d','s','y']:
                continue
            break
        
        if ch!='s':
            choice_dict.get(ch)()
            
        if ch=='y':
            player.new_cards()
            player.totaling()
            break  
        
        if player.cards_total>21:
            print('You lose!! you went over 21')
            player.total_money-=int(bet)
            player.new_cards()
            player.totaling()
            break
        
        if ch=='s':
            choice_dict.get(ch)(dealer,int(bet))  
            player.new_cards()
            player.totaling()
            break
else:
    print('You ran out of your fake money')
