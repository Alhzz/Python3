""" Run Length Encoding """

def encode(word):
    """ Encode words """
    newword = ""
    for i in range(len(word)):
        if i == 0:
            last = word[i]
            count = 1
        elif word[i] == last:
            count += 1
        else:
            newword += str(count) + str(last)
            last = word[i]
            count = 1
    newword += str(count) + str(last)
    print(newword)

encode(input())
