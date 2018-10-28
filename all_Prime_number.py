""" Chack all Prime number """

def check(num):
    """ Calculate prime number """
    count = 0
    for i in range(2, num+1):
        if num%i == 0:
            count += 1
        if count > 1:
            break

    if count > 1 or num < 2:
        return False
    else:
        return True

def main():
    """ Find All Primes """
    num = int(input())
    count = 0

    for i in range(2, num+1):
        if check(i):
            count += 1
    print(count)

main()
