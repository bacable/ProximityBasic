import os
from options import Options

class Menu:

	def __init__(self,gameLoopFunction, options):
		self.gameLoopFunction = gameLoopFunction
		self.options = options

	def showMainMenu(self):
		choice = self.run_menu(Menu.menu_data, "main_menu")
			
		if choice == "singleplayer":
			self.showMenuSinglePlayer()
		elif choice == "multiplayer":
			self.showMenuSinglePlayer()
		elif choice == "howtoplay":
			self.showHowToPlay()
		elif choice == "options":
			self.showOptions()
		elif choice == "leaderboards":
			self.showLeaderboards()
		elif choice == "exitgame":
			choosing = False

	def showMenuSinglePlayer(self):

		choosing = True
		while choosing:
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
		
		
	menu_data = {
		"main_menu": {
			"header": "Proximity - This Time It's Terminal!",
			"options": [
				{ "display": "Single Player", "value": "singleplayer", "submenu": "" },
				{ "display": "Multi Player", "value": "multiplayer", "submenu": "" },
				{ "display": "How to Play", "value": "howtoplay", "submenu": "" },
				{ "display": "Options", "value": "options", "submenu": "single_mode_menu" },
				{ "display": "Leaderboards", "value": "leaderboards", "submenu": "" },
				{ "display": "Exit", "value": "exitgame", "submenu": "" }
			]
		},
		"single_mode_menu": {
			"header": "Which game mode?",
			"options": [
				{ "display": "Normal Proximity - Capture tiles lower than you, weaken those you can't. Highest score wins.", "value": "single_mode_normal", "submenu": "single_mode_menu" },
				{ "display": "Abstract Proximity - All tiles available to you at the beginning, each player has the same tiles.", "value": "single_mode_abstract", "submenu": "" },
				{ "display": "Beggar Proximity - Same capture rules, but trying to have the lowest score at the end.", "value": "single_mode_beggar", "submenu": "" },
				{ "display": "Attrition Proximity - Number goes down by how many enemy tiles around it each turn.", "value": "single_mode_attrition", "submenu": "" },
				{ "display": "Chain Proximity - Each tile captured can try to capture what's around it.", "value": "single_mode_chain", "submenu": "" },
				{ "display": "Expansion Proximity - After first tile, only place tiles next to existing ally tiles.", "value": "single_mode_expansion", "submenu": "" },
				{ "display": "Assassin Proximity - Place two tiles on your turn, take 1. Can be opponent tile.", "value": "single_mode_rsp", "submenu": "" },
				{ "display": "Asteroids Proximity - No edges, bottom row captures the top, left captures right, and vice-versa.", "value": "single_mode_asteroids", "submenu": "" },
				{ "display": "Blind Proximity - Only shows tile and placed tiles for a turn, otherwise just shows if occupied.", "value": "single_mode_blind", "submenu": "" },
				{ "display": "Risky Proximity - Has ? tiles, which modifies your tile +5 to -5 before placed.", "value": "single_mode_risky", "submenu": "" },
				{ "display": "Neutral Proximity - Has neutral tiles prepopulating the board that can be captured.", "value": "single_mode_neutral", "submenu": "" },
				{ "display": "Simultaneous Proximity - Play X moves at same time. If choose same tile, it becomes a neutral tile.", "value": "single_mode_simult", "submenu": "" },
				{ "display": "Double Agent Proximity - Play one tile as yourself, then one tile as another random player.", "value": "single_mode_doubleagent", "submenu": "" }
			]
		}
	}
		
	def run_menu(self,data, root):
	
		current_menu_name = root
		
		while True:
			
			current_menu = data[current_menu_name]
			
			print(current_menu["header"] if "header" in current_menu else "")
			
			option_number = 1
			
			for option in current_menu["options"]:
				print(str(option_number) + ". " + option["display"])
				option_number += 1
				
			choice = input("? ")
			
			choice = int(choice) - 1
			
			if choice >= 0 and choice < len(current_menu["options"]):
				
				option = current_menu["options"][choice]
				
				if option["submenu"] != "":
					current_menu_name = option["submenu"]
					continue
				elif option["value"] != "":
					return option["value"]
				else:
					continue