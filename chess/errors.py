# -*- coding: utf-8 -*-


"""
errors.py
Error Classes
"""


class MoveNotPossible(Exception):
	def __init__(self, move):
		super(MoveNotPossible, self).__init__("Move '" + str(move) + "' is not possible")


class InvalidMove(Exception):
	def __init__(self, move):
		super(InvalidMove, self).__init__("Move '" + str(move) + "' is invalid")


class InvalidFEN(Exception):
	def __init__(self, fen):
		super(InvalidFEN, self).__init__("FEN '" + str(fen) + "' is invalid")


class InvalidCoordinate(Exception):
	def __init__(self, coordinate):
		super(InvalidCoordinate, self).__init__("Coordinate '" + str(coordinate) + "' is invalid")


class InvalidColor(Exception):
	def __init__(self, message):
		super(InvalidColor, self).__init__(message)


class InvalidPiece(Exception):
	def __init__(self, piece):
		super(InvalidPiece, self).__init__("Piece '" + str(piece) + "' is invalid")


class UndefinedColor(Exception):
	def __init__(self, color):
		if color.lower() == "w":
			super(UndefinedColor, self).__init__("Color 'w' is invalid. Maybe you meant 'white'?")
		elif color.lower() == "b":
			super(UndefinedColor, self).__init__("Color 'b' is invalid. Maybe you meant 'black'?")
		else:
			super(UndefinedColor, self).__init__("Color '" + str(color) + "' is invalid")


class UndefinedPiece(Exception):
	def __init__(self, piece):
		super(UndefinedPiece, self).__init__("Piece '" + str(piece) + "' is invalid")


class UndefinedGamePhase(Exception):
	def __init__(self, phase):
		super(UndefinedGamePhase, self).__init__("Game phase '" + str(phase) + "' is invalid")


class InvalidLineCoordinates(Exception):
	def __init__(self, start, end):
		super(InvalidLineCoordinates, self).__init__("The starting position " + str(start) + " and ending position " + str(end) + " do not form a valid line")


class InvalidPGNLine(Exception):
	def __init__(self, line, line_number):
		super(InvalidPGNLine, self).__init__("Invalid PGN (line " + str(line_number) + "):\n  " + line)


class InvalidPGNMove(Exception):
	def __init__(self, move, move_number):
		super(InvalidPGNMove, self).__init__("Invalid move in PGN:\n  " + str(move_number) + ". " + move)
