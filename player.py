'''	player.py

	Danielle Eisen, Nov 21, 2016

	This program creates the Player class,
	which handles whether a computer or
	human is playing as each player in the
	Backgammon game.
'''

import random
from die import *

class Player:

	def __init__(self, category, num):
		'''Player(category, num)'''
		self.category = category
		self.num = num
		self.playerColor = None
		self.isTurn = False
		self.num1 = 0
		self.num2 = 0
		self.isCaptured = False
		self.win = None
		self.dieA = None
		self.dieB = None
		self.createDice()
		self.setPlayerColor()

	def createDice(self):
		'''createDice() creates two dice for the player'''
		self.dieA = Die(300, 70)
		self.dieB = Die(550, 70)

	def setPlayerColor(self):
		'''setPlayerColor() sets the color for the player based on the player number'''
		if self.num == 1:
			self.playerColor = 'white'
		elif self.num == 2:
			self.playerColor = 'brown'

	def getPlayerColor(self):
		'''getPlayerColor() returns the player color'''
		return self.playerColor

	def getNum1(self):
		'''getNum1() returns the roll of die a'''
		return self.num1

	def getNum2(self):
		'''getNum2() returns the roll of die b'''
		return self.num2

	def setNum1(self, n):
		'''setNum1(n) changes the die a value to n'''
		self.num1 = n

	def setNum2(self, n):
		'''setNum2(n) changes the die b value to n'''
		self.num2 = n

	def getIsCaptured(self):
		'''getIsCaptured() returns True if the player has at least one captured piece'''
		return self.isCaptured

	def setIsCaptured(self, boolean):
		'''setIsCaptured(boolean) changes if the player has a captured piece'''
		self.isCaptured = boolean

	def turnOver(self):
		'''turnOver() returns True when both dice have been used to move'''
		if self.num1 == 0 and self.num2 == 0:
			return True
		else:
			return False

	def takeTurn(self, window):
		'''takeTurn(window) allows the player to take their turn'''
		self.win = window
		self.isTurn = True
		print('player', self.num, 'turn')
		self.dieA.draw(self.win)
		self.dieB.draw(self.win)
		
		if self.category == 'human':
			self.humanTurn()
		elif self.category == 'computer':
			self.computerTurn()

		self.isTurn = False

	def humanTurn(self):
		'''humanTurn() handles the turn if the player is a human'''
		self.num1 = self.dieA.rollDie()
		self.num2 = self.dieB.rollDie()

	def computerTurn(self):
		'''computerTurn() handles the turn if the player is a computer'''
		self.num1 = self.dieA.rollDie()
		self.num2 = self.dieB.rollDie()

		while not (self.num1 == 0 and self.num2 == 0):
			for eachWedge in self.win.getWedges():
				if eachWedge.getPieceCount() == 1 and not self.win.hasCurrentWedge():
					self.win.selectInitWedge(eachWedge.getX(), eachWedge.getY())
				elif eachWedge.getPieceCount() == 1 and self.win.hasCurrentWedge():
					self.win.selectDestWedge(eachWedge.getX(), eachWedge.getY())
				elif not self.win.hasCurrentWedge():
					self.win.selectInitWedge(random.randint(0, self.win.getWidth()), random.randint(0, self.win.getHeight()))
				elif self.win.hasCurrentWedge():
					self.win.selectDestWedge(random.randint(0, self.win.getWidth()), random.randint(0, self.win.getHeight()))