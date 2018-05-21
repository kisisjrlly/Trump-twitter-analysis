f=open('g:/python/test.txt')
#g=open('g:/python/1.txt','w')
L=[]
for line in f:
      line=f.readlines()
      L+=line
f.close()
tag=[]
for x in line:
      tag+=x.splitlines()
#print(tag)
      
num=[]
i=0
while i<36:
      num.append(0)
      i+=1

Tag=dict(zip(tag,num))
print(Tag)

