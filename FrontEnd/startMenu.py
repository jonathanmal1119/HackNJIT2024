import tkinter as tk
from tkinter import *
from ctypes import windll
from tkinter import font as tkFont

class startWindow():
    def __init__(self, start_funt):
        self.main = Tk()
        self.start_funct = start_funt
        self.main.geometry("500x700")
        self.main.title("SteamsReach")
        windll.shcore.SetProcessDpiAwareness(1)
        self.ws = self.main.winfo_screenwidth()  # width of the screen
        self.hs = self.main.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        self.w = 500
        self.h = 700
        self.x = (self.ws / 2) - (self.w / 2)
        self.y = (self.hs / 2) - (self.h / 2)

        # set the dimensions of the screen
        # and where it is placed
        self.main.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))

        self.frame = tk.Frame(self.main)
        self.frame.grid()
        self.frame.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor="c")
        self.titleF = tk.Frame(self.main, bg='blue')
        self.titleF.place(relx=0.5, rely=0.2, relwidth=1, relheight=0.3, anchor="c")
        self.mycanvas = tk.Canvas(self.titleF, width=200, height=25)
        self.mycanvas.pack(side="top", fill="both", expand=True)
        self.mycanvas.create_text(250, 150, anchor="center", text="SteamsReach", fill="black", font=('Helvetica 36 bold'))

        self.size = tkFont.Font(family='Helvetica', size=15, weight='bold')
        self.startButton = tk.Button(self.frame,text="Start",command=self.startGame)
        self.startButton['font'] = self.size
        self.startButton.grid()
        self.startButton.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.2, anchor="c")
        self.main.mainloop()


    def startGame(self):
       self.frame.destroy()
       self.titleF.destroy()
       self.start_funct()

    def returnMainWindow(self):
        return self.main


