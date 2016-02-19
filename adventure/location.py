
class Location(object):
    # pylint: disable=too-few-public-methods
    # this is to temporarily disable this warning.  It should be removed once
    # there are 2 public methods.
    """This class encapsulates location information and behavior"""
    def __init__(self, name="Room"):
        self.name = name
