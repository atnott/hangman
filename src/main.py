from src.engine import Hangman

if __name__ == '__main__':
    print('Консольная игра "Виселица"', '\nСЛОВА НА РУССКОМ ЯЗЫКЕ')
    temp = Hangman()
    while temp.flag:
        temp.start_game()
    print('Игра закончена! Возвращайся скорее!')