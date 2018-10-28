""" Chack Prime number """

def check(num):
    """ Calculate prime number """
    count = 0
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            count += 1
        if count > 0:
            break

    if count > 0 or num < 2:
        print("NO")
    else:
        print("YES")

check(int(input()))
