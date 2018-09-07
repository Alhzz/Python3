""" Sequence III """

def main(num):
    ''' Print sequence '''
    for j in range(num):
        for i in range(2, num+2):
            print(i+j, end=" ")
        print()

main(int(input()))
