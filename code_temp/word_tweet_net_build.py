

import numpy as np


word_source=""
tweet_souce=""

f=open(word_source)
g=open(tweet_source)

# 单词和tweet进行连接，如果单词在tweet中，则连接

#获取单词的长度：
l_word=len(f.read().spilt())

#获取tweet的长度，即多少条tweet
l_tweet=0
for line in g:
	l_tweet+=1

f.seek(0, os.SEEK_SET)
g.seek(0, os.SEEK_SET)

np.zeros(l_word*l_tweet).reshape(l_word,l_tweet)

for gline in g:
	for word in gline.split():
		for 





