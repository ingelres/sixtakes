# -*- coding: utf-8 -*-
#
# Author: François Ingelrest

import playerstype, random

from playerstype import Player


class Player3(playerstype.Player):


    def __init__(self):
        """ Constructor """
        pass


    def desc(self):
        return 'Play the shortest row'


    def play(self, table, hand):
        """
            Play the card that should go in the row with the smallest number of cards.
        """
        best = (9999, -1)    # (score, index)

        for hidx, hcard in enumerate(hand):
            for tidx, trow in enumerate(table):

                diff = hcard - trow[-1]

                if diff > 0:

                    if diff <= 5 - len(trow):
                        score = len(trow) * 100 + diff
                    else:
                        score = len(trow) * 1000 + diff
                    score = len(trow) * 1000 + diff
                else:
                    score = 6000 + hcard

                if score < best[0]:
                    best = (score, hidx)

        return best[1]



    def take(self, table, playerstype):
        """
            Choose the row with the smallest number of blockheads
        """
        return Player.getSmallestRow(self, table)

