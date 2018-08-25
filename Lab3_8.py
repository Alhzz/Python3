''' Circular II '''

def main():
    '''
    Find machine area and calculate
    '''
    me_x = float(input())
    me_y = float(input())
    mach = float(input())       # Radius of machine area
    friend_x = float(input())
    friend_y = float(input())
    mach += float(input())

    #Judge
    if ((me_x - friend_x)**2 + (me_y - friend_y)**2)**0.5 < mach:
        print('Yes')
    else:
        print('No')

main()
