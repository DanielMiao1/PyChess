"""
test__.py
Tests File
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.curdir))
from ChessLibrary.ChessLibrary import *

import random


def test():
	game = Game()  # Create Game
	# Test moves
	# # Test with invalid move
	try:
		game.move(random.random())
	except errors.InvalidMove:
		pass
	else:
		raise Exception("Invalid move does not raise a InvalidMove error")
	# Test with random valid move
	game.move(random.choice(game.moves()))
