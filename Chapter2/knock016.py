# -*- coding: utf-8 -*-
import sys
import math

if __name__ == "__main__":
    n = input()
    input_file = open('./hightemp.txt', 'r')
    lines = input_file.readlines()
    lines_list=[]
    for line in lines:
        lines_list.append(line.strip())

    block_size = int(math.ceil(float(len(lines_list))/float(n)))

    for file_index in range(n-1):
        output_file = open("./hightemp_%s.txt" % str(file_index+1),'w')
        for index in range(block_size):
            output_file.write(lines_list[file_index * block_size + index]+'\n')
    output_file = open("./hightemp_%s.txt" % str(n),'w')
    for index in range(len(lines_list)%n):
        output_file.write(lines_list[(n-1) * block_size + index]+'\n')
