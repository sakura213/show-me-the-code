

import json

filtered_wordsPath = '/home/x8/Desktop/python/show-me-the-code/0011/filtered_words.txt'


words = None

with open(filtered_wordsPath,'r') as f:
    words = [line.strip() for line in f]


while True:
    text = input('请输入文字:(提示： 输入CTRL + C ，退出)\n')
    if text in words:
        print ('Freedom')
    else:
        print ('Human Rights')   

            
