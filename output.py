#-*- coding: utf-8 -*-

__author__ = 'Marek'

import card
import hand


def print_cards_values_by_player(deal, position):
    """


    :rtype : object
    :param deal:
    :param position:
    """

    print("\nShow hand %s" % position)

    print_cards_values_by_color(deal, position, 'S')
    print_cards_values_by_color(deal, position, 'H')
    print_cards_values_by_color(deal, position, 'D')
    print_cards_values_by_color(deal, position, 'C')


def print_cards_values_by_color(deal, position, color):
    """


    :rtype : object
    :param deal:
    :param position:
    :param color:
    """

    unsorted_cards = hand.get_cards_values_by_color(deal, position, color)
    sorted_cards = hand.sort_A_2(unsorted_cards)
    values = ",".join(sorted_cards)
    print("%s: %s" % (color, values))


def print_cards_count_in_color_by_player(deal, position):
    print "\nPlayer = %s\n----------" % position
    print "S = %d" % hand.get_cards_color_count(deal, position, 'S')
    print "H = %d" % hand.get_cards_color_count(deal, position, 'H')
    print "D = %d" % hand.get_cards_color_count(deal, position, 'D')
    print "C = %d" % hand.get_cards_color_count(deal, position, 'C')
    print "======="


def print_cards_values_by_table(deal_i):
    """


    :rtype : object
    :param deal_i:
    """
    print("\nShow table\n----------------------")

    print_cards_values_by_player(deal_i, 'S')
    print_cards_values_by_player(deal_i, 'W')
    print_cards_values_by_player(deal_i, 'N')
    print_cards_values_by_player(deal_i, 'E')

    print("\nPoints\n--------")
    print("S = %d" % hand.get_points(deal_i, 'S'))
    print("W = %d" % hand.get_points(deal_i, 'W'))
    print("N = %d" % hand.get_points(deal_i, 'N'))
    print("E = %d" % hand.get_points(deal_i, 'E'))

    print("\nCount cards in color\n--------")
    print_cards_count_in_color_by_player(deal_i, 'S')
    print_cards_count_in_color_by_player(deal_i, 'W')
    print_cards_count_in_color_by_player(deal_i, 'N')
    print_cards_count_in_color_by_player(deal_i, 'E')


def print_deal(deal_i):
    for i in deal_i:
        card_i = card.Card(deal_i[i])
        card_rep_str = card_i.transfer_int_2_string()
        print("%d : %s" % (deal_i[i], card_rep_str))