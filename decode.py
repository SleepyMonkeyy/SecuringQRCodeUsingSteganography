from stegapy import decode_image
from xor import code

key = input("< Enter the key for encryption or decryption: >")
decoded = decode_image('stegoimage.png')

output_str = code(decoded, key)
print(output_str)
