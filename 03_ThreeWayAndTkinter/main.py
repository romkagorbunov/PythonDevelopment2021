import tkinter as tk
import random as rnd

class Application(tk.Frame):
    positions = []
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createButtonNew(self):
        self.newButton = tk.Button(self, text="New", command=self.initPositions)
        self.newButton.grid(row=0, column=0)

    def createButtonQuit(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row=0, column=1)

    def movecell(self):
        pass

    def createGrid(self):
        self.initPositions()
        for r in range(4):
            for c in range(4):
                index = r * 4 + c
                if (self.positions[index] == 0):
                    continue
                self.gameButtons[index] = tk.Button(self, 
                                                    text=str(self.positions[index]), 
                                                    command=self.movecell,
                                                    height=10,
                                                    width=10)
                self.gameButtons[index].grid(row=r+1, column=c)
    


    def initPositions(self):
        self.positions = [i for i in range(16)]
        rnd.shuffle(self.positions)
        self.gameButtons = [0] * 16

    def createWidgets(self):
        self.createButtonNew()
        self.createButtonQuit()
        self.createGrid()

app = Application()
app.master.title('15')
app.mainloop()
