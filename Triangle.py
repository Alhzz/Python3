""" Triangle """

def draw(size):
    """ Draw triangle """
    for i in range(size, 0, -1):
        print("  "*(i - 1) + "%02d" %i, end="")
        if i != size:
            print("  "*((size - i)*2 - 1) + "%02d" %i, end="")
        print()

draw(int(input()))
