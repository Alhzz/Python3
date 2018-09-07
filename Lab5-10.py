"""
Sequence X
Ason Uthatham
"""

def upper(num):
    '''
    Print upper Pyramid number

        keep: For keep number of the left Pyramid in str
        keep_r: For keep number of the right Pyramid in str
    '''
    keep = str()

    #Left triangle
    for j in range(1, num+1):
        keep += "%02d " % j
        keep_r = str()

        #Right triangle
        for i in range(j - 1, 0, -1):
            keep_r += "%02d " % i
        print("   "*(num-j) + keep + keep_r)

    lowwer(num)


def lowwer(num):
    """ Print lowwer Pyramid number """
    for k in range(num-1, 0, -1):
        keep = str()
        keep_r = str()
        #Left triangle
        for j in range(1, k+1):
            keep += "%02d " % j
            var_j = j
        #Right triangle
        for i in range(var_j - 1, 0, -1):
            keep_r += "%02d " % i
        print("   "*(num-var_j) + keep + keep_r)

upper(int(input()))
