""" Filter """
from json import loads

def filter_(dic, score):
    """ Filter by score """
    mylist = sorted(dic)
    display = str()
    for i in mylist:
        if dic[i] >= score:
            display += i + "\t" + str("%.02f" %dic[i]) + "\n"
    if display == str():
        print("Nope")
    else:
        print(display)

filter_(loads(input()), float(input()))
