import time
from GameLogic.player import Player
from GameLogic.ObjectiveClass import Objective, objectives
from GameLogic.Worker import Worker

class Gamemode():
    
    def start_game(self):
        self.start_time = time.time()
        self.current_player = Player(1000)
        self.current_objective = Objective(objectives.Engine1)
        self.game_active = True
        self.active_workers : Worker = [Worker(2,2)]
        self.tick_speed = 24
        
        self.start_game_loop()
    
    
    def pause_game(self):
        self.game_active = False
        
    def end_game(self):
        self.game_active = False
        print("Game Complete.")
        
        
    def start_game_loop(self):
        while (self.game_active):
            
            time.sleep(1/self.tick_speed)

            if (self.current_objective.parts_cost == self.current_objective.contributed_parts):
                self.Progress_Tier()
                
            for worker in self.active_workers:
                worker.think(self.get_play_time(),self)
                
            if (self.get_play_time() > 3600):
                self.game_active = False
                quit(0)
        
        
    def get_play_time(self) -> float:
        return time.time() - self.start_time


    def Progress_Tier(self):
        match (self.current_objective.target):
            case objectives.Engine1:
                self.current_objective = Objective(objectives.Engine2)
                print("New Objective: Engine2")
            case objectives.Engine2:
                self.current_objective = Objective(objectives.Air_Bag)
                print("New Objective: AirBag")
            case objectives.Air_Bag:
                self.current_objective = Objective(objectives.Carriage)
                print("New Objective: Carriage")
            case objectives.Carriage:
                self.current_objective = Objective(objectives.Rudder)
                print("New Objective: Rudder")
            case objectives.Rudder:
                self.current_objective = Objective(objectives.Final_Blimp)
                print("New Objective: Final Blimp")
            case objectives.Final_Blimp:
                self.end_game()
                pass
            
            
    def create_worker(self,work_speed,parts_per_cycle,price):
        if (self.current_player.money >= price):
            self.current_player.transact(price)
            print("Player Balance: " + str(self.current_player.money))
        else:
            return False
        
        worker = Worker(work_speed,parts_per_cycle)
        self.current_player.workers.append(worker)
        self.active_workers.append(worker)
        
        return True
    
    def upgrade_worker(self,price,index):
        if (self.current_player.money >= price):
            self.current_player.transact(price)
            print("Player Balance: " + str(self.current_player.money))
        else:
            return False
        
        self.worker[index].upgrade_worker()
        
        return True
        
        