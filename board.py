import random
from tile import Tile
from options import Options

class Board:
	rows = 0
	cols = 0
	tiles = {}

	def __init__(self, rows, cols, options):
		self.rows = rows
		self.cols = cols
		for row in range(0,rows):
			for col in range(0,cols):
				self.tiles[row,col] = Tile(row,col,options)
				
				if(random.randrange(0,100) > 60):
					self.tiles[row,col].exists = False
		
		for row in range(0,rows):
			for col in range(0,cols):
				self.setupNeighbors(row, col)
				#self.tiles[row,col].showNeighbors()
		
					
	def placeTile(self,row,col,tile):
		boardTile = self.tiles[row,col]
		if boardTile.exists and boardTile.team == 0:
			boardTile.team = tile.team
			boardTile.strength = tile.strength
			self.captureNeighbors(boardTile)
			return True
		return False
		
	def captureNeighbors(self,tile):
		numCaptured = 0
		for neighbor in tile.neighbors:
			if neighbor.exists and neighbor.team > 0:
				if neighbor.team != tile.team:
					if tile.strength > neighbor.strength:
						neighbor.team = tile.team
						numCaptured += 1
					else:
						neighbor.strength = max(0, neighbor.strength - 2)
				else:
					neighbor.strength = min(20, neighbor.strength + 2)
						
	def setupNeighbors(self, row, col):
		baseTile = self.tiles[row,col]
		
		# if these are valid rows or columns
		nextCol = bool((col + 1) < self.cols)
		prevCol = bool((col - 1) >= 0)
		nextRow = bool((row + 1) < self.rows)
		prevRow = bool((row - 1) >= 0)
		
		if prevRow:
			baseTile.neighbors.append(self.tiles[row-1,col])
			
		if nextRow:
			baseTile.neighbors.append(self.tiles[row+1,col])
		
		if prevCol:
			baseTile.neighbors.append(self.tiles[row,col-1])
			
		if nextCol:
			baseTile.neighbors.append(self.tiles[row,col+1])
			
		if row % 2 == 1:
			if nextCol:
				if prevRow:
					baseTile.neighbors.append(self.tiles[row-1,col+1])
				if nextRow:
					baseTile.neighbors.append(self.tiles[row+1,col+1])
		else:
			if prevCol:
				if prevRow:
					baseTile.neighbors.append(self.tiles[row-1,col-1])
				if nextRow:
					baseTile.neighbors.append(self.tiles[row+1,col-1])
					
	def text(board):
		out = ""
		header = "     "
		topRow = "   --"
		
		for i in range(0,board.cols):
			header += "  " + chr(ord('a') + i) + "  ."
			topRow += "------"
		topRow += "----\n"
		
		out = header + "\n" + topRow
		
		for row in range(0, board.rows):
			rowText = ""
			
			# add a character for rows <10 so it will right align
			if (row + 1) < 10:
				rowText += " "
			
			rowText += str(row + 1) + " | "
			
			# shift text over for even numbered rows for hex effect
			if row % 2 == 1:
				rowText += "   "
			
			# draw each tile in the row, including its team and strength
			for col in range(0, board.cols):
				currentTile = board.tiles[row,col]
				
				rowText += currentTile.text() + " "
			
			if row % 2 == 0:
				rowText += "   "
			
			out += rowText + "|\n"
			
		out += topRow
		
		return out
