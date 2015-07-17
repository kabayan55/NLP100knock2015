# -*- coding: utf-8 -*-
from collections import defaultdict
atomic_symbols= defaultdict(lambda:0)

def word_ngram(text,n):
    text = text.translate(None,',.')
    text_list = text.split(" ")
    word_ngram_list=[]
    if len(text_list) >= n:
        for i in range(len(text_list)-n+1):
            word_ngram_list.append(text_list[i:i+n])
    return word_ngram_list

def character_ngram(text,n):
    text = text.translate(None,' ,.')
    character_ngram_list=[]
    if len(text) >= n:
        for i in range(len(text)-n+1):
            character_ngram_list.append(text[i:i+n])
    return character_ngram_list

if __name__ == "__main__":
    text = "I am an NLPer"
    n = 2
    print word_ngram(text,n)
    print character_ngram(text,n)
