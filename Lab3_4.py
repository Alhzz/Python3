''' Triangle I '''

def re_order(num1, num2, num3):
    ''' Re-order number '''
    if num1 < num2:
        num1, num2 = num2, num1
    if num1 < num3:
        num1, num3 = num3, num1
    return num1, num2, num3

def judge():
    ''' Find is it possible to make triangle '''
    #Input length in centimater
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num1, num2, num3 = re_order(num1, num2, num3)

    diff = calculate(num1, num2, num3)
    if diff > 0.01:
        print('No')
    else:
        print('Yes')

def calculate(num1, num2, num3):
    ''' Calculate posibility '''
    num1 = pow(num1, 2)
    total = pow(num2, 2) + pow(num3, 2)
    return abs(num1 - total)

judge()
