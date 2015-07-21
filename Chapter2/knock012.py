# -*- coding: utf-8 -*-
import sys

if __name__ == "__main__":
    input_file = open('./hightemp.txt', 'r')
    col1_file = open('./col1.txt', 'w')
    col2_file = open('./col2.txt', 'w')
    for line in input_file:
        col1, col2, temperature, time = line.split("\t")
        col1_file.write(col1+'\n')
        col2_file.write(col2+'\n')
