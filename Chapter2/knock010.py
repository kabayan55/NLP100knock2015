# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    file = open('./hightemp.txt', 'r')
    lines = file.readlines()
    print len(lines)
