import pytest


import adventure.location as loc


def test_location_init():
    test_location = loc.Location()
    assert test_location != None

def test_location_has_a_name():
    home = loc.Location("Home")
    assert home.name == "Home"
