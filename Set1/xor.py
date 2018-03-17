import binascii
from Crypto.Util.strxor import strxor

def conv(value):
    return binascii.unhexlify(value)

buf1 = conv(raw_input("Enter buffer 1: "))
buf2 = conv(raw_input("Enter buffer 2: "))
print (binascii.hexlify(strxor(buf1, buf2)))
