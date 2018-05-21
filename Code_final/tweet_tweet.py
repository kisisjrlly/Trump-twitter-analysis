import os

source_tweet_file=r'C:\Users\Administrator\Desktop\tempResult3.txt'
net_tweet_file=r'C:\Users\Administrator\Desktop\net_tweet_file_matrix.txt'

f=open(source_tweet_file)
h2=open(net_tweet_file,'w')

I=0

for line in f:
    I=I+1
f.seek(0, os.SEEK_SET)



# 第二个网络，以以推文为节点，两篇推文中有相同的词（一个或者两个），连接

net_tweet=[['0' for x in range(I)] for y in range(I)]

i=j=0

f=open(source_tweet_file)
g=open(source_tweet_file)
for fline in f:
	j=0
	g.seek(0, os.SEEK_SET)
	for fline1 in g:
		if len(set(fline.split())&set(fline1.split()))>1:
			net_tweet[i][j]='1'
		j=j+1
	i=i+1
print(i,j)
f.close()
g.close()

i=0
while i<I:
	h2.write(' '.join([x for x in net_tweet[i]])+'\n')
	i=i+1
h2.close()



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
