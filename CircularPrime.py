""" CircularPrime """

def shuffle(number):
    """ Shuffle index of number """
    total = 0

    for j in range(2, int(number)+1):
        result = j
        for i in range(len(str(j))):
            tempo = int((str(j)[i:len(str(j))] + str(j)[:i]))
            if check(tempo) == False:
                result = 0
                break
        total += result
    print(total)

def check(digit):
    """ Calculate prime number """
    count = 0
    for i in range(2, int(digit**0.5)+1):
        if digit%i == 0:
            count += 1
        if count > 0:
            break

    if count > 0:
        return False
    else:
        return True

shuffle(input())
