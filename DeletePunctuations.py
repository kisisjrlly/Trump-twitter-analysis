# 此文档用来把标点符号去掉并分词
import nltk
english_punctuations = ['-', '//', '..', "'", '...', '``', "''", ',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
f=open('c:/Users/Administrator/Desktop/test/temp/Without_punctuations.txt')
g=open('c:/Users/Administrator/Desktop/test/temp/Without_punctuations.txt2','w')
for line in f:
      tokens = nltk.word_tokenize(line)
      l=[x.lower() for x in tokens if not x in english_punctuations]
      g.write(' '.join(l)+'\n')

f.close()
g.close()
      
