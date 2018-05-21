import sys,re,collections,nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet

'''
此代码用来处理文本，统计单词
输出单词文件为Norepeatfile.txt
输出文本文件为Norpeatefile3.txt
'''


## 在进行此文件中代码处理之前，请在centos中进行 iconv -f utf-8 -t utf-8 -c Base.dat>>base.txt 进行utf8编码过滤工作

#正则表达式处理

## .@或者@删除一整行
pat_at1=re.compile('(\.|")@.*')
## 删除掉@的人@[A-Za-z-.']+
pat_at2=re.compile(r"@[a-zA-Z0-9.-_']+")
## RT删除一整行
pat_rt=re.compile('RT.*')
## 删除&amp
pat_amp=re.compile('&amp;')
## 删除#hashtag
pat_hashtag=re.compile('#[A-Z]*[A-Za-z]*\s')
## 删除http等
pat_http=re.compile(r'https?://\S*\s')
# 接下来进行单词形式还原及删除掉标点符号和各种数字等。或者进行用nltk去除停用词

## 第一种方法：
# patterns that used to find or/and replace particular chars or words
# to find chars that are not a letter, a blank or a quotation
pat_letter = re.compile(r'[^a-zA-Z \']+')
# to find the 's following the pronouns. re.I is refers to ignore case
pat_is = re.compile("(it|he|she|that|this|there|here)(\'s)", re.I)
# to find the 's following the letters
pat_s = re.compile("(?<=[a-zA-Z])\'s")
# to find the ' following the words ending by s
pat_s2 = re.compile("(?<=s)\'s?")
# to find the abbreviation of not
pat_not = re.compile("(?<=[a-zA-Z])n\'t")
# to find the abbreviation of would
pat_would = re.compile("(?<=[a-zA-Z])\'d")
# to find the abbreviation of will
pat_will = re.compile("(?<=[a-zA-Z])\'ll")
# to find the abbreviation of am
pat_am = re.compile("(?<=[I|i])\'m")
# to find the abbreviation of are
pat_are = re.compile("(?<=[a-zA-Z])\'re")
# to find the abbreviation of have
pat_ve = re.compile("(?<=[a-zA-Z])\'ve")



lmtzr = WordNetLemmatizer()

# 删除多余元素
def firstdeal(sourcefile,tempfile1):
    with open(sourcefile) as f:
            g=open(tempfile1,'w')
            for line in f:
                    new_text = pat_http.sub("", line)
                    new_text=pat_amp.sub("",new_text)
                    new_text=pat_hashtag.sub("",new_text)
                    new_text=pat_rt.sub("",new_text)
                    new_text=pat_at1.sub("",new_text)
                    new_text=pat_at2.sub("",new_text)
                    g.write(new_text+'\n')
            f.close()
            g.close()

 # 替换所有的缩写形式
def replace_abbreviations(text):
    new_text = text
	# 先删除掉所有的非英文字符，再删除掉首位两端空白字符并化为小写
    new_text = pat_letter.sub(' ', text).strip().lower()
    new_text = pat_is.sub(r"\1 is", new_text)
    new_text = pat_s.sub("", new_text)
    new_text = pat_s2.sub("", new_text)
    new_text = pat_not.sub(" not", new_text)
    new_text = pat_would.sub(" would", new_text)
    new_text = pat_will.sub(" will", new_text)
    new_text = pat_am.sub(" am", new_text)
    new_text = pat_are.sub(" are", new_text)
    new_text = pat_ve.sub(" have", new_text)
    new_text = new_text.replace('\'', ' ')
    return new_text


## 删除空格
def deleteSpaceline(tempfile2,tempfile3):
    f=open(tempfile2)
    g=open(tempfile3,'w')
    for line in f:
        if line=='\n':
            continue
        else:
            g.write(line)
    f.close()
    g.close()

def get_words(tempfile1,tempfile2): 
    str=''
    with open (tempfile1,encoding='utf-8') as f:
        g=open(tempfile2,'w')
        words_box=[]
        pat = re.compile(r'[^a-zA-Z \']+') #匹配所有的非字母符号，如标点数字
        for line in f:
            #if re.match(r'[a-zA-Z]*',line): 
            #    words_box.extend(line.strip().strip('\'\"\.,').lower().split())
            # words_box.extend(pat.sub(' ', line).strip().lower().split())
            # spilt对单词进行切片
            Str=merge(replace_abbreviations(line))
            g.write(' '.join(Str)+'\n')
            words_box.extend(Str)
    g.close()
    f.close()
    return collections.Counter(words_box)  


def merge(words):
    new_words = []
    s=word_tokenize(words)
    tags = nltk.pos_tag(s)
    for tag in tags:
        if tag[0]:
            if (tag[0] in stopwords.words('english')) or (not wordnet.synsets(tag[0])):
                continue
            else:
                if get_wordnet_pos(tag[1]):
                    lemmatized_word = lmtzr.lemmatize(tag[0], get_wordnet_pos(tag[1]))
                    new_words.append(lemmatized_word)
    return new_words
                    
    '''        
    for word in s:
        if word:
            
            if (word in stopwords.words('english')) or (not wordnet.synsets(word)):
                continue
            tag = nltk.pos_tag(s) # tag [('bigger', 'JJR')]
            pos = get_wordnet_pos(tag[0][1])
            pos = tag[0][1]
            if pos:
                lemmatized_word = lmtzr.lemmatize(word, pos)
                new_words.append(lemmatized_word)
            else:
                new_words.append(word)
    return new_words
    '''

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return nltk.corpus.wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return nltk.corpus.wordnet.VERB
    elif treebank_tag.startswith('N'):
        return nltk.corpus.wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return nltk.corpus.wordnet.ADV
    else:
        return ''





def append_ext(words):
    new_words = []
    for item in words:
        word, count = item
        tag = nltk.pos_tag(word_tokenize(word))[0][1] # tag [('bigger', 'JJR')]
        new_words.append((word, count, tag))
    return new_words

def write_to_file(words, NoRepeatfile):
    f = open(NoRepeatfile, 'w')
    for item in words:
        i=1
        for field in item:
            if i==1:
                f.write(str(field)+' ')
                i=i+1
    f.close()

if __name__=='__main__':
    
    #打开的文件名
    #sourcefile='C:/Users/Administrator/Desktop/base.dat'
    sourcefile='C:/Users/Administrator/Desktop/shangren.dat'

    #中间临时文件，用来保存干净的纯单词文本
    tempfile1='C:/Users/Administrator/Desktop/tempResult1.txt'
    tempfile2='C:/Users/Administrator/Desktop/tempResult2.txt'
    tempfile3='C:/Users/Administrator/Desktop/tempResult3.txt'
    #结果文件，用来保存无重复的所有单词
    NoRepeatfile='C:/Users/Administrator/Desktop/NoRepatefile.txt'
    
    firstdeal(sourcefile,tempfile1)
    print("counting...")
    
    words = get_words(tempfile1,tempfile2)
    deleteSpaceline(tempfile2,tempfile3)
    print("writing file...")
    write_to_file(append_ext(words.most_common()),NoRepeatfile)
