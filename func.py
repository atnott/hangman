import random

def start(words):
    word = words[random.randint(0, len(words) - 1)]
    return [word, mask(word)]

def mask(word): return '*' * len(word)

def proc(word):
    cnt = 0
    while word[1].count('*') > 0 or cnt < 4:
        if word[0] == word[1].lower(): break
        char = input('Введите букву: ').lower()
        if char in word[0]: example(word, char)
        else: cnt += 1; draw(cnt, word)

def example(word, char):
    idx = [i for i in range(len(word[0])) if word[0][i] == char]
    word[1] = [ch for ch in word[1]]
    for i in idx: word[1][i] = char.upper()
    word[1] = ''.join(word[1])
    print(f'Вы попали! \n{word[1]}' if word[0] != word[1].lower() else f'Вы победили!!! Исходное слово: {word[0].upper()}')


def draw(cnt, word):
    print(f'Вы ошиблись:(' if cnt < 5 else f'Вы проиграли! Исходное слово: {word[0].upper()}')
    if cnt == 1:
        print('У вас осталось 4 попытки!')
        print(
f'''
    +---+
    |   |
    |   
    |  
    |   
    |  
=========''')
    elif cnt == 2:
        print('У вас осталось 3 попытки!')
        print(
'''
    +---+
    |   |
    |   O
    |  
    |   
    |  
========='''
    )
    elif cnt == 3:
        print('У вас осталось 2 попытки!')
        print(
'''
    +---+
    |   |
    |   O
    |  /|/
    |   
    |  
========='''
)
    elif cnt == 4:
        print('У вас осталась 1 попытка!')
        print(
'''
    +---+
    |   |
    |   O
    |  /|/
    |  / 
    |  
========='''
)
    elif cnt == 5:
        print(
'''
    +---+
    |   |
    |   O
    |  /|/
    |  / /
    |  
========='''
)

