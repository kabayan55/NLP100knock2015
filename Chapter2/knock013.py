# -*- coding: utf-8 -*-
import sys

if __name__ == "__main__":
    col1_file = open('./col1.txt', 'r')
    col2_file = open('./col2.txt', 'r')
    for col1,col2 in zip(col1_file,col2_file):
        print col1.strip()+'\t'+col2.strip()
