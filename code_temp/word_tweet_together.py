import numpy as np
word_tweet_file='C:/Users/Administrator/Desktop/BaseMatrix.txt'
word_tweet_together='C:/Users/Administrator/Desktop/word_tweet_together.txt'

f=open(word_tweet_together,'w')
weightArray=np.loadtxt(word_tweet_file)

weightArraySec=np.transpose(weightArray)

p=len(weightArray)
q=len(weightArraySec)

m=np.empty([p+q,p+q],dtype=int)

for i in range(p+q):
    for j in range(p+q):
        if i<p:
            if j<q:
                m[i][j]=weightArray[i][j]
            else:
                m[i][j]=0
        else:
            if j<q:
                m[i][j]=0
            else:
                m[i][j]=weightArraySec[i-p][j-q]
m=list(m)

for i in range(p+q):
    f.write(' '.join([str(int(x)) for x in m[i]])+'\n')
    
