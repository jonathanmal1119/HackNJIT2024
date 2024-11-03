import tkinter as tk
from PIL import ImageTk, Image


class GameBoard():
    def __init__(self,start_funt):
        
        self.window = tk.Tk()
        self.window.geometry("500x700")
        self.window.title("SteamsReach")
        self.start_funct=start_funt



        self.window.resizable(False,False)
        self.background = Image.open("./images/istockphoto-587510458-612x612.jpg").resize((500, 700))
        self.bg_image = ImageTk.PhotoImage(self.background)
        self.bg_label = tk.Label(self.window, image=self.bg_image)
        self.bg_label.image = self.bg_image
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame = tk.Frame(self.window)
        self.frame.pack()

        self.avatar = Image.open("./images/IMG_4430.png").resize((100, 100))
        self.photo1 = ImageTk.PhotoImage(self.avatar)

        self.label = tk.Label(self.frame, text="")
        self.label.pack()

        self.label2 = tk.Label(self.window,image=self.photo1)
        self.label2.image = self.photo1
        self.label2.place(x=0, y=0)

        self.tavern = Image.open("./images/IMG_4431.png").resize((50, 50))
        self.btn = ImageTk.PhotoImage(self.tavern)

        self.img_button = tk.Button(self.window, image=self.btn, borderwidth=0, highlightthickness=0)
        self.img_button.image = self.btn
        self.img_button.place(x=100, y=150)
        self.upgrade = tk.Button(self.window, text="UPGRADE!", borderwidth=0, highlightthickness=0,pady=0,padx=0)
        self.upgrade.place(x=100,y=200)

        self.airship = Image.open("./images/IMG_4437.png").resize((50, 50))
        self.btn1 = ImageTk.PhotoImage(self.airship)

        self.img_button1 = tk.Button(self.window, image=self.btn1, borderwidth=0, highlightthickness=0)
        self.img_button1.image = self.btn1
        self.img_button1.place(x=100, y=250)
        self.upgrade1 = tk.Button(self.window, text="UPGRADE!", borderwidth=0,highlightthickness=0,pady=0,padx=0)
        self.upgrade1.place(x=100,y=300)

        self.factory = Image.open("./images/IMG_4432.png").resize((50, 50))
        self.btn2 = ImageTk.PhotoImage(self.factory)
        self.img_button2 = tk.Button(self.window, image=self.btn2, borderwidth=0, highlightthickness=0)
        self.img_button2.image = self.btn2
        self.img_button2.place(x=100, y=350)
        self.upgrade2 = tk.Button(self.window, text="UPGRADE!", borderwidth=0,highlightthickness=0,bd=0,pady=0,padx=0)
        self.upgrade2.place(x=100,y=400)

        self.gadget = Image.open("./images/IMG_4433.png").resize((50, 50))
        self.btn3 = ImageTk.PhotoImage(self.gadget)
        self.img_button3 = tk.Button(self.window, image=self.btn3, borderwidth=0, highlightthickness=0)
        self.img_button3.image = self.btn3
        self.img_button3.place(x=100, y=450)
        self.upgrade3 = tk.Button(self.window, text="UPGRADE!", borderwidth=0,bd=0,highlightthickness=0,pady=0,padx=0)
        self.upgrade3.place(x=100,y=500)

        self.clocktower = Image.open("./images/IMG_4434.png").resize((50, 50))
        self.btn4 = ImageTk.PhotoImage(self.clocktower)
        self.img_button4 = tk.Button(self.window, image=self.btn4, borderwidth=0, highlightthickness=0)
        self.img_button4.image = self.btn4
        self.img_button4.place(x=100, y=550)
        self.upgrade4 = tk.Button(self.window, text="UPGRADE!", borderwidth=0,highlightthickness=0,bd=0,pady=0,padx=0)
        self.upgrade4.place(x=100,y=600)

        self.startButton = tk.Button(self.window,text="Start",command=self.startGame,highlightthickness=0,bd=0,pady=0,padx=0)
        
        self.startButton.pack()
        self.startButton.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.2, anchor="c")

        self.img_button["state"] = "disabled"
        self.img_button1["state"] = "disabled"
        self.img_button2["state"] = "disabled"
        self.img_button3["state"] = "disabled"
        self.img_button4["state"] = "disabled"  


        self.window.mainloop()

        


        
    def startGame(self):
        self.startButton.destroy()
        self.img_button["state"] = "normal"
        self.img_button1["state"] = "normal"
        self.img_button2["state"] = "normal"
        self.img_button3["state"] = "normal"
        self.img_button4["state"] = "normal"
        self.start_funct()
        #self.start_funct()   





