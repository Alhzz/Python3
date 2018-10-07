""" Kaprekar's Constant """

def pocess(num):
    """ Calculate round """
    count = 0
    while num != 6174:
        num1, num2 = re_order(num)
        if num1 > num2:
            num = num1 - num2
        else:
            num = num2 - num1
        count += 1
    print(count)

def re_order(num1):
    """ Re-order number """
    num1 = str(num1)
    while len(num1) < 4:
        num1 += '0'
    num_a = num1[0]
    num_b = num1[1]
    num_c = num1[2]
    num_d = num1[3]

    if int(num_a) > int(num_b):
        num_a, num_b = num_b, num_a
    if int(num_a) > int(num_c):
        num_a, num_c = num_c, num_a
    if int(num_a) > int(num_d):
        num_a, num_d = num_d, num_a
    if int(num_b) > int(num_c):
        num_b, num_c = num_c, num_b
    if int(num_b) > int(num_d):
        num_b, num_d = num_d, num_b
    if int(num_c) > int(num_d):
        num_c, num_d = num_d, num_c

    num1 = int(num_a + num_b + num_c + num_d)
    num2 = int(num_d + num_c + num_b + num_a)
    return num1, num2

pocess(int(input()))
