# -*- coding: utf-8 -*-
if __name__ == "__main__":
  import sys
  input_file = open('./hightemp.txt', 'r')
  for line in input_file:
    line_space = line.replace('\t', ' ')
    print line_space
