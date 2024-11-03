from GameLogic.Gamemode import Gamemode
from FrontEnd.startMenu import startWindow
import threading

gm = Gamemode()

def start_game_call():
    gm.start_game()
    
def GM_thread_st():
    thread2 = threading.Thread(target=start_game_call)
    thread2.daemon = True
    thread2.start()

def UI_thread_start():
    thread = threading.Thread(target=startWindow(GM_thread_st))
    thread.daemon = True
    thread.start()

UI_thread_start()
