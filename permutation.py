#-*- coding: utf-8 -*-

__author__ = 'm.forys'

import random


def create(n):
    result = []

    if n > 0:
        result = range(0, n)
        random.shuffle(result)
    return result
