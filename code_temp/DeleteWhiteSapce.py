f=open('c:/users/Administrator/Desktop/test/temp/Source2.dat',errors='ignore')
g=open('c:/users/Administrator/Desktop/test/temp/word2text2.txt','w')
for line in f:
      if line=='\n':
            continue
      else:
            g.write(line)
f.close()
g.close()
