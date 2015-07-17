# -*- coding: utf-8 -*-

def character_ngram(text,n):
    text = text.translate(None,' ,.')
    character_ngram_list=[]
    if len(text) >= n:
        for i in range(len(text)-n+1):
            character_ngram_list.append(text[i:i+n])
    return character_ngram_list

def se_in_set(set):
    if set == X_bigram_set:
        set_name = 'X'
    else:
        set_name = 'Y'
    if 'se' in set:
        print "se is in set " + set_name
    else:
        print "se is not in set " + set_name

if __name__ == "__main__":
    X_text = "paraparaparadise"
    Y_text = "paragraph"
    X_bigram = character_ngram(X_text,2)
    Y_bigram = character_ngram(Y_text,2)
    print "X: ", X_bigram
    print "Y: ", Y_bigram
    X_bigram_set = set(X_bigram)
    Y_bigram_set = set(Y_bigram)
    print "union: ", X_bigram_set | Y_bigram_set
    print "intersection: ", X_bigram_set & Y_bigram_set
    print "difference(X-Y): ", X_bigram_set - Y_bigram_set
    print "difference(Y-X): ", Y_bigram_set - X_bigram_set
    print se_in_set(X_bigram_set)
    print se_in_set(Y_bigram_set)
