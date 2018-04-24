class Card:
    def __init__(self, name, value, color, hidden=False):
        self.name = name
        self.value = value  # can be accessed by card.value
        self.color = color
        self.hidden = hidden
    
    def __str__(self):
        if self.hidden:
            return 'An unknown card'
        return f'{self.name} of {self.color}'

    def __repr__(self):
         return self.__str__()
    
# Values for all cards
colors = ['Clubs', 'Hearts', 'Spades', 'Diamonds']
values_names = [(2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five'), (6, 'Six'), (7, 'Seven'), (8, 'Eight'), (9, 'Nine'), (10, 'Ten'), (10, 'Jack'), (10, 'Queen'), (10 , 'King') , (11, 'Ace')]  # Add rest

# Generate cards
deck = []
for color in colors:
    for value, name in values_names:
        deck.append(Card(name, value, color))  # card gets created here
# random shuffle?
import random
random.shuffle(deck)

def player_input():
    
    choice = ''
    while not (choice == 'YES' or choice == 'STAY'):
        choice = input('do you want next card').upper()

    if choice == 'YES':
        return (deck.pop())#deck.pop
    else:
        return #sume of cards 
   # print(f'your score is {value} know Dealer turn')

   def new_deck():
    
    deck = []
    for color in colors:
        for value, name in values_names:
            deck.append(Card(name, value, color))  # card gets created here
# random shuffle?
    import random
    random.shuffle(deck)
    return deck
    deck = new_deck()

player_hand = [deck.pop(), deck.pop()]
print(player_hand)

dealer_hand = [deck.pop(), deck.pop()]
dealer_hand[0].hidden = True
print(dealer_hand)

def get_value(hand):
    hand_value = 0
    for card in hand:
        hand_value += card.value
    print(f'Your score is: {hand_value}')
    return hand_value

player_value = get_value(player_hand)
print(player_value)
dealer_value = get_value(dealer_hand)
# if get_value(player_hand) > get_value(dealer_hand): Wygrales!

def win():
    if player_value <= 21 and player_value > dealer_value:
        print('YOU WON \n NICE')

        def dealer(dealer_hand):
    if player_value >= dealer_value and dealer_value < 21:
          dealer_hand += [deck.pop()]
          #alternatywnie: dealer_hand.append(deck.pop())
    else :
            print('dupa')
    # if player card sum is <= play 
    # if dealer card sum is < 21 play 
    # if dlaler casrd sum is >= 21 stop play 

    class Player_Accout:
    def __init__(self,name,account=200):
        self.name = name
        self.account = account
        
    def win(self,win_amaut):
        self.balance += win_amaut#accont form balance
        print(f'You Win {win_amaut} YEY')  
        
     
    def bet(self,bet_amaut):
        if self.balance >= bet_amaut:
            self.balance -= bet_amaut
            print('Bet accepted')
        else:
            print('Get lost looser')

            print('Dealer cards:') #delar hand[]
#card_1 = deck[0]#deck.pop()
#print(card_1.value)
#card_1.hidden = True
#print(card_1) 
print()
print ('your cards are:')#player hand[]
print(deck[3])
print(deck[4])
#def player_choice()
    
    #choice = input('do you want next card')
     #if 'yes' 
     #   print (deck[5])
     #   check if sum is <=21 osobno liczenie 
      #      if sum is > 21 
    #        prinl(You LOST)
    # else  
    #     sum score 
    #     print('your score is {value} know Dealer turn' )
    #    