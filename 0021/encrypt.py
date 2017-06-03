import hashlib
import random,math



def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()

def Salt(len=64):
	return "%s"*len%tuple([chr(65+random.randint(0,25)) for i in range(len)])

def encrypt(password):

    Log = int(math.log(len(password),2))+1
    MaxLen = 2**Log
    SAL = Salt(MaxLen-len(password)+random.randint(8,16))
    ENC = md5((password+SAL).encode())
    return SAL,ENC



print(encrypt('123456'))