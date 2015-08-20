import random

class Deck:
	pool = []
	used = []
	
	def __init__(self):
	
		# have a working pool of 1 number per player (assuming 2 for the moment)
		for i in range(1, 21):
			self.pool.append(i)
			self.pool.append(i)
		
	def draw(self):
		if(len(self.pool) == 0):
			self.reshuffle()
			
		tile = self.pool.pop(random.randrange(len(self.pool)))
		self.used.append(tile)
		return tile
		
	def reshuffle(self):
		while self.used:
			self.pool.append(self.used.pop())