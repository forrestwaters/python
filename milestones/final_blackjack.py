ckjack game for udemy class'''
import itertools
import random

##print "Welcome to BlackJack!"

class Dealer(object):
    def __init__(self,number_of_decks=1):
        self.number_of_decks = number_of_decks
    '''Can build this out later with dealers hand, etc.'''

game = Dealer(1)
suits = 'HDSC'
cards = '23456789TJQKA'
deck = list(''.join(card) for card in itertools.product(cards,suits))*game.number_of_decks
class Player(object):
    def __init__(self,name,bankroll=100):
        self.name = name
        self.bankroll = bankroll
    def add_bankroll(self,amount):
        self.bankroll += amount
    def reduce_bankroll(self,amount):
        self.bankroll -= amount
    def players_hand(self):
        self.players_hand = players_hand
    def hit(self):
        self.hit = raw_input('Would you like to hit or stay?: ')
        while True:
            if self.hit == 'hit':
                player.players_hand += random.sample(deck, 1)
                print player.players_hand
                break
            elif response == 'stay':
                break
            else:
                print "Please enter 'hit' or 'stay'"
