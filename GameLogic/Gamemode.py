import time
from PlayerInfo.player import Player
from GameLogic.ObjectiveClass import Objective, objectives
from GameLogic.Worker import Worker

class Gamemode():
    
    def start_game(self):
        self.start_time = time.time()
        self.current_player = Player(1)
        self.current_objective = Objective(objectives.Engine1)
        self.game_active = True
        self.active_workers : Worker = [Worker(2,1)]
        self.tick_speed = 24
        
        self.start_game_loop()
    
    def get_play_time(self) -> float:
        return time.time() - self.start_time
    
    def get_player_progress(self) -> float:
        #return self.current_player.parts
        pass
    
    def pause_game(self):
        self.game_active = False
    
    def start_game_loop(self):
        while (self.game_active):
            time.sleep(1/self.tick_speed)
            for worker in self.active_workers:
                worker.think(self.get_play_time(),self)
            if (self.get_play_time() > 30):
                self.game_active = False
            
            
    def create_worker(self,work_speed,parts_per_cycle):
        worker = Worker(work_speed,parts_per_cycle)
        self.current_player.workers.append(worker)
        self.active_workers.append(worker)
        