from tkinter import *

BG_COLOR = "#ffffff"
FONT = ('Arial', 20, 'italic')

class Interface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Hangman")
        self.window.config(padx=20, pady=20, bg=BG_COLOR)

        self.window.mainloop()