#test the regex

import re

f=open('c:/Users/Administrator/Desktop/test.txt')
g=open('c:/Users/Administrator/Desktop/testResult.txt','w')
pat_http=re.compile(r'https?://\S*\s')
pat_amp=re.compile('&amp;')
pat_hashtag=re.compile('#[A-Z]*[A-Za-z]*\s')
pat_rt=re.compile('RT.*')

for line in f:
    new_text = pat_http.sub("", line)
    new_text=pat_amp.sub("",new_text)
    new_text=pat_hashtag.sub("",new_text)
    new_text=pat_rt.sub("",new_text)
    g.write(new_text+'\n')
f.close()
g.close()


with open(file) as f:
    
