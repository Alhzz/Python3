""" LastStand """
from json import loads

def last(mylist):
    """ Print last number from list """
    for i in mylist:
        print(i%10)

last(loads(input()))
