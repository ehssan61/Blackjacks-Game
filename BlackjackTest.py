# This file hold the test materials for the BlackJack Game 
# CS5001 course Final project
# Implemented by Ehsan Haghian
# 4/24/2023


import unittest
from BlackJack import Card, Deck, PlayerChips, Hand
import random

#Create class test
class CardTest(unittest.TestCase):
    #Define function to test the constructor
    def test_card_init(self):
        card = Card('Hearts', 'Two')
        self.assertEqual(card.suit, 'Hearts')
        self.assertEqual(card.vals, 'Two')
        self.assertEqual(str(card), 'Two of Hearts')
#Creat test for Deck class      
class DeckTest(unittest.TestCase):

    def test_deck_init(self):
        deck = Deck() #This line creates a new Deck object.
        self.assertEqual(len(deck.deck), 52) #This line tests whether the length of the deck attribute of the Deck object is equal to 52.
        
    def test_deck_shuffle(self):
         # Create a deck with known ordering
        deck = [1, 2, 3, 4, 5]
        
        # Shuffle the deck using the shuffle method
        random.seed(42) # Set the random seed for reproducibility
        random.shuffle(deck)
        
        # Verify that the deck is now in a different order
        self.assertNotEqual(deck, [1, 2, 3, 4, 5])
        
        # Verify that the deck still contains all the original cards
        self.assertCountEqual(deck, [1, 2, 3, 4, 5])

    def test_deck_deal(self):
        deck = Deck()
        card = deck.deal()
        self.assertIsInstance(card, Card)

#Create class for test the PlayerChips 
class PlayerChipsTest(unittest.TestCase):
    # Test conctructor
    def test_player_chips_init(self):
        player_chips = PlayerChips()
        self.assertEqual(player_chips.total, 100)
        self.assertEqual(player_chips.bet, 0)
    # Test the playe win method    
    def test_player_chips_win(self):
        player_chips = PlayerChips()
        player_chips.bet = 10
        player_chips.win()
        self.assertEqual(player_chips.total, 20)
        
    # Test palyer lose method
    def test_player_chips_lose(self):
        player_chips = PlayerChips()
        player_chips.bet = 10
        player_chips.lose()
        self.assertEqual(player_chips.total, -10)
        
    # Test for tie method
    def test_player_chips_tie(self):
        player_chips = PlayerChips()
        player_chips.tie()
        self.assertEqual(player_chips.total, 0)
        self.assertEqual(player_chips.chips_history, [100, 0])
# Test Hand class
class HandTest(unittest.TestCase):
    #Test constructor
    def test_hand_init(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])
        self.assertEqual(hand.hand_value, 0)
        self.assertEqual(hand.num_aces, 0)
    # Test add method
    def test_hand_add_card(self):
        hand = Hand()
        card = Card('Hearts', 'Two')
        hand.add(card)
        self.assertEqual(hand.cards, [card])
        self.assertEqual(hand.hand_value, 2)
        self.assertEqual(hand.num_aces, 0)
    # Test ace_handle method
    def test_hand_handle_ace(self):
        hand = Hand()
        card1 = Card('Hearts', 'Ace')
        card2 = Card('Diamonds', 'King')
        hand.add(card1)
        hand.add(card2)
        self.assertEqual(hand.hand_value, 21)
        self.assertEqual(hand.num_aces, 1)
        hand.add(card1)
        self.assertEqual(hand.hand_value, 32)
        self.assertEqual(hand.num_aces, 2)

if __name__ == '__main__':
    unittest.main()