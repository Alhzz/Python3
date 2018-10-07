""" FOR!F-Ball """

def main():
    """ Find location of ball """
    suffle = input()
    state = 1

    for i in suffle:
        if i == "A" and state == 1:
            state = 2
        elif i == "A" and state == 2:
            state = 1
        elif i == "B" and state == 2:
            state = 3
        elif i == "B" and state == 3:
            state = 2
        elif i == "C" and state == 3:
            state = 1
        elif i == "C" and state == 1:
            state = 3
    print(state)

main()
