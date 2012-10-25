from django.db import models
from random import shuffle

RANK_CHOICES = [
        # ('2', 'Two'),
        # ('3', 'Thee'),
        # ('4', 'Four'),
        # ('5', 'Five'),
        # ('6', 'Six'),
        # ('7', 'Seven'),
        # ('8', 'Eight'),
        'Nine',
        'Ten',
        'Jack',
        'Queen',
        'King',
        'Ace'
    ]

SUIT_CHOICES = [
        'Hearts',
        'Diamonds',
        'Spades',
        'Clubs'
    ]

class Card(models.Model):
    """ A playing card """

    rank =  models.CharField(max_length=12)
    suit =  models.CharField(max_length=12)
    played = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s of %s" % (self.rank, self.suit)

def deck():
    deck = []
    for suit in SUIT_CHOICES:
        for rank in RANK_CHOICES:
            new_card = "%s of %s" % (rank, suit)
            deck.append(new_card)
    shuffle(deck)
    return deck

def dealHand(deck, hands=4):
    cards = len(deck)
    num = cards/hands
    return deck[:num], deck[num:num*2], deck[num*2:num*3], deck[num*3:num*4]


    
    



