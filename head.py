import random; import string; from draw import *

words = [word for word in open('words.txt').read().split() if len(word) > 3 and '-' not in word]
mas, cnt, was = [], 0, ''

def clear(root):
    for el in root.winfo_children(): el.destroy()

def mask(word): return '*' * len(word)

def start(word, root):
    global was, cnt
    cnt = 0; was = ''
    word = words[random.randint(0, len(words) - 1)]
    Label(root, text='hangman play', font=("Times New Roman",21,"bold")).pack()
    btnStart = Button(root, text='Начать игру', command=lambda: proc(root, [word, mask(word)]))
    btnStart.pack()
    return root, [word, mask(word)]

def proc(root, word):
    clear(root); global cnt
    Label(root, text=f'Слово загадано \n{word[1]}', font=("Times New Roman", 21, "bold")).pack()
    Label(root, text='Введите букву: ').pack()

    en = Entry(root); en.pack(); en.focus()
    draw(root, word, cnt)

    en.bind("<Return>", lambda event: cin(root, word, en))

def cin(root, word, en):
    global was
    char = en.get().lower()
    if not correct_char(char):
        Label(root, text='Некорректная буква! Введите новую!').pack()
        en.delete(0, END)
        return
    was += char
    availability(root, char, word)

def correct_char(char):
    return 0 if ((char in string.printable) or (len(char) != 1) or (char == ' ') or (char in was)) else 1

def availability(root, char, word):
    global cnt, was
    if char in word[0]:
        replace_char(word, char)
        if word[0] == word[1].lower(): win(root, word)
        else: proc(root, word)
    else:
        if cnt < 4: cnt += 1; proc(root, word)
        else:
            clear(root)
            Label(root, text=f'Вы проиграли! \nИсходное слово: {word[0].upper()}', font=("Times New Roman", 21, "bold")).pack()
            draw(root, word, 5)
            btn = Button(root, text='Новая игра', command=lambda: proc(*start(words, root)))
            btnExit = Button(root, text='Закрыть игру', command=root.destroy)
            btn.pack(); btnExit.pack()

def replace_char(word, char):
    idx = [i for i in range(len(word[0])) if word[0][i] == char]
    word[1] = [ch for ch in word[1]]
    for i in idx: word[1][i] = char.upper()
    word[1] = ''.join(word[1])

def win(root, word):
    if word[0] == word[1].lower():
        clear(root)
        Label(root, text=f'Вы победили! Слово угадано! \n{word[0].upper()}', font=("Times New Roman", 21, "bold")).pack()
        btn = Button(root, text='Новая игра', command=lambda: proc(*start(words, root)))
        btnExit = Button(root, text='Закрыть игру', command=root.destroy)
        btn.pack(); btnExit.pack()