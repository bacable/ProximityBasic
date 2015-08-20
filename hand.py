from tile import Tile
from deck import Deck
from options import Options

class Hand:
	
	def __init__(self,team,deck,handSize,options):
		self.handSize = handSize
		self.team = team
		self.tiles = []
		self.deck = deck
		self.options = options
		
		for i in range(0, self.handSize):
			self.drawTile()
		
	def drawTile(self):
		tile = Tile(0,0,self.options)
		tile.strength = self.deck.draw()
		tile.team = self.team
		self.tiles.append(tile)
		
	def playTile(self,row,col,strength,board):
		for tile in self.tiles:
			if strength == tile.strength:
				if board.placeTile(row,col,tile):
					self.tiles.remove(tile)
					self.drawTile()
					return True
				else:
					print("Selected tile location not available.")
				
		return False
		
	def text(self):
		out = "   Hand: "
		for tile in self.tiles:
			out += tile.text() + ", "
		return out