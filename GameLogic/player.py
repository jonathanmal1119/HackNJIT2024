
class Player():
    
    def __init__(self, starting_money : int):    
        self.money = starting_money
        
    def transact(self, price):
        if (self.money >= price):
            self.money -= price
            return True
        else:
            return False

