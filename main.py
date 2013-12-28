#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: François Ingelrest

import os, playerstype, sys

from sixtakes    import SixTakes
from ui          import DummyUI
from ui.cursesui import CursesUI


def usage(error = None):
    """ Print usage  """
    print 'USAGE: %s NB_PLAYERS PLAYER_TYPE PLAYER_TYPE [PLAYER_TYPE, ...]' % os.path.basename(sys.argv[0])
    print
    print '    NB_PLAYERS  must be between 2 and 10'
    print '    PLAYER_TYPE must be one of the available players'
    print
    print 'Available players:'
    print

    for (name, instance) in playerstype.getAvailablePlayers():
        print '    %-15s %s' % (name, instance.desc())

    if error is not None:
        print '\n\nERROR: %s' % error

    sys.exit()


# Entry point
if len(sys.argv) < 2:
    usage()


players   = []
nbPlayers = 0


# Check the number of players
try:
    nbPlayers = int(sys.argv[1])

    if nbPlayers < 2 or nbPlayers > 10:
        raise Exception

except:
    usage('The number of player is invalid')


# Check that a valid player type has been chosen for each player
if len(sys.argv) != nbPlayers + 2:
    usage('A valid PLAYER_TYPE must be chosen for each player')

for type in sys.argv[2:]:
    try:
        players.append(playerstype.getAvailablePlayers()[[player[0] for player in playerstype.getAvailablePlayers()].index(type)])
    except:
        usage('"%s" is not a valid player' % type)


# Let's go
print SixTakes(players, DummyUI()).start()
