''' Circular I '''

def main():
    '''
    Find machine area and calculate
    '''
    me_x = float(input())
    me_y = float(input())
    mach = float(input())   # Radius of machine area
    mos_x = float(input())  # mos = mosquito
    mos_y = float(input())

    #Judge
    if ((me_x - mos_x)**2 + (me_y - mos_y)**2)**0.5 <= mach:
        print('Yes')
    else:
        print('No')

main()
