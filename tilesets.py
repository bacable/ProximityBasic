'''
TileSets.py
    
Has the values for the different tilesets each game uses, including how it gets
displayed and what its value is.
'''

class TileSets:
    def __init__(self):
        self.StandardTileSet = ["_1","_2","_3","_4","_5","_6","_7","_8","_9","10","11","12","13","14","15","16","17","18","19","20"]
        self.StandardTileVals = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.RspTileSet = ["[]","8<","~"]
        self.RspTileVals = ["rock","scissors","paper"]