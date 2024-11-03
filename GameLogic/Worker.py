from GameLogic.ObjectiveClass import objectives

class Worker():
    
    def __init__(self, work_speed : float, parts_per_cycle : int):
        self.work_speed = work_speed
        self.parts_per_cycle = parts_per_cycle
        self.count = 0
        
    def upgrade_worker(self):
        self.work_speed /= 2
        
    def think(self,time, gamemode):
        if (self.count / gamemode.tick_speed == self.work_speed):
            gamemode.current_objective.progress(self.parts_per_cycle)
            gamemode.current_player.money += 100
            print(str(self.parts_per_cycle)+" parts Made. " + str(gamemode.current_objective.contributed_parts))
            self.count = 0
            
        self.count += 1
        
    
            
            