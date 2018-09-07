"""
Sequence IX
Ason Uthatham
"""

def main(num):
    '''
    Print Pyramid number

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

main(int(input()))