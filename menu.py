import os
from options import Options

class Menu:

	def __init__(self,gameLoopFunction, options):
		self.gameLoopFunction = gameLoopFunction
		self.options = options

	def showMainMenu(self):
		choosing = True
		while choosing:
			os.system('clear')

			print("Proximity - This time it's Terminal!")
			print("---------------------")
			print("1. Play Single Player")
			print("2. How to Play")
			print("3. Options")
			print("4. Leaderboards")
			print("5. Quit")
			print("---------------------")
			
			choice = str(input())
			if choice == "1":
				self.showMenuSinglePlayer()
			elif choice == "2":
				self.showHowToPlay()
			elif choice == "3":
				self.showOptions()
			elif choice == "4":
				self.showLeaderboards()
			elif choice == "5":
				choosing = False

	def showMenuSinglePlayer(self):

		choosing = True
		while choosing:
			os.system('clear')

			self.options.numPlayers = int(input("How many players?"))
			
			choosing = False

		self.gameLoopFunction()

	def showHowToPlay(self):

		choosing = True
		while choosing:
			os.system('clear')

			print("Score higher than your opponents!\n")
			print("Your total score is the number of points on all of your tiles.\n")
			print("Place tiles next to smaller tiles of the other team to capture them.\n")
			print("Defend your tiles by placing your tiles next to them, increasing their points and reducing their chance of being captured.\n")
			choosing = False
			raw_input("ENTER to continue...")
			
	def showOptions(self):
		os.system('clear')

		print("Modes:")
		print(" 1. Normal Proximity - Capture tiles lower than you, weaken those you can't. Highest score wins.")
		print(" 2. Abstract Proximity - All tiles available to you at the beginning, each player has the same tiles.")
		print(" 3. Beggar Proximity - Same capture rules, but trying to have the lowest score at the end.")
		print(" 4. Attrition Proximity - Number goes down by how many enemy tiles around it each turn.")
		print(" 5. Chain Proximity - Each tile captured can try to capture what's around it.")
		print(" 6. Expansion Proximity - After first tile, only place tiles next to existing ally tiles.")
		print(" 7. RSP Proximity - Instead of numbers, have R for Rock, S for Scissors, and P for Paper.")
		print(" 8. Spy Proximity - Place two tiles on your turn, take 1. Can be opponent tile.")
		print(" 9. Asteroids Proximity - No edges, bottom row captures the top, left captures right, and vice-versa.")
		print("10. Blind Proximity - Only shows tile and placed tiles for a turn, otherwise just shows if occupied.")
		print("11. Risky Proximity - Has ? tiles, which modifies your tile +5 to -5 before placed.")
		print("12. Neutral Proximity - Has neutral tiles prepopulating the board that can be captured.")
		print("13. Simultaneous Proximity - Play X moves at same time. If choose same tile, it becomes a neutral tile.")
		pass
		
	def showLeaderboards(self):
		pass