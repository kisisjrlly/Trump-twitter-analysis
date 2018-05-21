# The follow function only calculates the value of after clusering


'''
word_net_file:the net file of word or tweet
K:the number of clusters
'''




import numpy as np
from sklearn.metrics.pairwise import rbf_kernel
import math



def cal_gauss(b):  
    res=rbf_kernel(b)
    for i in range(len(res)):
        res[i,i]=0
    return res

def ncut(matrix,K,ss):
    Ncut=0
    for i in range(K-1):
        ncut_inner=matrix[...,1:][ss[i]:ss[i+1],ss[i]:ss[i+1]].sum()
        ncut_out=matrix[...,1:][ss[i]:ss[i+1]].sum()-ncut_inner
        Ncut+=(ncut_inner/ncut_out)
    return (Ncut,matrix)
# simulated annealing technology

def sa(source,K):
    '''
    初始温度：B=100
    结束温度：b=1
    下降系数：t=0.99
    迭代次数：loop=10000
    
    '''
    res=np.loadtxt(source)
    l=len(res)
    while 1:
        s=np.random.randint(1,l//5,K)
        if s.sum()==l:
            print(s)
            break
    temp=0
    ss=s
    for i in range(len(s)):
        temp+=s[i]
        ss[i]=temp
    ss=ss-s[0]
    print(ss)

    word_index=np.array(range(1,l+1))
    matrix=np.c_[word_index,res]

    #初始随机打乱网络矩阵：
    
    #np.random.shuffle(matrix)

    for i in range(1000):
        a=np.random.randint(1,l)
        b=np.random.randint(1,l)
        matrix[[a-1,b-1],:]=matrix[[b-1,a-1],:]
        matrix[:,[a-1,b-1]]=matrix[:,[b-1,a-1]]

    #计算权重，接下来进行计算时要保持行和列的位置
    #此处不打算用高斯核函数进行计算，因为0-1矩阵本身就是距离矩阵，此时可选
    #matrix=np.c_[word_index,cal_gauss(matrix[...,1:])]

    
    B=100
    b=1
    t=0.9
    loop=10
    p=10

    (Best_cut_value,Best_cut_com)=ncut(matrix,K,ss)
    while B>b:
        for m in range(loop):
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
            (temp_cut_value,temp_cut_com)=ncut(matrix,K,ss)
            if temp_cut_value<Best_cut_value:
                (Best_cut_value,Best_cut_com)=(temp_cut_value,temp_cut_com)
            else:
                if np.random.rand() < math.exp(-( temp_cut_value- Best_cut_value) / B):
                    (Best_cut_value,Best_cut_com)=(temp_cut_value,temp_cut_com)
        B=t*B

    return (Best_cut_com,ss)
if __name__=='__main__':
    source='C:/Users/Administrator/Desktop/net_word_file_matrix.txt'
    word_file="C:/Users/Administrator/Desktop/NoRepatefile.txt"
    word_file_after_cut='C:/Users/Administrator/Desktop/word_file_after_cut.txt'
    K=10
    (result,ss)=sa(source,K)
    np.savetxt('C:/Users/Administrator/Desktop/net_word_after_cut.txt',result)
    word_index_after_cut=[int(x) for x in list(result[...,0])]

    f=open(word_file)
    g=open(word_file_after_cut,'w')
    
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

'''
    #用于标记有没有被选择过
    flag=[0 for x in range(l)]
    word_index=[x for x in range(l)]
    matrix=np.zeros(l*l).reshape(l,l)
    for j in range(l):
        temp_index=np.random.randint(1,l)
        while 1:
            temp_index=np.random.mm1,l)
            print(temp_index)
            if (flag[temp_index]==0):
                matrix[j]=res[temp_index]
                flag[temp_index]=1
                word_index[j]=temp_index
                break
'''
