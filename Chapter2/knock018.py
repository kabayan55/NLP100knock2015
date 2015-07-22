# -*- coding: utf-8 -*-
import sys

if __name__ == "__main__":
    input_file = open('./hightemp.txt', 'r')
    lines = input_file.readlines()
    lines_list=[]
    for line in lines:
        lines_list.append(line.strip().split('\t'))
    sorted_lines_list = sorted(lines_list, key=lambda x:x[2], reverse=True)
    for line in sorted_lines_list:
        print line[0]+'\t'+line[1]+'\t'+line[2]+'\t'+line[3]
