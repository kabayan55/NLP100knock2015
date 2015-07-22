# -*- coding: utf-8 -*-
import json

if __name__ == '__main__':
    input_file = open('./jawiki-country.json', 'r')
    for line in input_file:
        data = json.loads(line)
        if data['title'] == u"イギリス":
            print data['text'].encode('utf-8')
