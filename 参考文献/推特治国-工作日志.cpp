1. 假定政策全为正确

2.本论文提供了通过文字确定政策的方法 参考别的论文

3.三个阶段发的内容的不同区别其文字特征--基于网络的方法
  还可以通过语义识别区分出其不同阶段的主要政策核心

内容的不同区别：词性，形容词动词名次

3.1：词性统计识别方法：

4.大数据加机器学习

文献及网站：{

5.基于语义的领域政策要点分析与形式化方法研究 http://www.wanfangdata.com.cn/details/detail.do?_type=degree&id=D596184#

6.基于词义及语义分析的问答技术研究http://xueshu.baidu.com/s?wd=paperuri:(6f83149bcd9520416a3f4a1788e7cc09)&filter=sc_long_sign&sc_ks_para=q%3D%E5%9F%BA%E4%BA%8E%E8%AF%8D%E4%B9%89%E5%8F%8A%E8%AF%AD%E4%B9%89%E5%88%86%E6%9E%90%E7%9A%84%E9%97%AE%E7%AD%94%E6%8A%80%E6%9C%AF%E7%A0%94%E7%A9%B6&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&sc_us=9775255431822721017

7.基于词性的政策内容分析

8.政策文本计算：一种新的政策文本解读方式  http://www.fx361.com/page/2017/0417/1576832.shtml

9.政策文本计算主张运用政策编码、政策概念词表或政策与语词之间的映射关系进行政策概念的自动识别和自动处理，最终构建从政策文本到政策语义的自动解析框架，并在此基础上关注政策文本及其内涵分析。具体到方法论层次，政策文本计算被认为是一种非介入式、非精确性的解析方式，并广泛应用于元政策分析领域。

10.计算机辅助文本分析（Computer Assisted Text Analysis，CATA）分为文本内容分析、文本数据处理和文本挖掘三个研究层次，并先后经历了计算化内容分析（Computational Content Analysis，CCA）、计算机辅助定量数据分析（Computer-Assisted Qualitative Data Analysis，CAQDA）以及语料计算学（Lexicometrics for Corpus Exploration）等不同发展阶段

11.通过自然语言处理将政策文本解析为结构化文本数据（Textual Data），并构建语词、语义或情感等特殊对象，不仅能形成对大规模政策文本语料的系统化处理，而且能在不同的政策文本集中进行比较分析和一致性分析，推动政策文本融合分析。

12.政见语料库
}

2-7:
文本原始数据处理：

把日期删掉只留下文本，但是依然可以识别时间

2-23

利用分词服务，比如新浪分词服务

词类分析：
1,名词,Nouns (n.) 表示人或事物的名称 box,pen,tree,apple 
2,代词,Pronouns (pron.)代替名词、数词、形容词We,this,them,myself 
3,形容词,Adjectives(adj.) 用来修饰名词,表示人或事物的特征 good,sad,high,short 
4,数词,Numerals(num.)表示数目或顺序 one,two,first 
5,动词,Verb (v.) 表示动作或状态 Jump,sing,visit 
6,副词,Adverbs（adv.) 修饰动、形、副等词,表示动作特征 there,widely,suddenly 
7,冠词,Articles (art.) 用在名词前,帮助说明名词所指的范围 a,an,the 
8,介词,Prepositions (prep.) 用在名词或代词前,说明它与别的词的关系 in,on,down,up 
9,连词,Conjunctions (conj.) 表示人或事物的名称if,because,but 
10,感叹词,Interjections (int.) 代替名词、数词、形容词等 oh,hello,hi,yeah 
vt.是及物动词,vt.后必须跟宾语：sing a song 
vi.是不及物动词,vi.后不直接带宾语或不带宾语:jump high

3-3

用到的技术：
1.图与网络
2.矩阵
3.python
4.大数据
5.机器学习

流程：
文本数据原始处理-内容深加工-建模分析

3-5

三个矩阵按时间阶段手工分开

如何删除掉每一行前面的时间信息和后面的标志以及网站信息？

删除前面时间信息：用正则表达式，格式：0000+空格+00:00：00+空格+A/P+M换为excel处理

3-6

2015年6月16开始宣布竞选总统
在11032行
				
2016年11月9日竞选成功
在3216行

3-7
{
把所有的网址替换掉：利用正则表达式：
https?://\S*\s

把后缀替换掉
\s?\[.*\]\s{1,2}(link)?

删除掉回复推文
\.@.*
删除掉转发推文
RT.*

删除掉主题标记
#[A-Z]*[A-Za-z]*\s

删除掉&amp
&amp;\s

删除掉※

删除掉don*t
[a-zA-Z]*＊[a-z]*

删除掉§

删除掉  每

删除后缀 如I'm的m’
'[a-z]*

删除数字
\d+(?:\.\d+)?%?
}

3-8
统计出每一行各个词性的个数

3-26
进行上一步，统计每一行各种词性单词的个数：
首先利用nltk进行分词，得到每个单词对应的词性表元组，把最终结果存到一个文件中，矩阵形式存放，每一列代表：

3-27

Hopkins D J， King G.A Method of Automated Nonparametric
Content Analysis for Social Science[J].American Journal of Political Science，
2010， 54（1）： 229-247

3-28
建立两种网络:
第一种：
以词为节点，两个不同的词在同一个篇推文中，连接
第二种：
以推文为节点，两篇推文中有相同的词（一个或者两个），连接

建模过程：

1.统计出有多少不同的词，去除无用的词，如连词，叹词，代词，得到一组所有单词的列表：

利用nltk，对整个文章进行分词，去除各个单词，建立列表
去除各个单词：找到基本词，根据词性，删除对应词

2.建立一个大型矩阵：横坐标为单词，列坐标为推文，矩阵元素为0,1
3.根据建立的基础矩阵，建立两种网络

两种网络的建立过程：

第一种网络：

矩阵列为单词，横为单词：若在基础矩阵中每个行向量的各元素存在两个同时为1,则连接单词节点，即新矩阵对应两个单词处赋值为1

第二种网络：

矩阵列为推文，横为推文，若基础矩阵中有一列两个元素同时为一，则连接推文节点，即新矩阵中对应的两个推文中的坐标出赋值1



特朗普推文选择：只选择原创，回复和转发都不算

3-29
一定要做好严谨可行的规划，防止做一些无用功
接下来任务：
看懂python代码，并处理自己的内容

lemmatizer=WordNetLemmatizer()
#如果不提供第二个参数，单词变体还原为名词

3-30
3-31
4-1

正则表达式源码
import re

emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)

def remove_emoji(text):
    return emoji_pattern.sub(r'', text)

检查拼写错误
from enchant.checker import SpellChecker
chkr = SpellChecker("en_US")
chkr.set_text("Many peope likee to watch In the Name of People.")
for err in chkr:
    print "ERROR:", err.word


停用词 如'd  
'll  
'm  
're  
's  
't  
've  
ZT  
ZZ  
a  
a's  
able  
about  
above 

是否需要去除通用词要考虑清楚
去除停用词，分词以及词性标注的调用方法

from nltk.corpus import stopwords

import nltk

disease_List = nltk.word_tokenize(text)

#去除停用词

filtered = [w for w in disease_List if(w not in stopwords.words('english')]


判断一个词是不是英文单词
from nltk.corpus import wordnet

if not wordnet.synsets(word_to_test):
  #Not an English Word
else:
  #English Word


a=[72, 56, 76, 84, 80, 88]  
print(a.index(76))

1.粘贴复制文本，转为ascii
2.用正则表达式除去@，RT，链接，标签，&amp
3.删除掉空白行
4.删除掉重复的行
5.进行分词等操作写入到文件


暂时还没有去掉经识别不是英语单词的内容和停用词，共九万多条词汇

4-2
基础矩阵的方法内存太大，不行


2947

4-4:
发现单词数统计错误

4-6：
在老师提供的论文中，CNV之间的权重可以采用高斯核函数，但单词节点之间的权重如何计算？
为什么建立两种这样的网络?这两种网络之间有什么关系吗？
原先建立网络的方式：
1.若两个单词在同一条推文中，则连接。构建单词网络。若同时出现在两篇tweet中才连接呢？
2.如果两条tweet中出现了同一个单词，则连接。若同时出现两个相同的单词才连接呢？若同时记录相同的单词是哪个呢？若以两条推文中相同单词个数的多少为权重建立网络呢?
3.上述两种网络都是基于Base矩阵的，这两种网络有什么关系?
4-8:

自己论文想要解决的问题：
{
1.主题提取
2.不同主题随时间变化特朗普的态度
3.不同时间段内重要的主题中心，或者特朗普主题偏向程度随时间的变化趋势
4.tweet影响力：哪些主题最被人民关注，哪些关注的较轻
5.三个阶段特朗普用语变化

先提取出几个主题
然后再与tweet内容行对比
}

 文献阅读与思考
{
基本读完参考文献，模型过程基本了解，但感觉与自己想要做的无关。
文献思路:网络分层，每层内进行聚类，聚类结果的衡量函数相加。
跨层聚类：根据回归分析系数作为邻接矩阵进行聚类。
最后得到的结果：？

映射到推特治国中来：
分三个阶段，每个阶段分两个网络，
}



特朗普推特治国可以研究的问题：
{
Tweets as President (444 days)
200 tweets about Fake News
42 tweets about CNN
38 tweets about NBC
39 tweets about the New York Times
196 tweets about Fox News or Sean Hannity
135 tweets about Russia
92 tweets about Clinton
86 tweets about Obama
73 tweets about Obamacare
27 tweets about the NFL
96 tweets about deals
125 tweets about MAGA

作为总统的微博（444天）
关于虚假新闻的200条微博
关于美国有线电视新闻网的42条微博
关于NBC的38条推特
关于纽约时报的39条微博
196条对福克斯新闻或Sean Hannity
关于俄罗斯的135条微博
关于克林顿的92条微博
关于奥巴马的86条微博
73条关于奥巴马
关于NFL的27条微博
关于交易的96条微博
125条关于马夹

Latest Fake News

Personal Superlatives

Key to solving issues

On Global Warming

I have...

On President Barack Obama

What's the worst?

Who doesn't have a clue?

Media Disdain

Who's laughing?
}


我们用了nltk的一些方法来处理文本，然后又想用复杂网络的方法进行分析，会不会冲突或者有点重复？因为nltk等自然语言处理技术本身就可以用来语言处理。


4.12

聚类原理：
建立的网络为若两个单词在同一个推文中则连接，所以如果两个单词距离相近，则说明在表达同一主题
ncut算法加模拟退火算法：

1.生成权重矩阵
生成一个3659*3659的矩阵
（i，j）处元素为第i个单词和第j个单词的高斯距离
for(int i=0;i<3659;i++)
{
	for (j=i+1;j<3659;j++){
		weight[i][j]=rbf(net_word_matrix[...][i],net_word_matrix[...][j])
	}
}


2.随机分为K组，计算Ncut值，再重新分配，重新计算

2.1:随机分为k组：
	1.随机生成K个整数，使这K个整数相加和为3659，此步为随机生成K组数据每组的大小
	2.随机生成1-3659个整数，取前K1个为第一组，取第K2个为第二组，依次类推
2.2：计算Ncut值：
	1.计算组内距离
		eg.（k1-1）*sum（k1中所有元素的和）：
	2.计算组间距离
		eg.在weight中，计算k1中所有元素所在的列的剔除本k1组元素在内的所有的列和：
	3.Ncut+=每组组内距离/每组组间距离
2.3：重新分组，模拟退火算法
	1.重新分组：
	{
				随机选择几个分组，
				随机从选择的每一个分组中任一选出随机个列（依据温度数量逐渐减少）。
				随机把选出的列送入其他的分组中：
				选出送入其他每个分组的列个数随机
				
				随机生成一个数，判断其在哪一组。
				随机选择向前还是向后放，更改分组大小。
				随着温度的增加，上述迭代次数逐渐减少
	}
	2.依据概率接受其为最优解
	

	
	
如果想在两周内做完：
1.完全参照他的做法
2.接下来只需要看懂他的代码
3.进行分析


	