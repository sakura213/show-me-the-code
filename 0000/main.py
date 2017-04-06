from PIL import Image, ImageDraw, ImageFont

def ADD_NUM_ICON(img):
    draw = ImageDraw.Draw(img)    
    font = ImageFont.truetype('msyh.ttf',60)
    
#     x = img.size[0]*0.85
#     y = img.size[1]*0.05
    x,y = img.size
    draw.text((0.85*x,0.05*y),'7',font = font ,  fill = "#ff0000" )
    
    return 0




if __name__ =='__main__':
    img = Image.open('./github_icon.png')
    print(img.size)
    ADD_NUM_ICON(img)
#     img.show()
    img.save('./avanta.png')