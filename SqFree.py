""" SqFree """

def main(num):
    """ Find amoung of Square-free """
    count = 3
    if num <= 3:
        print(num)
    else:
        for i in range(4, num+1):
            if cal(i):
                count += 1
        print(count)

def cal(num):
    """ Calculate Square-free number """
    for i in range(2, int(num**0.5)+1):
        if num % (i**2) == 0:
            return False
    return True

main(int(input()))
