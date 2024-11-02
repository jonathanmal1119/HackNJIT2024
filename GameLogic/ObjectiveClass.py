from enum import Enum

class objectives(Enum):
    Engine1 = 100
    Engine2 = 200
    Structure = 300
    Air_Bag = 400
    Rudder = 500
    Carriage = 600
    Final_Blimp = 1000
    
class Objective():
    
    def __init__(self, objective : objectives):
        self.target = objective
        self.parts_cost = objective.value
        self.contributed_parts = 0
        
    def get_progress(self) -> float:
        return self.contributed_parts / self.parts_cost * 100
        
    def progress(self, progress_amt):
        self.contributed_parts += progress_amt