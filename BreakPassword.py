""" Encode SHA512 """
import hashlib
import string
def compare(word):
    """ Compare number between hash """
    for i in string.ascii_letters:
        for j in string.ascii_letters:
            for k in string.ascii_letters:
                for l in string.ascii_letters:
                    for m in string.ascii_letters:
                        print(i+j+k+l+m)
                        if encode(i+j+k+l+m) == word:
                            print(i)
                            break
    
def encode(num):
    """ Convert string to hash by SHA512 """
    num = hashlib.sha512(num.encode(encoding='utf-8')).hexdigest()
    return num.upper()

compare(input())
