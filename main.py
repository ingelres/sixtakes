#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: François Ingelrest

import argparse, os, playerstype, sys

from argparse    import ArgumentParser
from sixtakes    import SixTakes
from ui          import DummyUI
from ui.cursesui import CursesUI


# Create the command line parser
availablePlayers = 'Available players:\n\n' + '\n'.join(['    %-15s %s' % (name, inst.desc()) for (name, inst) in playerstype.getAvailablePlayers()])
mParser          = ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, epilog=availablePlayers)

mParser.add_argument('nbPlayers', metavar='NB_PLAYERS', type=int, help='Must be between 2 and 10')
mParser.add_argument('types', metavar='PLAYER', type=str, nargs='+', help='A player must be specified for each player in the game')
mParser.add_argument('-d', '--display', dest='display', action='store_true', help='Display the game proceedings (defaults to true when at least one player is human)')


# Entry point
mArgs   = mParser.parse_args()
players = []

# Check the number of players
if mArgs.nbPlayers < 2 or mArgs.nbPlayers > 10:
    mParser.error('The number of players is invalid')

# Check that a valid player type has been chosen for each player
if len(mArgs.types) != mArgs.nbPlayers:
    mParser.error('A valid PLAYER must be chosen for each player')

for type in mArgs.types:
    try:
        players.append(playerstype.getAvailablePlayers()[[player[0] for player in playerstype.getAvailablePlayers()].index(type)])
    except:
        mParser.error('"%s" is not a valid player' % type)

# Let's go
if mArgs.display: ui = CursesUI()
else:             ui = DummyUI()

print SixTakes(players, ui).start()
