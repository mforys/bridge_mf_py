#-*- coding: utf-8 -*-

__author__ = 'm.forys'

import itertools

import card


COLOR_SEQ = ['C', 'D', 'H', 'S', "NT"]

BIDS = itertools.product([1, 2, 3, 4, 5, 6, 7], COLOR_SEQ)


def __init__(self, volume, suit):
    self.volume = volume
    self.suit = suit


def get_all_bids():
    return itertools.product([1, 2, 3, 4, 5, 6, 7], card.color)


def print_all_bids():
    for i in BIDS:
        print(i)


def can_start_bidding(points):
    if points > 11:
        return True
    return False

