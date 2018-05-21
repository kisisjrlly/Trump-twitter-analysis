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
'''
for line in f:
    I=I+1

f.close()

'''
'''

f.close()
j=0
while j<J:
	h1.write(' '.join([x for x in net_word[j]])+'\n')
	j=j+1
'''
'''
# 第二个网络，以以推文为节点，两篇推文中有相同的词（一个或者两个），连接

net_tweet=[['0' for x in range(I)] for y in range(I)]

i=j=0

f=open(source_tweet_file)

for fline in f:
	j=0
	f1.seek(0, os.SEEK_SET)
	for fline1 in f1:
		if len(set(fline.split())&set(fline1.split()))>0:
			net_tweet[i][j]='1'
		j=j+1
	i=i+1	
f1.close()

i=0
while i<I:
	h2.write(' '.join([x for x in net_tweet[i]])+'\n')
	i=i+1
h2.close()


'''

'''
net_tweet=[]
i=j=0

f=open(source_tweet_file)

for fline in f:
	j=0
	f1.seek(0, os.SEEK_SET)
	for fline1 in f1:
		if len(set(fline)&set(fline1))>0:
			if [str(i),str(j)] not in net_tweet and [str(j),str(i)] not in net_tweet:
                            net_word.append([str(i),str(j)])
		j=j+1
	i=i+1	
f1.close()

'''
