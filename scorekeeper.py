class Scorekeeper:
	
	def __init__(self,playerCount,options):
		self.options = options
		self.scores = [0]
		for i in range(0,playerCount):
			self.scores.append(0)
	
	def calculateScores(self, board):
		for i in range(0, len(self.scores)):
			self.scores[i] = 0
			
		for row in range(0,board.rows):
			for col in range(0,board.cols):
				tile = board.tiles[row,col]
				if tile.exists:
					self.scores[tile.team] += tile.strength
	
	def text(self):
		out = "   Score: "
		for i in range(1,len(self.scores)):
			out += self.options.teamChars[i] + " = " + str(self.scores[i]) + ", "
		return out