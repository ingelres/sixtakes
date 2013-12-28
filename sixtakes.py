# -*- coding: utf-8 -*-
#
# Author: François Ingelrest


import random

class SixTakes:

    __NB_CARDS         = 104
    __TABLE_ROWS       =   4
    __CARDS_PER_PLAYER =  10

    # Indexes for player's data
    (
        PIDX_NAME,
        PIDX_INSTANCE,
    ) = range(2)

    # Number of blockheads per card
    #
    # All allCards with values:
    #  - Containing a 5 have 2 blockheads
    #  - That are multiple of 10 have 3 blockheads
    #  - That are doublets (e.g., 11, 22) have 5 blockheads
    #
    # Card 55 is a doublet that contains a 5, thus it has 7 blockheads
    CARDS_BLOCKHEADS = (
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


    def __init__(self, players, ui):
        """
            @param players The list of players such as [(p1Name, p1Instance), (p2Name, p2Instance), ...].
            @param ui      The user interface to use.
        """
        self.ui        = ui
        self.nbPlayers = len(players)

        self.ptypes     = [players[i][0] for i in xrange(self.nbPlayers)]
        self.pinstances = [players[i][1] for i in xrange(self.nbPlayers)]

        self.allCards   = [i for i in xrange(1, self.__NB_CARDS+1)]
        self.table      = None
        self.hands      = None
        self.blockheads = None


    def start(self):
        """ Start a new game """
        random.shuffle(self.allCards)

        self.hands      = [sorted([self.allCards[i] for i in xrange(j*self.__CARDS_PER_PLAYER, (j+1)*self.__CARDS_PER_PLAYER)]) for j in xrange(self.nbPlayers)]
        self.table      = [[self.allCards[i]] for i in xrange(self.nbPlayers*self.__CARDS_PER_PLAYER, self.nbPlayers*self.__CARDS_PER_PLAYER+4)]
        self.blockheads = [0 for i in xrange(self.nbPlayers)]

        while len(self.hands[0]) != 0:

            self.ui.display(self.table, self.hands, self.ptypes, self.blockheads)

            # Make a list of the cards played by each player
            cards = sorted([(self.hands[i].pop(self.pinstances[i].play(self.table, self.hands[i])), i) for i in xrange(self.nbPlayers)])

            for (j, (card, playerIdx)) in enumerate(cards):
                rowIdx = None

                # Find the row which last card is the closest to the card being played
                for (diff, i) in sorted([(card - self.table[i][-1], i) for i in xrange(self.__TABLE_ROWS)]):
                    if diff > 0:
                        rowIdx = i
                        break

                # If the card's value is too low or if the row is full, the player takes a row
                if rowIdx is None or len(self.table[rowIdx]) == 5:

                    # Let the player choose the row since his card can't be played
                    if rowIdx is None:
                        rowIdx = self.pinstances[playerIdx].take(self.table, [(cards[k][0], self.blockheads[cards[k][1]]) for k in xrange(j+1, len(cards))])

                    self.blockheads[playerIdx] += sum([self.CARDS_BLOCKHEADS[rowcard] for rowcard in self.table[rowIdx]])
                    self.table[rowIdx]          = [card]
                else:
                    # The most common case: Append the card to the row
                    self.table[rowIdx].append(card)

            self.ui.pause()

        self.ui.quit()
