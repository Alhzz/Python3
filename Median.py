""" Median """

def median(cycle):
    """ Calculate median """
    lst = list()
    for _ in range(cycle):
        lst.append(int(input()))
    lst.sort()

    if cycle % 2 != 0:
        print("%.1f" %lst[cycle//2])
    else:
        print("%.1f" %((lst[cycle//2 - 1] + lst[cycle//2])/2))

median(int(input()))
