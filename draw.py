from tkinter import *

STAGES = [
    "",
    "+---+  \n|   |  \n|      \n|      \n|      \n=========",
    "+---+  \n|   |  \n|   O  \n|      \n|      \n=========",
    "+---+  \n|   |  \n|   O  \n|   |  \n|      \n=========",
    "+---+  \n|   |  \n|   O  \n|  /|\\ \n|      \n=========",
    "+---+  \n|   |  \n|   O  \n|  /|\\ \n|  / \\ \n========="
]

def draw(root, word, cnt):
    Label(root, text=STAGES[cnt], font=('Courier', 29, 'bold')).pack()
    Label(root, text=f'Осталось попыток: {5 - cnt}').pack(side='bottom')