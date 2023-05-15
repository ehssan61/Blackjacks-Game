# This file hold the written codes for the BlackJack Game 
# Implemented by Ehsan Haghian
# 4/24/2023

import random
#A dictionary of card values. This shows the rate of each value
rate = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
# Tuple of card suits
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
# Tuple of card values
vals = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

#creating the Card class
class Card:
    # Initialize the Card object with a suit and a vals.
    # The suit and vals are stored as instance variables.
    def __init__(self, suit, vals):
        self.suit = suit
        self.vals = vals
        self.name= self.vals + " of " + self.suit

    # Convert the Card object to a human-readable string.
    # The string prints the nums and suit of the card
    def __str__(self):
        return self.name
    
# Creating the Deck class
class Deck:
    #Creat constructor for the Deck class
    def __init__(self):
        self.deck = [] # Creat an empty list to store the value of cards 
        for i in suits: # Iterate over the suits
            for j in vals: # Iterate over the values
                self.deck.append(Card(i, j)) # This line join the suits and values and append to the the self.deck to be stored
    
    #This line print or convert the object of deck to a string.
    def __str__(self):
        return "The self.deck has" + str(len(self.deck)) + "cards"
        

    # Method to shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)

    # Method to deal a card from the deck and removes and returns the last card in the deck
    def deal(self):
        if len(self.deck) == 0:
            return None
        else:
            return self.deck.pop()    

#Creat class to track players chip and the amount of bet    
class PlayerChips:
    #Constructor for the class
    def __init__(self, total=100):
        self.total = total
        self.bet = 0
        self.chips_history = [self.total] #initialize chips_history with empty values

    # Define method to add the player's bet to their total number of chips when they win a bet.
    def win(self):
        self.total += self.bet * 2 
        self.total-=100
        self.chips_history.append(self.total) #append the updated total number of chips to chips_history

    # Define a method to subtract the player's bet from their total number of chips when they lose a bet.
    def lose(self):
        self.total -=self.bet 
        self.total-=100
        self.chips_history.append(self.total) #append the updated total number of chips to chips_history   

    def tie(self):
        self.total-=100
        self.chips_history.append(self.total) #append the unchanged total number of chips to chips_history

#Creat Hand class that represent the card in the hands of player        
class Hand:
    #Create constructor for the class
    def __init__(self):
        #Create a Hand object with an empty list of cards, hand value of 0, and no aces
        self.cards = []
        self.hand_value = 0
        self.num_aces = 0

    def add(self, card):
        
        #Add a card to the hand, adjust for aces if necessary, and update the hand value.
        self.cards.append(card)
        self.hand_value += rate[card.vals]

        # Update the number of Ace if any
        if card.vals == 'Ace':
            self.num_aces += 1

    #This method reduce the hand value by 10 for each ace in the hand until the hand value is less than or equal to 21.
    def handle_ace(self):
        
        while self.hand_value > 21 and self.num_aces > 0:
            self.hand_value -= 10
            self.num_aces -= 1

# Define function to get the player bet abount
def get_player_bet(player_chips):
    # Loop until a valid bet is entered by the player
    while True:
        try:
            # Prompt the player to enter their bet and convert input to an integer
            bet = int(input("Please Enter Your Bet Amount: "))

            if bet > player_chips.total: # Check if the bet is greater than the player's available chips
                print("Sorry, your bet cannot exceed your available chips: ", player_chips.total)

            elif bet <= 0: # Check if the bet is not a positive integer
                print("Invalid input. Please enter a positive integer for your bet.")
            else:
                player_chips.bet = bet # Set the player's bet and break the loop if the bet is valid
                break
        # Catch a ValueError if the input cannot be converted to an integer   
        except ValueError:
            print("Invalid input. Your bet must be a positive integer.") 

# Function to display the dealer's hand
def display_dealer_hand(dealer):
    print("\nDealer's Hand")
    for card in dealer.cards:
        print(card)
    print("Dealer's Hand Value is:", dealer.hand_value)
    
def hide_dealer_hand(dealer):
    print("\nDealer's Hand")
    print("<card hidden>")
    print(dealer.cards[1])


# Function to display the player's hand
def display_player_hand(player):
    print("\nPlayer's Hand:")
    for card in player.cards:
        print(card)
    print("Player's Hand Value is:", player.hand_value)

     
# main function
def main():
    # Welcome message
    print("Welcome To Blackjack!")
    
    # Create a deck of cards and shuffle it
    deck = Deck()
    deck.shuffle()

    # Create player and dealer hands, and deal two cards to each
    playerHand = Hand()
    dealerHand = Hand()
    for i in range(2):
        playerHand.add(deck.deal())
        dealerHand.add(deck.deal())

    # Create player chips and get the player's bet amount
    chips = PlayerChips()
    while True:
        try:
            get_player_bet(chips)
            break
        except ValueError:
            print("Invalid bet amount. Please enter a valid number.")

    # Display the player's hand and one of the dealer's cards
    display_player_hand(playerHand)
    hide_dealer_hand(dealerHand)

   # Loop to handle player's turn
    while playerHand.hand_value <= 21:
        # Ask the player if they want to hit or stand
        hit_or_stand = input("Do You Want To Hit Or Stand? Enter 'h' or 's': ")

        if hit_or_stand.lower() == 'h':
            # Player chooses to hit
            playerHand.add(deck.deal())
            playerHand.handle_ace()
            print()
            print("********** Player's Hand After Hit **********")
            display_player_hand(playerHand)
            print()
            
        else:
            # Player chooses to stand
            display_player_hand(playerHand)
            display_dealer_hand(dealerHand)
            break

    # If player's hand exceeds 21, the player busts and loses the bet
    if playerHand.hand_value > 21:
        chips.lose()
        print("\nPlayer Busts!, You Lost",abs(chips.total), "Chips In This Round"  )
       

    else:
        
        while dealerHand.hand_value < 17:
            # Dealer hits until their hand value reaches 17 or greater
            print()
            print("********** Dealer's Hand After Hit **********")
            dealerHand.add(deck.deal())
            dealerHand.handle_ace()
            display_dealer_hand(dealerHand)
            

        # Determine the winner
        if dealerHand.hand_value > 21:
            chips.win()
            print("\nDealer Busts! You Catch",chips.total, "Chips In This Round")
            

        elif dealerHand.hand_value > playerHand.hand_value:
            chips.lose()
            print("\nPlayer Lose!, You Lost",abs(chips.total), "Chips In This Round" )
            


        elif playerHand.hand_value > dealerHand.hand_value:
            chips.win()
            print("\nPlayer WIN! You Catch",chips.total, "Chips In This Round" )
           

        elif playerHand.hand_value == dealerHand.hand_value:
            print("It's A Tie!")
            chips.tie()

    
    print("The Total Number Of Your Chips Is", sum(chips.chips_history))
    print()
    play_again = input("Do You Want To Play Again? Enter 'y' or 'n': ")
    print()

    
    if play_again.lower() == 'y':
        
        print("----------" * 10)
        print("Start New Game")
        main()
            
    else:
        # Print the player's final total number of chips and break out of the loop
        print("Thanks For Playing Blackjack!")
        print()
        
if __name__ == "__main__":
    main()     