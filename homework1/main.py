import jieba
import math
import sys

print(sys.argv)
print(len(sys.argv))

if (len(sys.argv)!=4):
    print("您的输入有误。")

file1=open(sys.argv[1],"r")
paragraph1=file1.read()
file1.close()
file2=open(sys.argv[2],"r")
paragraph2=file2.read()
file2.close()
file3=open(sys.argv[3],"w")
print(paragraph1+paragraph2)
file3.write(paragraph1+paragraph2)
file3.close()
