# -*- coding: utf-8 -*-
import sys

if __name__ == "__main__":
    n = input()
    input_file = open('./hightemp.txt', 'r')
    for line,i in zip(input_file,range(n)):
            print line
