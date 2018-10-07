"""
Sequence XI
Ason Uthatham
"""

def main(num):
    ''' Print Sequecen '''

    #Upper triangle
    for i in range(1, num+1):
        var_j = 0
        for j in range(1, i+1):
            print("%02d" % j, end=' ')
            var_j = j
        for _ in range((2*num) - 2*i):
            print("%02d" % var_j, end=' ')
        for k in range(i-1, 0, -1):
            print("%02d" % k, end=' ')
        print()

    #Lowwer triangle
    for i in range(num-1, 0, -1):
        for j in range(1, i+1):
            print("%02d" % j, end=' ')
            var_j = j
        for _ in range((2*num) - 2*i):
            print("%02d" % var_j, end=' ')
        for k in range(i-1, 0, -1):
            print("%02d" % k, end=' ')
        print()

main(int(input()))
