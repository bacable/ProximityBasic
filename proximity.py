import random
from menu import Menu
from scorekeeper import Scorekeeper
from options import Options
from player import Player
from board import Board
from deck import Deck
from tilesets import TileSets


		
class TurnAction:
	def __init__(self, row, col, tileToPlace, score):
		self.row = row
		self.col = col
		self.tileToPlace = tileToPlace
		self.score = score

	def text(self):
		letterCol = chr(ord('a') + self.col)
		print(str(tileToPlace.strength) + " tile played at " + letterCol + str(row) + ".")
		

class Heuristic:
	P2Eval = 1
	
	def __init__(self, heuristic, mistakeRange):
		# heuristic - the technique for evaluating each virtual move
		# mistakeRange - the range in which a random number can be that is added to the evaluated score to provide a way for the AI to make mistakes, i.e. in order to make a less optimal move. A range of 0 means the computer will make no mistakes
		self.heuristic = heuristic
		self.mistakeRange = mistakeRange
	
	def evaluate(self,board,hand):
		bestScoredMove = None
		
		# get the function for evaluating the move (could have multiple)
		evaluateMove = self.getHeuristicFunction()
		
		for handTile in hand.hand:
			for row in range(0,board.rows):
				for col in range(0, board.cols):
					score = evaluateMove(handTile,board.tiles[row,col])
					score += random.randrange(self.mistakeRange)
					if bestScoredMove is None or bestScoredMove.score < score:
						bestScoredMove = TurnAction(row,col,handTile,score)
		
		return bestScoredMove
	
	def getHeuristicFunction(self):
		if self.heuristic == Heuristic.P2Eval:
			return evalTileP2
			
	def evalTileP2(self,handTile,targetTile):
		pass
		

options = Options()
gameBoard = Board(7,8,options)

deck = Deck()
player1 = Player(1,deck, options)
player2 = Player(2,deck, options)
player2.nextPlayer = player1
player1.nextPlayer = player2
scorekeeper = Scorekeeper(2,options)




def gameLoop():
	playing = True
	currentPlayer = player1
	while playing:
		print('\n'*100)
		print(gameBoard.text())
		print(currentPlayer.hand.text())
		print(scorekeeper.text())
		
		waitingForCommand = True
		while waitingForCommand:
			command = input("Command? ")

			if command == "q":
				playing = False
				break
			
			tokens = command.split(" ")
			
			if len(tokens) >= 2:
				tileStrength = int(tokens[0])
				
				col = ord(tokens[1][0]) - ord('a')
				row = int(tokens[1][1]) - 1
				
				if(currentPlayer.playTile(row,col,tileStrength,gameBoard)):
					waitingForCommand = False
				else:
					print("Could not place tile")
			else:
				print("Not a valid command, please use '[Tile] [Row][Col]'")
		
		scorekeeper.calculateScores(gameBoard)
		currentPlayer = currentPlayer.nextPlayer
			

    
			
class P2Mode:
    def __init__():
        self.tileSet = TileSets.StandardTileSet
        self.tileVals = TileSets.StandardTileVals
        
    def pickMove(self,board):
        pass
    
    def captureTile(self,board):
        pass
    
    def scoreBoard(self,scorekeeper):
        pass

class RSPMode:
    def __init__():
        self.tileSet = Tilesets.RspTileSet
        self.tileVals = Tilesets.RspTileVals

    def evaluateMove(self,handTile, tile):
        for row in range(0, board.rows):
            for col in range(0, board.cols):
                pass

    def captureTile(self,board):
        pass

    def scoreBoard(self,scorekeeper):
        pass
	
menu = Menu(gameLoop, options)
menu.showMainMenu()
