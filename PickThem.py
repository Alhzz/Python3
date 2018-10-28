""" PickThem """
import json

def even():
    """ Print only even number from list """
    input_list = json.loads(input())
    mylist = list()

    for i in input_list:
        if i%2 == 0:
            mylist.append(i)
    if mylist == list():
        print("Nope")
    else:
        print(*mylist, sep="\n")

even()
