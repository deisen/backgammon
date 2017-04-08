'''	die.py

	Danielle Eisen, Nov 21, 2016

	This program creates the Die class
	which can be rolled to allow movement
	in the Backgammon game.
'''

import random
from graphics import *

class Die:

	def __init__(self, x, size):
		'''Die(x, size)'''
		self.number = random.randint(1, 6)
		self.x = x
		self.y = None
		self.size = size
		self.dots = []
		self.square = None
		self.win = None

	def rollDie(self):
		'''rollDie() selects a random number between 1 and 6 for the die'''
		self.number = random.randint(1, 6)
		print(self.number)
		self.draw(self.win)
		return self.number

	def draw(self, window):
		'''draw(window) draws the die with the correct number of dots'''
		self.win = window

		self.undraw()

		self.y = self.win.getHeight()//2
		self.square = Polygon(Point(self.x, self.y), Point(self.x + self.size, self.y), \
			Point(self.x + self.size, self.y + self.size), Point(self.x, self.y + self.size))
		self.square.setFill('brown')
		self.square.draw(self.win)
		
		if self.number == 1:
			self.dots.append(Circle(Point(self.x + self.size/2, self.y + self.size/2), self.size/8))
		elif self.number == 2:
			self.dots.append(Circle(Point(self.x + self.size/4, self.y + self.size/4), self.size/8))
			self.dots.append(Circle(Point(self.x + 3 * self.size/4, self.y + 3 * self.size/4), self.size/8))
		elif self.number == 3:
			self.dots.append(Circle(Point(self.x + self.size/4, self.y + self.size/4), self.size/8))
			self.dots.append(Circle(Point(self.x + self.size/2, self.y + self.size/2), self.size/8))
			self.dots.append(Circle(Point(self.x + 3 * self.size/4, self.y + 3 * self.size/4), self.size/8))
		elif self.number == 4:
			self.dots.append(Circle(Point(self.x + self.size/4, self.y + self.size/4), self.size/8))
			self.dots.append(Circle(Point(self.x + 3 * self.size/4, self.y + self.size/4), self.size/8))
			self.dots.append(Circle(Point(self.x + 3 * self.size/4, self.y + 3 * self.size/4), self.size/8))
			self.dots.append(Circle(Point(self.x + self.size/4, self.y + 3 * self.size/4), self.size/8))
		elif self.number == 5:
			self.dots.append(Circle(Point(self.x + self.size/4, self.y + self.size/4), self.size/8))
			self.dots.append(Circle(Point(self.x + 3 * self.size/4, self.y + self.size/4), self.size/8))
			self.dots.append(Circle(Point(self.x + 3 * self.size/4, self.y + 3 * self.size/4), self.size/8))
			self.dots.append(Circle(Point(self.x + self.size/4, self.y + 3 * self.size/4), self.size/8))
			self.dots.append(Circle(Point(self.x + self.size/2, self.y + self.size/2), self.size/8))
		elif self.number == 6:
			self.dots.append(Circle(Point(self.x + self.size/4, self.y + self.size/4), self.size/8))
			self.dots.append(Circle(Point(self.x + 3 * self.size/4, self.y + self.size/4), self.size/8))
			self.dots.append(Circle(Point(self.x + 3 * self.size/4, self.y + 3 * self.size/4), self.size/8))
			self.dots.append(Circle(Point(self.x + self.size/4, self.y + 3 * self.size/4), self.size/8))
			self.dots.append(Circle(Point(self.x + self.size/4, self.y + self.size/2), self.size/8))
			self.dots.append(Circle(Point(self.x + 3 * self.size/4, self.y + self.size/2), self.size/8))

		for eachCirc in self.dots:
			eachCirc.setFill('black')
			eachCirc.draw(self.win)
		
	def undraw(self):
		'''undraw() removes the dots to allow for a new list of dots'''
		for eachCirc in self.dots:
			eachCirc.undraw()
		self.dots = []