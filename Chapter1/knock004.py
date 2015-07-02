# -*- coding: utf-8 -*-
from collections import defaultdict
atomic_symbols= defaultdict(lambda:0)

def atomic_symbol():
    str1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    
    words=str1.translate(None,',.')
    i=0
    for word in words.split():
        if i in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
            atomic_symbols[word[:1]]=i
        else:
            atomic_symbols[word[:2]]=i
        i+=1
    print atomic_symbols

if __name__ == "__main__":
    atomic_symbol()
