
class Brain:
    def __init__(self, word_list):
        self.word_num = 0
        self.score = 0
        self.game_over = False

        self.words = word_list
        self.current_word = None
        self.word_underscore = []
        self.wrong_letters = 0

    def has_words_left(self):
        return self.word_num < len(self.words)

    def is_game_over(self):
        return self.game_over

    def next_word(self):
        self.wrong_letters = 0
        self.current_word = self.words[self.word_num]
        self.word_num += 1
        self.word_underscore = []
        for i in self.current_word:
            self.word_underscore.append('_')

        return self.word_underscore

    def check_letter(self, letter):
        letter = letter.lower()
        if letter not in self.current_word:
            self.wrong_letters += 1
            if self.wrong_letters == 7:
                self.game_over = True

        for i in range(len(self.current_word)):
            if letter == self.current_word[i]:
                self.word_underscore[i] = letter
