""" Kabata """

def kabata(round):
    """ Input and Print """
    for _ in range(round):
        word = input()
        if is_kabata(word):
            print("yes")
        else:
            print("no")

def is_kabata(word):
    """ Check syntex Kabata language """
    check = ""
    for i in range(len(word)):
        check += word[i]
        if len(check) == 2:
            if check == "ba" and word[i]


def is_word(word):
    """ Check is word in kabata """
    if word in "kabata":
        return True
    else:
        return False

kabata(int(input()))
