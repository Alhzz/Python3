''' Sort number '''

def order():
    ''' Input order and number you want to sort '''
    command = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())

    num1, num2, num3 = re_order(num1, num2, num3)

    if command == 'Ascend':
        print('%.2f, %.2f, %.2f' % (num3, num2, num1))
    else:
        print('%.2f, %.2f, %.2f' % (num1, num2, num3))

def re_order(num1, num2, num3):
    ''' Re-order number '''
    if num1 < num2:
        num1, num2 = num2, num1
    if num2 < num3:
        num2, num3 = num3, num2
    if num1 < num2:
        num1, num2 = num2, num1
    return num1, num2, num3

order()
