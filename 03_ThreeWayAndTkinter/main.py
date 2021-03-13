import tkinter as tk
from tkinter import messagebox
import random as rnd

class Application(tk.Frame):
    cntrows = 4
    cntcols = 4
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    positions = []
    gameButtons = []
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.createWidgets()

    def createButtonNew(self):
        self.newButton = tk.Button(self, text="New", command=self.initPositions)
        self.newButton.grid(row=0, column=1, sticky="NEWS")

    def createButtonQuit(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row=0, column=2, sticky="NEWS")

    def isFinished(self):
        need = 1
        for r in range(self.cntrows):
            for c in range(self.cntcols):
                if self.positions[r][c] != need:
                    return False
                need = (need + 1) % (self.cntrows * self.cntcols)
        return True

    def goodrow(self, r):
       return (r >= 0 and r < self.cntrows)

    def goodcol(self, c):
        return (c >= 0 and c < self.cntcols)

    def traverseToIndex(self, r, c):
        return r * self.cntcols + c

    def movecell(self, number):
        def mmove(self=self, number=number):
            row, column = -1, -1
            for r in range(self.cntrows):
                for c in range(self.cntcols):
                    if (self.positions[r][c] == number):
                        row, column = r, c
                        break
            print("Im here", row, column, len(self.gameButtons))
            if len(self.gameButtons) != self.cntrows * self.cntcols:
                 return
            index = self.traverseToIndex(row, column)
            for i in range(len(self.dx)):
                nrow = row + self.dx[i]
                ncol = column + self.dy[i]
                nindex = self.traverseToIndex(nrow, ncol)
                if self.goodrow(nrow) and self.goodcol(ncol) and self.positions[nrow][ncol] == 0:
                    assert(self.gameButtons[nindex] == 0)
                    self.gameButtons[index].grid(row=nrow+1, column=ncol)
                    self.gameButtons[index], self.gameButtons[nindex] = self.gameButtons[nindex], self.gameButtons[index]
                    self.positions[row][column], self.positions[nrow][ncol] = self.positions[nrow][ncol], self.positions[row][column]
                    if self.isFinished():
                        messagebox.showinfo("15 puzzle", "You won!")
                        self.initPositions()
                    return
        return mmove
         

    def drawGrid(self):
        for button in self.gameButtons:
            if button:
               button.destroy()
        self.gameButtons = []
        for r in range(self.cntrows):
            for c in range(self.cntcols):
                if (self.positions[r][c] == 0):
                    self.gameButtons.append(0)
                    continue
                self.gameButtons.append(tk.Button(self,
                                                  text=str(self.positions[r][c]), 
                                                  command=self.movecell(self.positions[r][c]),
                                                  ))
                self.gameButtons[-1].columnconfigure(0, weight=1)
                self.gameButtons[-1].grid(row=r+1, column=c)
                self.gameButtons[-1].grid(sticky="NEWS")
    


    def initPositions(self):
        helping = [i for i in range(self.cntrows * self.cntcols)]
        rnd.shuffle(helping)
        self.positions = [[helping[r * self.cntcols + c] for c in range(self.cntcols)] for r in range(self.cntrows)]
        self.drawGrid()

    def createWidgets(self):
        self.grid(sticky="NEWS")
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        for i in range(self.cntcols):
            self.columnconfigure(i, weight=1)
        for i in range(self.cntrows + 1):
            self.rowconfigure(i, weight=1)

        self.createButtonNew()
        self.createButtonQuit()
        self.initPositions()

root = tk.Tk()
app = Application(root)
root.title('15')
root.mainloop()
