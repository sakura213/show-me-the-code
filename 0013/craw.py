

import urllib.request
from bs4 import BeautifulSoup
import re

url = 'http://tieba.baidu.com/p/2166231880'
path = '/home/x8/Desktop/python/show-me-the-code/0013/'

def downloadimg(url):
    img = urllib.request.urlopen(url).read()
    imgName = re.split('/|%',url)[-1]
    with open(path+imgName,'wb') as f:
        f.write(img)


context = urllib.request.urlopen(url).read()

soup = BeautifulSoup(context.decode())

imgcontext = soup.find_all('img')
for img in imgcontext:
    print(img['src'])
    downloadimg(img['src'])
    