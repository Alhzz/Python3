""" Flatten """
from json import loads

def flat(lst):
    """ Convert list in list to one list """
    new_lst = convert(lst)
    new_lst.sort(reverse=True)
    print(new_lst)

def convert(lst):
    """ Convert list to string """
    new_lst = list()
    for i in lst:
        if isinstance(i, list):
            new_lst += convert(i)
        else:
            new_lst.append(i)
    return new_lst

flat(loads(input()))
