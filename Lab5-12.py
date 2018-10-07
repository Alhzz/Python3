"""
Sequence XII
Ason Uthatham
"""

def upper(num):
    ''' Print Upper Sequecen '''
    for i in range(num, 0, -1):
        for j in range(i, num+1):
            print('%02d' % j, end=' ')
            var_ij = i
        for j in range(num-1, (num-i), -1):
            print('%02d' % j, end=' ')
            var_ij = j
        if i == 1:
            for j in range(num-1, 0, -1):
                print('%02d' % j, end=' ')
                var_ij = j
        if i != 1:
            for k in range(var_ij+1, num+1):
                print('%02d' % k, end=' ')
                var_ij = k
        if i < num and i != 1:
            for j in range(var_ij-1, i-1, -1):
                print('%02d' % j, end=' ')
        print()
    lowwer(num)

def lowwer(num):
    ''' Print Lowwer Sequecen '''
    for i in range(2, num+1):
        for j in range(i, num+1):
            print('%02d' % j, end=' ')
            var_ij = i
        for j in range(num-1, (num-i), -1):
            print('%02d' % j, end=' ')
            var_ij = j
        if i == 1:
            for j in range(num-1, 0, -1):
                print('%02d' % j, end=' ')
                var_ij = j
        if i != 1:
            for k in range(var_ij+1, num+1):
                print('%02d' % k, end=' ')
                var_ij = k
        if i < num and i != 1:
            for j in range(var_ij-1, i-1, -1):
                print('%02d' % j, end=' ')
        print()

upper(int(input()))
