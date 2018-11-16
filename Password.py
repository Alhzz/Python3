""" Encode SHA512 """
import hashlib
 
def encode():
    """ Convert string to hash by SHA512 """
    word = input()
    word = hashlib.sha512(word.encode(encoding='utf-8')).hexdigest()
    print(word.upper())
 
encode()