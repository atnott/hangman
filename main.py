from func import *
words = [word for word in open('words.txt').read().split() if len(word) > 3]

word = start(words)
print(word)

proc(word)

