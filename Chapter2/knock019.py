# -*- coding: utf-8 -*-
import sys
from collections import Counter

if __name__ == "__main__":
    input_file = open('./hightemp.txt', 'r')
    lines = input_file.readlines()
    lines_list=[]
    for line in lines:
        lines_list.append(line.strip().split('\t')[0])
    for item in Counter(lines_list).most_common():
        print str(item[1]) + '\t' + item[0]
