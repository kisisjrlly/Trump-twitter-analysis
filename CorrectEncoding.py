import re
filename ='C:/Users/Administrator/Desktop/test/temp/Trump2018-3-7.txt'

fp = open(filename,'rb')

content = fp.read().decode('utf-8')

reg = r'<p>(.*?)</p>'


#print(content)
result = re.findall(reg,content)

fp.close()
fp = open(filename+'.txt','bw')
for r in result:
    r = r.encode('utf-8')
    fp.write(r)
    fp.write('\n'.encode('utf-8'))
fp.close()
