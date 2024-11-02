# from GameLogic.Gamemode import Gamemode

class Player():
    
    def __init__(self, starting_money : int):    
        self.money = starting_money
        self.completed_objectives = []
        self.workers = []
        
    def transact(self, price):
        if (self.money >= price):
            self.money -= price
        else:
            return False

