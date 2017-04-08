'''	wedge.py

	Danielle Eisen, Nov 21, 2016

	This program creates the Wedge class
	for the pieces to be moved to in the
	Backgammon game.
'''

from graphics import *
from piece import *

class Wedge:

	def __init__(self, x, y, color, quadrant, width, height, num):
		'''Wedge(x, y, color, quadrant, width, height, num)'''
		self.x = x
		self.y = y
		self.color = color
		self.quadrant = quadrant
		self.width = width
		self.height = height
		self.num = num
	
		self.win = None
		self.pieceCount = 0
		self.pieceColor = None
		self.triangle = None

		self.pieces = []

	def getX(self):
		'''getX() returns x'''
		return self.x

	def getY(self):
		'''getY() returns y'''
		return self.y

	def getNum(self):
		'''getNum() returns index num'''
		return self.num

	def getPieceColor(self):
		'''getPieceColor() returns the color of the pieces'''
		return self.pieceColor

	def setPieceColor(self, color):
		'''setPieceColor(color) sets the piece color to the given color'''
		self.pieceColor = color
		for eachPiece in self.pieces:
			eachPiece.setColor(color)

	def draw(self, window):
		'''draw(window) draws the wedge and pieces'''
		self.win = window

		self.drawTriangle()
		if self.pieceCount > 0:
			self.drawPieces()

	def drawTriangle(self):
		'''drawTriangle() creates and draws the wedge with its color'''
		if self.quadrant <= 2:
			self.triangle = Polygon(Point(self.x, self.y), Point(self.x - self.width/2,\
				self.y - self.height), Point(self.x + self.width/2, self.y - self.height))
		elif self.quadrant <= 4:
			self.triangle = Polygon(Point(self.x, self.y), Point(self.x - self.width/2,\
				self.y + self.height), Point(self.x + self.width/2, self.y + self.height))

		if self.color == 'brown':
			self.triangle.setFill(color_rgb(90, 20, 0))
		elif self.color == 'white':
			self.triangle.setFill(color_rgb(230, 230, 230))

		self.triangle.draw(self.win)

	def setPieceCount(self, pieceCount):
		'''setPieceCount(pieceCount) sets the piece count to the given value'''
		self.pieceCount = pieceCount

	def getPieceCount(self):
		'''getPieceCount() returns the piece count'''
		return self.pieceCount

	def drawPieces(self):
		'''drawPieces() draws all of the pieces on the wedge'''
		for eachPiece in self.pieces:
			eachPiece.undraw()

		self.pieces = []
		pieceX = self.x
		pieceRadius = self.width//4
		yShift = 0

		while len(self.pieces) < self.pieceCount:
			if self.quadrant <= 2:
				pieceY = self.y - 8 * self.height//9 + yShift
			elif self.quadrant <= 4:
				pieceY = self.y + 8 * self.height//9 - yShift

			newPiece = Piece(pieceX, pieceY, self.pieceColor, pieceRadius)

			yShift += 2 * pieceRadius
			newPiece.draw(self.win)
			self.pieces.append(newPiece)

	def removePiece(self):
		'''removePiece() removes one piece from the wedge and redraws the pieces'''
		self.pieceCount -= 1
		self.drawPieces()

	def addPiece(self):
		'''addPiece() adds one piece to the wedge and redraws the pieces'''
		self.pieceCount += 1
		self.drawPieces()

	def checkMouse(self, mouseX, mouseY):
		'''checkMouse(mouseX, mouseY) tests if the mouse click is within the wedge'''
		if abs(mouseX - self.x) < self.width/2:
			if self.quadrant <= 2:
				if mouseY < self.y:
					return True
			elif self.quadrant <= 4:
				if mouseY > self.y:
					return True
		return False