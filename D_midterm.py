""" Diginity_Midterm2014 """

def decode():
    """ Decode code from number """
    while True:
        num = int(input())
        if num == 0:
            break
        else:
            while num >= 10:
                total = 0
                for i in str(num):
                    total += int(i)
                num = total
            print(num)

decode()
