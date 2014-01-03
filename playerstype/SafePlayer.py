# -*- coding: utf-8 -*-
#
# Author: François Ingelrest

import playerstype, random

from playerstype import Player


class SafePlayer(playerstype.Player):


    def __init__(self):
        """ Constructor """
        pass


    def desc(self):
        return 'Play the shortest row'


    def play(self, table, hand):
        """
            Choose the smallest row, play the card that is the nearest of the last card of that row
        """
        for rowLen, rowIdx in sorted([(len(row), i) for i, row in enumerate(table)]):

            idx  = None
            card = table[rowIdx][-1]

            for (diff, i) in sorted([(hand[i] - card, i) for i in xrange(len(hand))]):
                if diff > 0:
                    return i

        return random.randint(0, len(hand)-1)


    def take(self, table, playerstype):
        """
            Choose the row with the smallest number of blockheads
        """
        return Player.getSmallestRow(self, table)
