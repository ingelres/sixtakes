# -*- coding: utf-8 -*-
#
# Author: François Ingelrest

import playerstype, random


class RandomPlayer(playerstype.Player):


    def __init__(self):
        """ Constructor """
        pass


    def desc(self):
        return 'Randomly choose a card to play or a row to take'


    def play(self, table, hand):
        """
            Choose a card at random in the hand
        """
        return random.randint(0, len(hand)-1)


    def take(self, table, playerstype, whoami):
        """
            Choose a row at random
        """
        return random.randint(0, len(table)-1)
