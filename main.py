#-*- coding: utf-8 -*-

__author__ = 'm.forys'

import deal
import bid
import output

deal_i = deal.create()

output.print_deal(deal_i)
output.print_cards_values_by_table(deal_i)
bid.start()
