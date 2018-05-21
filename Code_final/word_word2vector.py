import os

source_tweet_file=r'C:\Users\Administrator\Desktop\tempResult3.txt'
source_word_file=r'C:\Users\Administrator\Desktop\NoRepatefile.txt'
net_word_file=r'C:\Users\Administrator\Desktop\net_word_file.txt'
net_tweet_file=r'C:\Users\Administrator\Desktop\net_tweet_file.txt'
f=open(source_tweet_file)
#f1=open(source_tweet_file)
g=open(source_word_file)
h1=open(net_word_file,'w')
#h2=open(net_tweet_file,'w')

# 第一个网络，以词为节点，两个不同的词在同一个篇推文中，连接
Table=g.read()
J=len(Table)
I=0
#net_word=[['0' for x in range(J)] for  y in range(J)]


net_word=[]


for fline in f:
    for word1 in fline:
        for word2 in fline:
            if word1 in Table and word2 in Table:
                #net_word[Table.index(word1)][Table.index(word2)]='1'
                if ([str(Table.index(word1)),str(Table.index(word2))]) not in net_word and ([str(Table.index(word2)),str(Table.index(word1))]) not in net_word:
                    net_word.append([str(Table.index(word1)),str(Table.index(word2))])
    I=I+1
J=len(net_word)
j=0
while j<J:
	h1.write(' '.join([x for x in net_word[j]])+'\n')
	j=j+1
h1.close()
f.close()
g.close()

