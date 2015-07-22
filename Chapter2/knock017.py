# -*- coding: utf-8 -*-
import sys

if __name__ == "__main__":
    uniq_col1 = []
    input_file = open('./hightemp.txt', 'r')
    for line in input_file:
        col1, col2, temperature, time = line.split("\t")
        if col1 not in uniq_col1:
            uniq_col1.append(col1)

    print len(uniq_col1)
