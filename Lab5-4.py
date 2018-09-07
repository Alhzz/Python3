""" Sequence IV """

def main(num):
    ''' Print sequence '''
    for j in range(num):
        for i in range(1, num+1):
            print(i + (j*num), end=" ")
        print()

main(int(input()))
