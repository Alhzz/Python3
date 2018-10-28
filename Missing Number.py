""" Missing Numbers """

def find_number(top):
    """
    Find missing number from input
        top:        The heighest number
        all_num:    Sequence number from 0 to top
        number:     Number that user input
        fill:       Keep your last input for break loop
    """

    all_num = list(i for i in range(top+1))
    number = list()
    fill = -1
    while fill != 0:
        fill = int(input())
        if number.count(fill) == 0:
            number.append(fill)
    number.sort()
    for i in all_num:
        if i not in number:
            print(i)

find_number(int(input()))
    