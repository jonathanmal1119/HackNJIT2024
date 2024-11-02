
class Worker():
    
    def __init__(self, work_speed : float, parts_per_cycle : int):
        self.work_speed = work_speed
        self.parts_per_cycle = parts_per_cycle
        self.count = 0
        
    def think(self,time, gamemode):
        
        if (self.count / gamemode.tick_speed == self.work_speed):
            gamemode.current_objective.progress(self.parts_per_cycle)
            print(str(self.parts_per_cycle)+" parts Made.")
            self.count = 0
            
        self.count += 1
            
            