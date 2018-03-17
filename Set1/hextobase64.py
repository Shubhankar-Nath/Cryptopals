import base64
import binascii

def toBase64(value):
    temp = binascii.unhexlify(value)
    return base64.b64encode(temp).decode('ascii')


while True:
    print("Enter 'x' for exit.")
    hexdec = raw_input("Enter number in Hexadecimal Format: ")
    if hexdec == 'x':
		break
    else:
        print (toBase64(hexdec))
