import os
from PIL import Image


path = '/home/x8/Desktop/python/show-me-the-code/0005'

# im = Image.open('223.jpg')


for x in os.listdir(path):
    if 'jpg' in x:
        with Image.open(path +'/'+ x) as im:
           im.thumbnail((640,1136))
           im.show()
           im.save(path +'/'+'thub'+ x, 'jpeg')