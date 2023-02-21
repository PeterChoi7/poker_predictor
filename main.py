
#define all suits and ranks
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Create an empty dictionary to hold the cards
cards = []

# Loop through each suit and rank, and add the card to the dictionary
for suit in suits:
    for rank in ranks:
        cards.append((rank, suit))
        
def algorithm(my_cards, needed):
    rank_1 = my_cards[0][0]
    suit_1 = my_cards[0][1]
    rank_2 = my_cards[1][0]
    suit_2 = my_cards[1][1]
    
    connector_lst = []
    suited_lst = []
    high_cards_lst = []
    
    def royal_flush():
        if (abs(rank_1 - rank_2) > 4):
            return 0
        else:
            
    def stright_flush(suit_1, suit_2):
        return None
    
    def four_of_a_kind(suit_1, suit_2):
        return None
    
    def full_house(suit_1, suit_2):
        return None
    
    def flush(suit_1, suit_2):
        return None
    
    def straight(suit_1, suit_2):
        return None
    
    def three_of_a_kind(suit_1, suit_2):
        return None
    
    def two_pair():
        return None
    
    def pair():
        return None
    
    def high_cards():
        return None

def main():
    available_cards = cards.copy()
    needed_cards = cards.copy()
    
    print(available_cards)
    
    rank_1 = input("What is the rank of your first card? ")
    if rank_1 not in ranks:
        print("Please enter a valid rank")
        return
    
    suit_1 = input("What is the suit of your first card? ")
    if suit_1 not in suits:
        print("Please enter a valid rank")
        return
    
    # delete the dealt card from available cards
    available_cards.remove((rank_1, suit_1))

    rank_2 = input("What is the rank of your second card? ")
    if rank_2 not in ranks:
        print("Please enter a valid rank")
        return
    suit_2 = input("What is the suit of your second card? ")
    if suit_2 not in suits:
        print("Please enter a valid rank")
        return
    
    # delete the dealt card from available cards
    available_cards.remove((rank_2,suit_2))

    my_Cards = [
        (rank_1, suit_1),
        (rank_2, suit_2) 
    ]
    percentage = algorithm(my_Cards, needed_cards)
    
    board = {}

main()



