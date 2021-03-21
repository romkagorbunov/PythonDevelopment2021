import tkinter as tk
from tkinter import font

class Application(tk.Frame):
    ''' Simple tkinter application'''

    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("InputLabel")
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.createWidgets()
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)

    def createWidgets(self):
        self.label = InputLabel(self)
        self.label.grid(sticky="WE")

        self.quitButton = tk.Button(self, text="Quit", command=self.quit)
        self.quitButton.grid(sticky="SE")


class InputLabel(tk.Label):

    fontSize = 10

    def __init__(self, master=None):
        self.text = tk.StringVar()
        self.text.set("abracadabria")
        self.font = "Consolas"
        # print(self.font.actual())
        # print(self.font.metrics())
        super().__init__(master, textvariable=self.text, font="Fixedsys", takefocus = 1, highlightthickness = 1, anchor="w")

        self.bind("<Button-1>", self.clickMouse)
        self.bind("<KeyPress>", self.clickButton)

        self.cursorPos = 0
        self.cursor = tk.Frame(self, background="black", width=1)
        self.cursor.place(x=self.cursorPos, y=self.fontSize)
        self.cursor.place(anchor=tk.CENTER, height=self.fontSize * 2)
        
    def clickMouse(self, event):
        self.focus()
        self.setCursorPosition(event.x)

    def setCursorPosition(self, newPos):
        newPosition = int(newPos / self.fontSize + 0.5) * self.fontSize
        length = len(self.text.get()) * self.fontSize
        if newPosition > length:
            newPosition = length
        if newPosition < 0:
            newPosition = 0
        self.cursorPos = newPosition
        self.cursor.place(x=self.cursorPos, y=self.fontSize)

    def clickButton(self, event):
        if event.keysym == "Left":
            self.setCursorPosition(self.cursorPos - self.fontSize)
        elif event.keysym == "Right":
            self.setCursorPosition(self.cursorPos + self.fontSize)
        elif event.keysym == "Home":
            self.setCursorPosition(0)
        elif event.keysym == "End":
            self.setCursorPosition(len(self.text.get()) * self.fontSize)
        elif event.keysym == "BackSpace":
            ind = self.cursorPos // self.fontSize
            if ind:
                self.text.set(self.text.get()[:ind - 1] + self.text.get()[ind:])
                self.setCursorPosition(self.cursorPos - self.fontSize)
        elif event.keysym == "Delete":
            ind = self.cursorPos // self.fontSize
            if ind != len(self.text.get() * self.fontSize):
                self.text.set(self.text.get()[:ind] + self.text.get()[ind + 1:])
        elif event.char.isprintable():
            ind = self.cursorPos // self.fontSize
            self.text.set(self.text.get()[:ind] + event.char + self.text.get()[ind:])
            self.setCursorPosition(self.cursorPos + self.fontSize)

app = Application()
app.mainloop()