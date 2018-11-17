#-*- coding: utf-8 -*-

__author__ = 'm.forys'

position = ('S', 'W', 'N', 'E')

import card


def get(deal, position):
    """

    :param deal:
    :param position:
    :return:
    """
    return {
        'S': deal[:13],
        'W': deal[13:26],
        'N': deal[26:39],
        'E': deal[39:]
    }[position]


def get_cards_values(deal, position):

    """

    :param deal:
    :param position:
    :return:
    """
    cards = get(deal, position)

    values = []
    for i in range(len(cards)):
        val = card.Card(cards[i]).transfer_int_2_rep()
        values.append(val)

    return values


def get_cards_values_by_color(deal, position, color):

    """

    :param deal:
    :param position:
    :param color:
    :return:
    """
    cards = get_cards_values(deal, position)

    values = []
    for c in cards:
        if c[0] == color:
            values.append(c[1])

    return values


def is_between(x, y, z):
    if x in (y, z):
        return True
    return False


def card_order_key(x):
    if x == 'A':
        return 1
    if x == 'K':
        return 2
    if x == 'Q':
        return 3
    if x == 'J':
        return 4
    if x == "10":
        return 5
    if x == '9':
        return 6
    if x == '8':
        return 7
    if x == '7':
        return 8
    if x == '6':
        return 9
    if x == '5':
        return 10
    if x == '4':
        return 11
    if x == '3':
        return 12
    if x == '2':
        return 13


def sort_A_2(cards_in_color):
    cards_sorted = sorted(cards_in_color, key=card_order_key)
    return cards_sorted


def get_points(deal, position):
    cards = get_cards_values(deal, position)

    points = 0
    for c in cards:
        if c[1] == 'A':
            points += 4
        if c[1] == 'K':
            points += 3
        if c[1] == 'Q':
            points += 2
        if c[1] == 'J':
            points += 1

    return points


def get_cards_color_count(deal, position, color):

    """

    :param deal:
    :param position:
    :param color:
    :return:
    """

    cards = get_cards_values_by_color(deal, position, color)

    return len(cards)

