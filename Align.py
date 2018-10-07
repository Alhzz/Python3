""" Align """

def main():
    """ Print text """
    size = int(input())
    locate = input()
    word = input()

    if locate == "left":
        pass
    elif locate == "right":
        print(" "*(size - len(word)), end="")
    else:
        if (size - len(word)) % 2 == 0:
            print(" "*((size - len(word))//2), end="")
        else:
            print(" "*(((size - len(word))//2) + 1), end="")
    print(word)

main()
