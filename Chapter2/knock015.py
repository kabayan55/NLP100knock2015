# -*- coding: utf-8 -*-
import sys

if __name__ == "__main__":
    n = input()
    input_file = open('./hightemp.txt', 'r')
    lines = input_file.readlines()
    lines_list=[]
    for line in lines:
        lines_list.append(line.strip())
    for i in range(len(lines_list)-n, len(lines_list)):
        print lines_list[i]
