import jieba
import math
import sys
#测试代码
#print(sys.argv)
#print(len(sys.argv))
#print(paragraph1+paragraph2)
if (len(sys.argv)!=4):#检测输入数据是否有误
    print("您的输入有误。")
    exit(1)
file1=open(sys.argv[1],"r")
paragraph1=file1.read()
file1.close()

file2=open(sys.argv[2],"r")
paragraph2=file2.read()
file2.close()

paragraph1_cut=[i for i in jieba.cut(paragraph1, cut_all=True) if i != '']
paragraph2_cut=[i for i in jieba.cut(paragraph2, cut_all=True) if i != '']# 分词
word_set = set(paragraph1_cut).union(set(paragraph2_cut))# 创建分词并集
word_dict = dict()#创建分词编码词典
t = 0
for word in word_set:
    word_dict[word] = t
    t += 1
paragraph1_cut_node=[word_dict[word] for word in paragraph1_cut]#将词按词典进行编码
paragraph1_cut_node_loc=[0] * len(word_dict)
t=0;
for rank in paragraph1_cut_node:
    paragraph1_cut_node_loc[rank]+=1# 根据编码后词组映射向量
paragraph2_cut_node=[word_dict[word] for word in paragraph2_cut]#将词按词典进行编码
t=0;
paragraph2_cut_node_loc=[0] * len(word_dict)
for rank in paragraph2_cut_node:
    paragraph2_cut_node_loc[rank]+=1
sum = 0
sq1=0
sq2=0
for t in range(len(word_dict)):#进行余弦相似度计算
    sum += paragraph1_cut_node_loc[t]*paragraph2_cut_node_loc[t]
    sq1 += pow(paragraph1_cut_node_loc[t],2)
    sq2 += pow(paragraph2_cut_node_loc[t],2)
file3=open(sys.argv[3],"w")
try:
    result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 2)
except ZeroDivisionError:
    result = 0.0
file3.write(str(result))
file3.close()