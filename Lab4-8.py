''' Table I '''

def main():
    ''' Multiply by 15 from 1 to n '''
    bow = int(input()) + 1

    for i in range(1, bow):
        print('15 x {} = {}'.format(i, i*15))

main()
