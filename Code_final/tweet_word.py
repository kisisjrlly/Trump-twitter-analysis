import numpy as np

'''
此文本文件用来建立单词tweet网络
'''

tempResult=r'C:\Users\Administrator\Desktop\tempResult3.txt'
NoRepeatfile=r'C:\Users\Administrator\Desktop\NoRepatefile.txt'
BaseMatrixFile=r'C:\Users\Administrator\Desktop\BaseMatrix.txt'
f=open(tempResult)
g=open(NoRepeatfile)
h=open(BaseMatrixFile,'w')


base=[]
b=[]
Table=g.read().split()
J=len(Table)
print(J)
I=0
for line in f:
    I=I+1

print(I)

i=j=0

base=[['0' for x in range(J)] for y in range(I)]

print(i,j)



f.close()
f=open(tempResult)

i=j=0


try:
    for fline in f:
        for word in fline.split():
            j=0
            for s in Table:
                if word==s:
                    base[i][j]='1'
                j=j+1
        h.write(' '.join([x for x in base[i]])+'\n')
        i=i+1
    print(i,j)
except IndexError as msg:
    print(msg)
    print(i,j)
                
            

f.close()
g.close()
h.close()



            
