'''	center.py

	Danielle Eisen, Nov 21 2016

	This program creates the class Center to
	deal with the center portion of the Backgammon
	board for captured pieces.
'''

from graphics import *
from piece import *

class Center:

	def __init__(self, x, y, color, width, height):
		'''Center(x, y, color, width, height)'''
		self.x = x
		self.y = y
		self.color = color
		self.width = width
		self.height = height

		self.pieceCount = 0
		self.rect = None
		self.win = None

		self.pieces = []

	def getX(self):
		'''getX() returns x'''
		return self.x

	def getY(self):
		'''getY() returns y'''
		return self.y

	def getNum(self):
		'''getNum() returns an index that allows the pieces to be moved to the correct wedge'''
		if self.color == 'white':
			return 0
		elif self.color == 'brown':
			return 25

	def getPieceColor(self):
		'''getPieceColor returns color of pieces allowed'''
		return self.color

	def setPieceColor(self, color):
		pass

	def draw(self, window):
		'''draw(window) draws the center rectangle and its pieces'''
		self.win = window

		self.drawRect()
		if self.pieceCount > 0:
			self.drawPieces()

	def drawRect(self):
		'''drawRect() creates and draws the center rectangle'''
		self.rect = Polygon(Point(self.x, self.y), Point(self.x + self.width, self.y), \
		 	Point(self.x + self.width, self.y + self.height), Point(self.x, self.y + self.height))

		self.rect.draw(self.win)

	def getPieceCount(self):
		'''getPieceCount() returns pieceCount'''
		return self.pieceCount

	def drawPieces(self):
		'''drawPieces() creates and draws the pieces that are on the center area'''
		for eachPiece in self.pieces:
			eachPiece.undraw()

		self.pieces = []
		pieceX = self.x + self.width//2
		pieceRadius = self.width//4
		yShift = 0

		while len(self.pieces) < self.pieceCount:
			if self.color == 'white':
				pieceY = self.y + 8 * self.height//9 - yShift
			elif self.color == 'brown':
				pieceY = self.y + self.height//9 + yShift

			newPiece = Piece(pieceX, pieceY, self.color, pieceRadius)

			yShift += 2 * pieceRadius
			newPiece.draw(self.win)
			self.pieces.append(newPiece)

	def removePiece(self):
		'''removePiece() removes one piece from the center and redraws the pieces'''
		self.pieceCount -= 1
		self.drawPieces()

	def addPiece(self):
		'''addPiece() adds one piece to the center and redraws the pieces'''
		self.pieceCount += 1
		self.drawPieces()

	def checkMouse(self, mouseX, mouseY):
		'''checkMouse(mouseX, mouseY) tests if the mouse click is within the center'''
		if (mouseX - self.x) < self.width:
			return True
		return False