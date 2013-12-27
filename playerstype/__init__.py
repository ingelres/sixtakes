# -*- coding: utf-8 -*-
#
# Author: François Ingelrest

import os, sys, traceback


class Player:
    """ Base class for a six takes player """


    def __init__(self):
        """ Constructor """
        pass


    def desc(self):
        """
            @return A description of the player.
        """
        return 'Always play the first card and take the first row'


    def play(self, table, hand):
        """
            The player must choose which card he's going to play.

            @param table A list of the table's rows of cards such as [[16, 31, 73], [54, 83], ...].
            @param hand  A sorted list of the player's cards such as [3, 45, 47, 71, ...].

            @return The index of the hand's card to be played.
        """
        return 0


    def take(self, table, players, whoami):
        """
            The card played has a lower value than the last card of all the table's rows.
            The player must take one of the rows to put his own card instead.

            @param table   A list of the table's rows of cards such as [[16, 31, 73], [54, 83], ...].
            @param players A list of tuples giving the state of the current round such as [(p1Card, p1Score), (p2Card, p2Score), ...].
            @param whoami  The index of the current player in the players list.

            @return The index of the table's row the player wants to take.

            @note Only the players whose card has not been played yet are listed in players, so there may be only one tuple (the current player) in the list.
        """
        return 0


# Find available players
mPlayers    = []
mPlayersDir = os.path.dirname(__file__)

sys.path.append(mPlayersDir)

for file in [os.path.splitext(file)[0] for file in os.listdir(mPlayersDir) if file.endswith('.py') and file != '__init__.py']:
    try:
        mPlayers.append((file, getattr(__import__(file), file)()))
    except:
        print 'Unable to load module %s\n\n%s' % (file, traceback.format_exc())


def getAvailablePlayers():
    """
        @return A list of players such as [(name, instance), (name, instance), ...]
    """
    return mPlayers
