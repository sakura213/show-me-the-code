
#  '第 0010 题：使用 Python 生成类似于图中的字母验证码图片'

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random,string

def rndChar():
    stringletters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return random.choice(stringletters)
def rndColor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

fontpath = '/home/x8/Desktop/python/show-me-the-code/0010/Futura.ttf'

width = 60*4
height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))

font = ImageFont.truetype(font=fontpath,size = int(height * 0.7))
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor1())

for t in range(4):
    draw.text((60 * t + 10, 0), rndChar(), font=font, fill=rndColor2())
    
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
# image.show()


