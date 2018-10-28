""" PickThemAgain """

def pick(mylist):
    """ Find number that can divide 3 or 5  """
    display = ""
    mylist.reverse()
    for i in mylist:
        if int(i)%3 == 0 or int(i)%5 == 0:
            display += i + "\n"

    if display == "":
        print("Nope")
    else:
        print(display)

pick(input().split(" "))
