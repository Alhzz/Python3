""" Sequence I """

def main(num):
    ''' Print sequence '''
    for _ in range(num):
        for i in range(1, num+1):
            print(i, end=" ")
        print()

main(int(input()))
