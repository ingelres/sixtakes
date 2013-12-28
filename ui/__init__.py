# -*- coding: utf-8 -*-
#
# Author: François Ingelrest


class DummyUI:
    """ Base class for a user interface """


    def __init__(self):
        """ Constructor """
        pass


    def display(self, table, hands, types, blockheads):
        """
            Display the current state of the game.

            @param table      A list of the table's rows of cards such as [[16, 31, 73], [54, 83], ...].
            @param hands      A list of the player's cards in ascending order such as [[12, 46, 98], [3, 45, 47, 71], ...].
            @param types      List of the players' types
            @param blockheads A list of the blockheads per player such as [12, 5, ...].
        """
        pass


    def pause(self):
        """
            Make a pause.
        """
        pass


    def quit(self):
        """
            Quit the user interface.
        """
        pass
