'''	piece.py

	Danielle Eisen, Nov 21, 2016

	This program creates the class Piece
	for the pieces that can be moved in
	the Backgammon game.
'''

from graphics import *

class Piece:

	def __init__(self, x, y, color, radius):
		'''Piece(x, y, color, radius)'''
		self.x = x
		self.y = y
		self.color = color
		self.radius = radius
		self.win = None

		self.circ = None

	def setColor(self, color):
		'''setColor(color) sets color to given color'''
		self.color = color

	def draw(self, window):
		'''draw(window) draws the piece with its color'''
		self.win = window
		self.circ = Circle(Point(self.x, self.y), self.radius)

		if self.color == 'brown':
			self.circ.setFill(color_rgb(140, 50, 10))
		elif self.color == 'white':
			self.circ.setFill(color_rgb(240, 220, 180))

		self.circ.draw(self.win)

	def undraw(self):
		'''undraw() undraws the piece'''
		self.circ.undraw()

	def checkMouse(self, mouseX, mouseY):
		'''checkMouse(mouseX, mouseY) tests if the mouse click is within the piece'''
		if (abs(mouseX - self.x) < self.radius) and (abs(mouseY - self.y) < self.radius):
			return True
		return False