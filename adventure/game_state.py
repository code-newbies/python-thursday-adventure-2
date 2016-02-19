""" This module tracks the current status of the game """

class State(object):
    # pylint: disable=too-few-public-methods
    # this is to temporarily disable this warning.  It should be removed once
    # there are 2 public methods.
    """ This class encapsulates the current status of the game """
    def __init__(self):
        self.turn = 0
