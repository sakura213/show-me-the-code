
#**第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。

path = "/home/x8/Desktop/python/show-me-the-code/004/LICENSE"

def readline(path):
    fp = open(path,'r')
    line = fp.readline()
    while line:
        yield line
        line = fp.readline()
    fp.close()

def countlineWord(str):
    alist = str.split(' ')
    return len(alist) -alist.count('')

num = 0
for line in readline(path):
    num += countlineWord(line)


print(num)
