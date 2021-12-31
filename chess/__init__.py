# -*- coding: utf-8 -*-

import chess.errors
import chess.openings
import chess.functions

try:
	unicode
except NameError:
	unicode = str


class Color:
	white, black = "white", "black"
	current, any = "current", "any"

	@staticmethod
	def all():
		return [Color.white, Color.black]

	@staticmethod
	def invert(color):
		if not Color.valid(color):
			raise errors.UndefinedColor(color)
		elif Color.isWhite(color):
			return "black"
		else:
			return "white"

	@staticmethod
	def valid(color):
		return color in Color.all()

	@staticmethod
	def isWhite(color):
		return color in [Color.white, "w"]

	@staticmethod
	def isBlack(color):
		return color in [Color.black, "b"]


class PieceEnum:
	pawn, knight, bishop, rook = "pawn", "knight", "bishop", "rook"
	queen, king = "queen", "king"
	unicode_dictionary = {"whiteking": "♔", "blackking": "♚", "whitequeen": "♕", "blackqueen": "♛", "whiterook": "♖", "blackrook": "♜", "whitebishop": "♗", "blackbishop": "♝", "whiteknight": "♘", "blackknight": "♞", "whitepawn": "♙", "blackpawn": "♟"}
	piece_values = {"pawn": 1, "knight": 3, "bishop": 3, "rook": 5, "queen": 9, "king": float("inf")}
	piece_square_tables = {
		"middlegame": {
			"pawn": [[0, 0, 0, 0, 0, 0, 0, 0], [50, 50, 50, 50, 50, 50, 50, 50], [35, 35, 35, 35, 35, 35, 35, 35], [5, 5, 15, 14, 14, 15, 5, 5], [5, 5, 7, 12, 12, 7, 5, 5], [-4, -4, -4, -2, -2, -4, -4, -4], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]],
			"knight": [[-100, -70, -50, -50, -50, -50, -70, -100], [-70, -30, 0, 0, 0, 0, -30, -70], [-50, 10, 15, 16, 16, 15, 10, -50], [-30, 5, 8, 30, 30, 8, 5, -30], [-30, 4, 12, 15, 15, 12, 4, -30], [-50, 5, 15, 5, 5, 15, 5, -50], [-70, -50, -5, -2, -7, -5, -50, -70], [-100, -20, -50, -10, -10, -20, -20, -100]],
			"bishop": [[-20, 0, -2, -2, -2, -2, 0, -20], [-10, 0, 0, 0, 0, 0, 0, -10], [-6, 10, 8, 5, 5, 8, 10, -6], [-4, 15, 10, 9, 9, 10, 15, -4], [-2, 0, 20, 12, 12, 20, 0, -2], [-5, -5, 2, 15, 15, 2, -5, -5], [0, 30, -5, 5, 5, -5, 30, 0], [-50, -20, -10, -40, -40, -10, -20, -50]],
			"rook": [[10, 10, 10, 10, 10, 10, 10, 10], [25, 25, 25, 25, 25, 25, 25, 25], [5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5], [-5, -5, -5, -5, -5, -5, -5, -5], [-15, -15, -5, -15, -15, -15, -15, -15], [0, -5, 0, 10, 15, 10, -5, 0]],
			"queen": [[0, 30, 30, 40, 40, 30, 30, 0], [5, 20, 20, 25, 25, 20, 20, 5], [0, 20, 20, 25, 25, 20, 20, 0], [0, 20, 20, 20, 20, 20, 20, 6], [-2, 5, 5, 5, 5, 5, 5, -2], [-5, 0, 0, -5, -5, 6, 0, -5], [-10, -2, 0, 2, 2, 2, -2, -10], [-20, -19, -5, 5, 0, -5, -19, -20]],
			"king": [[-50, -50, -50, -50, -50, -50, -50, -50], [-50, -50, -50, -50, -50, -50, -50, -50], [-50, -50, -50, -50, -50, -50, -50, -50], [-50, -50, -50, -50, -50, -50, -50, -50], [-50, -50, -50, -50, -50, -50, -50, -50], [-50, -50, -50, -50, -50, -50, -50, -50], [-50, -50, -50, -45, -45, -50, -50, -50], [5, 7, 5, -10, 0, 0, 5, 7]]
		},
		"endgame": {
			"pawn": [[0, 0, 0, 0, 0, 0, 0, 0], [200, 200, 200, 200, 200, 200, 200, 200], [80, 80, 80, 80, 80, 80, 80, 80], [40, 30, 20, 10, 10, 20, 30, 40], [20, 10, 0, -2, -2, 0, 10, 20], [10, 10, 5, 0, 0, 5, 10, 10], [5, 5, 5, 5, 5, 5, 5, 5], [0, 0, 0, 0, 0, 0, 0, 0]],
			"knight": [[-100, -70, -50, -50, -50, -50, -70, -100], [-70, -30, 0, 0, 0, 0, -30, -70], [-50, 10, 15, 16, 16, 15, 10, -50], [-30, 5, 8, 30, 30, 8, 5, -30], [-30, 4, 12, 15, 15, 12, 4, -30], [-50, 5, 15, 5, 5, 15, 5, -50], [-70, -50, -5, -2, -7, -5, -50, -70], [-100, -150, -50, -10, -10, -20, -150, -100]],
			"bishop": [[-20, -10, -2, -2, -2, -2, -10, -20], [-10, 0, 0, 0, 0, 0, 0, -10], [-6, 10, 8, 5, 5, 8, 10, -6], [-4, 15, 10, 9, 9, 10, 15, -4], [-2, 0, 20, 12, 12, 20, 0, -2], [-5, -5, 2, 15, 15, 2, -5, -5], [0, 30, -5, 5, 5, -5, 30, 0], [-50, -20, -150, -40, -40, -150, -20, -50]],
			"rook": [[10, 10, 10, 10, 10, 10, 10, 10], [30, 30, 30, 30, 30, 25, 25, 25], [5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5], [-5, -5, -5, -5, -5, -5, -5, -5], [-15, -15, -5, -15, -15, -15, -15, -15], [0, -5, 0, 10, 15, 10, -5, 0]],
			"queen": [[20, 30, 30, 40, 40, 30, 30, 20], [5, 20, 20, 25, 25, 20, 20, 5], [0, 20, 20, 25, 25, 20, 20, 0], [0, 20, 20, 20, 20, 20, 20, 0], [5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5, 5, 5], [5, 5, 5, -150, 5, 5, 5, 5]],
			"king": [[-500, -250, -200, -200, -200, -200, -250, -500], [-250, 10, 10, 10, 10, 10, 10, -250], [-200, 10, 10, 10, 10, 10, 10, -200], [-200, 10, 10, 10, 10, 10, 10, -200], [-200, 10, 10, 10, 10, 10, 10, -200], [-200, 10, 10, 10, 10, 10, 10, -200], [-250, 0, 0, 0, 0, 0, 0, -250], [-500, -400, -350, -200, -200, -200, -400, -500]]
		}
	}

	@staticmethod
	def all():
		return [PieceEnum.pawn, PieceEnum.knight, PieceEnum.bishop, PieceEnum.rook, PieceEnum.queen, PieceEnum.king]

	@staticmethod
	def unicode(piece, color="white"):
		if not PieceEnum.valid(piece):
			raise errors.UndefinedPiece(piece)
			return False
		if not Color.valid(color):
			raise errors.UndefinedColor(color)
			return False
		return PieceEnum.unicode_dictionary[color + piece]

	@staticmethod
	def value(piece):
		try:
			piece = piece.piece_type
		except AttributeError:
			pass
		if PieceEnum.valid(piece):
			return PieceEnum.piece_values[piece]
		raise errors.UndefinedPiece(piece)

	@staticmethod
	def evaluate_piece_position(piece, position, color, game_phase):
		if not Phase.valid(game_phase):
			raise errors.UndefinedGamePhase(game_phase)
		if not PieceEnum.valid(piece):
			raise errors.UndefinedPiece(piece)
		if not Color.valid(color):
			raise errors.UndefinedColor(color)
		if color == Color.white:
			return PieceEnum.piece_square_tables["middlegame" if game_phase in [Phase.opening, Phase.middlegame] else "endgame"][piece][functions.coordinateToIndex(position)[0]][functions.coordinateToIndex(position)[1]]
		return list(reversed([list(reversed(i)) for i in PieceEnum.piece_square_tables["middlegame" if game_phase in [Phase.opening, Phase.middlegame] else "endgame"][piece]]))[functions.coordinateToIndex(position)[0]][functions.coordinateToIndex(position)[1]]

	@staticmethod
	def valid(piece):
		return piece in PieceEnum.all()


class Phase:
	opening, middlegame, endgame = "opening", "middlegame", "endgame"

	@staticmethod
	def all():
		return [Phase.opening, Phase.middlegame, Phase.endgame]

	@staticmethod
	def valid(phase):
		return phase in Phase.all()


class Castle:
	kingside, queenside = "kingside", "queenside"

	@staticmethod
	def all():
		return [Castle.kingside, Castle.queenside]

	@staticmethod
	def valid(castle):
		return castle in Castle.all()


class Stop:
	never, capture_piece, no_capture, piece = "never", "capture_piece", "no_capture", "piece"

	@staticmethod
	def all():
		return [Stop.never, Stop.capture_piece, Stop.no_capture, Stop.piece]

	@staticmethod
	def valid(stop):
		return stop in Stop.all()


class Move:
	def __init__(self, name, old_position, new_position, piece, is_capture=False, check=False, castle=None, castle_rook=None, double_pawn_move=False, en_passant=False, en_passant_position=None, promotion=False):
		self.piece = piece
		self.name = name
		self.old_position, self.new_position = old_position, new_position
		self.is_capture = is_capture
		self.check = check
		self.castle = castle
		self.castle_rook = castle_rook
		self.double_pawn_move = double_pawn_move
		self.en_passant = en_passant
		self.en_passant_position = en_passant_position
		self.promotion = promotion
		if is_capture and piece is not None:
			self.captured_piece = self.piece.board.pieceAt(new_position)
		else:
			self.captured_piece = None

	def visualized(self, print_result=False, empty_squares=" ", separators=True, old_position_symbol="□", new_position_symbol="■", capture_symbol="X"):
		if empty_squares == "":
			empty_squares = " "
		empty_squares = empty_squares[0]
		squares = []
		for x in range(8):
			row = []
			for y in range(8):
				row.append(old_position_symbol if functions.coordinateToIndex(self.old_position) == [x, y] else capture_symbol if functions.coordinateToIndex(self.new_position) == [x, y] and self.is_capture else new_position_symbol if functions.coordinateToIndex(self.new_position) == [x, y] else empty_squares)
			squares.append(row)
		if print_result:
			print(("---------------------------------\n" if separators else "") + ("\n---------------------------------\n" if separators else "\n").join([("| " if separators else "") + (" | " if separators else " ").join(i) + (" |" if separators else "") for i in squares]) + ("\n---------------------------------" if separators else ""))
		else:
			return ("---------------------------------\n" if separators else "") + ("\n---------------------------------\n" if separators else "\n").join([("| " if separators else "") + (" | " if separators else " ").join(i) + (" |" if separators else "") for i in squares]) + ("\n---------------------------------" if separators else "")

	__str__ = __repr__ = lambda self: str(self.name)


class MoveSet:
	def __init__(self, *moves):
		if len(moves) == 1 and isinstance(moves[0], (list, set, tuple)):
			self.moves = [i for i in list(moves[0]) if isinstance(i, Move)]
		else:
			self.moves = [i for i in moves if isinstance(i, Move)]

	def visualized(self, print_result=False, empty_squares=" ", separators=True, old_position_symbol="□", new_position_symbol="■", capture_symbol="X"):
		if empty_squares == "":
			empty_squares = " "
		empty_squares = empty_squares[0]
		squares = []
		for x in range(8):
			row = []
			for y in range(8):
				row.append(old_position_symbol if [x, y] in map(functions.coordinateToIndex, self.old_positions()) else capture_symbol if [x, y] in [i.new_position for i in self.moves if i.is_capture] else new_position_symbol if [x, y] in map(functions.coordinateToIndex, self.new_positions()) else empty_squares)
			squares.append(row)
		if print_result:
			print(("---------------------------------\n" if separators else "") + ("\n---------------------------------\n" if separators else "\n").join([("| " if separators else "") + (" | " if separators else " ").join(i) + (" |" if separators else "") for i in squares]) + ("\n---------------------------------" if separators else ""))
		else:
			return ("---------------------------------\n" if separators else "") + ("\n---------------------------------\n" if separators else "\n").join([("| " if separators else "") + (" | " if separators else " ").join(i) + (" |" if separators else "") for i in squares]) + ("\n---------------------------------" if separators else "")

	def old_positions(self):
		return [i.old_position for i in self.moves]

	def new_positions(self):
		return [i.new_position for i in self.moves]

	def __contains__(self, obj):
		if isinstance(obj, Move):
			return obj in self.moves
		return False

	def __add__(self, other):
		if isinstance(other, MoveSet):
			return MoveSet(self.moves + other.moves)
		if isinstance(other, Move):
			return MoveSet(self.moves + [other])
		if isinstance(other, (list, set, tuple)):
			new_set = MoveSet(self.moves)
			for i in other:
				new_set += i
			return new_set
		return self

	def __radd__(self, other):
		return self.__add__(other)

	def __iadd__(self, other):
		return self.__add__(other)

	def __sub__(self, other):
		if isinstance(other, MoveSet):
			new_set = MoveSet(self.moves)
			for i in other.moves:
				if i in self.moves:
					new_set.moves.remove(i)
			return new_set
		if isinstance(other, Move):
			return MoveSet([i for i in self.moves if i != other])
		if isinstance(other, (list, set, tuple)):
			new_set = MoveSet(self.moves)
			for i in other:
				new_set -= i
			return new_set
		return self

	def __rsub__(self, other):
		return self.__sub__(other)

	def __isub__(self, other):
		return self.__sub__(other)

	def __neg__(self):
		new_set = MoveSet(self.moves)
		for i in new_set:
			i.new_position, i.old_position = i.old_position, i.new_position
		return new_set

	def __pos__(self):
		return MoveSet(self.moves)

	def __len__(self):
		return len(self.moves)

	def __iter__(self):
		self.iter_position = 0
		return self

	def __next__(self):
		if self.iter_position < len(self.moves):
			self.iter_position += 1
			return self.moves[self.iter_position - 1]
		else:
			raise StopIteration

	def next(self):
		if self.iter_position < len(self.moves):
			self.iter_position += 1
			return self.moves[self.iter_position - 1]
		else:
			raise StopIteration

	__str__ = __repr__ = lambda self: ", ".join(map(str, self.moves))


class Line:
	def __init__(self, start, end, jump=False):
		self.start_position = start
		self.end_position = end
		if not jump:
			if start[0] == end[0]:
				self.positions = [start[0] + str(i) for i in range(int(start[1]) + 1, int(end[1]))]
			elif start[1] == end[1]:
				self.positions = [("a", "b", "c", "d", "e", "f", "g", "h")[i] + start[1] for i in range({"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}[start[0]] + 1, {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}[end[0]])]
			elif int(functions.coordinateToIndex(start)[1]) < int(functions.coordinateToIndex(end)[1]) and int(functions.coordinateToIndex(start)[0]) < int(functions.coordinateToIndex(end)[0]):
				pos1, pos2 = functions.coordinateToIndex(end)
				pos1, pos2 = pos1 - 1, pos2 - 1
				self.positions = []
				while [pos1, pos2] != functions.coordinateToIndex(start):
					if pos1 < 0 or 0 > pos2:
						raise errors.InvalidLineCoordinates(start, end)
					self.positions.append(functions.indexToCoordinate([pos1, pos2]))
					pos1, pos2 = pos1 - 1, pos2 - 1
			elif int(functions.coordinateToIndex(start)[1]) > int(functions.coordinateToIndex(end)[1]) and int(functions.coordinateToIndex(start)[0]) > int(functions.coordinateToIndex(end)[0]):
				pos1, pos2 = functions.coordinateToIndex(end)
				pos1, pos2 = pos1 + 1, pos2 + 1
				self.positions = []
				while [pos1, pos2] != functions.coordinateToIndex(start):
					if pos1 >= 8 or 8 <= pos2:
						raise errors.InvalidLineCoordinates(start, end)
					self.positions.append(functions.indexToCoordinate([pos1, pos2]))
					pos1, pos2 = pos1 + 1, pos2 + 1
			elif int(functions.coordinateToIndex(start)[1]) < int(functions.coordinateToIndex(end)[1]) and int(functions.coordinateToIndex(start)[0]) > int(functions.coordinateToIndex(end)[0]):
				pos1, pos2 = functions.coordinateToIndex(end)
				pos1, pos2 = pos1 + 1, pos2 - 1
				self.positions = []
				while [pos1, pos2] != functions.coordinateToIndex(start):
					if pos1 >= 8 or 0 > pos2:
						raise errors.InvalidLineCoordinates(start, end)
					self.positions.append(functions.indexToCoordinate([pos1, pos2]))
					pos1, pos2 = pos1 + 1, pos2 - 1
			elif int(functions.coordinateToIndex(start)[1]) > int(functions.coordinateToIndex(end)[1]) and int(functions.coordinateToIndex(start)[0]) < int(functions.coordinateToIndex(end)[0]):
				pos1, pos2 = functions.coordinateToIndex(end)
				pos1, pos2 = pos1 - 1, pos2 + 1
				self.positions = []
				while [pos1, pos2] != functions.coordinateToIndex(start):
					if pos1 < 0 or 8 <= pos2:
						raise errors.InvalidLineCoordinates(start, end)
					self.positions.append(functions.indexToCoordinate([pos1, pos2]))
					pos1, pos2 = pos1 - 1, pos2 + 1
			else:
				raise errors.InvalidLineCoordinates(start, end)
		else:
			self.positions = []

	def visualized(self, print_result=False, separators=True, empty_squares=" ", line_symbol="●", start_position_symbol="○", end_position_symbol="◎"):
		squares = [[empty_squares for _ in range(8)] for _ in range(8)]
		for i in self.positions:
			squares[functions.coordinateToIndex(i)[0]][functions.coordinateToIndex(i)[1]] = line_symbol
		squares[functions.coordinateToIndex(self.start_position)[0]][functions.coordinateToIndex(self.start_position)[1]] = start_position_symbol
		squares[functions.coordinateToIndex(self.end_position)[0]][functions.coordinateToIndex(self.end_position)[1]] = end_position_symbol
		if print_result:
			print(("---------------------------------\n| " if separators else "") + (" |\n---------------------------------\n| " if separators else "\n").join((" | " if separators else " ").join(i) for i in squares) + (" |\n---------------------------------" if separators else ""))
		else:
			return ("---------------------------------\n| " if separators else "") + (" |\n---------------------------------\n| " if separators else "\n").join((" | " if separators else " ").join(i) for i in squares) + (" |\n---------------------------------" if separators else "")

	def __str__(self):
		return self.visualized()

	def __repr__(self):
		return str(self.positions)

	def __unicode__(self):
		return self.visualized()

	def __contains__(self, item):
		return item in self.positions


class Square:
	"""A square"""
	def __init__(self, position, board):
		"""Initialize the square"""
		self.position = functions.indexToCoordinate(position)
		self.board = board
		if ((position[0] + position[1]) & 1) == 0:
			self.color = Color.white
		else:
			self.color = Color.black

	def __str__(self):
		return self.color.title() + " square from " + str(self.board)

	def __eq__(self, other):
		return self.position == other.position and isinstance(other, Square)

	def __unicode__(self):
		return self.color.title() + " square"

	__lt__ = __le__ = lambda self, *args: self.error(Exception("Cannot compare squares"))

	__add__ = __radd__ = __sub__ = __rsub__ = __mul__ = __rmul__ = __div__ = __rdiv__ = __truediv__ = __rtruediv__ = __floordiv__ = __rfloordiv__ = __mod__ = __rmod__ = __divmod__ = __rdivmod__ = __pow__ = __rpow__ = __lshift__ = __rlshift__ = __rshift__ = __rrshift__ = __and__ = __rand__ = __or__ = __ror__ = __xor__ = __rxor__ = __iadd__ = __isub__ = __imul__ = __idiv__ = __itruediv__ = __ifloordiv__ = __imod__ = __ipow__ = __iand__ = __ior__ = __ixor__ = __ilshift__ = __irshift__ = __neg__ = __pos__ = __abs__ = __invert__ = __int__ = __long__ = __float__ = __complex__ = __oct__ = __hex__ = __coerce__ = lambda self, *args: self.error(ArithmeticError("Cannot perform arithmetic operations on Square object"))

	__getitem__ = __setitem__ = __delitem__ = __getslice__ = __setslice__ = __delslice__ = __contains__ = lambda self, *args: self.board.error(IndexError("Cannot perform operation on Square"))


class Piece:
	def __init__(self, position, piece_type, color, board):
		"""Initialize the piece"""
		self.position = position if isinstance(position, str) else functions.indexToCoordinate(position)
		self.piece_type, self.color, self.board = piece_type, color, board
		self.moved = False
		self.en_passant = False

	def moveTo(self, position, override_pieces=True, evaluate_opening=True, evaluate_checks=True):
		"""Move the piece to a position"""
		if self.board.pieceAt(position) and override_pieces:
			self.board.pieces.remove(self.board.pieceAt(position))
			self.board.squares_hashtable[position] = False
		elif not override_pieces and self.board.pieceAt(position):
			self.board.pieceAt(position).position = self.position
		self.board.squares_hashtable[self.position], self.board.squares_hashtable[position] = self.board.squares_hashtable[position], self.board.squares_hashtable[self.position]
		self.position = position
		if evaluate_checks:
			for i in self.moves(show_data=True, evaluate_checks=False):
				if i.new_position == self.board.getKing(Color.invert(self.color)).position:
					self.board.in_check = Color.invert(self.color)
					break
		if evaluate_opening:
			self.board.updateOpening()

	def moves(self, show_data=False, evaluate_checks=True):
		"""Legal moves of the piece"""
		if self.board.game_over:
			return []
		moves = []
		if self.piece_type == PieceEnum.pawn:  # Pawn moves
			moves.extend(self.board.generatePawnCaptures(self.position, self.color, piece=self))
			moves.extend(self.board.generatePawnMoves(self.position, self.color, piece=self))
		elif self.piece_type == PieceEnum.knight:  # Knight moves
			moves.extend(self.board.generateKnightMoves(self.position, self.color, piece=self))
		elif self.piece_type == PieceEnum.bishop:  # Bishop moves
			moves.extend(self.board.generateBishopMoves(self.position, self.color, piece=self))
		if self.piece_type == PieceEnum.rook:  # Rook moves
			moves.extend(self.board.generateRookMoves(self.position, self.color, piece=self))
		elif self.piece_type == PieceEnum.queen:  # Queen moves
			moves.extend(self.board.generateQueenMoves(self.position, self.color, piece=self))
		elif self.piece_type == PieceEnum.king:
			if self.position[0] != "h" and self.position[1] != "1":
				if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] + 1])):
					valid = not self.board.protectors(self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] + 1])))
				else:
					valid = not self.board.attackers(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] + 1]), Color.invert(self.color))
				if valid:
					if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] + 1])):
						if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] + 1])).color != self.color:
							moves.append(Move(name="Kx" + functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] + 1]), old_position=self.position, new_position=functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] + 1]), piece=self, is_capture=True))
					else:
						moves.append(Move(name="K" + functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] + 1]), old_position=self.position, new_position=functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] + 1]), piece=self))
			if self.position[0] != "a" and self.position[1] != "8":
				if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] - 1])):
					valid = not self.board.protectors(self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] - 1])))
				else:
					valid = not self.board.attackers(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] - 1]), Color.invert(self.color))
				if valid:
					if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] - 1])):
						if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] - 1])).color != self.color:
							moves.append(Move(name="Kx" + functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] - 1]), old_position=self.position, new_position=functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] - 1]), piece=self, is_capture=True))
					else:
						moves.append(Move(name="K" + functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] - 1]), old_position=self.position, new_position=functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] - 1]), piece=self))
			if self.position[0] != "a" and self.position[1] != "1":
				if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] - 1])):
					valid = not self.board.protectors(self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] - 1])))
				else:
					valid = not self.board.attackers(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] - 1]), Color.invert(self.color))
				if valid:
					if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] - 1])):
						if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] - 1])).color != self.color:
							moves.append(Move(name="Kx" + functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] - 1]), old_position=self.position, new_position=functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] - 1]), piece=self, is_capture=True))
					else:
						moves.append(Move(name="K" + functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] - 1]), old_position=self.position, new_position=functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1] - 1]), piece=self))
			if self.position[0] != "h" and self.position[1] != "8":
				if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] + 1])):
					valid = not self.board.protectors(self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] + 1])))
				else:
					valid = not self.board.attackers(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] + 1]), Color.invert(self.color))
				if valid:
					if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] + 1])):
						if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] + 1])).color != self.color:
							moves.append(Move(name="Kx" + functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] + 1]), old_position=self.position, new_position=functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] + 1]), piece=self, is_capture=True))
					else:
						moves.append(Move(name="K" + functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] + 1]), old_position=self.position, new_position=functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1] + 1]), piece=self))
			if self.position[0] != "a":
				if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] - 1])):
					valid = not self.board.protectors(self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] - 1])))
				else:
					valid = not self.board.attackers(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] - 1]), Color.invert(self.color))
				if valid:
					if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] - 1])):
						if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] - 1])).color != self.color:
							moves.append(Move(name="Kx" + functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] - 1]), old_position=self.position, new_position=functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] - 1]), piece=self, is_capture=True))
					else:
						moves.append(Move(name="K" + functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] - 1]), old_position=self.position, new_position=functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] - 1]), piece=self))
			if self.position[0] != "h":
				if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] + 1])):
					valid = not self.board.protectors(self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] + 1])))
				else:
					valid = not self.board.attackers(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] + 1]), Color.invert(self.color))
				if valid:
					if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] + 1])):
						if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] + 1])).color != self.color:
							moves.append(Move(name="Kx" + functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] + 1]), old_position=self.position, new_position=functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] + 1]), piece=self, is_capture=True))
					else:
						moves.append(Move(name="K" + functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] + 1]), old_position=self.position, new_position=functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], functions.coordinateToIndex(self.position)[1] + 1]), piece=self))
			if self.position[1] != "1":
				if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1]])):
					valid = not self.board.protectors(self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1]])))
				else:
					valid = not self.board.attackers(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1]]), Color.invert(self.color))
				if valid:
					if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1]])):
						if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1]])).color != self.color:
							moves.append(Move(name="Kx" + functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1]]), old_position=self.position, new_position=functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1]]), piece=self, is_capture=True))
					else:
						moves.append(Move(name="K" + functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1]]), old_position=self.position, new_position=functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] + 1, functions.coordinateToIndex(self.position)[1]]), piece=self))
			if self.position[1] != "8":
				if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1]])):
					valid = not self.board.protectors(self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1]])))
				else:
					valid = not self.board.attackers(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1]]), Color.invert(self.color))
				if valid:
					if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1]])):
						if self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1]])).color != self.color:
							moves.append(Move(name="Kx" + functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1]]), old_position=self.position, new_position=functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1]]), piece=self, is_capture=True))
					else:
						moves.append(Move(name="K" + functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1]]), old_position=self.position, new_position=functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0] - 1, functions.coordinateToIndex(self.position)[1]]), piece=self))
			# Castling
			if self.board.castling_rights is not None and not self.moved and self.board.in_check != self.color:
				valid = True
				for x in self.board.pieceType(PieceEnum.rook, self.color):
					if x.position[1] == self.position[1] and not x.moved:
						if functions.coordinateToIndex(self.position)[1] < functions.coordinateToIndex(x.position)[1] and ((self.color == "white" and "K" in self.board.castling_rights) or (self.color == "black" and "k" in self.board.castling_rights)):
							for y in range(functions.coordinateToIndex(self.position)[1] + 1, functions.coordinateToIndex(x.position)[1]):
								if self.board.attackers(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], y]), Color.invert(self.color)) or self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], y])):
									valid = False
									break
							if valid:
								moves.append(Move("O-O", self.position, "g" + self.position[1], piece=self, castle=Castle.kingside, castle_rook=x))
							else:
								valid = True
								continue
						elif functions.coordinateToIndex(self.position)[1] > functions.coordinateToIndex(x.position)[1] and ((self.color == "white" and "Q" in self.board.castling_rights) or (self.color == "black" and "q" in self.board.castling_rights)):
							for y in range(functions.coordinateToIndex(x.position)[1] + 1, functions.coordinateToIndex(self.position)[1]):
								if self.board.attackers(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], y]), Color.invert(self.color)) or self.board.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(self.position)[0], y])):
									valid = False
									break
							if valid:
								moves.append(Move("O-O-O", self.position, "c" + self.position[1], piece=self, castle=Castle.queenside, castle_rook=x))
							else:
								valid = True
								continue
		check_line = self.board.checkLine()
		new_moves = []
		for x in moves:
			if self.board.in_check and self.piece_type != PieceEnum.king and x.new_position not in check_line.positions + [check_line.start_position]:
				continue
			if evaluate_checks:
				if self.piece_type == PieceEnum.pawn:
					if self.board.getKing(Color.invert(self.color)).position in [z.new_position for z in self.board.generatePawnCaptures(x.new_position, self.color)]:
						x.name += "+"
						x.check = True
				elif self.piece_type == PieceEnum.knight:
					if self.board.getKing(Color.invert(self.color)).position in [z.new_position for z in self.board.generateKnightMoves(x.new_position, self.color)]:
						x.name += "+"
						x.check = True
				elif self.piece_type == PieceEnum.bishop:
					if self.board.getKing(Color.invert(self.color)).position in [z.new_position for z in self.board.generateBishopMoves(x.new_position, self.color)]:
						x.name += "+"
						x.check = True
				elif self.piece_type == PieceEnum.rook:
					if self.board.getKing(Color.invert(self.color)).position in [z.new_position for z in self.board.generateRookMoves(x.new_position, self.color)]:
						x.name += "+"
						x.check = True
				elif self.piece_type == PieceEnum.queen:
					if self.board.getKing(Color.invert(self.color)).position in [z.new_position for z in self.board.generateQueenMoves(x.new_position, self.color)]:
						x.name += "+"
						x.check = True
			if show_data:
				new_moves.append(x)
			else:
				new_moves.append(x.name)
		return new_moves

	def __str__(self):
		return self.color.title() + " " + self.piece_type + " at " + self.position

	def __lt__(self, other):
		return PieceEnum.value(self.piece_type) < PieceEnum.value(other)

	def __le__(self, other):
		return PieceEnum.value(self.piece_type) <= PieceEnum.value(other)

	def __eq__(self, other):
		if isinstance(other, Piece):
			return {x: y for x, y in vars(self).items() if x != "board"} == {x: y for x, y in vars(other).items() if x != "board"}
		return False

	def __unicode__(self):
		return self.color.title() + " " + self.piece_type

	__add__ = __radd__ = __sub__ = __rsub__ = __mul__ = __rmul__ = __div__ = __rdiv__ = __truediv__ = __rtruediv__ = __floordiv__ = __rfloordiv__ = __mod__ = __rmod__ = __divmod__ = __rdivmod__ = __pow__ = __rpow__ = __lshift__ = __rlshift__ = __rshift__ = __rrshift__ = __and__ = __rand__ = __or__ = __ror__ = __xor__ = __rxor__ = __iadd__ = __isub__ = __imul__ = __idiv__ = __itruediv__ = __ifloordiv__ = __imod__ = __ipow__ = __iand__ = __ior__ = __ixor__ = __ilshift__ = __irshift__ = __neg__ = __pos__ = __abs__ = __invert__ = __int__ = __long__ = __float__ = __complex__ = __oct__ = __hex__ = __coerce__ = lambda self, *args: self.error(ArithmeticError("Cannot perform arithmetic operations on Piece object"))

	__getitem__ = __setitem__ = __delitem__ = __getslice__ = __setslice__ = __delslice__ = __contains__ = lambda self, *args: self.board.error(IndexError("Cannot perform operation on Piece"))


class Game:
	"""Game class"""
	def __init__(self, raise_errors=True, fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", evaluate_openings=False):
		"""Initialize"""
		if not functions.FENvalid(fen):
			fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
		self.tags = {"Result": "*"}
		self.opening = ""  # Opening
		self.evaluate_openings = evaluate_openings
		self.squares, self.pieces = [], []  # Pieces and squares
		self.squares_hashtable = {(x + str(y)): False for x in "abcdefgh" for y in range(1, 9)}  # Squares hashtable
		self.in_check = False  # False if neither side is in check, Color.white if white is in check, otherwise Color.black if black is in check
		self.game_over = False
		self.is_checkmate = False
		self.is_stalemate = False
		self.drawn = False
		self.checking_piece = None  # The piece checking a king, or None
		self.white_king = self.black_king = None
		# Append squares
		for x in range(8):
			self.squares.append([Square([x, y], self) for y in range(8)])
		self.raise_errors = raise_errors  # Raise errors
		# Load FEN-specific values
		self.loadFEN(fen, evaluate_opening=fen != "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

	def loadFEN(self, fen, evaluate_opening=True, evaluate_checks=True):
		"""Load/Reload with the specified FEN. Returns True if the FEN loaded successfully, otherwise False."""
		self.move_list, self.raw_move_list = "", []  # Move lists
		if not functions.FENvalid(fen):
			self.error(errors.InvalidFEN(fen))
			return False
		self.starting_fen = fen  # Set the starting FEN
		# Reset self.pieces
		if self.pieces:
			self.pieces = []
		self.captured_piece = sum([int(not unicode(y).isnumeric()) for x in fen.split(" ")[0].split("/") for y in x]) < 32  # If a piece has been captured
		self.turn = Color.white if fen.split(" ")[-5].lower() == "w" else Color.black  # The side to move
		self.half_moves = int(fen.split(" ")[-2])  # Halfmove clock
		self.full_moves = int(fen.split(" ")[-1])  # Fullmove clock
		self.castling_rights = fen.split(" ")[2] if fen.split(" ")[2] != "-" else None  # Castling rights
		self.en_passant_positions = fen.split(" ")[3] if fen.split(" ")[3] != "-" else None  # En passant pawns
		# Add pieces
		for i, j in enumerate(functions.splitNumbers(fen.split(" ")[0]).split("/")):
			for x, y in enumerate(j):
				if unicode(y).isnumeric():
					continue
				self.pieces.append(Piece(functions.indexToCoordinate([i, x]), PieceEnum.pawn if y.lower() == "p" else PieceEnum.knight if y.lower() == "n" else PieceEnum.bishop if y.lower() == "b" else PieceEnum.rook if y.lower() == "r" else PieceEnum.queen if y.lower() == "q" else PieceEnum.king, Color.white if y.isupper() else Color.black, self))
				self.squares_hashtable[functions.indexToCoordinate([i, x])] = self.pieces[-1]
				if self.pieces[-1].piece_type == PieceEnum.king:
					if self.pieces[-1].color == Color.white:
						self.white_king = self.pieces[-1]
					else:
						self.black_king = self.pieces[-1]
		# Load opening
		if evaluate_opening:
			self.updateOpening()
		if evaluate_checks:
			in_check = [self.pieceAt(i.new_position) for i in self.legal_moves(show_data=True, color=self.turn, evaluate_checks=False, evaluate_checkmate=False) if i.new_position == self.pieceType(PieceEnum.king, color=Color.invert(self.turn))[0].position]
			if in_check:
				self.in_check = in_check[0]
			else:
				self.in_check = False
		return True

	def loadPGN(self, pgn=None, file=None, quotes="\""):
		"""Loads the specified pgn. If the file argument is specified (is not None), loads the text of the file instead."""
		if file is pgn is None:
			return

		if file is not None:
			pgn = open(file).read()
		self.__init__()
		for x, y in enumerate(pgn.splitlines()):
			if y.strip() == "":
				continue
			if y.strip().startswith("[") and y.strip().endswith("]"):
				self.tags[y[1:y.index(quotes) - 1]] = y[y.index(quotes) + 1:-2]
				continue
			if y.startswith("1."):
				moves = functions.getMovesFromString(y)
				for i, j in enumerate(moves):
					try:
						if i == len(moves) - 1:
							self.move(j)
						else:
							self.move(j, evaluate_checks=False, evaluate_opening=False)
					except:
						self.error(errors.InvalidPGNMove(j, i))
						return False
			else:
				self.error(errors.InvalidPGNLine(y, x + 1))
				return False

	def loadOpening(self, opening_name):
		"""Load an opening"""
		for i in openings.openings:
			if opening_name.lower().replace("king's pawn game", "open game").replace("queen's pawn game", "closed game").replace("russian game", "petrov's defense") in [i["name"].lower(), i["eco"].lower() + " " + i["name"].lower(), i["eco"].lower() + i["name"].lower(), i["eco"].lower().replace("'", ""), i["eco"].lower() + " " + i["name"].lower().replace("'", ""), i["eco"].lower() + i["name"].lower().replace("'", "")]:
				self.loadFEN(i["fen"] + " - 0 1")
				return True
		return False

	def reset(self):
		"""Reset game"""
		self.loadFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

	def FEN(self):
		"""Returns the FEN of the game"""
		fen = ""  # Set fen variable
		# Get squares
		for x in self.squares:
			for y in x:
				if self.pieceAt(y.position):
					fen += (self.pieceAt(y.position).piece_type[0] if self.pieceAt(y.position).piece_type != PieceEnum.knight else "n").upper() if self.pieceAt(y.position).color == Color.white else (self.pieceAt(y.position).piece_type[0] if self.pieceAt(y.position).piece_type != PieceEnum.knight else "n")
				else:
					fen += "1"
			fen += "/"
		fen = functions.combineNumbers(fen[:-1])
		fen += " " + self.turn[0]  # Add the side to move
		fen += " " + (self.castling_rights if self.castling_rights is not None else "-")  # Castling rights
		fen += " " + (self.en_passant_positions if self.en_passant_positions is not None else "-")  # En Passant captures
		fen += " " + str(self.half_moves) + " " + str(self.full_moves)  # Add halfmove and fullmove clock
		return fen

	def PGN(self, **kwargs):
		"""Returns the PGN of the game."""
		pgn = ""
		for i in kwargs:
			pgn += "[" + i + " \"" + str(kwargs[i]) + "\"]\n"
		pgn += ("\n" if kwargs else "") + self.move_list + str(self.tags["Result"])
		return pgn

	def error(self, error):
		"""Raises an error if allowed"""
		if self.raise_errors:
			raise error

	def placePiece(self, coordinate, color, piece_type):
		"""Places a piece with the specified properties at position `coordinate`, overriding any existing pieces on the coordinate."""
		if self.pieceAt(coordinate):
			self.pieces.remove(self.pieceAt(coordinate))
		self.pieces.append(Piece(coordinate, piece_type, color, self))
		self.squares_hashtable[coordinate] = self.pieces[-1]

	def getKing(self, color):
		"""Get the king of color `color`"""
		if not Color.valid(color):
			self.error(errors.UndefinedColor(color))
			return None

		if color == Color.white:
			return self.white_king
		return self.black_king

	def checkLine(self):
		if not self.in_check:
			return False
		return Line(self.checking_piece.position, self.getKing(self.in_check).position, jump=self.checking_piece.piece_type == PieceEnum.knight)

	def move(self, move, evaluate_checks=True, evaluate_opening=True, evaluate_move_checks=True, evaluate_move_checkmate=True):
		"""Moves the specified move, if possible"""
		if isinstance(move, Move):  # If move is a Move object
			if move.is_capture:  # If the move is a capture
				self.pieces.remove(self.squares_hashtable[move.new_position])  # Remove the captured piece from the list of pieces
				# Update the hashtable
				self.squares_hashtable[move.new_position] = move.piece
				self.squares_hashtable[move.old_position] = False
				if not self.captured_piece:
					self.captured_piece = True  # Set captured piece to True
			else:
				self.squares_hashtable[move.piece.position], self.squares_hashtable[move.new_position] = self.squares_hashtable[move.new_position], self.squares_hashtable[move.piece.position]  # Move the piece in the hashtable
			move.piece.position = move.new_position  # Move the position of the piece to the new position
			move.piece.moved = True

			if move.castle_rook:  # If the move is a castle
				move.castle_rook.moved = True
				if move.castle == Castle.kingside:  # Kingside castling
					# Move the rook's position to the f-file
					self.squares_hashtable[move.castle_rook.position], self.squares_hashtable["f" + move.castle_rook.position[1]] = self.squares_hashtable["f" + move.castle_rook.position[1]], self.squares_hashtable[move.castle_rook.position]
					move.castle_rook.position = "f" + move.castle_rook.position[1]
				else:  # Queenside castling
					# Move the rook's position to the d-file
					self.squares_hashtable[move.castle_rook.position], self.squares_hashtable["d" + move.castle_rook.position[1]] = self.squares_hashtable["d" + move.castle_rook.position[1]], self.squares_hashtable[move.castle_rook.position]
					move.castle_rook.position = "d" + move.castle_rook.position[1]

			# Reset piece giving check
			self.checking_piece = None

			# Reset en passant positions
			self.en_passant_positions = None
			for i in self.pieces:
				i.en_passant = False

			if move.double_pawn_move:  # If the move is a double pawn push
				move.piece.en_passant = True  # Enable en passant for the piece
				self.en_passant_positions = move.new_position[0] + str(int(move.new_position[1]) - (1 if move.piece.color == Color.white else -1))  # Append position to en passant positions

			if move.en_passant:  # If the move is an en passant capture
				# Remove captured pawn
				self.pieces.remove(self.squares_hashtable[move.en_passant_position])
				self.squares_hashtable[move.en_passant_position] = False
				self.captured_piece = True

			if self.castling_rights is not None and move.piece.piece_type == PieceEnum.king:  # If the king moved
				if move.piece.color == Color.white:  # If the king is white
					self.castling_rights = self.castling_rights.replace("K", "").replace("Q", "")  # Disable white castling
				else:  # If the king is black
					self.castling_rights = self.castling_rights.replace("k", "").replace("q", "")  # Disable black castling

				if self.castling_rights == "":  # If the castling rights variable becomes an empty string
					self.castling_rights = None  # Set the variable to None

			if self.castling_rights is not None and move.piece.piece_type == PieceEnum.rook:  # If the rook moved
				if move.old_position == "a1":  # If the rook was on a1
					self.castling_rights = self.castling_rights.replace("Q", "")  # Disable white queenside castling
				elif move.old_position == "a8":  # If the rook was on a8
					self.castling_rights = self.castling_rights.replace("q", "")  # Disable black queenside castling
				elif move.old_position == "h1":  # If the rook was on h1
					self.castling_rights = self.castling_rights.replace("K", "")  # Disable white kingside castling
				elif move.old_position == "h8":  # If the rook was on h8
					self.castling_rights = self.castling_rights.replace("k", "")  # Disable black kingside castling

			if i.promotion:
				i.piece.piece_type = {"N": PieceEnum.knight, "B": PieceEnum.bishop, "R": PieceEnum.rook, "Q": PieceEnum.queen}[i.promotion]

			self.raw_move_list.append(move)  # Append move to the raw move list

			if self.in_check:  # If a king was in check before this move
				# This move must have gotten out of check
				self.in_check = False
				self.checking_piece = None
			else:  # Otherwise
				if evaluate_checks:  # If the evaluate_checks parameter is True
					if any([True for i in self.legal_moves(show_data=True, color=self.turn, evaluate_checks=evaluate_move_checks, evaluate_checkmate=evaluate_move_checkmate) if i.new_position == self.pieceType(PieceEnum.king, color=Color.invert(self.turn))[0].position]):  # If the king can be captured
						move.name += "+"  # Append a check symbol to the end of the move
						self.in_check = Color.invert(self.turn)  # Set in_check variable
						self.checking_piece = move.piece
					else:  # Otherwise
						self.in_check = False  # Set in_check to False
						self.checking_piece = None  # Reset piece giving check

			if self.turn == Color.white:  # If white moved
				# Add move to move list
				if self.move_list == "":  # If there has not been any moves
					self.move_list += "1. " + move.name
				else:  # Otherwise
					self.move_list += " " + str(int(self.move_list.split(" ")[-3][0]) + 1) + ". " + move.name
			else:  # If black moved
				if self.move_list == "":  # Check for custom FENs
					self.move_list += "1. ... " + move.name  # Add move to move list
				else:
					self.move_list += " " + move.name  # Add move to move list
				self.full_moves += 1  # Increase fullmove counter
			# Calculate halfmove counter
			if move.is_capture or move.piece.piece_type == PieceEnum.pawn:  # Reset halfmove counter if the move is a pawn move or a capture
				self.half_moves = 0
			else:  # Otherwise, increase the halfmove counter by 1
				self.half_moves += 1
			self.turn = Color.invert(self.turn)  # Invert turn
			# Get opening
			if evaluate_opening:
				self.updateOpening()

			if not self.legal_moves(evaluate_checks=evaluate_move_checks, evaluate_checkmate=evaluate_move_checkmate):
				self.game_over = True
				if self.in_check:
					self.is_checkmate = True
					self.tags["Result"] = "1-0" if self.turn == Color.black else "0-1"
				else:
					self.drawn = True
					self.is_stalemate = True
					self.tags["Result"] = "1/2-1/2"

			return move  # Return the applied move

		if not isinstance(move, str):  # If move is not a string, raise an error and return False
			self.error(errors.InvalidMove(move))
			return False

		if " " in move:
			for i in move.split(" ")[:-1]:
				self.move(i, evaluate_checks=False, evaluate_move_checks=False, evaluate_opening=False)
			move = move.split(" ")[-1]

		move = functions.toSAN(move, self)  # Convert to SAN
		legal_moves = self.legal_moves(show_data=True, evaluate_checks=evaluate_move_checks, evaluate_checkmate=evaluate_move_checkmate)  # Store legal moves in legal_moves variable
		move_data = None

		# Iterate through the legal moves
		for i in legal_moves:
			if i.name == move:  # If the name of the current move is the move specified
				move_data = i  # Set move_data equal to the current move
				if i.is_capture:  # If the move is a capture
					# Remove the captured piece
					self.pieces.remove(self.squares_hashtable[i.new_position])
					self.squares_hashtable[i.new_position] = False
					self.captured_piece = True

				self.squares_hashtable[i.piece.position], self.squares_hashtable[i.new_position] = self.squares_hashtable[i.new_position], self.squares_hashtable[i.piece.position]
				i.piece.position = i.new_position
				i.piece.moved = True
				if i.castle_rook:  # If the move is a castle
					i.castle_rook.moved = True
					if i.castle == Castle.kingside:  # Kingside castling
						# Move the rook's position to the f-file
						self.squares_hashtable[i.castle_rook.position], self.squares_hashtable["f" + i.castle_rook.position[1]] = self.squares_hashtable["f" + i.castle_rook.position[1]], self.squares_hashtable[i.castle_rook.position]
						i.castle_rook.position = "f" + i.castle_rook.position[1]
					else:  # Queenside castling
						# Move the rook's position to the d-file
						self.squares_hashtable[i.castle_rook.position], self.squares_hashtable["d" + i.castle_rook.position[1]] = self.squares_hashtable["d" + i.castle_rook.position[1]], self.squares_hashtable[i.castle_rook.position]
						i.castle_rook.position = "d" + i.castle_rook.position[1]

				# Clear en passant positions
				self.en_passant_positions = None
				for x in self.pieces:
					x.en_passant = False

				# If the move was a double pawn push
				if i.double_pawn_move:
					i.piece.en_passant = True  # Set en_passant variable of moved piece to true
					self.en_passant_positions = i.new_position[0] + str(int(i.new_position[1]) - (1 if i.piece.color == Color.white else -1))  # Append en passant position to en_passant_positions variable

				# If the move was an en passant capture
				if i.en_passant:
					# Remove the captured piece
					self.pieces.remove(self.squares_hashtable[i.en_passant_position])
					self.squares_hashtable[i.en_passant_position] = False
					self.captured_piece = True

				if self.castling_rights is not None and i.piece.piece_type == PieceEnum.king:  # If the piece moved was a king
					if i.piece.color == Color.white:  # If moved side is white
						self.castling_rights = self.castling_rights.replace("K", "").replace("Q", "")  # Disable white castling
					else:  # Otherwise (if moved side is black)
						self.castling_rights = self.castling_rights.replace("k", "").replace("q", "")  # Disable black castling
					if self.castling_rights == "":  # If the castling_rights variable is now an empty string
						self.castling_rights = None  # Set the castling_rights variable to None

				if self.castling_rights is not None and i.piece.piece_type == PieceEnum.rook:  # If the piece moved was a rook
					if i.old_position == "a1":  # If the rook was on a1
						self.castling_rights = self.castling_rights.replace("Q", "")  # Disable white queenside castling
					elif i.old_position == "a8":  # If the rook was on a8
						self.castling_rights = self.castling_rights.replace("q", "")  # Disable black queenside castling
					elif i.old_position == "h1":  # If the rook was on h1
						self.castling_rights = self.castling_rights.replace("K", "")  # Disable white kingside castling
					elif i.old_position == "h8":  # If the rook was on h8
						self.castling_rights = self.castling_rights.replace("k", "")  # Disable black kingside castling

				if i.promotion:
					i.piece.piece_type = {"N": PieceEnum.knight, "B": PieceEnum.bishop, "R": PieceEnum.rook, "Q": PieceEnum.queen}[i.promotion]

				self.raw_move_list.append(i)  # Append the move to the raw_move_list list
				break  # Break from the loop

		if move_data is None:  # If move_data is None (no move was found), raise an error and return False
			self.error(errors.MoveNotPossible(move))
			return False
		if self.in_check:  # If a king was in check before this move
			# This move must have gotten out of check
			self.in_check = False
			self.checking_piece = None
		else:  # Otherwise
			if evaluate_checks:  # If the evaluate_checks parameter is True
				if any([True for i in self.legal_moves(show_data=True, color=self.turn, evaluate_checks=evaluate_move_checks, evaluate_checkmate=evaluate_move_checkmate) if i.new_position == self.pieceType(PieceEnum.king, color=Color.invert(self.turn))[0].position]):  # If the king can be captured
					self.in_check = Color.invert(self.turn)  # Set in_check variable
					self.checking_piece = move_data.piece
				else:  # Otherwise
					self.in_check = False  # Set in_check to False
					self.checking_piece = None  # Reset piece giving check

		# Add move to move list and increase fullmove counter if necessary
		if self.turn == Color.white:  # If white moved
			# Add move to move list
			if self.move_list == "":  # If there has not been any moves
				self.move_list += "1. " + move  # Add a "1. " before the move string to the moves list
			else:  # Otherwise
				self.move_list += " " + str(int(self.move_list.split(" ")[-3][0]) + 1) + ". " + move  # Add a space character, the move number, followed by a period before the move string to the moves list
		else:  # If black moved
			if self.move_list == "":  # If there has not been any moves (a custom FEN)
				self.move_list += "1. ... " + move  # Add a "1. ..." string before the move name to the moves list
			else:  # Otherwise
				self.move_list += " " + move  # Add move name (preceded by a space) to move list

			self.full_moves += 1  # Increase the fullmove counter

		# Calculate halfmove counter
		if move_data.is_capture or move_data.piece.piece_type == PieceEnum.pawn:  # Reset halfmove counter if the move is a pawn move or a capture
			self.half_moves = 0
		else:  # Otherwise, increase the halfmove counter by 1
			self.half_moves += 1

		self.turn = Color.invert(self.turn)  # Invert turn

		if evaluate_opening:  # If the evaluate_opening parameter is True
			self.updateOpening()  # Update the opening using the updateOpening function

		if not self.legal_moves(evaluate_checks=False, evaluate_checkmate=False):
			self.game_over = True
			if self.in_check:
				self.is_checkmate = True
				self.tags["Result"] = "1-0" if self.turn == Color.black else "0-1"
			else:
				self.drawn = True
				self.is_stalemate = True
				self.tags["Result"] = "1/2-1/2"

		return move_data  # Return the move data (Move object)

	def legal_moves(self, show_data=False, color=Color.current, evaluate_checks=True, evaluate_checkmate=True, piece_type=PieceEnum.all()):
		"""Returns all legal moves by pieces of type(s) piece_type"""
		moves = []  # Define empty moves list

		if color == Color.current:
			color = self.turn

		if isinstance(piece_type, (list, set, tuple)):  # If the piece_type parameter is an iterable
			pieces = {"pawn": [], "knight": [], "bishop": [], "rook": [], "queen": [], "king": []}  # Define hashtable of piece types

			for i in self.pieces:  # Iterate through pieces
				if color == Color.any or i.color == color:
					pieces[i.piece_type].append(i)  # Append piece to respective list in pieces hashtable

			for x in piece_type:  # Iterate through the piece types
				for y in pieces[x]:  # Iterate through the pieces of this type
					moves.extend(y.moves(show_data, evaluate_checks=evaluate_checks))  # Append the piece moves
		elif piece_type in PieceEnum.all():  # If the piece type is a single type
			for i in self.pieceType(piece_type):  # Iterate through the pieces of the specified type
				if color == Color.any or i.color == color:  # If the specified color(s) includes the piece color
					moves.extend(i.moves(show_data, evaluate_checks=evaluate_checks))  # Append the piece moves

		return moves  # Return result

	def pieceType(self, piece, color=Color.any):
		"""Returns all pieces with type `piece` and color `color`"""
		if color == Color.any:
			color = [Color.white, Color.black]
		elif color == Color.current:
			color = [self.turn]
		else:
			color = [color]

		return [i for i in self.pieces if i.color in color and i.piece_type == piece]

	def gamePhase(self):
		"""Returns the current game phase"""
		# The game is in the opening phase if there are less than 7 full moves or a piece has not been captured
		if len(self.raw_move_list) // 2 <= 6 or not self.captured_piece:
			return Phase.opening

		# If the game is not in the opening phase, it is in the endgame phase if both sides do not have a queen, or if the king moved more than three times
		if not self.pieceType(PieceEnum.queen) or [i.piece.piece_type for i in self.raw_move_list].count(PieceEnum.king) > 3:
			return Phase.endgame

		return Phase.middlegame  # Otherwise, the game must be in the middlegame phase

	def totalMaterial(self):
		"""The total amount of material"""
		material = 0
		for i in self.pieces:
			if i.piece_type != PieceEnum.king:
				material += PieceEnum.value(i.piece_type)
		return material

	def materialDifference(self):
		"""Returns the material difference. Positive values indicate white has more material, while negative values indicate black has more."""
		difference = 0
		for i in PieceEnum.all():
			if i == PieceEnum.king:
				continue

			difference += sum([PieceEnum.value(x) for x in self.pieceType(i, Color.white)]) - sum([PieceEnum.value(x) for x in self.pieceType(i, Color.black)])

		return difference

	def evaluate(self):
		"""Evaluates the current position"""
		evaluation_centipawns = (self.materialDifference() * 100) + (0.1 * (len(self.legal_moves(color=Color.white)) - len(self.legal_moves(color=Color.black))))  # Material difference + piece mobility

		for i in self.pieces:
			evaluation_centipawns += PieceEnum.evaluate_piece_position(i.piece_type, i.position, i.color, self.gamePhase()) / 10

		return round(evaluation_centipawns / 100, 5)

	def pieceAt(self, coordinate):
		"""Returns the piece at coordinate if one exists, otherwise return None"""
		if not functions.coordinateValid(coordinate):  # If the coordinate is not valid, raise an error and return None
			self.error(errors.InvalidCoordinate(coordinate))
			return None
		if self.squares_hashtable[coordinate]:
			return self.squares_hashtable[coordinate]
		return None

	def takeback(self):
		"""Take backs one move. To take back multiple moves, call the function multiple times."""
		# TODO: update fullmove and halfmove counters
		# TODO: update in_check variable
		if not self.raw_move_list:  # If there has not been any moves, return
			return

		# Reset the moved piece's position
		self.squares_hashtable[self.raw_move_list[-1].piece.position], self.squares_hashtable[self.raw_move_list[-1].old_position] = self.squares_hashtable[self.raw_move_list[-1].old_position], self.squares_hashtable[self.raw_move_list[-1].piece.position]
		self.raw_move_list[-1].piece.position = self.raw_move_list[-1].old_position

		if self.raw_move_list[-1].is_capture:  # If the last move was a capture
			# Bring back the captured piece
			self.pieces.append(Piece(self.raw_move_list[-1].new_position, self.raw_move_list[-1].captured_piece.piece_type, self.raw_move_list[-1].captured_piece.color, self))
			self.squares_hashtable[self.raw_move_list[-1].new_position] = self.pieces[-1]

		# Reset the castle rook's position if the last move was a castle
		if self.raw_move_list[-1].castle == Castle.kingside:  # If the last move was a kingside castle
			self.squares_hashtable[self.raw_move_list[-1].castle_rook.position], self.squares_hashtable["h" + self.raw_move_list[-1].castle_rook.position[1]] = self.squares_hashtable["h" + self.raw_move_list[-1].castle_rook.position[1]], self.squares_hashtable[self.raw_move_list[-1].castle_rook.position]
			self.raw_move_list[-1].castle_rook.position = "h" + self.raw_move_list[-1].castle_rook.position[1]
		elif self.raw_move_list[-1].castle == Castle.queenside:  # If the last move was a queenside castle
			self.squares_hashtable[self.raw_move_list[-1].castle_rook.position], self.squares_hashtable["f" + self.raw_move_list[-1].castle_rook.position[1]] = self.squares_hashtable["f" + self.raw_move_list[-1].castle_rook.position[1]], self.squares_hashtable[self.raw_move_list[-1].castle_rook.position]
			self.raw_move_list[-1].castle_rook.position = "f" + self.raw_move_list[-1].castle_rook.position[1]

		# If the last move was a promotion
		if self.raw_move_list[-1].promotion:
			self.raw_move_list[-1].piece.piece_type = PieceEnum.pawn  # Make the promoted piece a pawn

		self.raw_move_list.pop()  # Remove the last move from the raw move list

		# Remove the last move from the move list
		if self.move_list.split(" ")[-2][-1] == ".":
			self.move_list = " ".join(self.move_list.split(" ")[:-2])
		else:
			self.move_list = " ".join(self.move_list.split(" ")[:-1])

		self.turn = Color.invert(self.turn)  # Invert the turn
		self.en_passant_positions = None  # Reset en_passant_positions
		# Set opening
		if self.move_list == "":
			self.opening = ""
		else:
			self.updateOpening()

	def updateOpening(self):
		"""Updates the opening if evaluate_openings is True"""
		if self.evaluate_openings:
			opening = False
			for i in openings.openings:
				if i["position"] == self.FEN().split(" ")[0]:
					self.opening = i["eco"] + " " + i["name"]
					opening = i["eco"] + " " + i["name"]
					break
			return opening
		else:
			return False

	def attackers(self, coordinate, color):
		"""Returns a list of the pieces that attack the coordinate"""
		if color == Color.current:
			color = self.turn
		if color not in [Color.white, Color.black]:
			self.error(errors.UndefinedColor(color))
			return []
		if self.pieceAt(coordinate) and self.pieceAt(coordinate).color == color:
			self.error(errors.InvalidColor("The color " + str(color) + " is invalid, as the piece at " + str(coordinate) + " has the same color. Perhaps you meant to use the protectors() function?"))
			return []
		attackers = []
		for i in self.pieces:
			if i.color != color:
				continue
			if i.piece_type == PieceEnum.pawn:  # Pawn capture squares
				if coordinate in [x.new_position for x in self.generatePawnCaptures(i.position, color, return_all=True)]:
					attackers.append(i)
			elif i.piece_type == PieceEnum.knight:  # Knight capture squares
				if coordinate in [x.new_position for x in self.generateKnightMoves(i.position, color)]:
					attackers.append(i)
			elif i.piece_type == PieceEnum.bishop:  # Bishop capture squares
				if coordinate in [x.new_position for x in self.generateBishopMoves(i.position, color)]:
					attackers.append(i)
			elif i.piece_type == PieceEnum.rook:  # Rook capture squares
				if coordinate in [x.new_position for x in self.generateRookMoves(i.position, color)]:
					attackers.append(i)
			elif i.piece_type == PieceEnum.queen:  # Queen capture squares
				if coordinate in [x.new_position for x in self.generateQueenMoves(i.position, color)]:
					attackers.append(i)
			elif i.piece_type == PieceEnum.king:  # King capture squares
				if functions.coordinateToIndex(coordinate) in [[functions.coordinateToIndex(i.position)[0] - 1, functions.coordinateToIndex(i.position)[1] - 1], [functions.coordinateToIndex(i.position)[0] - 1, functions.coordinateToIndex(i.position)[1]], [functions.coordinateToIndex(i.position)[0] - 1, functions.coordinateToIndex(i.position)[1] + 1], [functions.coordinateToIndex(i.position)[0], functions.coordinateToIndex(i.position)[1] - 1], [functions.coordinateToIndex(i.position)[0], functions.coordinateToIndex(i.position)[1] + 1], [functions.coordinateToIndex(i.position)[0] + 1, functions.coordinateToIndex(i.position)[1] - 1], [functions.coordinateToIndex(i.position)[0] + 1, functions.coordinateToIndex(i.position)[1]], [functions.coordinateToIndex(i.position)[0] + 1, functions.coordinateToIndex(i.position)[1] + 1]]:
					attackers.append(i)
		return attackers

	def protectors(self, piece):
		"""Returns a list of the pieces that protect the piece"""
		if not isinstance(piece, Piece):
			self.error(errors.InvalidPiece(piece))
		protectors = []
		for x in self.pieces:
			if x.color != piece.color:
				continue
			if x.piece_type == PieceEnum.pawn:
				if piece.position in [i.new_position for i in self.generatePawnCaptures(x.position, x.color, return_all=True)]:
					protectors.append(x)
			elif x.piece_type == PieceEnum.knight:
				if piece.position in [i.new_position for i in self.generateKnightMoves(x.position, x.color, return_all=True)]:
					protectors.append(x)
			elif x.piece_type == PieceEnum.bishop:
				if piece.position in [i.new_position for i in self.generateBishopMoves(x.position, x.color, stop=Stop.piece)]:
					protectors.append(x)
			elif x.piece_type == PieceEnum.rook:
				if piece.position in [i.new_position for i in self.generateRookMoves(x.position, x.color, stop=Stop.piece)]:
					protectors.append(x)
			elif x.piece_type == PieceEnum.queen:
				if piece.position in [i.new_position for i in self.generateQueenMoves(x.position, x.color, stop=Stop.piece)]:
					protectors.append(x)
		return protectors

	def visualized(self, print_result=False, use_unicode=True, empty_squares=" ", separators=True):
		if empty_squares == "":
			empty_squares = " "
		empty_squares = empty_squares[0]
		if print_result:
			print((("---------------------------------\n| " if use_unicode else "-----------------------------------------\n| ") + (" |\n---------------------------------\n| " if use_unicode else " |\n-----------------------------------------\n| ").join(" | ".join([y + ((empty_squares if use_unicode else empty_squares + " ") if y == "" else "") for y in x]) for x in [["".join([((PieceEnum.unicode(z.piece_type, z.color)) if use_unicode else (z.color[0].upper() + (z.piece_type[0].upper() if z.piece_type != "knight" else "N"))) if functions.coordinateToIndex(z.position) == [x, y] else "" for z in self.pieces]) for y in range(len(self.squares[x]))] for x in range(len(self.squares))]) + (" |\n---------------------------------" if use_unicode else " |\n-----------------------------------------")) if separators else ("\n".join(" ".join([y + ((empty_squares if use_unicode else empty_squares + " ") if y == "" else "") for y in x]) for x in [["".join([((PieceEnum.unicode(z.piece_type, z.color)) if use_unicode else (z.color[0].upper() + (z.piece_type[0].upper() if z.piece_type != "knight" else "N"))) if functions.coordinateToIndex(z.position) == [x, y] else "" for z in self.pieces]) for y in range(len(self.squares[x]))] for x in range(len(self.squares))])))
		else:
			return (("---------------------------------\n| " if use_unicode else "-----------------------------------------\n| ") + (" |\n---------------------------------\n| " if use_unicode else " |\n-----------------------------------------\n| ").join(" | ".join([y + ((empty_squares if use_unicode else empty_squares + " ") if y == "" else "") for y in x]) for x in [["".join([((PieceEnum.unicode(z.piece_type, z.color)) if use_unicode else (z.color[0].upper() + (z.piece_type[0].upper() if z.piece_type != "knight" else "N"))) if functions.coordinateToIndex(z.position) == [x, y] else "" for z in self.pieces]) for y in range(len(self.squares[x]))] for x in range(len(self.squares))]) + (" |\n---------------------------------" if use_unicode else " |\n-----------------------------------------")) if separators else ("\n".join(" ".join([y + ((empty_squares if use_unicode else empty_squares + " ") if y == "" else "") for y in x]) for x in [["".join([((PieceEnum.unicode(z.piece_type, z.color)) if use_unicode else (z.color[0].upper() + (z.piece_type[0].upper() if z.piece_type != "knight" else "N"))) if functions.coordinateToIndex(z.position) == [x, y] else "" for z in self.pieces]) for y in range(len(self.squares[x]))] for x in range(len(self.squares))]))

	def generatePawnMoves(self, position, color, return_all=False, piece=None):
		moves = []
		if (color == Color.black and position[1] == "1") or (color == Color.white and position[1] == "8") or not functions.coordinateValid(position):
			return moves if (color == Color.black and position[1] == "1") or (color == Color.white and position[1] == "8") else [self.error(errors.InvalidCoordinate(position)), moves][1]

		if Color.isWhite(color):
			if return_all:
				moves = [Move(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1]]), piece), Move(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 2, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 2, functions.coordinateToIndex(position)[1]]), piece, double_pawn_move=True)]
			else:
				if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1]])):
					return moves
				if position[1] == "2" and not self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 2, functions.coordinateToIndex(position)[1]])):
					moves = [Move(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1]]), piece), Move(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 2, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 2, functions.coordinateToIndex(position)[1]]), piece, double_pawn_move=True)]
				else:
					moves = [Move(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1]]), piece)]
			if position[1] == "7" and not self.pieceAt(position[0] + "8"):
				moves.extend([Move(position[0] + "8=" + i, position, position[0] + "8", piece, promotion=i) for i in ["N", "B", "R", "Q"]])
			return moves
		elif Color.isBlack(color):
			if return_all:
				moves = [Move(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1]]), piece), Move(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 2, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 2, functions.coordinateToIndex(position)[1]]), piece, double_pawn_move=True)]
			else:
				if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1]])):
					return moves
				if position[1] == "7" and not self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 2, functions.coordinateToIndex(position)[1]])):
					moves = [Move(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1]]), piece), Move(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 2, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 2, functions.coordinateToIndex(position)[1]]), piece, double_pawn_move=True)]
				else:
					moves = [Move(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1]]), piece)]
			if position[1] == "2" and not self.pieceAt(position[0] + "1"):
				moves.extend([Move(position[0] + "1=" + i, position, position[0] + "1", piece, promotion=i) for i in ["N", "B", "R", "Q"]])
			return moves
		else:
			self.error(errors.UndefinedColor(color))
			return []

	def generatePawnCaptures(self, position, color, return_all=False, piece=None):
		if (color == Color.black and position[1] == "1") or (color == Color.white and position[1] == "8"):
			return []

		if not functions.coordinateValid(position):
			self.error(errors.InvalidCoordinate(position))
			return []

		if Color.isWhite(color):
			if position[0] not in "ah" and (return_all or (self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 1])) and self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 1])) and self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 1])).color != color and self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 1])).color != color)):
				if position[1] == "7":
					return [Move(position[0] + "x" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 1]) + "=" + i, position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 1]), piece, is_capture=True, promotion=i) for i in ["N", "B", "R", "Q"]] + [Move(position[0] + "x" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 1]) + "=" + i, position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 1]), piece, is_capture=True, promotion=i) for i in ["N", "B", "R", "Q"]]
				return [Move(position[0] + "x" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 1]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 1]), piece, is_capture=True), Move(position[0] + "x" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 1]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 1]), piece, is_capture=True)]

			if position[0] != "h" and self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 1])) and self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 1])).color != color:
				if position[1] == "7":
					return [Move(position[0] + "x" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 1]) + "=" + i, position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 1]), piece, is_capture=True, promotion=i) for i in ["N", "B", "R", "Q"]]
				return [Move(position[0] + "x" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 1]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 1]), piece, is_capture=True)]

			if position[0] != "a" and self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 1])) and self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 1])).color != color:
				if position[1] == "7":
					return [Move(position[0] + "x" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 1]) + "=" + i, position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 1]), piece, is_capture=True, promotion=i) for i in ["N", "B", "R", "Q"]]
				return [Move(position[0] + "x" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 1]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 1]), piece, is_capture=True)]
		elif Color.isBlack(color):
			if position[0] not in "ah" and (return_all or (self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 1])) and self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 1])) and self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 1])).color != color and self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 1])).color != color)):
				if position[1] == "2":
					return [Move(position[0] + "x" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 1]) + "=" + i, position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 1]), piece, is_capture=True, promotion=i) for i in ["N", "B", "R", "Q"]] + [Move(position[0] + "x" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 1]) + "=" + i, position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 1]), piece, is_capture=True, promotion=i) for i in ["N", "B", "R", "Q"]]
				return [Move(position[0] + "x" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 1]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 1]), piece, is_capture=True), Move(position[0] + "x" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 1]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 1]), piece, is_capture=True)]

			if position[0] != "h" and self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 1])) and self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 1])).color != color:
				if position[1] == "2":
					return [Move(position[0] + "x" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 1]) + "=" + i, position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 1]), piece, is_capture=True, promotion=i) for i in ["N", "B", "R", "Q"]]
				return [Move(position[0] + "x" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 1]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 1]), piece, is_capture=True)]

			if position[0] != "a" and self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 1])) and self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 1])).color != color:
				if position[1] == "2":
					return [Move(position[0] + "x" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 1]) + "=" + i, position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 1]), piece, is_capture=True, promotion=i) for i in ["N", "B", "R", "Q"]]
				return [Move(position[0] + "x" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 1]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 1]), piece, is_capture=True)]
		else:
			self.error(errors.UndefinedColor(color))

		return []

	def generateKnightMoves(self, position, color, return_all=False, piece=None):
		if not functions.coordinateValid(position):
			self.error(errors.InvalidCoordinate(position))
			return []
		if not Color.valid(color):
			self.error(errors.UndefinedColor(color))
			return []
		moves = []
		if position[0] != "h" and position[1] not in ["1", "2"]:
			if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 2, functions.coordinateToIndex(position)[1] + 1])) and not return_all:
				if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 2, functions.coordinateToIndex(position)[1] + 1])).color == Color.invert(color):
					moves.append(Move("Nx" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 2, functions.coordinateToIndex(position)[1] + 1]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 2, functions.coordinateToIndex(position)[1] + 1]), piece, is_capture=True))
			else:
				moves.append(Move("N" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 2, functions.coordinateToIndex(position)[1] + 1]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 2, functions.coordinateToIndex(position)[1] + 1]), piece))
		if position[0] not in ["g", "h"] and position[1] != "1":
			if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 2])) and not return_all:
				if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 2])).color == Color.invert(color):
					moves.append(Move("Nx" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 2]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 2]), piece, is_capture=True))
			else:
				moves.append(Move("N" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 2]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] + 2]), piece))
		if position[0] != "a" and position[1] not in ["7", "8"]:
			if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 2, functions.coordinateToIndex(position)[1] - 1])) and not return_all:
				if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 2, functions.coordinateToIndex(position)[1] - 1])).color == Color.invert(color):
					moves.append(Move("Nx" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 2, functions.coordinateToIndex(position)[1] - 1]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 2, functions.coordinateToIndex(position)[1] - 1]), piece, is_capture=True))
			else:
				moves.append(Move("N" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 2, functions.coordinateToIndex(position)[1] - 1]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 2, functions.coordinateToIndex(position)[1] - 1]), piece))
		if position[0] not in ["a", "b"] and position[1] != "8":
			if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 2])) and not return_all:
				if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 2])).color == Color.invert(color):
					moves.append(Move("Nx" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 2]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 2]), piece, is_capture=True))
			else:
				moves.append(Move("N" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 2]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] - 2]), piece))
		if position[0] != "a" and position[1] not in ["1", "2"]:
			if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 2, functions.coordinateToIndex(position)[1] - 1])) and not return_all:
				if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 2, functions.coordinateToIndex(position)[1] - 1])).color == Color.invert(color):
					moves.append(Move("Nx" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 2, functions.coordinateToIndex(position)[1] - 1]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 2, functions.coordinateToIndex(position)[1] - 1]), piece, is_capture=True))
			else:
				moves.append(Move("N" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 2, functions.coordinateToIndex(position)[1] - 1]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 2, functions.coordinateToIndex(position)[1] - 1]), piece))
		if position[0] not in ["a", "b"] and position[1] != "1":
			if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 2])) and not return_all:
				if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 2])).color == Color.invert(color):
					moves.append(Move("Nx" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 2]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 2]), piece, is_capture=True))
			else:
				moves.append(Move("N" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 2]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] + 1, functions.coordinateToIndex(position)[1] - 2]), piece))
		if position[0] != "h" and position[1] not in ["7", "8"]:
			if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 2, functions.coordinateToIndex(position)[1] + 1])) and not return_all:
				if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 2, functions.coordinateToIndex(position)[1] + 1])).color == Color.invert(color):
					moves.append(Move("Nx" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 2, functions.coordinateToIndex(position)[1] + 1]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 2, functions.coordinateToIndex(position)[1] + 1]), piece, is_capture=True))
			else:
				moves.append(Move("N" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 2, functions.coordinateToIndex(position)[1] + 1]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 2, functions.coordinateToIndex(position)[1] + 1]), piece))
		if position[0] not in ["g", "h"] and position[1] != "8":
			if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 2])) and not return_all:
				if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 2])).color == Color.invert(color):
					moves.append(Move("Nx" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 2]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 2]), piece, is_capture=True))
			else:
				moves.append(Move("N" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 2]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0] - 1, functions.coordinateToIndex(position)[1] + 2]), piece))
		return moves

	def generateBishopMoves(self, position, color, stop=Stop.capture_piece, piece=None):
		moves = []
		capture, (pos1, pos2), piece_found = False, functions.coordinateToIndex(position), 0
		while pos1 != 0 and pos2 != 0:
			pos1, pos2 = pos1 - 1, pos2 - 1
			if stop == Stop.piece:
				moves.append(Move("B" + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece))
				if self.pieceAt(functions.indexToCoordinate([pos1, pos2])):
					break
			elif stop != Stop.never:
				for i in self.pieces:
					if functions.coordinateToIndex(i.position) == [pos1, pos2]:
						if stop == Stop.capture_piece:
							if i.color == color:
								break
							capture = True
						elif stop == Stop.no_capture:
							break
				else:
					moves.append(Move("B" + ("x" if capture else "") + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece, is_capture=capture))
					if capture:
						break
					continue
				break
			else:
				moves.append(Move("B" + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece))
		capture, (pos1, pos2) = False, functions.coordinateToIndex(position)
		while pos1 != 7 and pos2 != 7:
			pos1, pos2 = pos1 + 1, pos2 + 1
			if stop == Stop.piece:
				moves.append(Move("B" + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece))
				if self.pieceAt(functions.indexToCoordinate([pos1, pos2])):
					break
			elif stop != Stop.never:
				for i in self.pieces:
					if functions.coordinateToIndex(i.position) == [pos1, pos2]:
						if stop == Stop.capture_piece:
							if i.color == color:
								break
							capture = True
						elif stop == Stop.no_capture:
							break
				else:
					moves.append(Move("B" + ("x" if capture else "") + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece, is_capture=capture))
					if capture:
						break
					continue
				break
			else:
				moves.append(Move("B" + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece))
		capture, (pos1, pos2) = False, functions.coordinateToIndex(position)
		while pos1 != 0 and pos2 != 7:
			pos1, pos2 = pos1 - 1, pos2 + 1
			if stop == Stop.piece:
				moves.append(Move("B" + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece))
				if self.pieceAt(functions.indexToCoordinate([pos1, pos2])):
					break
			elif stop != Stop.never:
				for i in self.pieces:
					if functions.coordinateToIndex(i.position) == [pos1, pos2]:
						if stop == Stop.capture_piece:
							if i.color == color:
								break
							capture = True
						elif stop == Stop.no_capture:
							break
				else:
					moves.append(Move("B" + ("x" if capture else "") + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece, is_capture=capture))
					if capture:
						break
					continue
				break
			else:
				moves.append(Move("B" + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece))
		capture, (pos1, pos2) = False, functions.coordinateToIndex(position)
		while pos1 != 7 and pos2 != 0:
			pos1, pos2 = pos1 + 1, pos2 - 1
			if stop == Stop.piece:
				moves.append(Move("B" + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece))
				if self.pieceAt(functions.indexToCoordinate([pos1, pos2])):
					break
			elif stop != Stop.never:
				for i in self.pieces:
					if functions.coordinateToIndex(i.position) == [pos1, pos2]:
						if stop == Stop.capture_piece:
							if i.color == color:
								break
							capture = True
						elif stop == Stop.no_capture:
							break
				else:
					moves.append(Move("B" + ("x" if capture else "") + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece, is_capture=capture))
					if capture:
						break
					continue
				break
			else:
				moves.append(Move("B" + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece))
		return moves

	def generateRookMoves(self, position, color, stop=Stop.capture_piece, piece=None):
		moves = []
		capture = False
		for x in reversed(range(functions.coordinateToIndex(position)[0])):
			if stop == Stop.piece:
				moves.append(Move("R" + functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), piece))
				if self.pieceAt(functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]])):
					break
			elif stop != Stop.never:
				for y in self.pieces:
					if functions.coordinateToIndex(y.position) == [x, functions.coordinateToIndex(position)[1]]:
						if y.color == color or stop == Stop.no_capture:
							break
						capture = True
				else:
					moves.append(Move("R" + ("x" if capture else "") + functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), piece, is_capture=capture))
					if capture:
						break
					continue
				break
			else:
				moves.append(Move("R" + functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), piece))
		capture = False
		for x in reversed(range(functions.coordinateToIndex(position)[1])):
			if stop == Stop.piece:
				moves.append(Move("R" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), piece))
				if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x])):
					break
			elif stop != Stop.never:
				for y in self.pieces:
					if functions.coordinateToIndex(y.position) == [functions.coordinateToIndex(position)[0], x]:
						if y.color == color or stop == Stop.no_capture:
							break
						capture = True
				else:
					moves.append(Move("R" + ("x" if capture else "") + functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), piece, is_capture=capture))
					if capture:
						break
					continue
				break
			else:
				moves.append(Move("R" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), piece))
		capture = False
		for x in range(functions.coordinateToIndex(position)[0] + 1, 8):
			if stop == Stop.piece:
				moves.append(Move("R" + functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), piece))
				if self.pieceAt(functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]])):
					break
			elif stop != Stop.never:
				for y in self.pieces:
					if functions.coordinateToIndex(y.position) == [x, functions.coordinateToIndex(position)[1]]:
						if y.color == color or stop == Stop.no_capture:
							break
						capture = True
				else:
					moves.append(Move("R" + ("x" if capture else "") + functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), piece, is_capture=capture))
					if capture:
						break
					continue
				break
			else:
				moves.append(Move("R" + functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), piece))
		capture = False
		for x in range(functions.coordinateToIndex(position)[1] + 1, 8):
			if stop == Stop.piece:
				moves.append(Move("R" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), piece))
				if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x])):
					break
			elif stop != Stop.never:
				for y in self.pieces:
					if functions.coordinateToIndex(y.position) == [functions.coordinateToIndex(position)[0], x]:
						if y.color == color or stop == Stop.no_capture:
							break
						capture = True
				else:
					moves.append(Move("R" + ("x" if capture else "") + functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), piece, is_capture=capture))
					if capture:
						break
					continue
				break
			else:
				moves.append(Move("R" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), piece))
		return moves

	def generateQueenMoves(self, position, color, stop=Stop.capture_piece, piece=None):
		moves = []
		# Diagonal moves
		capture, (pos1, pos2), piece_found = False, functions.coordinateToIndex(position), 0
		while pos1 != 0 and pos2 != 0:
			pos1, pos2 = pos1 - 1, pos2 - 1
			if stop == Stop.piece:
				moves.append(Move("Q" + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece))
				if self.pieceAt(functions.indexToCoordinate([pos1, pos2])):
					break
			elif stop != Stop.never:
				for i in self.pieces:
					if functions.coordinateToIndex(i.position) == [pos1, pos2]:
						if stop == Stop.capture_piece:
							if i.color == color:
								break
							capture = True
						elif stop == Stop.no_capture:
							break
				else:
					moves.append(Move("Q" + ("x" if capture else "") + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece, is_capture=capture))
					if capture:
						break
					continue
				break
			else:
				moves.append(Move("Q" + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece))
		capture, (pos1, pos2) = False, functions.coordinateToIndex(position)
		while pos1 != 7 and pos2 != 7:
			pos1, pos2 = pos1 + 1, pos2 + 1
			if stop == Stop.piece:
				moves.append(Move("Q" + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece))
				if self.pieceAt(functions.indexToCoordinate([pos1, pos2])):
					break
			elif stop != Stop.never:
				for i in self.pieces:
					if functions.coordinateToIndex(i.position) == [pos1, pos2]:
						if stop == Stop.capture_piece:
							if i.color == color:
								break
							capture = True
						elif stop == Stop.no_capture:
							break
				else:
					moves.append(Move("Q" + ("x" if capture else "") + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece, is_capture=capture))
					if capture:
						break
					continue
				break
			else:
				moves.append(Move("Q" + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece))
		capture, (pos1, pos2) = False, functions.coordinateToIndex(position)
		while pos1 != 0 and pos2 != 7:
			pos1, pos2 = pos1 - 1, pos2 + 1
			if stop == Stop.piece:
				moves.append(Move("Q" + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece))
				if self.pieceAt(functions.indexToCoordinate([pos1, pos2])):
					break
			elif stop != Stop.never:
				for i in self.pieces:
					if functions.coordinateToIndex(i.position) == [pos1, pos2]:
						if stop == Stop.capture_piece:
							if i.color == color:
								break
							capture = True
						elif stop == Stop.no_capture:
							break
				else:
					moves.append(Move("Q" + ("x" if capture else "") + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece, is_capture=capture))
					if capture:
						break
					continue
				break
			else:
				moves.append(Move("Q" + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece))
		capture, (pos1, pos2) = False, functions.coordinateToIndex(position)
		while pos1 != 7 and pos2 != 0:
			pos1, pos2 = pos1 + 1, pos2 - 1
			if stop == Stop.piece:
				moves.append(Move("Q" + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece))
				if self.pieceAt(functions.indexToCoordinate([pos1, pos2])):
					break
			elif stop != Stop.never:
				for i in self.pieces:
					if functions.coordinateToIndex(i.position) == [pos1, pos2]:
						if stop == Stop.capture_piece:
							if i.color == color:
								break
							capture = True
						elif stop == Stop.no_capture:
							break
				else:
					moves.append(Move("Q" + ("x" if capture else "") + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece, is_capture=capture))
					if capture:
						break
					continue
				break
			else:
				moves.append(Move("Q" + functions.indexToCoordinate([pos1, pos2]), position, functions.indexToCoordinate([pos1, pos2]), piece))
		# Straight moves
		capture = False
		for x in reversed(range(functions.coordinateToIndex(position)[0])):
			if stop == Stop.piece:
				moves.append(Move("Q" + functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), piece))
				if self.pieceAt(functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]])):
					break
			elif stop != Stop.never:
				for y in self.pieces:
					if functions.coordinateToIndex(y.position) == [x, functions.coordinateToIndex(position)[1]]:
						if y.color == color or stop == Stop.no_capture:
							break
						capture = True
				else:
					moves.append(Move("Q" + ("x" if capture else "") + functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), piece, is_capture=capture))
					if capture:
						break
					continue
				break
			else:
				moves.append(Move("Q" + functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), piece))
		capture = False
		for x in reversed(range(functions.coordinateToIndex(position)[1])):
			if stop == Stop.piece:
				moves.append(Move("Q" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), piece))
				if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x])):
					break
			elif stop != Stop.never:
				for y in self.pieces:
					if functions.coordinateToIndex(y.position) == [functions.coordinateToIndex(position)[0], x]:
						if y.color == color or stop == Stop.no_capture:
							break
						capture = True
				else:
					moves.append(Move("Q" + ("x" if capture else "") + functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), piece, is_capture=capture))
					if capture:
						break
					continue
				break
			else:
				moves.append(Move("Q" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), piece))
		capture = False
		for x in range(functions.coordinateToIndex(position)[0] + 1, 8):
			if stop == Stop.piece:
				moves.append(Move("Q" + functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), piece))
				if self.pieceAt(functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]])):
					break
			elif stop != Stop.never:
				for y in self.pieces:
					if functions.coordinateToIndex(y.position) == [x, functions.coordinateToIndex(position)[1]]:
						if y.color == color or stop == Stop.no_capture:
							break
						capture = True
				else:
					moves.append(Move("Q" + ("x" if capture else "") + functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), piece, is_capture=capture))
					if capture:
						break
					continue
				break
			else:
				moves.append(Move("Q" + functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), position, functions.indexToCoordinate([x, functions.coordinateToIndex(position)[1]]), piece))
		capture = False
		for x in range(functions.coordinateToIndex(position)[1] + 1, 8):
			if stop == Stop.piece:
				moves.append(Move("Q" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), piece))
				if self.pieceAt(functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x])):
					break
			elif stop != Stop.never:
				for y in self.pieces:
					if functions.coordinateToIndex(y.position) == [functions.coordinateToIndex(position)[0], x]:
						if y.color == color or stop == Stop.no_capture:
							break
						capture = True
				else:
					moves.append(Move("Q" + ("x" if capture else "") + functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), piece, is_capture=capture))
					if capture:
						break
					continue
				break
			else:
				moves.append(Move("Q" + functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), position, functions.indexToCoordinate([functions.coordinateToIndex(position)[0], x]), piece))
		return moves

	def __str__(self):
		return "Chess Game with FEN " + self.FEN()

	def __lt__(self, other):
		return self.totalMaterial() < other.totalMaterial()

	def __le__(self, other):
		return self.totalMaterial() <= other.totalMaterial()

	def __contains__(self, obj):
		if isinstance(obj, Piece):
			return self.squares_hashtable[obj.position] == obj
		if isinstance(obj, Square):
			return vars(obj) in map(vars, self.squares)

		self.error(TypeError("Invalid type: " + str(obj)))
		return False

	def __unicode__(self):
		return "---------------------------------\n| " + " |\n---------------------------------\n| ".join(" | ".join([y + (" " if y == "" else "") for y in x]) for x in [["".join([(PieceEnum.unicode(z.piece_type, z.color)) if functions.coordinateToIndex(z.position) == [x, y] else "" for z in self.pieces]) for y in range(len(self.squares[x]))] for x in range(len(self.squares))]) + " |\n---------------------------------"

	def __eq__(self, other):
		return self.FEN() == other.FEN()

	__add__ = __radd__ = __sub__ = __rsub__ = __mul__ = __rmul__ = __div__ = __rdiv__ = __truediv__ = __rtruediv__ = __floordiv__ = __rfloordiv__ = __mod__ = __rmod__ = __divmod__ = __rdivmod__ = __pow__ = __rpow__ = __lshift__ = __rlshift__ = __rshift__ = __rrshift__ = __and__ = __rand__ = __or__ = __ror__ = __xor__ = __rxor__ = __iadd__ = __isub__ = __imul__ = __idiv__ = __itruediv__ = __ifloordiv__ = __imod__ = __ipow__ = __iand__ = __ior__ = __ixor__ = __ilshift__ = __irshift__ = __neg__ = __pos__ = __abs__ = __invert__ = __int__ = __long__ = __float__ = __complex__ = __oct__ = __hex__ = __coerce__ = lambda self, *args: self.error(ArithmeticError("Cannot perform arithmetic operations on Game object"))

	__getitem__ = __setitem__ = __delitem__ = __getslice__ = __setslice__ = __delslice__ = lambda self, *args: self.error(IndexError("Cannot perform operation on Game object"))
