""" GCD2 """
def cal(num1, num2):
    """ Calculate GCD """
    num1, num2 = max(num1, num2), min(num1, num2)
    while True:
        num1 = num1%num2
        if num1 == 0:
            print(num2)
            break
        num2 = num2%num1
        if num2 == 0:
            print(num1)
            break
 
cal(int(input()), int(input()))
