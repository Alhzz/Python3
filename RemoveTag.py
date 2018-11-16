""" RemoveTag """

def remove(sectence):
    """ Remove Tag of HTML """
    status = 0
    lst = list()
    word = ""

    for i in sectence:
        if i == "<":
            status = 1
            if word != "":
                lst += word.strip().split()
                word = ""
        elif i == ">":
            status = 0
        elif status == 0:
            word += i
    if word != "":
        lst += word.strip().split()
    print(lst)

remove(input())
