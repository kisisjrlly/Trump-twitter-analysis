# BaseMatrix=''
# tempResult3=''
# NoRepeatefile=''

# f=open(BaseMatrix)
# g=open(tempResult3)
# h=open(NoRepeatefile)



# I=len()


# I,J,base,Table

# 第一个网络，以词为节点，两个不同的词在同一个篇推文中，连接

net_word=[['0' for x in range(J)] for  y in range(J)]


i=j=0
for row in base:
	i=0
	for col1 in row:
		j=0
		for col2 in row:

                        if col1=='1' and col2=='1'
			net_word[i][j]='1'
			j=j+1
		i=i+1
# 第二个网络，以以推文为节点，两篇推文中有相同的词（一个或者两个），连接

net_tweet=[['0' for x in range(I)] for y in range(J)]

for index_count_word in range(J):
	for index_count_tweet1 in range(I):
		for index_count_tweet2 in range(I):
			if base[index_count_tweet1][index_count_word]=='1' and base[index_count_tweet2][index_count_word]=='1':
				net_tweet[index_count_tweet1][index_count_tweet2]=='1'
		
	
