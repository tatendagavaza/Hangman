from tkinter import *

BG_COLOR = "#ffffff"
FONT = ('Arial', 20, 'italic')
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWZYZ    "

class Interface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Hangman")
        self.window.config(padx=20, pady=20, bg=BG_COLOR)

        # ---------------------------- IMAGE CANVAS ------------------------------- #
        self.canvas = Canvas(width=512, height=512, highlightthickness=0)
        self.imgs = []
        self.fill_images()
        image = self.canvas.create_image(0,0, anchor=NW, image=self.imgs[0])
        self.canvas.grid(column=0, row=0, pady=20, columnspan=5)

        # ---------------------------- WORD LABEL ------------------------------- #
        self.word = "_ _ _ _ _ _"
        self.wordLabel = Label(text= self.word, font = FONT, bg=BG_COLOR).grid(column=0,row=1, columnspan=5)

        # ---------------------------- LETTER BUTTONS ------------------------------- #
        self.letter_frame = Frame(self.window).grid(column=0,row=2,sticky=W)
        self.btns = []
        i = 0
        for j in range(1, 7):
            for k in range(5):
                btn = Button(self.letter_frame, width=6, height=1, font=FONT, text=ALPHABET[i], bd=.5,highlightthickness=0)

                if btn['text'] == ' ':
                    btn.config(state=DISABLED)
                else:
                    btn.config(command= lambda x= ALPHABET[i]: self.guess(x))

                self.btns.append(btn)
                self.btns[i].grid(row=j + 2, column=k)
                i+=1
        self.window.mainloop()

    def fill_images(self):
        for i in range(7):
            img = PhotoImage(file=f'images/hangman{i}.png')
            self.imgs.append(img)

    def guess(self, letter):
        print(letter)