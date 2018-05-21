'''
def ncut(ss,matrix,K):

    return (Ncut)
    
def Del_zero_not(source_file,type):

    return res ,len(res)

def Init_Division(source_file,K,ty):

    (res,l)=Del_zero_not(source_file,ty)

    return ss,matrix,l
    
    
def SA_random_division_withTempture(ss,matrix,B,p,l):

    return ss,matrix
    
def MuNcut(word_file,tweet_file,word_tweet_file,K,p,loop):
    (ss_word,matrix_word,l_word)=Init_Division(word_file,K,'word')
    (ss_tweet,matrix_tweet,l_tweet)=Init_Division(tweet_file,K,'tweet')
    (ss_word_tweet,matrix_word_tweet,l_word_tweet)=Init_Division(word_tweet_file,K,'others')


    Ncut_word=ncut(ss_word,matrix_word,K)
    Ncut_tweet=ncut(ss_tweet,matrix_tweet,K)
    Ncut_word_tweet=ncut(ss_word_tweet,matrix_word_tweet,K)

    (ss_word,matrix_word)=SA_random_division_withTempture(ss_word,matrix_word,B,p,l_word)
            (ss_tweet,matrix_tweet)=SA_random_division_withTempture(ss_tweet,matrix_tweet,B,p,l_tweet)
            (ss_word_tweet,matrix_word_tweet)=SA_random_division_withTempture(ss_word_tweet,matrix_word_tweet,B,p,l_word_tweet)

            
            Ncut_word = ncut(ss_word,matrix_word,K)
            Ncut_tweet = ncut(ss_tweet,matrix_word,K)
            Ncut_word_tweet = ncut(ss_word_tweet,matrix_word_tweet,K)
            temp_cut_value = Ncut_word + Ncut_tweet + Ncut_word_tweet
            
    return (Best_cut_com_word[...,0],Best_cut_com_tweet[...,0],Best_cut_com_word_tweet[...,0],ss_word,ss_tweet)
    
def Output_word_after_MuNcut(Best_cut_com_word,ss,K):
    pass
    
def Output_tweet_after_MuNcut(Best_cut_com_tweet,ss,K):
    pass

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
'''
import time
import numpy as np
import math
import os
#from ctypes import *

#Ncutc=CDLL('./ncut.dll')


#Time=0

def ncut(ss,matrix,K):
    Ncut=0
    for i in range(K-1):
        ncut_inner=matrix[...,1:][ss[i]:ss[i+1],ss[i]:ss[i+1]].sum()
        ncut_out=matrix[...,1:][ss[i]:ss[i+1]].sum()-ncut_inner
        
        Ncut+=(ncut_out/ncut_inner)
    return (Ncut)
def ncut_together(ss_word,ss_tweet,word_list,tweet_list,word_tweet_matrix):

    
    #print('for times:',end=' ')
    #print(Time)
    #start=time.clock()
    
    ss_word=list(ss_word)

    ss_tweet=list(ss_tweet)
    ss_word=ss_word[1:]
    ss_word.append(len(word_list))

    ss_tweet=ss_tweet[1:]
    ss_tweet.append(len(tweet_list))
    Ncut=0
    temp=0
    i=0
    #np.array(word_list,dtype=np.int8)
    #np.array(tweet_list,dtype=np.int8)
    
    word_list=list(word_list)
    tweet_list=list(tweet_list)
    word_list=[int(x) for x in word_list]
    tweet_list=[int(x) for x in tweet_list]
    


    #end=time.clock()

    #print('ncut_together_first%s'%(end-start))

    ncut_inner=0
    
    '''
    print(len(word_list))
    print(len(tweet_list))
    print(np.shape(word_tweet_matrix))
    '''

    
    for I,J in zip(ss_word,ss_tweet):
        while i<I:
            j=temp
            while j<J:
                ncut_inner+=word_tweet_matrix[tweet_list[j]-1][word_list[i]-1]
                j+=1
            i+=1
        ncut_out=word_tweet_matrix.sum()-ncut_inner
        Ncut+=(ncut_out/ncut_inner)
        temp=J
    
    #global Ncutc
    #Ncut=Ncutc.ncut(ss_word,ss_tweet,word_list,tweet_list,word_tweet_matrix)
    return (Ncut)   
            
    

def Del_zero_not(source_file,ty,matrix_word_tweet):
    res=np.loadtxt(source_file)
    l_init=len(res)
    
    if ty=='word':
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
                matrix_word_tweet=np.delete(matrix_word_tweet,i-j,1)
                del Table[i-j]
                j+=1
        g.write(' '.join([x for x in Table]))
        f.close()
        g.close()
        
    if ty=='tweet':
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
                matrix_word_tweet=np.delete(matrix_word_tweet,i-j,0)
                flag=0
                j+=1
            if flag==1:
                g.write(fline)
        f.close()
        g.close()
    
       
    return res ,len(res),matrix_word_tweet
    

def Init_Division(source_file,K,ty,matrix_word_tweet):

    (res,l,matrix_word_tweet)=Del_zero_not(source_file,ty,matrix_word_tweet)
    
    print(l)
    res+=1
    matrix_word_tweet+=1
    '''
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
    '''

    ss=list(range(l))[::l//K][:K]
    ss=np.array(ss)

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
    
    return ss,matrix,l,matrix_word_tweet


def SA_random_division_withTempture(ss,matrix,B,p,l,K):
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

    #start = time.clock()
    #读取文件并初始随机分组处理
    matrix_word_tweet=np.loadtxt(word_tweet_file)
    (ss_word,matrix_word,l_word,matrix_word_tweet)=Init_Division(word_file,K,'word',matrix_word_tweet)
    (ss_tweet,matrix_tweet,l_tweet,matrix_word_tweet)=Init_Division(tweet_file,K,'tweet',matrix_word_tweet)
    
    #(ss_word_tweet,matrix_word_tweet,l_word_tweet)=Init_Division(word_tweet_file,K,'others')
    matrix_word_tweet=np.loadtxt(word_tweet_file)
    
    #end=time.clock()

    #print('InitTime:%s'%(end-start))
    

    
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

    #start=time.clock()
    
    Ncut_word=ncut(ss_word,matrix_word,K)
    Ncut_tweet=ncut(ss_tweet,matrix_tweet,K)
    
    #Ncut_word_tweet=ncut(ss_word_tweet,matrix_word_tweet,K)
    Ncut_word_tweet=ncut_together(ss_word,ss_tweet,matrix_word[...,0],matrix_tweet[...,0],matrix_word_tweet)

    #end=time.clock()

    #print('nut one times:%s'%(end-start))
    
    Best_cut_com_word=matrix_word
    Best_cut_com_tweet=matrix_tweet
    #Best_cut_com_word_tweet=matrix_word_tweet
    Best_cut_value=Ncut_word+Ncut_tweet+Ncut_word_tweet
    
    #start=time.clock()
    
    while B>b:
        for m in range(loop):
            (ss_word,matrix_word)=SA_random_division_withTempture(ss_word,matrix_word,B,p,l_word,K)
            (ss_tweet,matrix_tweet)=SA_random_division_withTempture(ss_tweet,matrix_tweet,B,p,l_tweet,K)
            #(ss_word_tweet,matrix_word_tweet)=SA_random_division_withTempture(ss_word_tweet,matrix_word_tweet,B,p,l_word_tweet)

            
            Ncut_word = ncut(ss_word,matrix_word,K)
            Ncut_tweet = ncut(ss_tweet,matrix_word,K)
            #Ncut_word_tweet = ncut(ss_word_tweet,matrix_word_tweet,K)
            Ncut_word_tweet=ncut_together(ss_word,ss_tweet,matrix_word[...,0],matrix_tweet[...,0],matrix_word_tweet)
            temp_cut_value = Ncut_word + Ncut_tweet + Ncut_word_tweet

            
            if temp_cut_value < Best_cut_value:
                Best_cut_value = temp_cut_value
                Best_cut_com_word = matrix_word
                Best_cut_com_tweet = matrix_tweet
                #Best_cut_com_word_tweet = matrix_word_tweet
            else:
                #print('temp_cut_value:%f'%temp_cut_value)
                #print('Best_cut_value:%f'%Best_cut_value)
                #print('B%s'%B)
                #print('-( temp_cut_value - Best_cut_value) / B:%f'%-( temp_cut_value - Best_cut_value) / B)
                if np.random.rand() < math.exp(-( temp_cut_value - Best_cut_value) / B):
                    Best_cut_value = temp_cut_value
                    Best_cut_com_word = matrix_word
                    Best_cut_com_tweet = matrix_tweet
                    #Best_cut_com_word_tweet = matrix_word_tweet
        B=t*B
    #end=time.clock()

    #print('SA times:%s'%(end-start))
    #return (Best_cut_com_word[...,0],Best_cut_com_tweet[...,0],Best_cut_com_word_tweet[...,0],ss_word,ss_tweet)    
    return (Best_cut_com_word[...,0],Best_cut_com_tweet[...,0],ss_word,ss_tweet)

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

    #查看tweet每个分组的下标
    print(ss)

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

            
            
        
def MuNcut_main():


    word_file='C:/Users/Administrator/Desktop/net_word_file.txt'
    tweet_file='C:/Users/Administrator/Desktop/net_tweet_file.txt'
    
    word_tweet_file='C:/Users/Administrator/Desktop/BaseMatrix.txt'
    #word_tweet_file='C:/Users/Administrator/Desktop/word_tweet_together.txt'
    K=20
    p=10
    loop=10
    (Best_cut_com_word,Best_cut_com_tweet,ss_word,ss_tweet)=MuNcut(word_file,tweet_file,word_tweet_file,K,p,loop)
    '''
    Output_word_after_MuNcut(Best_cut_com_word,ss_word,K)
    Output_tweet_after_MuNcut(Best_cut_com_tweet,ss_tweet,K)
    '''

    return Best_cut_com_tweet,ss_tweet



