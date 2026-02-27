from tkinter import *

STAGES = [
    "", # 0 ошибок
    "+---+  \n|   |  \n|      \n|      \n|      \n=========", # 1: Стойка слева
    "+---+  \n|   |  \n|   O  \n|      \n|      \n=========", # 2: Голова
    "+---+  \n|   |  \n|   O  \n|   |  \n|      \n=========", # 3: Туловище
    "+---+  \n|   |  \n|   O  \n|  /|\\ \n|      \n=========", # 4: Руки
    "+---+  \n|   |  \n|   O  \n|  /|\\ \n|  / \\ \n========="  # 5: Ноги
]

def draw(root, word, cnt):
    Label(root, text=STAGES[cnt], font=('Courier', 29, 'bold')).pack()
    Label(root, text=f'Осталось попыток: {5 - cnt}').pack(side='bottom')