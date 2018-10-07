""" FourDirections """

def print_direction():
    """ Print direction """
    direct = input()
    for i in range(5):
        for j in direct:
            if (i == 0 or i == 4) or (i == 1 and j == 'D') or (i > 2 and j == 'U') \
            or (j == 'D' and i == 4):
                print('  *   ', end='')
            if (i == 1 and j == 'U') or (i == 3 and j == 'D'):
                print(' ***  ', end='')
            if (i == 1 or i == 3) and j == 'L':
                print(' *    ', end='')
            if (i == 1 or i == 3) and j == 'R':
                print('   *  ', end='')
            if (i == 2 and j == 'U') or (i == 2 and j == 'D'):
                print('* * * ', end='')
            if i == 2 and (j == 'R' or j == 'L'):
                print('***** ', end='')
        print()

print_direction()

