""" Perfect """

def perfect_number(num):
    """ Calculate Perfect number """
    if num < 2:
        print(0)
    else:
        count = 0
        for i in range(2, num):
            if check_prime(i):
                if pow(2, i-1)*(pow(2, i) - 1) > num:
                    break
                else:
                    count += pow(2, i-1)*(pow(2, i) - 1)
        print(count)

def check_prime(num):
    """ Calculate prime number """
    count = 0
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            count += 1
        if count > 0:
            break

    if count > 0 or num < 2:
        return False
    else:
        return True

perfect_number(int(input()))
