''' BootSequence '''

def main():
    ''' Print 1 to n and seperate by _ '''
    count = int(input()) + 1
    print(*[i for i in range(1, count)], sep='_')

main()
