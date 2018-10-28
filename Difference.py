""" Difference """

def delete(num1, num2):
    """ Minus set """
    set1 = set()
    set2 = set()

    for _ in range(num1):
        set1.add(int(input()))
    for _ in range(num2):
        set2.add(int(input()))
    print(*(sorted(set1 - set2)))

delete(int(input()), int(input()))
