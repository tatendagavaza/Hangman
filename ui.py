from tkinter import *
from logic import Brain

BG_COLOR = "#ffffff"
FONT = ('Arial', 20, 'italic')
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ    "

class Interface:
    def __init__(self, brain: Brain):
        self.brain = brain

        self.window = Tk()
        self.window.title("Hangman")
        self.window.config(padx=20, pady=20, bg=BG_COLOR)

        # ---------------------------- IMAGE CANVAS ------------------------------- #
        self.canvas = Canvas(width=512, height=512, highlightthickness=0)
        self.imgs = []
        self.fill_images()
        self.image = self.canvas.create_image(0,0, anchor=NW, image=self.imgs[0])
        self.canvas.grid(column=0, row=0, pady=20, columnspan=5)

        # ---------------------------- WORD LABEL ------------------------------- #
        self.wordLabel = Label(text="", font=FONT, bg=BG_COLOR)
        self.wordLabel.grid(column=0,row=1, columnspan=5)
        self.get_next_question()
        # ---------------------------- LETTER BUTTONS ------------------------------- #
        self.letter_frame = Frame(self.window).grid(column=0,row=2,sticky=W)
        self.btns = []
        i = 0
        for j in range(1, 7):
            for k in range(5):
                btn = Button(self.letter_frame, width=6, height=1, font=FONT, text=ALPHABET[i], bd=.5,highlightthickness=0)

                if btn['text'] == ' ':
                    btn.config(state=DISABLED, bd=0, bg=BG_COLOR)
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
        self.imgs.append(PhotoImage(file="images/gameover.png"))
    def get_next_question(self):
        if self.brain.has_words_left():
            self.brain.next_word()
            print(self.brain.current_word)
            self.update_display()

    def update_display(self):
        self.wordLabel.configure(text=" ".join(self.brain.word_underscore))
        self.canvas.itemconfig(self.image, image=self.imgs[self.brain.wrong_letters])

    def guess(self, letter):
        self.brain.check_letter(letter)
        for btn in self.btns:
            if btn['text'] == letter:
                btn.config(state=DISABLED)

        if self.brain.is_game_over():
            self.canvas.itemconfig(self.image, image=self.imgs[self.brain.wrong_letters])
            self.wordLabel.configure(text=" ")
            for btn in self.btns:
                btn.config(state=DISABLED)
        else:
            self.update_display()