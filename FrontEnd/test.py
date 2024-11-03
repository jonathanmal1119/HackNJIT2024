import tkinter as tk
from tkinter import *
from ctypes import windll
from tkinter import font as tkFont


main = Tk()
main.geometry("500x700")
main.title("SteamsReach")
windll.shcore.SetProcessDpiAwareness(1)
ws = main.winfo_screenwidth() # width of the screen
hs = main.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
w=500
h= 700
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen
# and where it is placed
main.geometry('%dx%d+%d+%d' % (w, h, x, y))


frame = tk.Frame(main)
frame.grid()
frame.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor="c")
titleF = tk.Frame(main,bg ='blue')
titleF.place(relx=0.5, rely=0.2, relwidth=1, relheight=0.3, anchor="c")
mycanvas = tk.Canvas(titleF, width = 200, height = 25)
mycanvas.pack(side = "top", fill = "both", expand = True)
mycanvas.create_text(250,150,  anchor="center",text="SteamsReach", fill="black", font=('Helvetica 36 bold'))





def startGame():
    frame.destroy()

size = tkFont.Font(family='Helvetica', size=15, weight='bold')

startButton = tk.Button(frame,text="Start",command=startGame)
startButton['font'] = size
startButton.grid()
startButton.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.2, anchor="c")

main.mainloop()
