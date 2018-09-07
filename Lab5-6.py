""" Sequence VI """

def main(num):
    ''' Print sequence '''
    keep = str()    #Keep number in string type

    for j in range(1, num+1):
        keep += "%d " % j
        print(keep)

main(int(input()))
