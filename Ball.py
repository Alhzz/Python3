""" Ball """

def bounce(high):
    """ Find bounce time """
    count = 0
    while high >= 1:
        high *= 3/5
        count += 1
    print(count-1)

bounce(float(input())*100)
