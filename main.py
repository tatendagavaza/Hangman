from ui import Interface
from data import word_data
from logic import Brain


brain = Brain(word_data)
hangman_ui = Interface(brain)