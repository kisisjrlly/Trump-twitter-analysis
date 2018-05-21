
import numpy as np  
from sklearn.metrics.pairwise import rbf_kernel 

b=np.loadtxt('C:/Users/Administrator/Desktop/net_word_file_matrix.txt')
res=rbf_kernel(b)
for i in range(len(res)):
    res[i,i]=0
np.savetxt('C:/Users/Administrator/Desktop/net_word_gauss_matrix.txt',res)
