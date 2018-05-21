# 判断是不是英文单词


from nltk.corpus import wordnet


sourcefile=''
outfile1=''
outfile2=''

f=open(sourcefile)
g=open(outfile1,'w')
h=open(outfile2,'w')


Table=f.read()

for word in Table:
    if not wordnet.synsets(word):
        g.write(word+' ')
    else:
        h.write(word+' ')

f.close()
g.close()
h.close()
