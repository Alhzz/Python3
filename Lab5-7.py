""" Sequence VII """

def main(num):
    ''' Print sequence '''
    keep = str()    #Keep number in string type

    #Upper triangle
    for j in range(1, num+1):
        keep += "%d " % j
        print(keep)

    #Lowwer triangle
    for i in range(num-1, 0, -1):
        keep = str()
        for j in range(1, i+1):
            keep += str(j) + ' '
        print(keep)


main(int(input()))