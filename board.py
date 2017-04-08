'''	board.py

	Danielle Eisen, Nov 21 2016

	This program runs the Backgammon board
	and handles the main components of the
	game functionality.
'''

from graphics import *
from wedge import *
from player import *
from center import *

class Board(GraphWin):

	def __init__(self, *args):
		'''Board(*args)'''
		GraphWin.__init__(self, *args)
		self.bind_all('<Button-1>', self.mouseHandler)

		self.currentWedge = None
		self.wedges = [None] * 26
		self.centerTop = None
		self.centerBottom = None

		self.drawBoard()

		self.player1 = None
		self.player2 = None
		self.currentPlayer = None
		self.nextPlayer = None

		self.createPlayers()
		self.playGame()

	def getWedges(self):
		return self.wedges

	def drawBoard(self):
		'''drawBoard() creates the graphics of the Board'''
		self.setBackground(color_rgb(170, 110, 70))

		self.drawWedges()
		self.initPieces()

		self.drawCenter()

		rightBar = Polygon(Point(27 * self.getWidth()//30, 0), Point(27 * self.getWidth()//30, self.getHeight()),\
			Point(self.getWidth(), self.getHeight()), Point(self.getWidth(), 0))
		rightBar.draw(self)

		bottomEnd = Polygon(Point(55 * self.getWidth()//60, 5 * self.getHeight()//9), Point(55 * self.getWidth()//60, self.getHeight()),\
			Point(59 * self.getWidth()//60, self.getHeight()), Point(59 * self.getWidth()//60, 5 * self.getHeight()//9))
		bottomEnd.draw(self)

		topEnd = Polygon(Point(55 * self.getWidth()//60, 0), Point(55 * self.getWidth()//60, 4 * self.getHeight()//9),\
			Point(59 * self.getWidth()//60, 4 * self.getHeight()//9), Point(59 * self.getWidth()//60, 0))
		topEnd.draw(self)

	def drawCenter(self):
		'''drawCenter() creates the center part of the board, where the captured pieces rest'''
		self.centerTop = Center(13 * self.getWidth()//30, 0, 'white', 2 * self.getWidth()//30, self.getHeight()//2)
		self.wedges[0] = self.centerTop
		self.centerTop.draw(self)

		self.centerBottom = Center(13 * self.getWidth()//30, self.getHeight()//2, 'brown', 2 * self.getWidth()//30, self.getHeight())
		self.wedges[25] = self.centerBottom
		self.centerBottom.draw(self)

	def drawWedges(self):
		'''drawWedges() draws the wedges around the board in separate quadrants'''
		wedgeX = 13 * self.getWidth()//15
		wedgeY = 1 * self.getHeight()//3
		self.drawQuadrant(wedgeX, wedgeY, 1)

		wedgeX = 6 * self.getWidth()//15
		self.drawQuadrant(wedgeX, wedgeY, 2)

		wedgeX = 1 * self.getWidth()//15
		wedgeY = 2 * self.getHeight()//3
		self.drawQuadrant(wedgeX, wedgeY, 3)

		wedgeX = 8 * self.getWidth()//15
		self.drawQuadrant(wedgeX, wedgeY, 4)

	def drawQuadrant(self, wedgeX, wedgeY, quadrant):
		'''drawQuadrant(wedgeX, wedgeY, quadrant) draws the wedges in a given quadrant'''
		width = self.getWidth()//15
		height = self.getHeight()//3
		color = 'brown'
		for i in range(6):
			wedgeNum = (quadrant - 1) * 6 + i + 1
			newWedge = Wedge(wedgeX, wedgeY, color, quadrant, width, height, wedgeNum)
			self.wedges[wedgeNum] = newWedge
			newWedge.draw(self)

			if quadrant <= 2:
				wedgeX -= width
			elif quadrant <= 4:
				wedgeX += width

			if color == 'brown':
				color = 'white'
			elif color == 'white':
				color = 'brown'

	def initPieces(self):
		'''initPieces() creates the pieces in their start positions'''
		initPieceNums = [2, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 5, 5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, 2]
		initPieceColors = ['white', None, None, None, None, 'brown', None, 'brown', None, None, None, 'white',\
			'brown', None, None, None, 'white', None, 'white', None, None, None, None, 'brown']

		for i in range(len(self.wedges) - 2):
			self.wedges[i + 1].setPieceCount(initPieceNums[i])
			self.wedges[i + 1].setPieceColor(initPieceColors[i])
			self.wedges[i + 1].drawPieces()

	def selectInitWedge(self, initX, initY):
		'''selectInitWedge(initX, initY) selects the wedge from which a piece will be moved'''
		if not self.currentPlayer.getIsCaptured():
			for eachWedge in self.wedges:
				if (eachWedge.checkMouse(initX, initY)) and \
			 	 (eachWedge.getPieceCount() > 0) and \
				 (eachWedge.getPieceColor() == self.currentPlayer.getPlayerColor()):
					self.currentWedge = eachWedge
					break
		elif self.currentPlayer.getIsCaptured():
			if (self.currentPlayer == self.player1) and \
			 (self.centerTop.checkMouse(initX, initY)):
				self.currentWedge = self.centerTop
			elif (self.currentPlayer == self.player2) and \
			 (self.centerBottom.checkMouse(initX, initY)):
				self.currentWedge = self.centerBottom

	def selectDestWedge(self, destX, destY):
		'''selectDestWedge(destX, destY) selects the wedge to which a piece will be moved'''
		for eachWedge in self.wedges:
			if (eachWedge.checkMouse(destX, destY)) and \
			 ((eachWedge.getPieceColor() == self.currentPlayer.getPlayerColor()) or \
			 (eachWedge.getPieceColor() == None)) and \
			 (self.testWedgeDist(self.currentWedge, eachWedge)):
				print('moved')
				self.currentWedge.removePiece()
				if eachWedge.getPieceCount() == 0:
					eachWedge.setPieceColor(self.currentWedge.getPieceColor())
				eachWedge.addPiece()
				break
			elif (eachWedge.checkMouse(destX, destY)) and \
			 (eachWedge.getPieceColor() == self.nextPlayer.getPlayerColor()) and \
			 (eachWedge.getPieceCount() == 1) and \
			 (self.testWedgeDist(self.currentWedge, eachWedge)):
			 	print('captured')
			 	self.capturePiece(self.currentPlayer.getPlayerColor(), eachWedge)
			 	break

		if ((self.currentWedge == self.centerTop) or \
		 (self.currentWedge == self.centerBottom)) and \
		 (self.currentWedge.getPieceCount() == 0):
		 	self.currentPlayer.setIsCaptured(False)

		self.currentWedge = None
		self.testTurnEnd()

	def capturePiece(self, currentPlayerColor, capturedWedge):
		'''capturePiece(currentPlayerColor, capturedWedge) allows a player to capture a single piece of the other color'''
		capturedWedge.removePiece()
		if currentPlayerColor == 'brown':
			self.centerTop.addPiece()
		elif currentPlayerColor == 'white':
			self.centerBottom.addPiece()

		self.nextPlayer.setIsCaptured(True)

		self.currentWedge.removePiece()
		capturedWedge.setPieceColor(currentPlayerColor)
		capturedWedge.addPiece()

	def testTurnEnd(self):
		'''testTurnEnd() switches which player has a turn if the current player is done'''
		if self.currentPlayer == self.player1 and self.player1.turnOver():
			self.currentPlayer = self.player2
			self.nextPlayer = self.player1
			self.player2.takeTurn(self)
		elif self.currentPlayer == self.player2 and self.player2.turnOver():
			self.currentPlayer = self.player1
			self.nextPlayer = self.player2
			self.player1.takeTurn(self)

	def testWedgeDist(self, wedge1, wedge2):
		'''testWedgeDist(wedge1, wedge2) returns True if the destination wedge is a distance represented by
		the dice, and False otherwise'''
		if self.currentPlayer == self.player1:
			if self.getWedgeDist(wedge1, wedge2) == self.player1.getNum1():
				self.player1.setNum1(0)
				return True
			elif self.getWedgeDist(wedge1, wedge2) == self.player1.getNum2():
				self.player1.setNum2(0)
				return True
		elif self.currentPlayer == self.player2:
			if self.getWedgeDist(wedge2, wedge1) == self.player2.getNum1():
				self.player2.setNum1(0)
				return True
			elif self.getWedgeDist(wedge2, wedge1) == self.player2.getNum2():
				self.player2.setNum2(0)
				return True
		return False

	def getWedgeDist(self, wedge1, wedge2):
		'''getWedgeDist(wedge1, wedge2) returns the distance between two given wedges'''
		return wedge2.getNum() - wedge1.getNum()

	def mouseHandler(self, event):
		'''mouseHandler(event) allows the mouse clicks to control the wedge selection'''
		if (not self.currentWedge):
			self.selectInitWedge(event.x, event.y)
		elif self.currentWedge:
			self.selectDestWedge(event.x, event.y)


	def createPlayers(self):
		'''createPlayers() initializes the two players'''
		self.player1 = Player(input('Is player 1 a human or computer? '), 1)
		self.player2 = Player(input('Is player 2 a human or computer? '), 2)
		self.currentPlayer = self.player1
		self.nextPlayer = self.player2

	def playGame(self):
		'''playGame() makes the current player take their turn'''
		if self.currentPlayer == self.player1:
			self.player1.takeTurn(self)
		elif self.currentPlayer == self.player2:
			self.player2.takeTurn(self)

	def hasCurrentWedge(self):
		if self.currentWedge:
			return True
		return False

if __name__ == '__main__':
	window = Board('Backgammon', 1000, 600)
	while window.winfo_exists():
		window.update()