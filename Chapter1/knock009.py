# -*- coding: utf-8 -*-
import random

def typoglycemia(words):
    shuffle = ""
    for word in words:
        if len(word) < 4:
            shuffle += word
        else:
            shuffle += word[0] + shuffle_char(word[1:-1]) + word[-1]
        shuffle += ' '
    return shuffle

def shuffle_char(word):
     word_list = list(word)
     random.shuffle(word_list)
     shuffle = "".join(word_list)
     return shuffle

if __name__ == "__main__":
    text = "I could'nt believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    words = text.split(" ")
    print typoglycemia(words)
