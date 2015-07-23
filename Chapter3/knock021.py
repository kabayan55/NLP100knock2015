# -*- coding: utf-8 -*-
import re

if __name__ == '__main__':
    input_file = open('./jawiki-country.json', 'r')
    category = re.compile('\[\[Category:.*')
    for line in input_file:
        if category.search(line):
            print line
