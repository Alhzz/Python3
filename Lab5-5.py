""" Sequence V """

def main(num):
    ''' Print sequence '''
    count = 0
    for j in range(num, 0, -1):
        count += 1
        print(j, end=' ')
        if count == 7:
            count = 0
            print()

main(int(input()))
