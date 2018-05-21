# This file is created to build the matrix of word

source_tweet_file=r'C:\Users\Administrator\Desktop\tempResult3.txt'
source_word_file=r'C:\Users\Administrator\Desktop\NoRepatefile.txt'
net_word_file=r'C:\Users\Administrator\Desktop\net_word_file.txt'


f=open(source_tweet_file)
g=open(source_word_file)
h1=open(net_word_file,'w')

Table=g.read().split()
print('a' in  Table)
print('get' in  Table)
J=len(Table)
print(J)
print(Table[0:10])

net_word=[[2 for x in range(J)] for  y in range(J)]

tim=0

for fline in f:
    for word1 in fline.split():
        for word2 in fline.split():
            if word1 in Table and word2 in Table:
                net_word[Table.index(word1)][Table.index(word2)]-=1
                tim+=1

for i in range(J):
    for j in range(J):
        if net_word[i][j]<=0:
            net_word[i][j]='1'
        else:
            net_word[i][j]='0'

                
j=0
while j<J:
	h1.write(' '.join([x for x in net_word[j]])+'\n')
	j=j+1
print('tim')
h1.close()
f.close()
g.close()
