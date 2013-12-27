# -*- coding: utf-8 -*-
#
# Author: François Ingelrest


import random

class SixTakes:

    __NB_CARDS         = 104
    __TABLE_ROWS       =   4
    __CARDS_PER_PLAYER =  10

    # Number of blockheads per card
    #
    # All cards with values:
    #  - Containing a 5 have 2 blockheads
    #  - That are multiple of 10 have 3 blockheads
    #  - That are doublets (e.g., 11, 22) have 5 blockheads
    #
    # Card 55 is a doublet that contains a 5, thus it has 7 blockheads
    __CARDS_BLOCKHEADS = (
                            # 0  1  2  3  4  5  6  7  8  9
                              0, 1, 1, 1, 1, 2, 1, 1, 1, 1, #   0
                              3, 5, 1, 1, 1, 2, 1, 1, 1, 1, #  10
                              3, 1, 5, 1, 1, 2, 1, 1, 1, 1, #  20
                              3, 1, 1, 5, 1, 2, 1, 1, 1, 1, #  30
                              3, 1, 1, 1, 5, 2, 1, 1, 1, 1, #  40
                              3, 1, 1, 1, 1, 7, 1, 1, 1, 1, #  50
                              3, 1, 1, 1, 1, 2, 5, 1, 1, 1, #  60
                              3, 1, 1, 1, 1, 2, 1, 5, 1, 1, #  70
                              3, 1, 1, 1, 1, 2, 1, 1, 5, 1, #  80
                              3, 1, 1, 1, 1, 2, 1, 1, 1, 5, #  90
                              3, 1, 1, 1, 1                 # 100
                         )


    def __init__(self, players):
        """
            @param The list of players such as [(p1Name, p1Instance), (p2Name, p2Instance), ...]
        """
        self.players   = players
        self.nbPlayers = len(players)

        self.cards      = [i for i in xrange(1, self.__NB_CARDS+1)]
        self.table      = [[] for i in xrange(self.__TABLE_ROWS)]
        self.hands      = [[] for i in xrange(self.nbPlayers)]
        self.graveyards = [[] for i in xrange(self.nbPlayers)]


    def start(self):
        """ Start a new game """
        random.shuffle(self.cards)

        self.hands      = [sorted([self.cards[i] for i in xrange(j*self.__CARDS_PER_PLAYER, (j+1)*self.__CARDS_PER_PLAYER)]) for j in xrange(self.nbPlayers)]
        self.table      = [[self.cards[i]] for i in xrange(self.nbPlayers*self.__CARDS_PER_PLAYER, self.nbPlayers*self.__CARDS_PER_PLAYER+4)]
        self.graveyards = [[] for i in xrange(self.nbPlayers)]
