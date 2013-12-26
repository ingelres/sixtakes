#!/usr/bin/env python

import os, sys

from sixtakes import SixTakes


# Entry point
if len(sys.argv) < 2:
    print 'USAGE: %s NB_PLAYERS [PLAYER_TYPE, PLAYER_TYPE, ...]' % os.path.basename(sys.argv[0])
    print
    print '    NB_PLAYERS must be between 2 and 10'
    sys.exit()

# Check the number of players
try:
    nbPlayers = int(sys.argv[1])

    if nbPlayers < 2 or nbPlayers > 10:
        raise Exception

except:
    print 'The number of player is invalid'
    sys.exit()

game = SixTakes(nbPlayers)
