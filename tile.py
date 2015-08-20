from options import Options

class Tile:

	def __init__(self, row, col, options):
		self.row = row
		self.col = col
		self.team = 0
		self.strength = 0
		self.exists = True
		self.neighbors = []
		self.options = options
		
	def text(self):
		out = ""
		if self.exists:
			out += "<" + self.options.teamChars[self.team]
			if(self.strength < 10):
				out += "_"

			if(self.strength == 0):
				out += "_"
			else:
				out += str(self.strength)
				
			out += ">"
		else:
			out = "     "
		return out
		
	def showNeighbors(self):
		out = "Tile at " + str(self.row) + "," + str(self.col) + " has neighbors at "
		for neighbor in self.neighbors:
			out += str(neighbor.row) + "," + str(neighbor.col) + "|"
		print(out)