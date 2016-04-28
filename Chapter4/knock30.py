# -*- encoding: utf-8 -*-
"""
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．
-> $ cat neko.txt | mecab >& neko.txt.mecab
"""

"""
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

def ReadMecabResult(file):
    sentence_morpheme=[]
    morpheme_mapping=[]
    for line in file:
        line = line.rstrip()

        if line == 'EOS':
            sentence_morpheme.append(morpheme_mapping)
            morpheme_mapping =[]
            continue
        features = line.split('\t')
        feature = features[1].split(',')

        morpheme = {
            'surface' : features[0],
            'base'    : feature[6],
            'pos'     : feature[0],
            'pos1'    : feature[1]
        }

        morpheme_mapping.append(morpheme)
    return sentence_morpheme
        
if __name__ == '__main__':
    input_file = open('neko.txt.mecab','r')
    sentence_morpheme = ReadMecabResult(input_file)
    print str(sentence_morpheme).decode('string-escape')
