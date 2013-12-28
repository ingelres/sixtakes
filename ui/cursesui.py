# -*- coding: utf-8 -*-
#
# Author: François Ingelrest

import curses, ui


class CursesUI(ui.UI):
    """ A user interface using ncurses """


    def __init__(self):
        """ Constructor """
        self.screen = curses.initscr()

        curses.noecho()


    def display(self, table, hands, types, blockheads):
        """ Display the current state of the game """
        self.screen.clear()
        self.screen.border(0)

        self.screen.addstr(3, 2, 'TABLE', curses.A_UNDERLINE)
        for i in xrange(4):
            self.screen.addstr(4+i, 6, ' '.join(['%3u' % v for v in table[i]]))

        self.screen.addstr(10, 2, 'PLAYERS', curses.A_UNDERLINE)
        for i in xrange(len(hands)):
            self.screen.addstr(12+i, 6, 'Player %u    Type: %15s    Blockheads: %2u    Hand: %s' % (i, types[i], blockheads[i], ' '.join(['%3u' % v for v in hands[i]])))

        self.screen.refresh()


    def pause(self):
        """ Make a pause """
        self.screen.getch()


    def quit(self):
        """ Quit the user interface """
        curses.endwin()
