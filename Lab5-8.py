""" Sequence VIII """

def main(num):
    ''' Print sequence '''
    keep = str()    #Keep number in string type

    #Upper triangle
    for j in range(1, num+1):
        keep += "%02d " % j
        print("   "*(num - j) + keep)


main(int(input())
