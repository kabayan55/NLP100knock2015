# -*- coding: utf-8 -*-

def word_lens():
    str1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    len_words=[]
    words=str1.translate(None,',.')
    for word in words.split():
        len_words.append(len(word))
    print len_words

if __name__ == "__main__":
    word_lens()
