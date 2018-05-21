import numpy as np
import math
import os


def Del_zero_not(source_file,type):
    res=np.loadtxt(source_file)
    l_init=len(res)

    if type=='word':
        Noreapetfile='C:/Users/Administrator/Desktop/NoRepatefile.txt'
        wordafterDelzeronot="C:/Users/Administrator/Desktop/wordafterDelzeronot.txt"
        f=open(Noreapetfile)
        g=open(wordafterDelzeronot,'w')
        j=0
        Table=f.read().split()
        for i in range(l_init):
            if (res[i-j]==0).all():
                np.delete(res,i-j,0)
                np.delete(res,i-j,1)
                print(len(res))
                del Table[i-j]
                j+=1
        g.write(' '.join([x for x in Table]))
        f.close()
        g.close()
        
    if type=='tweet':
        j=0
        tempResultfile3='C:/Users/Administrator/Desktop/tempResult3.txt'
        tweetafterDelzeronot='C:/Users/Administrator/Desktop/tweetafterDelzeronot.txt'
        f=open(tempResultfile3)
        g=open(tweetafterDelzeronot,'w')
        for i,fline in zip(range(l_init),f):
            flag=1
            if (res[i-j]==0).all():
                np.delete(res,i-j,0)
                np.delete(res,i-j,1)
                flag=0
            if flag==1:
                g.write(fline)
        f.close()
        g.close()
    
        
    return res ,len(res)

word_file='C:/Users/Administrator/Desktop/net_word_file.txt'


print(Del_zero_not(word_file,'word')[1])

