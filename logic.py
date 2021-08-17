
class Brain:
    def __init__(self, word_list):
        self.word_num = 0
        self.score = 0

        self.words = word_list
        self.current_word = None
        self.word_underscore = []
        self.wrong_letters = 0

    def has_words_left(self):
        return self.word_num < len(self.words)

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
        print(letter)

        if letter not in self.current_word:
            self.wrong_letters += 1

        for i in range(len(self.current_word)):
            if letter == self.current_word[i]:
                self.word_underscore[i] = letter
