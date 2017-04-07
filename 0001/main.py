
#**第 0001 题：**做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用**生成激活码**（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import time
import random,string

def random_str(length = 8):
    str =''
    chars = string.ascii_letters+string.digits       
    while length > 0:
        str += random.choice(chars)
        length -=1    
    return str 

def write_activeCode(file,num = 200):
    fp = open(file,'w')
    
    while num >0:
        num -=1
        
        fp.write(random_str()+' '+str(200-num)+'\n')
#         fp.write()
    fp.close()
    


if __name__ == '__main__':
    print(time.strftime("Start:%Y-%m-%d %H:%M:%S", time.localtime()))
    start =time.time()
    write_activeCode('Activation_Code.txt')
    print('End:S:',time.time()-start)


# fp = open('Activation_Code.txt','wb')