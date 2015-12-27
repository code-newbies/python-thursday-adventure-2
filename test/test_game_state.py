""" Tests the game_state module """
import pytest


import adventure.game_state as subject


def test_game_state_starts_on_turn_zero():
    state = subject.State()
    assert 0 == state.turn
