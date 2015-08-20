from hand import Hand
from options import Options

class Player:
	
	def __init__(self, team, deck, options):
		self.nextPlayer = None
		self.team = team
		self.teamChar = options.teamChars[team]
		self.hand = Hand(team,deck,options.handSize,options)
		self.isAutoPlayer = False
		self.score = 0
		
	def playTile(self,row,col,strength,board):
		return self.hand.playTile(row,col,strength,board)