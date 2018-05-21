import numpy as np
import math
import os

def ncut(ss,matrix,K):
    Ncut=0
    for i in range(K-1):
        ncut_inner=matrix[...,1:][ss[i]:ss[i+1],ss[i]:ss[i+1]].sum()
        ncut_out=matrix[...,1:][ss[i]:ss[i+1]].sum()-ncut_inner
        Ncut+=(ncut_inner/ncut_out)
    return (Ncut)

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
                res=np.delete(res,i-j,0)
                res=np.delete(res,i-j,1)
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
                res=np.delete(res,i-j,0)
                res=np.delete(res,i-j,1)
                flag=0
            if flag==1:
                g.write(fline)
        f.close()
        g.close()
    
        
    return res ,len(res)
    

def Init_Division(source_file,K,ty):

    (res,l)=Del_zero_not(source_file,ty)
    res+=1
    print(l)
    while 1:
        s=np.random.randint(1,l//5,K)
        if s.sum()==l:
            #print(s)
            break
    temp=0
    ss=s
    for i in range(len(s)):
        temp+=s[i]
        ss[i]=temp
    ss=ss-s[0]
    #print(ss)

    word_index=np.array(range(1,l+1))
    matrix=np.c_[word_index,res]

    #初始随机打乱网络矩阵：
    
    #np.random.shuffle(matrix)

    for i in range(1000):
        a=np.random.randint(1,l)
        b=np.random.randint(1,l)
        if(a<b):
            matrix[[a-1,b-1],:]=matrix[[b-1,a-1],:]
            matrix[:,[a,b]]=matrix[:,[b,a]]
    
    return ss,matrix,l


def SA_random_division_withTempture(ss,matrix,B,p,l):
    for j in range(int(B*p)):

        #print(j)
        choice=np.random.randint(1,l)

        #print("choice:%d" %choice)
        #print(ss)      
        choice_index=len(np.where(ss<choice)[0])
        #print("choice_index:%d"%choice_index)
        
        if choice_index==1:
            matrix[[choice-1, ss[1]-1], :] = matrix[[ss[1]-1, choice-1], :]
            matrix[:,[choice, ss[1]]] = matrix[:,[ss[1], choice]]
            ss[1]=ss[1]-1
        elif choice_index==K:
            matrix[[choice-1, ss[K-1]], :] = matrix[[ss[K-1], choice-1], :]
            matrix[:,[choice, ss[K-1]]] = matrix[:,[ss[K-1], choice]]
            ss[K-1]=ss[K-1]+1
        else:
            if np.random.rand()>0.5:
                matrix[[choice-1,ss[choice_index-1]-1],:]=matrix[[ss[choice_index-1]-1,choice-1],:]
                matrix[:,[choice,ss[choice_index-1]]]=matrix[:,[ss[choice_index-1],choice]]
                ss[choice_index]-=1
            else:
                matrix[[choice-1,ss[choice_index-1]-1],:]=matrix[[ss[choice_index-1]-1,choice-1],:]
                matrix[:,[choice,ss[choice_index-1]]]=matrix[:,[ss[choice_index-1],choice]]
                ss[choice_index-1]+=1
        return ss,matrix


def MuNcut(word_file,tweet_file,word_tweet_file,K,p,loop):
    '''
    wordfile: the word 0-1 net
    tweetfile: the tweet 0-1 net
    word_tweet_file:the word and tweet 0-1 net
    K:the number of clusters
    
    '''
    #读取文件并初始随机分组处理
    (ss_word,matrix_word,l_word)=Init_Division(word_file,K,'word')
    (ss_tweet,matrix_tweet,l_tweet)=Init_Division(tweet_file,K,'tweet')
    (ss_word_tweet,matrix_word_tweet,l_word_tweet)=Init_Division(word_tweet_file,K,'others')

    
    '''
    初始温度：B=100
    结束温度：b=1
    下降系数：t=0.99
    迭代次数：loop=10000
    '''
    
    B=100
    b=1
    t=0.9
    #loop=100 #每个温度进行的次数
    #p=100#退火过程分组随温度变化的过程：当温度越低，随机分组的扰乱程度越低
    Ncut_word=ncut(ss_word,matrix_word,K)
    Ncut_tweet=ncut(ss_tweet,matrix_tweet,K)
    Ncut_word_tweet=ncut(ss_word_tweet,matrix_word_tweet,K)
    
    Best_cut_com_word=matrix_word
    Best_cut_com_tweet=matrix_tweet
    Best_cut_com_word_tweet=matrix_word_tweet
    Best_cut_value=Ncut_word+Ncut_tweet+Ncut_word_tweet
    
    
    while B>b:
        for m in range(loop):
            (ss_word,matrix_word)=SA_random_division_withTempture(ss_word,matrix_word,B,p,l_word)
            (ss_tweet,matrix_tweet)=SA_random_division_withTempture(ss_tweet,matrix_tweet,B,p,l_tweet)
            (ss_word_tweet,matrix_word_tweet)=SA_random_division_withTempture(ss_word_tweet,matrix_word_tweet,B,p,l_word_tweet)

            
            Ncut_word = ncut(ss_word,matrix_word,K)
            Ncut_tweet = ncut(ss_tweet,matrix_word,K)
            Ncut_word_tweet = ncut(ss_word_tweet,matrix_word_tweet,K)
            temp_cut_value = Ncut_word + Ncut_tweet + Ncut_word_tweet

            
            if temp_cut_value < Best_cut_value:
                Best_cut_value = temp_cut_value
                Best_cut_com_word = matrix_word
                Best_cut_com_tweet = matrix_tweet
                Best_cut_com_word_tweet = matrix_word_tweet
            else:
                if np.random.rand() < math.exp(-( temp_cut_value - Best_cut_value) / B):
                    Best_cut_value = temp_cut_value
                    Best_cut_com_word = matrix_word
                    Best_cut_com_tweet = matrix_tweet
                    Best_cut_com_word_tweet = matrix_word_tweet
        B=t*B

    return (Best_cut_com_word[...,0],Best_cut_com_tweet[...,0],Best_cut_com_word_tweet[...,0],ss_word,ss_tweet)    


def Output_word_after_MuNcut(Best_cut_com_word,ss,K):
    
    word_file="C:/Users/Administrator/Desktop/wordafterDelzeronot.txt"
    word_file_after_cut='C:/Users/Administrator/Desktop/word_file_after_cut.txt'

    f=open(word_file)
    g=open(word_file_after_cut,'w')

    word_index_after_cut=[int(x) for x in list(Best_cut_com_word)]
    
    Table=f.read().split()
    L=len(Table)
    i=j=1
    temp=[]
    
    for i in range(L):
        temp.append(Table[word_index_after_cut[i]-1])
        if i==ss[j]:
           g.write(' '.join(temp)+'\n')
           if j<K-1:
               j+=1
           temp=[]
    g.write(' '.join(temp)+'\n')
    
    g.close()
    f.close()

def Output_tweet_after_MuNcut(Best_cut_com_tweet,ss,K):
    tweetfile='C:/Users/Administrator/Desktop/tweetafterDelzeronot.txt'
    tweet_file_after_cut='C:/Users/Administrator/Desktop/tweet_file_after_cut.txt'
    f=open(tweetfile)
    g=open(tweet_file_after_cut,'w')


    word_index_after_cut=[int(x) for x in list(Best_cut_com_tweet)]

    k=1
    for i in word_index_after_cut:
        j=0
        f.seek(0, os.SEEK_SET)
        for fline in f:
            if i==j:
                g.write(fline)
                break
            j+=1
        if i==ss[k]:
            g.write('\n')
            if k<K-1:
                k+=1
            
            
        
if __name__=='__main__':


    word_file='C:/Users/Administrator/Desktop/net_word_file.txt'
    tweet_file='C:/Users/Administrator/Desktop/net_tweet_file.txt'
    word_tweet_file='C:/Users/Administrator/Desktop/BaseMatrix.txt'
    K=20
    p=10
    loop=100
    (Best_cut_com_word,Best_cut_com_tweet,Best_cut_com_word_tweet,ss_word,ss_tweet)=MuNcut(word_file,tweet_file,word_tweet_file,K,p,loop)

    Output_word_after_MuNcut(Best_cut_com_word,ss_word,K)
    Output_tweet_after_MuNcut(Best_cut_com_tweet,ss_tweet,K)
