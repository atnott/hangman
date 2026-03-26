from data.data_words import get_random_word as word
from src.config import MASK_SYMBOL, MAX_ATTEMPTS, START_TEXT, win_text
from string import printable
from src.draw.stages import STAGES

class Hangman:
    def __init__(self):
        self.__word = ''
        self.used_letters = list()
        self.cnt = 0
        self.current_guess = ''
        self.flag = True

        self.regenerate_word()

    def regenerate_word(self):
        self.__word = word()
        self.used_letters = list()
        self.cnt = MAX_ATTEMPTS
        self.current_guess = self.mask()

    def mask(self) -> str:
        return MASK_SYMBOL * len(self.__word)

    @staticmethod
    def is_correct_answer(answer: str) -> bool:
        return answer in ('0', '1')

    def start_game(self):
        self.regenerate_word()
        answer = input(START_TEXT)
        if self.is_correct_answer(answer):
            if answer == '1':
                print(f'Слово загадано! \n{self.current_guess}')
                self.input_guess()
            else:
                self.flag = False

    def win_game(self):
        if self.current_guess == self.__word.upper():
            print(win_text, f'\nЗАГАДАННОЕ СЛОВО - {self.__word.upper()}')
            self.start_game()
        else:
            print(self.current_guess)
            self.input_guess()

    def replace_char(self, char: str):
        idx = [i for i in range(len(self.__word)) if self.__word[i] == char]
        self.current_guess = [ch for ch in self.current_guess]
        for i in idx:
            self.current_guess[i] = char.upper()
        self.current_guess = ''.join(self.current_guess)
        self.win_game()

    def is_valid_guess(self, guess: str) -> bool:
        return guess.lower() in self.__word

    def is_correct_guess(self, guess: str) -> bool:
        russian_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        return not any([
                guess.lower() not in russian_letters,
                guess in printable,
                len(guess) != 1,
                guess == ' ',
                guess in self.used_letters
        ])

    def decrease_attempts(self):
        if self.cnt - 1 == 0:
            print(STAGES[self.cnt - 1], f'\nТЫ ПРОИГРАЛ!\nЗАГАДАННОЕ СЛОВО - {self.__word.upper()}')
            self.start_game()
        else:
            self.cnt -= 1
            print(STAGES[self.cnt])
            print(self.current_guess)
            self.input_guess()

    def input_guess(self):
        guess = input('Введите любую русскую букву: ')
        if self.is_correct_guess(guess):
            self.used_letters += [guess]
            self.process_guess(guess)
        else:
            print('Некорректная буква!')
            self.input_guess()

    def process_guess(self, guess):
        if self.is_valid_guess(guess):
            self.replace_char(guess)
        else:
            self.decrease_attempts()