#-*- coding: utf-8 -*-

__author__ = 'm.forys'

import permutation



class Deal:
    initial_position = 'S'
    cards = {}
    hands = {}

    def __init__(self, _position):
        self.initial_position = _position
        self.cards = self.init()
        self.hands = {
            'S': self.cards[:13],
            'W': self.cards[13:26],
            'N': self.cards[26:39],
            'E': self.cards[39:]
        }

    def init(self):
        self.cards =  permutation.create(52)
        return self.cards

    def get_hand(self, position):
        return self.hands[position]
