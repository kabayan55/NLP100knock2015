# -*- coding: utf-8 -*-
import re

if __name__ == '__main__':
    input_file = open('./jawiki-country.json', 'r')

    #pattern = '\[\[Category\:(.*)\]\]'
    pattern = '\[\[Category\:(((?P<category1>.*)\|+.*)|(?P<category2>.*))\]\]'
    category = re.compile(pattern)
    for line in input_file:
        category_name = category.search(line)
        if category_name:
            if category_name.group('category2') is None:
                print category_name.group('category1')
            else:
                category_name.group('category2')
