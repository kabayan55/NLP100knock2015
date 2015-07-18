# -*- coding: utf-8 -*-

def cipher(words):
    text = ''
    for word in words:
        if word.islower():
            text += chr(219 - ord(word))
        else:
            text += word
    return text

if __name__ == "__main__":
    words = 'abcdefgABCDEFG123456あいうえお'
    cip = cipher(words)
    print 'cipher: ', cip
    dec = cipher(cip)
    print 'decode: ', dec
