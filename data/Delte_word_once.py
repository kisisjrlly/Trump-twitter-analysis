#  This file is created to delete the word that occurs once

import sys,re,collections,nltk

sourcefile='c:/Users/Administrator/Desktop/tempResult3.txt'
Norepatefile_without_word_once='c:/Users/Administrator/Desktop/Wordfile_without_once1.txt'


words=[]
def get_words(sourcefile):
    f=open(sourcefile)
    for line in f:
        words.extend(line.split())
    f.close()
    return collections.Counter(words)
'''
def write_to_file(words, file):
    f = open(file, 'w')
    for item in words:
        if item[1]!=1:
            for field in item:
                f.write(str(field)+',')
            f.write('\n')
    f.close()
'''

def write_to_file(words, file):
    f = open(file, 'w')
    for item in words:
        for field in item:
            f.write(str(field)+',')
        f.write('\n')
    f.close()

if __name__=='__main__':
    words=get_words(sourcefile)
    write_to_file(words.most_common(),Norepatefile_without_word_once)


