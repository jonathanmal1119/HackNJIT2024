from GameLogic.Gamemode import Gamemode
import threading
from FrontEnd.ui import GameBoard
import time

gm = Gamemode()

def start_game_call():
    gm.start_game()
    
    
def GM_thread_st():
    thread2 = threading.Thread(target=start_game_call)
    thread2.daemon = True
    thread2.start()

def UI_thread_start():
    thread = threading.Thread(target=GameBoard(GM_thread_st))
    thread.daemon = True
    thread.start()

UI_thread_start()

