from GameLogic.Interaction import Interact

class Player(Interact):
    
    def __init__(self):
        self.money = 0
        self.ownedItems = []
    