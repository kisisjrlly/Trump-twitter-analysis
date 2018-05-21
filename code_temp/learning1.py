import nltk
f=open('C:/Users/Administrator/Desktop/test/temp/word2text.txt',encoding='utf-8')
t=open('C:/Users/Administrator/Desktop/test/temp/last1.txt','w')
Tag={'CD': 0, 'DT': 0, 'EX': 0, 'FW': 0, 'IN': 0, 'JJ': 0, 'JJR': 0, 'JJS': 0, 'LS': 0, 'MD': 0, 'NN': 0, 'NNS': 0, 'NNP': 0, 'NNPS': 0, 'PDT': 0, 'POS': 0, 'PRP': 0, 'PRP$': 0, 'RB': 0, 'RBR': 0, 'RBS': 0, 'RP': 0, 'SYM': 0, 'TO': 0, 'UH': 0, 'VB': 0, 'VBZ': 0, 'VBP': 0, 'VBD': 0, 'VBN': 0, 'VBG': 0, 'WDT': 0, 'WP': 0, 'WP$': 0, 'WRB': 0, 'OTHERS': 0}
for line in f:
    s=''
    Tag_temp={'CD': 0, 'DT': 0, 'EX': 0, 'FW': 0, 'IN': 0, 'JJ': 0, 'JJR': 0, 'JJS': 0, 'LS': 0, 'MD': 0, 'NN': 0, 'NNS': 0, 'NNP': 0, 'NNPS': 0, 'PDT': 0, 'POS': 0, 'PRP': 0, 'PRP$': 0, 'RB': 0, 'RBR': 0, 'RBS': 0, 'RP': 0, 'SYM': 0, 'TO': 0, 'UH': 0, 'VB': 0, 'VBZ': 0, 'VBP': 0, 'VBD': 0, 'VBN': 0, 'VBG': 0, 'WDT': 0, 'WP': 0, 'WP$': 0, 'WRB': 0}
    #print(Tag_temp)
    ListLine=[]
    text=nltk.word_tokenize(line)
    ListLine=nltk.pos_tag(text)
    #print(ListLine)

    # 此2-for用于统计每行的各词性单词的个数
    for x in ListLine:
        for y in Tag_temp.keys():
            if x[1]==y:
                Tag_temp[x[1]]+=1

    #此for用于把每一行统计的结果进行拼接为字符串
    for m in Tag_temp.values():
        s+=(str(m)+' ')
    
    #输出到文件
    t.write(s+'\n')
f.close()
t.close()
               




#接下里把统计得到的数据写到文件中就可以了
    
