#-*- coding: utf-8 -*-

__author__ = 'm.forys'

import itertools

import card


COLOR_SEQ = ['C', 'D', 'H', 'S', "BA"]

#BIDS = itertools.product([1,2,3,4,5,6,7], list(card.color).reverse())
BIDS = itertools.product([1, 2, 3, 4, 5, 6, 7], COLOR_SEQ)


def get_all_bids():
    return itertools.product([1, 2, 3, 4, 5, 6, 7], card.color)


def start():
    """

    :rtype :
    """
    for i in BIDS:
        print(i)
#    print get_all_bids()


def can_start_bidding(cards):
    points = 12
    return True

