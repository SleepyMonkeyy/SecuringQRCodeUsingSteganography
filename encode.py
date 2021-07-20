from stegapy import create_image
from xor import code



input_str = input("< Enter the message: >" )
key = input("< Enter the key for encryption or decryption: >")




output_str= code(input_str,key)
message = output_str
print(message)

create_image(message,'defaultimage3.png','stegoimage.png')