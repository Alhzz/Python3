""" BreachTheDoor """
import string

def decode(puzzle):
    """ Decode by puzzle """
    newword = ""
    for i in puzzle:
        if i in string.ascii_letters or i in " ":
            newword += i

    puzzle = newword.split(" ")
    print(" ".join(list(filter(lambda x: len(x) > 6, puzzle))))

decode(input())
