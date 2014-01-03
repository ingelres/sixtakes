#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: François Ingelrest

import argparse, operator, os, playerstype, sys, tools, ui, ui.cursesui

from argparse import ArgumentParser
from sixtakes import SixTakes


# Create the command line parser
availablePlayers = 'Available players:\n\n' + '\n'.join(['    %-15s %s' % (name, inst.desc()) for (name, inst) in playerstype.getAvailablePlayers()])
mParser          = ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, epilog=availablePlayers)

mParser.add_argument('nbPlayers', metavar='NB_PLAYERS', type=int, help='Must be between 2 and 10')
mParser.add_argument('types', metavar='PLAYER', type=str, nargs='+', help='A player must be specified for each player in the game')
mParser.add_argument('-d', '--display', dest='display', action='store_true', help='Display the game proceedings (defaults to true when at least one player is human)')
mParser.add_argument('-i', '--iterations', dest='nbIters', type=int, default=1, help='Number of iterations (defaults to 1)')


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
if mArgs.display: display = ui.cursesui.CursesUI()
else:             display = ui.DummyUI()

game       = SixTakes(players, display)
victories  = [0 for i in xrange(mArgs.nbPlayers)]
blockheads = [0 for i in xrange(mArgs.nbPlayers)]

if not mArgs.display:
    print 'Simulations in progress...'

for i in xrange(mArgs.nbIters):

    if not mArgs.display and (i & 7) == 0:
        tools.progressbar(i, mArgs.nbIters, 20)

    results    = game.play()
    blockheads = map(operator.add, blockheads, results)

    victories[sorted([(v, i) for (i, v) in enumerate(results)])[0][1]] += 1

if not mArgs.display:
    tools.progressbar(mArgs.nbIters, mArgs.nbIters, 20)
    print '\n\n'

# Display results
longestName = max([len(player[0]) for player in players])

print 'By number of victories:'
for v, i in sorted([(v, i) for i, v in enumerate(victories)], reverse=True):
    print '    %s %4u - %.2f%%' % (players[i][0].ljust(longestName), victories[i], victories[i] * 100.0 / mArgs.nbIters)

print
print 'By number of blockheads:'
for v, i in sorted([(v, i) for i, v in enumerate(blockheads)]):
    print '    %s %4u - %.2f%%' % (players[i][0].ljust(longestName), blockheads[i], blockheads[i] * 100.0 / sum(blockheads))
