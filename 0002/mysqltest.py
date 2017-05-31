

import re
import pymysql

path = '/home/x8/Desktop/python/show-me-the-code/0002/Activation_Code.txt'
config = {  'host' : '127.0.0.1',
            'port' : 3306,
            'user' : 'root',
            'passwd' : '895622982',
            'db' : 'active_code'
   #         'charset' : 'utf-8',
 #           'cursorclass' : pymysql.cursors.DictCursor
}

def readline(path):
    fp = open(path,'r')
    line = fp.readline()
    while line:
        yield line
        line = fp.readline()
    fp.close()


# [str,num ]=  'zyfqKqkV 195'.split(' ')
# print(str,num)

# with pymysql.connect(**config) as conn:
#     with conn.cursor() as cursor:
#         effect_row = cursor.execute(r"insert into code value(7,'abc')")

#         conn.commit()
    
conn = pymysql.connect(**config)
cursor = conn.cursor()
for str in readline(path):
    [code,id,no] = re.split(' |\n',str)
    try:
        print('%s %s %d %s' % (type(int(id)),type(code),int(id),code))
        cursor.execute(r"insert into code value(%s,%s)",[int(id),code])
    except Exception as e:
        print('Exception %s' % e)

    

conn.commit()
cursor.close()
conn.close()




