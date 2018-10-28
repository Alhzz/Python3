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
        return "No"
    else:
        return "Yes"

def main():
    """ Find All Primes """
    num = int(input())
    check(int(input()))

main()
