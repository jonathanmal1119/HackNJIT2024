from enum import Enum

class objectives(Enum):
    Engine1 = 10
    Engine2 = 20
    Structure = 30
    Air_Bag = 40
    Carriage = 50
    Rudder = 60
    Final_Blimp = 100
    
class Objective():
    
    def __init__(self, objective : objectives):
        self.target = objective
        self.parts_cost = objective.value
        self.contributed_parts = 0
        
    def get_progress(self) -> float:
        return self.contributed_parts / self.parts_cost * 100
        
    def progress(self, progress_amt):
        self.contributed_parts += progress_amt
        