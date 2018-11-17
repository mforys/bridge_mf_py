#-*- coding: utf-8 -*-

__author__ = 'm.forys'

card = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2")
color = ("S", "H", "D", "C")


class Card:
    def __init__(self, card_id):
        self.id = card_id
        self.rep = self.transfer_int_2_rep()

    def transfer_int_2_rep(self):
        color_i = int(self.id / 13)
        card_i = self.id % 13
        card_color = color[color_i]
        card_value = card[card_i]

        result = []
        result.extend(card_color)
        result.append(card_value)
        return result

    def transfer_int_2_string(self):
        result = ' '.join(self.rep)
        return result
